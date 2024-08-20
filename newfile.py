#CODED BY HARSHIT KHANDELWAL
import random
import time

print("WELCOME TO WORST FAKE PASSPORT GENERATOR")
print("Please follow the instructions carefully and start by typing in two first names, and two last names below;")

ffn=str(input("Enter first first name: "))
sfn=str(input("Enter second first name: "))
fln=str(input("Enter first last name: "))
sln=str(input("Enter second last name: "))

lffn=len(ffn)
lsfn=len(sfn)
lfln=len(fln)
lsln=len(sln)

if (lffn%2!=0 and lsfn%2!=0) or (lffn%2!=0 and lsfn%2==0):
    nfn=(ffn[0:int(lffn//2)+1] + sfn[int(lsfn//2):lsfn])
elif (lffn%2==0 and lsfn%2==0) or (lffn%2==0 and lsfn%2!=0):
    nfn=(ffn[0:int(lffn//2)] + sfn[int(lsfn//2):lsfn])
    
if (lfln%2!=0 and lsln%2!=0) or (lfln%2!=0 and lsln%2==0):
    nln=(fln[0:int(lfln//2)+1] + sln[int(lsln//2):lsln])
elif (lfln%2==0 and lsln%2==0) or (lfln%2==0 and lsln%2!=0):
    nln=(fln[0:int(lfln//2)] + sln[int(lsln//2):lsln])

fage=int(input("Please enter first age in years: "))
sage=int(input("Please enter second age in years: "))

sdfage=0
sdsage=0
soa=0
for i in str(fage):
    sdfage+=int(i)
for i in str(sage):
    sdsage+=int(i)
soa=sdfage+sdsage
date, month, year = time.strftime('%d,%m,%Y').split(',')
yr=int(year)-soa
if yr%4==0 and int(month)==2:
    ndob=(date+'/'+str(int(month)-1)+'/'+str(yr))
else:
    ndob=(date+'/'+month+'/'+str(yr))
ID=soa
while len(str(ID))<10:
    if len(str(ID))>=2:
        adl2=int(str(ID)[-1])+int(str(ID)[-2])
        ID=int(str(ID)+str(adl2%10))
    else:
        adl2=int(str(ID)[-1])+0
        ID=int(str(ID)+str(adl2%10))
        
print('\n\n\n\n\n**************************************************\n\t\tP A S S P O R T\n\nNAME: ',nfn.upper(),nln.upper(),'\tID: ',ID,'\n')
print('DOB: ',ndob,'\n')
print('Authorised by: DORA HE\n**************************************************')

print('\n\n\nEncryption')
def cipher(n):
    ciphered = ''
    for ltr in n:
        if ltr.isalpha():
            num = ord(ltr)
            num += random.randint(1,25)
            if (ltr.isupper()) and (num > ord('Z')):
                num -= 26
            elif (ltr.islower()) and (num > ord('z')):
                num -= 26
            ciphered += chr(num)
        else:
            ciphered += ltr
    return ciphered

print('**************************************************\n\t\tP A S S P O R T\n\nNAME: ',cipher(nfn).upper(),cipher(nln).upper(),'\tID: ',ID,'\n')
print('DOB: ',ndob,'\n')
print('Authorised by: DORA HE\n**************************************************')