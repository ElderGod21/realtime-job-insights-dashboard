import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time

def scrape_internshala_jobs(max_pages=50):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    # Data lists
    job_titles = []
    companies = []
    skills= []
    locations = []
    salaries = []
    experiences = []
    links = []
    posted = []

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
                title_tag = job.find("a", class_="job-title-href") # type: ignore
                job_title = title_tag.get_text(strip=True) if title_tag else "N/A"
                job_link = "https://internshala.com" + (title_tag.get("href", "") if title_tag else "") # type: ignore

                # Company Name
                company_tag = job.find("p", class_="company-name") # type: ignore
                company_name = company_tag.get_text(strip=True) if company_tag else "N/A"

                # Location
                location_tag = job.find("p", class_="locations") # type: ignore
                location = location_tag.get_text(strip=True) if location_tag else "N/A"

                # Salary
                salary_tag = job.find("span", class_="desktop") # type: ignore
                salary = salary_tag.get_text(strip=True) if salary_tag else "N/A"

                # Experience
                experience = "N/A"
                row_items = job.find_all("div", class_="row-1-item") # type: ignore
                for item in row_items:
                    icon = item.find("i") # type: ignore
                    if icon and "ic-16-briefcase" in icon.get("class", []): # type: ignore
                        span = item.find("span")# type: ignore
                        if span:
                            experience = span.get_text(strip=True)# type: ignore
                        break
                
                #Date Posted
                # Try both classes: active and inactive
                status_div = job.find("div", class_="status-success") or job.find("div", class_="status-inactive") # type: ignore
                datePosted = ""

                if status_div:
                    span = status_div.find("span") # type: ignore
                    if span:
                        datePosted = span.get_text(strip=True) # type: ignore

                
                #skills required
                                #skills required
                skills_required = "N/A"
                try:
                    job_response = requests.get(job_link, headers=headers)
                    if job_response.status_code == 200:
                        job_soup = BeautifulSoup(job_response.content, "html.parser")
                        skill_tags = job_soup.find_all("span", class_="round_tabs")
                        if skill_tags:
                            skills_required = ', '.join([tag.get_text(strip=True) for tag in skill_tags])
                        else :
                            skills_required = 'See job description via link'
                except Exception as e:
                    print(f"⚠️ Error fetching skills for job: {job_link} | Error: {e}")
                
            

                # Append to lists
                job_titles.append(job_title)
                companies.append(company_name)
                skills.append(skills_required)
                locations.append(location)
                salaries.append(salary)
                experiences.append(experience)
                links.append(job_link)
                posted.append(datePosted)

            except Exception as e:
                print(f"⚠️ Error parsing a job on page {page}: {e}")
                continue

        # To avoid hammering the server
        time.sleep(1)

    # Save to CSV
    df = pd.DataFrame({
        "Job Title": job_titles,
        "Company": companies,
        "Skills": skills,
        "Location": locations,
        "Salary": salaries,
        "Experience": experiences,
        "Posted": posted,
        "Link": links

    })

    df.to_csv("data/internshala_jobs.csv", index=False)
    print(f"✅ Scraped {len(df)} jobs across {page} pages.")
    print("📁 Saved to data/internshala_jobs.csv")

if __name__ == "__main__":
    scrape_internshala_jobs(50)  # You can change this number as needed

