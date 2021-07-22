import requests
from bs4 import BeautifulSoup
import all_jobs

f = open("python5.html", "w")

all_jobs = all_jobs.my_list
i=0

for job in all_jobs:
    i+=1

print(job)
url = job
response = requests.get(url)
soup     = BeautifulSoup(response.content, "html.parser")

details = soup.find_all("div", class_="job_description")
apply_here = soup.find_all(id="apply_button_gtm")

print(apply_here)

for detail in details:
    responsibility = detail.find_all("ul")[1]
    requirement = detail.find_all("ul")[2]
    for apply in apply_here:
        link = apply.get('href')

    f.write(f"{i}:{responsibility}")