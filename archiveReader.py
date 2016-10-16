from BeautifulSoup import BeautifulSoup
import collections
import csv
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
            if int(str(firstTD.contents[0][:4].encode('utf-8'))) >= 2014:
                quarterLinks_List = timeSchedule_List[1].findChildren('a')
                yearURL_Map[str(firstTD.contents[0].encode('utf-8'))] = {}
                for quarter in quarterLinks_List:
                    quarter_String = str(quarter.string.encode('utf-8'))
                    quarter_Link = quarter.get('href')
                    yearURL_Map[str(firstTD.contents[0].encode('utf-8'))][quarter_String] = "https://www.washington.edu" + str(quarter_Link.encode('utf-8'))
    browser.close()

    return yearURL_Map

def getMajor(yearURL_Map):
    browser = mechanize.Browser()
    majorCourse_Map = collections.OrderedDict()
    with open('result.csv','wb') as _file:
        csv_writer = csv.writer(_file)
        headerRow = ['Course Number', 'Full Course Name', 'Quarter','Year','Type','Department','Abbreviation']
        csv_writer.writerow(headerRow)
        for yearInterval in yearURL_Map:
            for quarter in yearURL_Map[yearInterval]:
                print quarter
                soup = BeautifulSoup(browser.open(yearURL_Map[yearInterval][quarter]).read())
                liElement_List = soup.findChildren('li')
                for li in liElement_List:
                    major_HTML = li.findChildren('a')
                    if len(major_HTML) > 0:
                        major_HTML = major_HTML[0]
                        majorName =  str(major_HTML.string.encode('utf-8'))
                        if("&nbsp;" in majorName):
                            majorName = majorName[:majorName.find('&')] + " " + majorName[majorName.find('&')+6:]
                        if("&amp;" in majorName):
                            majorName = majorName[:majorName.find('&')] + "&" + majorName[majorName.find('&')+5:]
                        if major_HTML.get('href'):
                            major_URL = yearURL_Map[yearInterval][quarter] + major_HTML.get('href')
                            major_HTML_String = str(major_HTML)
                            if 'http' not in major_HTML_String and '.html' in major_HTML_String:
                                if 'CSE' in majorName:
                                    majorCourse_Map[majorName] = {}
                                    pageOK = True
                                    #try:
                                    try:
                                        response = browser.open(major_URL)
                                    except:
                                        pageOK = False
                                    if pageOK:
                                        courseSoup = BeautifulSoup(response.read())
                                        tableSoup = courseSoup.findChildren('table')
                                        print tableSoup
                                        for table in tableSoup:
                                            if isinstance(table.get('bgcolor'), unicode):
                                                if str((table.get('bgcolor')).encode('utf-8')) == '#ffcccc' or str((table.get('bgcolor')).encode('utf-8')) == '#ccffcc' or str((table.get('bgcolor')).encode('utf-8')) == '#99ccff'\
                                                        or str((table.get('bgcolor')).encode('utf-8')) == '#ffffcc':
                                                    courseName = ""
                                                    type_HTML = table.findChildren('td')[1].findChild('b')
                                                    type = ""
                                                    if type_HTML.string:
                                                        type = type_HTML.string
                                                    try:
                                                        courseName = str(
                                                            table.findChild('tr').findChild('td').findChild('b').findChild(
                                                                'a').string.encode('utf-8'))
                                                    except:
                                                        courseName = "n/a"

                                                    fullCourseName = "n/a"
                                                    try:
                                                        fullCourseName = table.findChild('tr').findChild('td').findChild('b').findChildren('a')[1].string.encode('utf-8')
                                                    except:
                                                        fullCourseName = "n/a"
                                                    courseName = courseName[:len(courseName)-1]
                                                    courseName = courseName.replace("&nbsp;", "")
                                                    majorCourse_Map[majorName][courseName] = {}
                                                    if type:
                                                        majorCourse_Map[majorName][courseName]['type'] = type
                                                    else:
                                                        majorCourse_Map[majorName][courseName]['type'] = "n/a"
                                                    majorCourse_Map[majorName][courseName]['year'] = yearInterval
                                                    courseNumber = courseName[courseName.rfind(' ')+1:]
                                                    majorCourse_Map[majorName][courseName]['course-number'] = courseNumber
                                                    majorAbbrv = courseName[:courseName.find(' ')]
                                                    abbrvQuarter = quarter[:quarter.find(' ')]
                                                    majorCourse_Map[majorName][courseName]['abbrv'] = majorAbbrv
                                                    majorCourse_Map[majorName][courseName]['course-name'] = fullCourseName
                                                    majorCourse_Map[majorName][courseName]['quarter'] = abbrvQuarter
                                                    fullMajorName = majorName[:majorName.find(' ')]
                                                    majorCourse_Map[majorName][courseName]['department'] = fullMajorName
                                                    row = []
                                                    row.append(courseNumber)
                                                    row.append(fullCourseName)
                                                    row.append(abbrvQuarter)
                                                    row.append(yearInterval)
                                                    row.append(type)
                                                    row.append(fullMajorName)
                                                    row.append(majorAbbrv)
                                                    csv_writer.writerow(row)





yearURL_Map = getURLs()
getMajor(yearURL_Map)

