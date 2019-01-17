# list=[]
# k=0
# value=()
# while not value == "/":
#     value = input("Enter a value: ")
#     list.append(value)
#
# print("Stopping input...")
# del(list[-1])
#
# if "butt" in list:
#     print("Yes, Butt is in the list.")
# else:
#     print("No, Butt is not in the list.")
#
# print("The list is: ")
# print(list)
#
# k=0
# for item in list:
#     print(list[k])
#     k+=1
#


#start second text
import string
import random

def GenName(size=6):
    return random.choice(string.ascii_uppercase) + ''.join(random.choice(string.ascii_lowercase) for _ in range(size))

def GenNum(max=9999):
    return random.randint(1,max)

orgs=[]
thisOrg=()
findOrg=""

k=0
while k < 5:
    # Generate test org
    orgName = str(GenName(10) + ' Family')
    orgAddr1 = str(GenNum(9999)) + ' ' + GenName(6) + ' St.'
    orgAddr2 = 'P.O. Box ' + str(GenNum(99999))
    orgCity = GenName(10)
    orgState = GenName(1).upper()
    orgZip = str(GenNum(79999) + 10000)
    orgTel = 'Not Listed'
    orgEmail = GenName(4).lower() + '@' + GenName(6).lower() + '.notreal'
    thisOrg = (orgName,orgAddr1,orgAddr2,orgCity,orgState,orgZip,orgTel,orgEmail)
    print(thisOrg)
    orgs.append(thisOrg)
    findOrg=thisOrg
    k+=1

print('\n' + '='*100)
print('\nThe full list of orgs is...')
print(orgs)
print('\n' + '='*100)
print('\nThe org we will find is: ' + str(findOrg))

if findOrg in orgs:
    print('true')
else:
    print('false')

print('\nIf we just search for the org name... ' + str(findOrg[0]))

if findOrg[0] in orgs:
    print('true')
else:
    print('false')
