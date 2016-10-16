from BeautifulSoup import BeautifulSoup
import collections
import csv
import mechanize

# [aut, win, spr, sum]
# [0  , 1  , 2  , 3  ]

# Code to find quarters by frequency / majority
# def openCSV():
#     class_Map = collections.OrderedDict()
#
#     with open('result.csv','rb') as csvfile:
#         reader = csv.reader(csvfile)
#         header = reader.next()
#         for row in reader:
#             # Reads each row of CSV file.
#             if row[0] not in class_Map.keys():
#                 class_Map[row[0]] = [0,0,0,0]
#             quarter = row[2]
#             if quarter == 'AUT':
#                 class_Map[row[0]][0] += 1
#             elif quarter == 'WIN':
#                 class_Map[row[0]][1] += 1
#             elif quarter == 'SPR':
#                 class_Map[row[0]][2] += 1
#             elif quarter == 'SUM':
#                 class_Map[row[0]][3] += 1
#     for classNumber in class_Map:
#         print classNumber,
#         maxFreq = max( class_Map[classNumber] )
#         maxIndices = [i for i, j in enumerate(class_Map[classNumber]) if j == maxFreq]
#         for index in maxIndices:
#             if index == 0:
#                 print 'AUT',
#             elif index == 1:
#                 print 'WIN',
#             elif index == 2:
#                 print 'SPR',
#             elif index == 3:
#                 print 'SUM',
#         print

def getPrereqs():
    browser = mechanize.Browser()
    response = browser.open('https://www.washington.edu/students/crscat/cse.html')
    soup = BeautifulSoup(response.read())
    aList = soup.findChildren('a')

    class_Map = collections.OrderedDict()
    classOptions = []
    htmlText = ""

    for a in aList:
        className = ""
        preReq_String = ""
        if len(classOptions) > 0:
            class_Map[htmlText.get('name')].append(classOptions)
            classOptions = []
        if a.get('name'):
            class_Map[a.get('name')] = []
            classDescription = str( a.findChild('p') )
            if classDescription.find('Prerequisite') > 0:
                classLetter_index = 0
                if classDescription.find('Offered') > 0:
                    preReq_String = classDescription[classDescription.find('Prerequisite'):classDescription.find('Offered')]
                else:
                    preReq_String = classDescription[classDescription.find('Prerequisite'):]
                for index in range(len(preReq_String)):
                    letter = preReq_String[index]
                    if letter.isupper():
                        if classLetter_index == 0:
                            classLetter_index = index
                            className += letter
                        else:
                            className += letter
                    else:
                        if classLetter_index != 0 and len(className) > 1:
                            preReq_Class = className + preReq_String[index:index+5]
                            if preReq_Class[len(preReq_Class)-1] == ';':
                                if hasNumbers(preReq_Class):
                                    class_Map[a.get('name')].append(preReq_Class[:len(preReq_Class)-1])
                            else:
                                if hasNumbers(preReq_Class):
                                    classOptions.append(preReq_Class[:len(preReq_Class)-1])

                            className = ""
                            classLetter_index = 0
                        elif classLetter_index != 0:
                            className = ""
                            classLetter_index = 0
                        if classLetter_index == 0:
                            className = ""
        htmlText = a

    # for i in class_Map:
    #     print i
    #     print '\t',
    #     print class_Map[i]
    return class_Map


def hasNumbers(className):
    return any(char.isdigit() for char in className)

def openCSV(preReq_Map):
    class_Map = collections.OrderedDict()
    with open('result.csv','rb') as csvfile:
        reader = csv.reader(csvfile)
        header = reader.next()
        for row in reader:
            if row[0] not in class_Map.keys():
                class_Map[row[0]] = {}
                class_Map[row[0]]['quarter'] = []
                class_Map[row[0]]['prereq'] = []
            quarter = row[2]
            preReq_Key = 'cse' + str(row[0])
            if preReq_Key in preReq_Map.keys():
                if len(class_Map[row[0]]['prereq']) == 0:
                    class_Map[row[0]]['prereq'] = preReq_Map[preReq_Key]
            if quarter not in class_Map[row[0]]['quarter']:
                class_Map[row[0]]['quarter'].append(quarter)



    with open('preReq_freq.csv','wb') as csvfile:
        printRow = []
        csv_writer = csv.writer(csvfile)
        for classNum in class_Map.keys():
            printRow.append("CSE" + " " + str(classNum))
            printRow.append(class_Map[classNum].get('quarter'))
            printRow.append(class_Map[classNum].get('prereq'))
            csv_writer.writerow(printRow)
            printRow = []




class_Map = getPrereqs()
openCSV(class_Map)
