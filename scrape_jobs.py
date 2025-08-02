# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# from datetime import datetime
# import time

# def scrape_internshala_jobs(max_pages=50):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
#     }
    
#     # Data lists
#     job_titles = []
#     companies = []
#     skills= []
#     locations = []
#     salaries = []
#     experiences = []
#     links = []
#     posted = []

#     for page in range(1, max_pages + 1):
#         if page == 1:
#             url = "https://internshala.com/jobs"
#         else:
#             url = f"https://internshala.com/jobs/page-{page}/"

#         print(f"🔄 Scraping page {page}: {url}")
#         response = requests.get(url, headers=headers)
#         if response.status_code != 200:
#             print(f"⚠️ Skipping page {page}: Status code {response.status_code}")
#             break

#         soup = BeautifulSoup(response.content, "html.parser")
#         job_listings = soup.find_all("div", class_="individual_internship")

#         if not job_listings:
#             print(f"🚫 No job listings found on page {page}. Stopping.")
#             break

#         for job in job_listings:
#             try:
#                 # Job Title
#                 title_tag = job.find("a", class_="job-title-href") # type: ignore
#                 job_title = title_tag.get_text(strip=True) if title_tag else "N/A"
#                 job_link = "https://internshala.com" + (title_tag.get("href", "") if title_tag else "") # type: ignore

#                 # Company Name
#                 company_tag = job.find("p", class_="company-name") # type: ignore
#                 company_name = company_tag.get_text(strip=True) if company_tag else "N/A"

#                 # Location
#                 location_tag = job.find("p", class_="locations") # type: ignore
#                 location = location_tag.get_text(strip=True) if location_tag else "N/A"

#                 # Salary
#                 salary_tag = job.find("span", class_="desktop") # type: ignore
#                 salary = salary_tag.get_text(strip=True) if salary_tag else "N/A"

#                 # Experience
#                 experience = "N/A"
#                 row_items = job.find_all("div", class_="row-1-item") # type: ignore
#                 for item in row_items:
#                     icon = item.find("i") # type: ignore
#                     if icon and "ic-16-briefcase" in icon.get("class", []): # type: ignore
#                         span = item.find("span")# type: ignore
#                         if span:
#                             experience = span.get_text(strip=True)# type: ignore
#                         break
                
#                 #Date Posted
#                 # Try both classes: active and inactive
#                 status_div = job.find("div", class_="status-success") or job.find("div", class_="status-inactive") # type: ignore
#                 datePosted = ""

#                 if status_div:
#                     span = status_div.find("span") # type: ignore
#                     if span:
#                         datePosted = span.get_text(strip=True) # type: ignore

                
#                 #skills required
#                                 #skills required
#                 skills_required = "N/A"
#                 try:
#                     job_response = requests.get(job_link, headers=headers)
#                     if job_response.status_code == 200:
#                         job_soup = BeautifulSoup(job_response.content, "html.parser")
#                         skill_tags = job_soup.find_all("span", class_="round_tabs")
#                         if skill_tags:
#                             skills_required = ', '.join([tag.get_text(strip=True) for tag in skill_tags])
#                         else :
#                             skills_required = 'See job description via link'
#                 except Exception as e:
#                     print(f"⚠️ Error fetching skills for job: {job_link} | Error: {e}")
                
            

#                 # Append to lists
#                 job_titles.append(job_title)
#                 companies.append(company_name)
#                 skills.append(skills_required)
#                 locations.append(location)
#                 salaries.append(salary)
#                 experiences.append(experience)
#                 links.append(job_link)
#                 posted.append(datePosted)

#             except Exception as e:
#                 print(f"⚠️ Error parsing a job on page {page}: {e}")
#                 continue

#         # To avoid hammering the server
#         time.sleep(1)

#     # Save to CSV
#     df = pd.DataFrame({
#         "Job Title": job_titles,
#         "Company": companies,
#         "Skills": skills,
#         "Location": locations,
#         "Salary": salaries,
#         "Experience": experiences,
#         "Posted": posted,
#         "Link": links

#     })

#     df.to_csv("data/internshala_jobs.csv", index=False)
#     print(f"✅ Scraped {len(df)} jobs across {page} pages.")
#     print("📁 Saved to data/internshala_jobs.csv")

# if __name__ == "__main__":
#     scrape_internshala_jobs(190)  # You can change this number as needed

# scrape_jobs.py (Optimized and Corrected)

# scrape_jobs.py (Corrected Version with Selenium)

# scrape_jobs.py (Final Version with Pop-up Handling)

# scrape_jobs.py (Final Hybrid Approach)

# scrape_jobs.py (Final, Robust Version)

# scrape_jobs.py (Built from provided HTML)
# scrape_jobs.py (Corrected Logic)



#-- Without skills great speed scraper 

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import time
# from pathlib import Path

# def scrape_internshala_jobs(max_pages=5):
#     """
#     Scrapes job listings from Internshala using a robust requests-based approach.
#     This version correctly parses the nested HTML structure to find all jobs and skips ads.
#     """
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#     }
    
#     job_data = []

#     for page in range(1, max_pages + 1):
#         url = f"https://internshala.com/jobs/page-{page}/" if page > 1 else "https://internshala.com/jobs/"
#         print(f"\n🔄 Scraping page {page}: {url}")
        
#         try:
#             response = requests.get(url, headers=headers, timeout=15)
#             response.raise_for_status()
#         except requests.exceptions.RequestException as e:
#             print(f"⚠️ Could not fetch page {page}. Stopping scraper. Error: {e}")
#             break

#         soup = BeautifulSoup(response.content, 'html.parser')
        
#         # --- KEY FIX: Find ALL divs with the 'individual_internship' class, regardless of nesting ---
#         # This is a more robust way to get all job cards on the page.
#         job_cards = soup.find_all('div', class_='individual_internship')
        
#         if not job_cards:
#             print(f"✅ No job cards found on page {page}. Scraper finished.")
#             break
            
#         print(f"   - Found {len(job_cards)} potential job listings.")

#         for card in job_cards:
#             try:
#                 # --- INTELLIGENT AD SKIPPING ---
#                 # Ads have a different structure inside. A real job will have a 'company_name' div.
#                 if not card.find('div', class_='company_name'):
#                     # print("     - Skipping a non-job card (likely an ad or promoted course).")
#                     continue
                
#                 # --- Scrape all data directly from the job card ---
#                 title_element = card.find('a', class_='job-title-href')
#                 job_title = title_element.get_text(strip=True)
#                 link = "https://internshala.com" + title_element['href']

#                 company = card.find('p', class_='company-name').get_text(strip=True)
#                 location = card.find('p', class_='locations').get_text(strip=True)

#                 # --- CORRECTED Salary and Experience scraping ---
#                 salary = "Not Disclosed"
#                 experience = "Not Specified"
                
#                 # Find all items in the details row
#                 details = card.find_all('div', class_='row-1-item')
                
#                 # The salary and experience are inside specific spans within these divs
#                 salary_element = card.find('span', class_='desktop')
#                 if salary_element:
#                     salary = salary_element.get_text(strip=True)
                
#                 experience_element = card.find('i', class_='ic-16-briefcase')
#                 if experience_element and experience_element.find_next_sibling('span'):
#                     experience = experience_element.find_next_sibling('span').get_text(strip=True)


#                 # Since skills are not on the card, we set a default value
#                 skills = "See job description via link"

#                 # print(f"     ✅ Scraped: '{job_title}'")
                
#                 job_data.append({
#                     "Job Title": job_title,
#                     "Company": company,
#                     "Skills": skills,
#                     "Location": location,
#                     "Salary": salary,
#                     "Experience": experience,
#                     "Link": link
#                 })

#             except Exception as e:
#                 print(f"     - An unexpected error occurred on a listing, skipping. Error: {e.__class__.__name__}")
#                 continue
        
#         time.sleep(1)

#     if not job_data:
#         print("\n\n❌ No job data was successfully scraped.")
#         return

#     df = pd.DataFrame(job_data)
#     df.drop_duplicates(subset=['Job Title', 'Company', 'Location'], keep='first', inplace=True)
    
#     output_path = Path("data/internshala_jobs.csv")
#     output_path.parent.mkdir(parents=True, exist_ok=True)
#     df.to_csv(output_path, index=False)

#     print(f"\n\n✅ Scraping complete. Successfully cleaned and saved {len(df)} unique jobs.")
#     print(f"📁 Data saved to {output_path}")


# if __name__ == "__main__":
#     scrape_internshala_jobs(max_pages=50)


# scrape_jobs.py (Final Version - Hybrid Selenium Approach)

# scrape_jobs.py (Final Version - Built from your HTML)

# scrape_jobs.py (Final Version with Correct Page Navigation)



##-- Finaly great script

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import time
# from pathlib import Path

# def scrape_internshala_jobs(max_pages=5): # Set to a higher number for a full scrape
#     """
#     Scrapes all job details from Internshala, including skills from detail pages.
#     This version correctly navigates all pages.
#     """
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#     }
    
#     job_data = []

#     for page in range(1, max_pages + 1):
#         url = f"https://internshala.com/jobs/page-{page}/" if page > 1 else "https://internshala.com/jobs/"
#         print(f"\n🔄 Scraping page {page}: {url}")
        
#         try:
#             response = requests.get(url, headers=headers, timeout=20)
#             response.raise_for_status()
#         except requests.exceptions.RequestException as e:
#             print(f"⚠️  Could not fetch page {page}. Stopping scraper. Error: {e}")
#             break

#         soup = BeautifulSoup(response.content, 'html.parser')
        
#         # --- KEY FIX: Use a more general selector that works for ALL pages ---
#         # The 'internship_list_container' class is present on all pages, unlike the specific ID.
#         job_list_container = soup.find('div', class_="internship_list_container")
        
#         if not job_list_container:
#             print("   - No job list container found on this page. It might be the last page.")
#             break

#         # Find all job cards within that container
#         job_cards = job_list_container.find_all('div', class_='individual_internship')
        
#         # A final check to see if any actual cards were found inside the container
#         if not job_cards:
#             print("   - Container found, but no job cards inside. Stopping scraper.")
#             break

#         print(f"   - Found {len(job_cards)} potential listings.")

#         for card in job_cards:
#             try:
#                 # --- Intelligent Ad Skipping ---
#                 # Check for the presence of a company name to distinguish jobs from ads.
#                 if not card.find('div', class_='company_name'):
#                     print("     - Skipping a non-job card (likely an ad or promoted course).")
#                     continue
                
#                 title_element = card.find('a', class_='job-title-href')
#                 job_title = title_element.get_text(strip=True)
#                 detail_link = "https://internshala.com" + title_element['href']

#                 company = card.find('p', class_='company-name').get_text(strip=True)
#                 location = card.find('p', class_='locations').get_text(strip=True)
                
#                 salary_element = card.find('span', class_='desktop')
#                 salary = salary_element.get_text(strip=True) if salary_element else "Not Disclosed"
                
#                 experience = "Not Specified"
#                 exp_element = card.find('i', class_='ic-16-briefcase')
#                 if exp_element and exp_element.find_next_sibling('span'):
#                     experience = exp_element.find_next_sibling('span').get_text(strip=True)
                
#                 # --- Fetching skills from the detail page ---
#                 skills = "Not Specified"
#                 try:
#                     # Optional: Add a small print statement to see progress
#                     # print(f"     - Fetching skills for: {job_title}")
#                     detail_page_response = requests.get(detail_link, headers=headers, timeout=10)
#                     if detail_page_response.status_code == 200:
#                         detail_soup = BeautifulSoup(detail_page_response.content, 'html.parser')
#                         skills_container = detail_soup.find('div', class_='round_tabs_container')
#                         if skills_container:
#                             skill_tags = skills_container.find_all('span', class_='round_tabs')
#                             skills = ', '.join([tag.get_text(strip=True) for tag in skill_tags])
                    
#                     # A polite pause to avoid overwhelming the server
#                     time.sleep(0.5) 
#                 except Exception as e:
#                     print(f"     - Could not fetch skills for {job_title}. Error: {e.__class__.__name__}")

#                 print(f"     ✅ Scraped: '{job_title}'")
                
#                 job_data.append({
#                     "Job Title": job_title, "Company": company, "Skills": skills,
#                     "Location": location, "Salary": salary, "Experience": experience, "Link": detail_link
#                 })

#             except Exception as e:
#                 print(f"     - Error processing a job card, skipping. Error: {e.__class__.__name__}")
#                 continue
        
#     if not job_data:
#         print("\n\n❌ No data was successfully scraped.")
#         return

#     df = pd.DataFrame(job_data)
#     df.drop_duplicates(subset=['Job Title', 'Company', 'Location'], keep='first', inplace=True)
   
#     df.to_csv("data/internshala_jobs.csv", index=False)

#     print(f"\n\n✅ Scraping complete. Successfully cleaned and saved {len(df)} unique jobs.")
#     print(f"📁 Data saved to {"data/internshala_jobs.csv"}")

# if __name__ == "__main__":
#     # Scrape a larger number of pages
#     scrape_internshala_jobs(max_pages=2)



# scrape_jobs.py (Corrected requests-only version with "Posted" Date)

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from pathlib import Path

def scrape_internshala_jobs(max_pages=189): # Set a high limit; the script will stop itself intelligently.
    """
    Scrapes all job details from Internshala using a robust requests-based approach.
    - Includes the 'Posted' date.
    - Intelligently stops by checking the 'Next' button's status.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    job_data = []

    for page in range(1, max_pages + 1):
        url = f"https://internshala.com/jobs/page-{page}/" if page > 1 else "https://internshala.com/jobs/"
        print(f"\n🔄 Scraping page {page}: {url}")
        
        try:
            response = requests.get(url, headers=headers, timeout=20)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"⚠️  Could not fetch page {page}. Stopping scraper. Error: {e}")
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        
        job_list_container = soup.find('div', class_="internship_list_container")
        if not job_list_container:
            print("   - No job list container found on this page. Assuming this is the end.")
            break

        job_cards = job_list_container.find_all('div', class_='individual_internship')
        if not job_cards:
            print("   - Container found, but no job cards inside. Stopping scraper.")
            break
            
        print(f"   - Found {len(job_cards)} potential listings.")

        for card in job_cards:
            try:
                if not card.find('div', class_='company_name'):
                    print("     - Skipping a non-job card (likely an ad or promoted course).")
                    continue
                
                title_element = card.find('a', class_='job-title-href')
                job_title = title_element.get_text(strip=True)
                detail_link = "https://internshala.com" + title_element['href']

                company = card.find('p', class_='company-name').get_text(strip=True)
                location = card.find('p', class_='locations').get_text(strip=True)
                
                salary_element = card.find('span', class_='desktop')
                salary = salary_element.get_text(strip=True) if salary_element else "Not Disclosed"
                
                experience = "Not Specified"
                exp_element = card.find('i', class_='ic-16-briefcase')
                if exp_element and exp_element.find_next_sibling('span'):
                    experience = exp_element.find_next_sibling('span').get_text(strip=True)
                
                # --- KEY CHANGE: Added "Posted" date scraping back in ---
                posted = "N/A"
                try:
                    # This selector is robust and finds the date regardless of 'status-success' or 'status-info'
                    posted_element = card.find(lambda tag: tag.name == 'div' and ('status-success' in tag.get('class', []) or 'status-info' in tag.get('class', [])))
                    if posted_element:
                        posted = posted_element.get_text(strip=True)
                except Exception:
                    pass # Default to "N/A" if it fails

                skills = "Not Specified"
                try:
                    detail_page_response = requests.get(detail_link, headers=headers, timeout=10)
                    if detail_page_response.status_code == 200:
                        detail_soup = BeautifulSoup(detail_page_response.content, 'html.parser')
                        skills_container = detail_soup.find('div', class_='round_tabs_container')
                        if skills_container:
                            skill_tags = skills_container.find_all('span', class_='round_tabs')
                            skills = ', '.join([tag.get_text(strip=True) for tag in skill_tags])
                    time.sleep(0.5) 
                except Exception as e:
                    print(f"     - Could not fetch skills for {job_title}. Error: {e.__class__.__name__}")

                print(f"     ✅ Scraped: '{job_title}'")
                
                job_data.append({
                    "Job Title": job_title, "Company": company, "Skills": skills,
                    "Location": location, "Salary": salary, "Experience": experience,
                    "Posted": posted, # Added the 'Posted' column here
                    "Link": detail_link
                })

            except Exception as e:
                print(f"     - Error processing a job card, skipping. Error: {e.__class__.__name__}")
                continue

        # --- Intelligent "Last Page" Check ---
        pagination_div = soup.find('div', id='pagination')
        if pagination_div:
            next_button = pagination_div.find('a', id='navigation-forward')
            if next_button and 'disabled' in next_button.get('class', []):
                print("\n✅ 'Next' button is disabled. This was the final page. Stopping scraper.")
                break
        else:
            print("\n✅ No pagination found. Assuming single page of results. Stopping scraper.")
            break
        
    if not job_data:
        print("\n\n❌ No data was successfully scraped.")
        return

    df = pd.DataFrame(job_data)
    df.drop_duplicates(subset=['Job Title', 'Company', 'Location'], keep='first', inplace=True)
    
    output_path = Path("data/internshala_jobs.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"\n\n✅ Scraping complete. Successfully cleaned and saved {len(df)} unique jobs.")
    print(f"📁 Data saved to {output_path}")

if __name__ == "__main__":
    scrape_internshala_jobs(189)

