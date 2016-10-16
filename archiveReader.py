from BeautifulSoup import BeautifulSoup
import mechanize

def openBrowser():
    browser = mechanize.Browser()
    response = browser.open('https://www.washington.edu/students/timeschd/archive/')
    soup = BeautifulSoup(response.read())
    archiveTable = soup.findChildren('tbody')[0]
    yearInterval_List = archiveTable.findChildren('tr')
    for yearInterval in yearInterval_List:
        timeSchedule_List = yearInterval.findChildren('td')
        firstTD = timeSchedule_List[0]
        stringRep_TD = str(firstTD.get('class'))
        if (stringRep_TD == 'year'):
            print(firstTD.contents[0])




openBrowser()

