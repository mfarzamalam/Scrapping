import requests
from bs4 import BeautifulSoup

url = "https://remote.co/remote-jobs/developer/"
response = requests.get(url)
soup     = BeautifulSoup(response.content, "html.parser")

f = open("python4.html", "w")
# f.write(soup.prettify())

results  = soup.find(class_="card bg-white m-0")
all_jobs = results.find_all("a", class_="card m-0 border-left-0 border-right-0 border-top-0 border-bottom")
# print(len(all_jobs))


f = open("result4.html", "w")
i = 0
for all_job in all_jobs:
    i+=1
    link        = all_job.find("span", class_="font-weight-bold")
    posted_time = all_job.find("small")
    for link in all_job:
        details     = link.find_all("a")[0]["href"]
        print(f"{i}", details)
    # print(f"{i}",link.text)
    # print(f"{i}", posted_time.text)