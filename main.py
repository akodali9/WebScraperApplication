from bs4 import BeautifulSoup
import requests

# to get the new python job requirements

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')

jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
valid = 0
unfamiliar_skill = input('Put Some Skill That you Are not Familiar with \n>').split(" ")
print(f"Filtering out..............{unfamiliar_skill}")


for job in jobs:
    published_date = job.find('span',class_ = "sim-posted").span.text.replace(' ','')
    if 'few' in published_date:
        company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ','')
        skills = job.find('span', class_="srp-skills").text.replace(' ','')
        more_info = job.header.h2.a['href']
        l = 0
        while l == len(unfamiliar_skill):
            if unfamiliar_skill[l] not in skills:
                valid = 1
            l=l+1
                
        if valid == 1:   
            print(f"Company Name: {company_name.strip()}")
            print(f"Required Skills: {skills.strip()}")
            print(f"More Info: {more_info}")

            print("")