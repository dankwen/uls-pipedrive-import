#  =======================================================
#  Pipedrive Data Converter for ULS
#  Created by Dan Wenger (github/dankwen)
#  Date 13 Jan 2019
#  -------------------------------------------------------
#  Data will be converted from one database output CSV
#  into four separate pipe-delimited text files which can
#  be imported to Excel, then imported to Pipedrive
#  =======================================================


#  IMPORT  ===============================================
from csv import reader

#  OPEN FILE  ============================================
#  Open the file and return file read errors
file = "Results.csv"
try:
    infile = open(file, "r")
except FileNotFoundError:
    print("File not found " + file)
    raise
except IOerror:
    print("could not open the file " + file)
    raise
print("File opened... " + str(file))

#  PARSING FUNCTION  =====================================
#  Create lists of tuples for our data build and add first line data keys
orgs = [('Org Name','Owner','Visible To','Address')]
people = [('Family Role','Name','Phone','Email','Organization','Owner','Visible To')]
deals = [('Year Applying For','Grade','Deal Title','Creator','Owner','Organization','Pipeline')]
activities = [('Subject','Done Date','Deal')]

#  Create tuples for our data processing
thisOrg = ()
thisStudent = ()
thisParent1 = ()
thisParent2 = ()
thisDeal = ()
thisAction = ()

#  Create other variables needed
thisOrgName = 'Initial Name'
thisOrgAddress = '123 test street'
thisStudentName = 'Student Name'
thisDealName = 'Deal Name'

#  Begin the line parsing  ------------------------------

for line in reader(infile):

    #  Build a few variables out of the data in this line
    thisOrgName = line[1] + ' Family'

    if line[11]:  #  If address 2 is filled, this line runs
        thisOrgAddress = str(line[10]) + ', ' + \
                         str(line[11]) + ', ' + \
                         str(line[12]) + ', ' + \
                         str(line[13]) + ', ' + \
                         str(line[14])
    elif line[10]:  #  If address 1 is filled, this line runs
        thisOrgAddress = str(line[10]) + ', ' + \
                         str(line[12]) + ', ' + \
                         str(line[13]) + ', ' + \
                         str(line[14])
    else:  #  There is no address
        thisOrgAddress = ''

    if line[3]:  #  If there is a preferred name, we run this line
        thisStudentName = line[3] + ' ' + line[1]
        thisDealName = line[1] + ', ' + line[3] + ' ' + str(line[4])
    else:
        thisStudentName = line[2] + ' ' + line[1]
        thisDealName = line[1] + ', ' + line[2] + ' ' + str(line[4])

    #  Now build the tuples from this line
    thisOrg = (thisOrgName,'Angie Wenger','Entire Company',thisOrgAddress)
    thisStudent = ('Student',thisStudentName,'',thisOrgName,'Angie Wenger','Entire Company')
    thisParent1 = ('Guardian',(line[8] + ' ' + line[1]),line[15],thisOrgName,'Angie Wenger','Entire Company')
    thisParent2 = ('Guardian',(line[9] + ' ' + line[1]),line[16],thisOrgName,'Angie Wenger','Entire Company')
    thisDeal = (str(line[0]),str(line[4]),thisDealName,'Angie Wenger','Angie Wenger',thisOrgName,'Admissions Process')
    thisAction = (line[21],line[20],thisDealName)

    #  Now add the tuples to the list if they are unique
    if thisOrg not in orgs:
        orgs.append(thisOrg)
    if thisStudent not in people:
        people.append(thisStudent)
    if thisParent1 not in people:
        people.append(thisParent1)
    if thisParent2 not in people:
        people.append(thisParent2)
    if thisDeal not in deals:
        deals.append(thisDeal)
    if thisAction not in activities:
        activities.append(thisAction)

infile.close()
print('\nInput file closed... ' + str(file))

#  OUTPUT AND CLOSE  =====================================
#  Output Orgs -------------------
print('='*50 + '\n')
outOrgsFile = open('orgs_output.txt', 'w')
print('Writing orgs_output.txt...')
print('-'*50)
tsvItem=[]
for item in orgs:
    tsvItem=str(item)[2:-2].replace("', '",'|')
    print(tsvItem)
    outOrgsFile.write(tsvItem + '\n')
outOrgsFile.close()
print('-'*50)
print('Closing orgs_output.txt...')
print('='*50 + '\n')


#  Output People -----------------
print('='*50 + '\n')
outPeopleFile = open('people_output.txt', 'w')
print('Writing people_output.txt...')
print('-'*50)
tsvItem=[]
for item in people:
    tsvItem=str(item)[2:-2].replace("', '",'|')
    print(tsvItem)
    outPeopleFile.write(tsvItem + '\n')
outPeopleFile.close()
print('-'*50)
print('Closing people_output.txt...')
print('='*50 + '\n')


#  Output Deals -----------------
print('='*50 + '\n')
outDealsFile = open('deals_output.txt', 'w')
print('Writing deals_output.txt...')
print('-'*50)
tsvItem=[]
for item in deals:
    tsvItem=str(item)[2:-2].replace("', '",'|')
    print(tsvItem)
    outDealsFile.write(tsvItem + '\n')
outDealsFile.close()
print('-'*50)
print('Closing deals_output.txt...')
print('='*50 + '\n')


#  Output Activities -----------------
print('='*50 + '\n')
outActivitiesFile = open('activities_output.txt', 'w')
print('Writing activities_output.txt...')
print('-'*50)
tsvItem=[]
for item in activities:
    tsvItem=str(item)[2:-2].replace("', '",'|')
    print(tsvItem)
    outActivitiesFile.write(tsvItem + '\n')
outActivitiesFile.close()
print('-'*50)
print('Closing activities_output.txt...')
print('='*50 + '\n')



#  Exit the Program ==========================================
exit()
