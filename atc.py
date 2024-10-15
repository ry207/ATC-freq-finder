from bs4 import BeautifulSoup
import requests
from rich import print

def search(type):
    # --------------PAGE 1---------------

    url = f"https://www.liveatc.net/search/?icao={type}"
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    job_elements = soup.find_all('table', class_='freqTable')

    print(url)
    print("\n\n")

    for job_element in job_elements:
        categories = job_element.find('b')
        name = job_element.find('td', class_='td1')
        text = "1"
        tr = job_element.find_all('tr')

        #print("NAME: ", name.text)
        #print("PHONE:", phone.text)
        #print(job_element.text)
        try:
            print("\n")
            print("[bold green]-[/bold green]"*50)
            print("NAME: ", name.text)
        except:
            pass
        try:
            for t in tr:
                print(t.text)
            #print("FREQUENCY: ", tr)

            print("[bold green]-[/bold green]"*50)

        except:
            pass



print("Welcome\nEnter your search in this format:captain+america or Food+in+Atlanta")
type = input("\n\n\nSearch word(XXX or XXXX): ")
print("\n\n")
search(type)
