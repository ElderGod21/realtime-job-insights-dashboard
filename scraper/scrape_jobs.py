# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# # Step 1: Send request
# url = "https://internshala.com/jobs"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
# }
# response = requests.get(url, headers=headers)

# # Step 2: Parse content
# soup = BeautifulSoup(response.content, "html.parser")
# job_listings = soup.find_all("div", class_="individual_internship")

# # Step 3: Extract data
# job_titles = []
# companies = []
# locations = []
# salaries = []
# experiences = []
# links = []

# for job in job_listings:
#     try:
#         # Job Title
#         title_tag = job.find("a", class_="job-title-href")
#         job_title = title_tag.get_text(strip=True) if title_tag else "N/A"
#         job_link = "https://internshala.com" + (title_tag.get("href", "") if title_tag else "")

#         # Company Name
#         company_tag = job.find("p", class_="company-name")
#         company_name = company_tag.get_text(strip=True) if company_tag else "N/A"

#         # Location
#         location_tag = job.find("p", class_="locations")
#         location = location_tag.get_text(strip=True) if location_tag else "N/A"

#         # Salary or stipend
#         salary_tag = job.find("span", class_="desktop")
#         salary = salary_tag.get_text(strip=True) if salary_tag else "N/A"

#         # Experience (if any — Internshala usually doesn’t list it, use dummy or N/A)
#         experience = "N/A"  # Default value

#         row_items = job.find_all("div", class_="row-1-item")

#         for item in row_items:
#             icon = item.find("i")
#             if icon and "ic-16-briefcase" in icon.get("class", []):
#                 span = item.find("span")
#                 if span:
#                     experience = span.get_text(strip=True)
#                 break

#         # Append to lists
#         job_titles.append(job_title)
#         companies.append(company_name)
#         locations.append(location)
#         salaries.append(salary)
#         experiences.append(experience)
#         links.append(job_link)

#     except Exception as e:
#         print(f"Error parsing a job: {e}")

# # Step 4: Save to CSV
# df = pd.DataFrame({
#     "Job Title": job_titles,
#     "Company": companies,
#     "Location": locations,
#     "Salary": salaries,
#     "Experience": experiences,
#     "Link": links
# })

# df.to_csv("internshala_jobs.csv", index=False)
# print("Saved jobs to internshala_jobs.csv")


import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time

def scrape_internshala_jobs(max_pages=5):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    # Data lists
    job_titles = []
    companies = []
    locations = []
    salaries = []
    experiences = []
    links = []

    for page in range(1, max_pages + 1):
        if page == 1:
            url = "https://internshala.com/jobs"
        else:
            url = f"https://internshala.com/jobs/page-{page}/"

        print(f"🔄 Scraping page {page}: {url}")
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"⚠️ Skipping page {page}: Status code {response.status_code}")
            break

        soup = BeautifulSoup(response.content, "html.parser")
        job_listings = soup.find_all("div", class_="individual_internship")

        if not job_listings:
            print(f"🚫 No job listings found on page {page}. Stopping.")
            break

        for job in job_listings:
            try:
                # Job Title
                title_tag = job.find("a", class_="job-title-href")
                job_title = title_tag.get_text(strip=True) if title_tag else "N/A"
                job_link = "https://internshala.com" + (title_tag.get("href", "") if title_tag else "")

                # Company Name
                company_tag = job.find("p", class_="company-name")
                company_name = company_tag.get_text(strip=True) if company_tag else "N/A"

                # Location
                location_tag = job.find("p", class_="locations")
                location = location_tag.get_text(strip=True) if location_tag else "N/A"

                # Salary
                salary_tag = job.find("span", class_="desktop")
                salary = salary_tag.get_text(strip=True) if salary_tag else "N/A"

                # Experience
                experience = "N/A"
                row_items = job.find_all("div", class_="row-1-item")
                for item in row_items:
                    icon = item.find("i")
                    if icon and "ic-16-briefcase" in icon.get("class", []):
                        span = item.find("span")
                        if span:
                            experience = span.get_text(strip=True)
                        break

                # Append to lists
                job_titles.append(job_title)
                companies.append(company_name)
                locations.append(location)
                salaries.append(salary)
                experiences.append(experience)
                links.append(job_link)

            except Exception as e:
                print(f"⚠️ Error parsing a job on page {page}: {e}")
                continue

        # Be polite: avoid hammering the server
        time.sleep(1)

    # Save to CSV
    df = pd.DataFrame({
        "Job Title": job_titles,
        "Company": companies,
        "Location": locations,
        "Salary": salaries,
        "Experience": experiences,
        "Link": links,
        "Scraped On": datetime.now().strftime("%Y-%m-%d %H:%M")
    })

    df.to_csv("internshala_jobs.csv", index=False)
    print(f"✅ Scraped {len(df)} jobs across {page} pages.")
    print("📁 Saved to data/internshala_jobs.csv")

if __name__ == "__main__":
    scrape_internshala_jobs(max_pages=5)  # You can change this number as needed

