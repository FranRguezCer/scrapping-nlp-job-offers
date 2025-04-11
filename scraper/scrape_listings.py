import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def fetch_job_listings(keyword: str = "data", page: int = 1) -> str:
    """
    Fetch HTML content from a Tecnoempleo job listings page.

    Args:
        keyword: Search keyword to filter job listings.
        page: Page number to fetch.

    Returns:
        HTML content as a string.
    """
    base_url = "https://www.tecnoempleo.com/ofertas-trabajo/"
    params = {
        "te": keyword,
        "pagina": page
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()
    print(f"✅ Fetched page {page}")
    return response.text


def parse_job_cards(html: str) -> list[dict[str, str]]:
    """
    Parse job cards from Tecnoempleo HTML and extract title, company, and URL.

    Args:
        html: Raw HTML content from a listings page.

    Returns:
        A list of dictionaries, each containing job information.
    """
    soup = BeautifulSoup(html, "html.parser")
    job_cards = soup.select("div.p-3.border.rounded.mb-3.bg-white")
    print(f"🔍 Found {len(job_cards)} job cards.")
    
    jobs = []
    for card in job_cards:
        try:
            title_tag = card.select_one("a.font-weight-bold.text-cyan-700")
            company_tag = card.select_one("a.text-primary.link-muted")

            title = title_tag.get_text(strip=True)
            link = title_tag["href"]
            if not link.startswith("http"):
                link = "https://www.tecnoempleo.com" + link
            company = company_tag.get_text(strip=True) if company_tag else "N/A"

            jobs.append({
                "Title": title,
                "Company": company,
                "URL": link
            })
        except Exception as e:
            print("⚠️ Error parsing job card:", e)

    return jobs


def scrape_multiple_pages(keyword: str = "data", max_pages: int = 5, delay: int = 2) -> pd.DataFrame:
    """
    Scrape multiple pages of job listings and return as a DataFrame.

    Args:
        keyword: Search keyword for job listings.
        max_pages: Number of pages to scrape.
        delay: Seconds to wait between page requests.

    Returns:
        DataFrame with all job offers scraped.
    """
    all_jobs = []

    for page in range(1, max_pages + 1):
        try:
            html = fetch_job_listings(keyword=keyword, page=page)
            jobs = parse_job_cards(html)
            all_jobs.extend(jobs)
            time.sleep(delay)  # Be polite to the server
        except Exception as e:
            print(f"❌ Failed on page {page}: {e}")
            break

    return pd.DataFrame(all_jobs)


def main() -> None:
    """
    Run the scraping process and save the job offers to CSV.
    """
    df = scrape_multiple_pages(keyword="data", max_pages=5)
    df.drop_duplicates(subset="URL", inplace=True)  # Avoid duplicate offers
    df.to_csv("./data/job_offers_list.csv", index=False)
    print(f"📁 Saved {len(df)} job offers to ./data/job_offers_list.csv")


if __name__ == "__main__":
    main()
    