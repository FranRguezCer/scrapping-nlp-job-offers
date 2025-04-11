# 📊 Data Jobs in Spain – End-to-End Analysis with Web Scraping & NLP

This project is an **end-to-end pipeline** that scrapes and analyzes job offers for data-related roles in Spain using **real listings from [Tecnoempleo](https://www.tecnoempleo.com/)**.

It combines:
- ✅ Web scraping with Python to collect job market data
- ✅ Exploratory Data Analysis (EDA) to identify trends
- ✅ Rule-based NLP with `spaCy` to extract structured information (tech skills, soft skills, work mode)
- ✅ A dual comparison of keyword matching vs NLP pattern matching

> Ideal for aspiring **Data Analysts** and **Junior Data Scientists** aiming to understand real job market expectations in 2025.

---

## 🚀 Project Highlights

- 🔎 Scrapes 150 real job offers related to *data roles* (e.g. Data Analyst, Data Scientist, Data Engineer)
- 🌐 Handles listings in both **Spanish and English**
- 🧠 Applies multilingual NLP (`spaCy`) to detect soft/technical skills and work modality
- 📊 Compares results from basic keyword matching and smart rule-based NLP
- 🧼 Cleans, structures and enriches raw text data into actionable insights

---

## 📦 Project Structure

```bash
data-jobs-analysis/
│
├── data/                            # All raw and processed datasets
│   ├── job_offers_list.csv          # Listings scraped from Tecnoempleo (title, company, URL)
│   └── job_offers_detailed.csv      # Enriched offers with descriptions, metadata, tech tags
│
├── scraper/                         # Web scraping scripts
│   ├── scrape_listings.py           # Scrapes multiple pages of job listings
│   └── scrape_offer_details.py      # Extracts detailed info from each job URL
│
├── notebooks/                       # Analysis and visualization notebooks
│   └── EDA_jobs.ipynb               # Exploratory data analysis and feature engineering
│
├── requirements.txt                 # List of Python dependencies
├── README.md                        # Project documentation and summary
└── .gitignore                       # Files and folders to ignore in version control
```

---

## 🧰 Technologies Used

- **Python** – main programming language
  - `requests`, `BeautifulSoup` – for HTML parsing and web scraping
  - `pandas`, `re`, `collections` – for structured data manipulation and keyword extraction
  - `matplotlib`, `seaborn` – for data visualization and comparisons
  - `spaCy` – for NLP-based skill extraction in both **English** and **Spanish**
    - Language models used: `en_core_web_md` and `es_core_news_md`
    - `PhraseMatcher` for multilingual rule-based entity detection
  - `Jupyter Notebook` / `Google Colab` – for interactive and cloud-based analysis

---

## 🔧 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/FranRguezCer/scrapping-nlp-job-offers.git
cd scrapping-nlp-job-offers
```

### 2. (Optional but recommended) Create and activate a virtual environment
```bash
python -m venv venv-nlp
source venv-nlp/bin/activate         # Windows: .\venv-nlp\Scripts\activate
```

### 3. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 4. Download spaCy language models
```bash
python -m spacy download en_core_web_md
python -m spacy download es_core_news_md
```

---

## 📊 Dataset Summary

- ✅ Offers collected with the keyword: `"data"`
- ✅ Scraped from 5+ pages of search results (a total of 150 job offers from [Tecnoempleo](tecnoempleo.com))
- ✅ Full details extracted per offer: title, company, location, description, publication date, contract type, etc.
- ✅ Technologies auto-detected from free-text job descriptions (Python, SQL, Power BI, etc.)

---

## 🕸️ Web Scraping Process

The job offers were scraped from [Tecnoempleo](https://www.tecnoempleo.com/), a major Spanish tech job board.  
The scraping pipeline consists of two steps:

1. **Listing Scraper (`scrape_listings.py`)**  
   - Crawls multiple pages and collects basic info (job title, company, and URL to each job offer).

2. **Details Scraper (`scrape_offer_details.py`)**  
   - Visits each job URL to extract full descriptions, contract type, work modality, required skills, and more.

Both scripts use `requests` + `BeautifulSoup`, and results are saved into `job_offers_list.csv` and `job_offers_detailed.csv`.

---

## 📓 Try the EDA and NLP analysis in Google Colab

The main notebook includes all preprocessing, skill detection, and comparisons between keyword-based and NLP-based extractions.

> ⚡ No installation needed — run it directly in the cloud:

<div align="center">
  <a href="https://colab.research.google.com/github/FranRguezCer/scrapping-nlp-job-offers/blob/main/notebooks/EDA_jobs.ipynb" target="_blank">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="height: 40px;">
  </a>
</div>


---

## 🧠 Future Work

- Applying Named Entity Recognition (NER) or transformer-based models to enrich the analysis.
- Extracting salary ranges or required years of experience using NLP.
- Automating updates to track how trends evolve over time.

---

## 👨‍💻 Author

> Created by **[Francisco José Rodríguez Cerezo]**, aspiring data analyst with a passion for real-world applications and strong technical curiosity.  
> Currently enhancing my portfolio with practical end-to-end projects.

[LinkedIn](https://linkedin.com/in/franciscojoserodriguezcerezo) | [Portfolio](https://franrguezcer.github.io/portfolio/) | [Email](mailto:fjrguezcerezo@gmail.com)

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

You are free to use, modify, and distribute this code for personal or commercial purposes, provided that proper credit is given.  
This software is provided **"as is"**, without warranty of any kind.

© 2025 Francisco José Rodríguez Cerezo

