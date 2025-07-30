# scraper/scrape_jobs.py

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def scrape_internshala_jobs():
    url = "https://internshala.com/jobs"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    job_titles = []
    companies = []
    locations = []
    salaries = []
    links = []

    jobs = soup.find_all("div", class_="individual_internship")
    for job in jobs:
        title = job.find("div", class_="heading_4_5 profile").get_text(strip=True)
        company = job.find("a", class_="link_display_like_text").get_text(strip=True)
        location = job.find("a", class_="location_link").get_text(strip=True)
        salary = job.find("span", class_="stipend").get_text(strip=True)
        link = "https://internshala.com" + job.find("a")["href"]

        job_titles.append(title)
        companies.append(company)
        locations.append(location)
        salaries.append(salary)
        links.append(link)

    df = pd.DataFrame({
        "job_title": job_titles,
        "company": companies,
        "location": locations,
        "salary": salaries,
        "link": links,
        "scraped_on": datetime.now().strftime("%Y-%m-%d %H:%M")
    })

    df.to_csv("data/jobs.csv", index=False)
    print("✅ Job data scraped and saved to jobs.csv")

if __name__ == "__main__":
    scrape_internshala_jobs()
