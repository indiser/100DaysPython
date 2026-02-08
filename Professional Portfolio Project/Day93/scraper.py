import requests
from bs4 import BeautifulSoup
import os
import json
import time
import random

script_path = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_path, "Paper_data.json")


total_papers_needed = 2000
batch_size = 250
base_url = "https://arxiv.org/list/cs.AI/recent"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

papers_database = []

# Loop from 0 to 2000, stepping by 200 (0, 200, 400...)
for skip in range(0, total_papers_needed, batch_size):
    print(f"Scraping papers {skip} to {skip + batch_size}...")
    
    params = {
        "skip": skip,
        "show": batch_size
    }

    try:
        response = requests.get(base_url, headers=headers, params=params)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find(name="dl", id="articles")

        if not articles:
            print(f"No articles found at skip={skip}. Stopping.")
            break

        data_tables = articles.find_all(name="dt")
        main_element = articles.find_all(name="dd")

        for dt, dd in zip(data_tables, main_element):
            # Paper Number
            paper_numbers=dt.select_one(selector='a[title="Abstract"]')
            paper_number=paper_numbers.getText().strip() if paper_numbers else None

            # Direct Paper Link
            direct_link=f"https://arxiv.org{paper_numbers['href']}" if paper_numbers else None

            # HTML TAG
            html_tag=dt.select_one(selector='a[title="View HTML"]')
            html_link=html_tag["href"] if html_tag else None

            # PDF Link
            pdf_tag = dt.select_one('a[title="Download PDF"]')
            full_link = f"https://arxiv.org{pdf_tag['href']}" if pdf_tag else None

            # Other Formats
            other_tags=dt.select_one(selector='a[title="Other formats"]')
            other_links=f"https://arxiv.org{other_tags['href']}" if other_tags else None

            # Title
            title_tag = dd.select_one(selector="div.list-title")
            paper_title = title_tag.getText().replace("Title:", "").strip() if title_tag else "Unknown"

            # Authors
            author_div = dd.select_one(selector="div.list-authors")
            if author_div:
                author_tags = author_div.select("a")
                authors = [tag.getText() for tag in author_tags]
            else:
                authors = []
            
            # Subjects
            subjects_div = dd.select_one(selector="div.list-subjects")
            if subjects_div:
                subject_text = subjects_div.getText().replace("Subjects:", "").strip()
                subjects = [s.strip() for s in subject_text.split(";")]
            else:
                subjects = []
            
            obj = {
                "Paper Number": paper_number,
                "Paper Title": paper_title,
                "Direct Link":direct_link,
                "Pdf Link": full_link,
                "Html Link": html_link,
                "Other Formats": other_links,
                "Authors": authors,
                "Subjects": subjects
            }

            papers_database.append(obj)

        print(f"Batch complete. Total collected so far: {len(papers_database)}")
        
        time.sleep(random.uniform(2, 5))

    except Exception as e:
        print(f"Error occurred at skip={skip}: {e}")
        break

# Save Result
with open(filename, "w", encoding="utf-8") as filp:
    json.dump(papers_database, filp, indent=4, ensure_ascii=False)

print(f"Done. Successfully caught {len(papers_database)} Papers.")