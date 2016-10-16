from BeautifulSoup import BeautifulSoup
import collections
import mechanize

def getURLs ():
    yearURL_Map = collections.OrderedDict()

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
            if int(str(firstTD.contents[0][:4].encode('utf-8'))) >= 2011:
                quarterLinks_List = timeSchedule_List[1].findChildren('a')
                yearURL_Map[str(firstTD.contents[0].encode('utf-8'))] = {}
                for quarter in quarterLinks_List:
                    quarter_String = str(quarter.string.encode('utf-8'))
                    quarter_Link = quarter.get('href')
                    yearURL_Map[str(firstTD.contents[0].encode('utf-8'))][quarter_String] = "https://www.washington.edu" + str(quarter_Link.encode('utf-8'))


    for yearInterval in yearURL_Map:
        print yearInterval
        for quarter in yearURL_Map[yearInterval]:
            print "\t" + quarter + " " + yearURL_Map[yearInterval][quarter]
getURLs()

