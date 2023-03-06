import requests
import sqlite3
from bs4 import BeautifulSoup

INSERT_QUERY = "INSERT INTO jobs(title, company, loc) VALUES(?,?,?)"

URL = "https://realpython.github.io/fake-jobs"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")

if __name__ == "__main__":
    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")

        con = sqlite3.connect("jobs.db")
        cur = con.cursor()
        cur.execute(
            INSERT_QUERY,
            [
                title_element.text.strip(),
                company_element.text.strip(),
                location_element.text.strip(),
            ],
        )

        print(title_element.text.strip())
        print(company_element.text.strip())
        print(location_element.text.strip())
        print()

        con.commit()
        con.close()
