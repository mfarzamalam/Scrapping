import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_="card-content")


f = open("result2.html", "w")

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    # f.write(str(title_element.text))
    # f.write("\n")
    # f.write(str(company_element.text))
    # f.write("\n")
    # f.write(str(location_element.text.strip()))
    # f.write("\n"+"\n")



python_job   = results.find_all("h2", string= lambda text: "python" in text.lower())
# print(len(python_job))

f = open("python.html", "w")
for job in python_job:
    # f.write(str(job))
    # f.write("\n")
    pass



python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_job
]

f = open("result2.html", "w")

i = 0
for job_element in python_job_elements:
    i+=1
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    # link_apply       = job_element.find_all("a", string = lambda text: "apply" in text.lower())
    link_apply       = job_element.find_all("a")[1]["href"]

    f.write(f"ID:{i}")
    f.write("\n")
    f.write(str(title_element.text))
    f.write("\n")
    f.write(str(company_element.text))
    f.write("\n")
    f.write(str(location_element.text.strip()))
    f.write("\n")
    
    # for link_apply in link_apply:
    #     link_url = link_apply["href"]

    # f.write(str(f"Apply here: {link_url}"))
    f.write(str(f"Apply here: {link_apply}"))
    f.write("\n\n\n")

# with open("home.html", "w") as f:
#     f.write(str(job_elements))