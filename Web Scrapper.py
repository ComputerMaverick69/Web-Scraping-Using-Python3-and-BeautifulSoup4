from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv

try:
    max = 20
    #Get the page elements into a variable   
    page = urlopen(Request('https://stackoverflow.com/questions', headers={'User-Agent': 'Mozilla/5.0'})).read()

    #create a BeautifulSoup Object
    soup = BeautifulSoup(page, 'html5lib')

    #Create a File to write your data to and add header rows
    csv_file = csv.writer(open('stackoverflow-latest.csv', 'w'))
    csv_file.writerow(['Question', 'Link'])

    #Print the Page Title using the HTML title tag
    page_title = soup.title.string
    print(page_title + "\n")

    #Get the list of all the latest titles using their css class
    latest_titles = soup.findAll(class_='question-hyperlink')
    asked_by = soup.findAll('div', class_='user-details')

    #Print the values of latest_titles by iterating through the entire result
    #Print their links as well using their href attribute
    for latest_title, link in zip(latest_titles, latest_titles):
        #print("\n" + latest_title.text.strip())
        #print(link.get('href'))

        questions = latest_title.text.strip()
        links = link.get('href')

        #Add each question and link to a row
        csv_file.writerow([questions, links])
    
except Exception as e:
    print (e)
