from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://www.mygov.in/covid-19/"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
label = page_soup.find("div", {"class": "info_label"})
status = page_soup.findAll("span", {"class": "icount"})
#print(len(status))
TotalCases = status[0]
ActiveCases = status[1]
Discharged = status[2]
Deaths = status[3]
print("Total Cases: "+TotalCases.text)
print("Active Cases: "+ActiveCases.text)
print("Discharged: "+Discharged.text)
print("Deaths: "+Deaths.text)
print()
St_name = page_soup.findAll("span", {"class": "st_name"})
st_number = page_soup.findAll("span", {"class": "st_number"})
tick_confirmed = page_soup.findAll("div", {"class": "tick-confirmed"})
tick_active = page_soup.findAll("div", {"class": "tick-active"})
tick_death= page_soup.findAll("div", {"class": "tick-death"})

for i in range(len(st_number)):
    print("State Name: "+St_name[i].text)
    print("State Number: "+str(i+1))
    print(tick_confirmed[i].text)
    print(tick_active[i].text)
    print(tick_death[i].text)
    print()