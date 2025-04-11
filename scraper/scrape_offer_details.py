import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def scrape_offer_details(url: str) -> dict[str, str]:
    """
    Scrape the detailed view of a single job offer from Tecnoempleo.

    Args:
        url: URL of the job offer to scrape.

    Returns:
        A dictionary containing structured job information, or None if an error occurs.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Title
        title = soup.select_one("h1.h3.h5-xs.mb-2")
        title = title.text.strip() if title else "N/A"

        # Company
        company_tag = soup.select_one("a.text-primary.link-muted.fs--18")
        company = company_tag.text.strip() if company_tag else "N/A"

        # Location
        location_tag = soup.select_one("div.ml-0.mt-2 a")
        location = location_tag.text.strip() if location_tag else "N/A"

        # Date posted
        date_tag = soup.select_one("div.ml-0.mt-2 span")
        date_posted = date_tag.text.strip() if date_tag else "N/A"

        # Description
        description_div = soup.select_one("div[itemprop='description']")
        description = description_div.get_text(separator="\n").strip() if description_div else "N/A"

        # Technologies / Tags
        tags = soup.select("div.pl--12.pr--12 a.btn.btn-primary.btn-soft")
        tech_tags = [tag.text.strip() for tag in tags]

        # Meta information (experience, contract, etc.)
        # THIS IS A PLACEHOLDER FOR POSSIBLE FUTURE UPGRADES
        meta_info = {
            "Experience": "N/A",
            "Contract Type": "N/A",
            "Job Type": "N/A",
            "Seniority": "N/A"
        }

        detail_labels = soup.select("div.row.mb-2 div.col-6")
        for item in detail_labels:
            label = item.select_one("div.text-muted")
            value = item.select_one("div.fw-bold")
            if label and value:
                key = label.text.strip()
                val = value.text.strip()
                if "Experiencia" in key:
                    meta_info["Experience"] = val
                elif "Tipo contrato" in key:
                    meta_info["Contract Type"] = val
                elif "Jornada" in key:
                    meta_info["Job Type"] = val
                elif "Nivel Profesional" in key:
                    meta_info["Seniority"] = val

        return {
            "Title": title,
            "Company": company,
            "Location": location,
            "Date Posted": date_posted,
            "Technologies": ", ".join(tech_tags),
            "Experience": meta_info["Experience"], # PLACEHOLDER FOR POSSIBLE FUTURE UPGRADES
            "Contract Type": meta_info["Contract Type"], # PLACEHOLDER FOR POSSIBLE FUTURE UPGRADES
            "Job Type": meta_info["Job Type"], # PLACEHOLDER FOR POSSIBLE FUTURE UPGRADES
            "Seniority": meta_info["Seniority"], # PLACEHOLDER FOR POSSIBLE FUTURE UPGRADES
            "Description": description,
            "URL": url
        }

    except Exception as e:
        print(f"⚠️ Error scraping offer {url}: {e}")
        return None


def main() -> None:
    """
    Load basic job offers from CSV, enrich each with detailed info, and save the output.
    """
    input_path = "./data/job_offers_list.csv"
    output_path = "./data/job_offers_detailed.csv"

    df_input = pd.read_csv(input_path)
    print(f"📥 Loaded {len(df_input)} URLs from {input_path}")

    detailed_offers = []

    for idx, row in df_input.iterrows():
        url = row["URL"]
        print(f"🔗 Scraping {url}")
        details = scrape_offer_details(url)
        if details:
            detailed_offers.append(details)
        time.sleep(2)  # be nice to the server

    df_output = pd.DataFrame(detailed_offers)
    df_output.to_csv(output_path, index=False)
    print(f"📦 Saved {len(df_output)} detailed offers to {output_path}")


if __name__ == "__main__":
    main()
