from bs4 import BeautifulSoup

with open("D:/Codes/Projects/My_Resume_p/Portfolio.html",'r') as html_file:
    content =  html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('div','div', class_ = "reference")
    for tag in tags:
        tag_details = tag.p
        print(tag_details)