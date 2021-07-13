import requests
from bs4 import BeautifulSoup

url = "https://pythonjobs.github.io/"
response = requests.get(url)
soup     = BeautifulSoup(response.content, "html.parser")

# f = open("python3.html", "w")
# f.write(soup.prettify())


result = soup.find(id="main")
all_jobs = result.find_all("div", class_="job")

# f = open("python3.html", "w")
# f.write(str(all_jobs))

f = open("result3.html", "w")

for all_job in all_jobs:
    title = all_job.find("h1")
    location = all_job.find("i", class_="i-globe")
    date     = all_job.find("i", class_="i-calendar")
    timing   = all_job.find("i", class_="i-chair")
    company  = all_job.find("i", class_="i-company")
    desc     = all_job.find("p", class_="detail")
    apply    = all_job.find_all("a")[0]["href"]
    print(""+apply)

    f.write(f"Title:{title.text}\n")
    f.write(f"Location:{location.parent.text.title()}\n")
    f.write(f"Date:{date.parent.text}\n")
    f.write(f"Timing:{timing.parent.text.title()}\n")
    f.write(f"Company:{company.parent.text}\n")
    f.write(f"Description:{desc.text}\n")
    f.write(f"Apply here:{url+apply}\n\n\n")