import requests
from bs4 import BeautifulSoup

f = open("all_jobs.txt", "w")

website = "https://remote.co/"
url = "https://remote.co/remote-jobs/developer/"
response = requests.get(url)
soup     = BeautifulSoup(response.content, "html.parser")

all_jobs = soup.find_all("a", class_="card m-0 border-left-0 border-right-0 border-top-0 border-bottom")
print(len(all_jobs))
i = 0
j = 0
k = 0

for job in all_jobs:
    i+=1
    urls  = website+job.get('href')
    response = requests.get(urls)
    soup     = BeautifulSoup(response.content, "html.parser")

    title   = soup.find("h1", class_="font-weight-bold").text
    job_type= soup.find("span", class_="location_sm").text
    posted  = soup.find("time").text
    details = soup.find_all("div", class_="job_description")
    apply_here = soup.find_all(id="apply_button_gtm")
    j = 0
    k = 0

    f.write(f"({i})")
    f.write(f"URl: {urls}\n")
    f.write(f"Title: {title}\n")
    f.write(f"Posted: {posted}\n")
    f.write(f"Job-Type: {job_type}\n")

    for detail in details:
        try:
            f.write("\nResponsiblities:\n")
            responsibility = detail.find_all("ul")[1]
            for children in responsibility.find_all("li"):
                j += 1
                f.write(f"{j}-{children.text}\n")

            f.write("\nRequirements:\n")
            requirement = detail.find_all("ul")[2]
            for children in requirement.find_all("li"):
                k += 1
                f.write(f"{k}-{children.text}\n")
        except:
            pass

        for apply in apply_here:
            link = apply.get('href')
            f.write(f"\nApply-Here: {link}\n\n\n\n")

    print(i)