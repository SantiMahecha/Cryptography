#@Santiago Mahecha Pinzón
#smahechap@unal.edu.co

import numpy as np

print("-------------------------------------------------------HILL CIPHER ALGORITHM----------------------------------------------------------\n")

def create_matrix(rows,columns,initial):
    return [[initial for i in range(rows)]for j in range(columns)]

l = 65
abc_num = create_matrix(26,1,0)
for i in range(0,26):
  abc_num[0][i]=chr(l)
  l+=1

key = create_matrix(2,2,0)
for m in range(0,2):
  for n in range (0,2):
    key[m][n] = int(input(f"Input the {n} element of the {m} row of the key (KEY): "))

print("\n")
print("KEY: ")
print(key)

def locindex(c): #Get location of each character.
    loc=list()
    for i ,j in enumerate(abc_num):
        #print(i,j)
        for m,n in enumerate(j):
            #print(m,n)
            if c == n:
                loc.append(i)
                loc.append(m)
                return loc

def MIM(mx):
  detKey = (mx[0][0]*mx[1][1])-(mx[0][1]*mx[1][0])
  #print(detKey)
  adjKey = create_matrix(2,2,0)
  adjKey[0][0] = mx[1][1]
  adjKey[1][1] = mx[0][0]
  adjKey[0][1] = -(mx[1][0])
  adjKey[1][0] = -(mx[0][1])
  m = (detKey)%26
  Ki = create_matrix(2,2,0)
  Ki[0][0] = (m*(adjKey[0][0]))%26
  Ki[1][1] = (m*(adjKey[1][1]))%26
  Ki[0][1] = (m*(adjKey[1][0]))%26
  Ki[1][0] = (m*(adjKey[0][1]))%26
  return Ki

def encrypt():
  message = str(input("Input the plain text: "))
  message = message.upper()
  message = message.replace(" ","")

  if len(message)%2!=0:
    message=message[:]+'X'

  print("PLAIN TEXT: ",message)

  print("CIPHER TEXT: ",end='')
  for i in range (0,len(message),2):
    locA = locindex(message[i])
    locB = locindex(message[i+1])
    A = locA[1] * key[0][0]
    B = locB[1] * key[1][0]
    C = locA[1] * key[0][1]
    D = locB[1] * key[1][1]
    cipherA = ((A+B)%26)
    cipherB = ((C+D)%26)
    print("{}{}".format(chr(65+cipherA),chr(65+cipherB)),end='')

def decrypt():
  inv = MIM(key)
  print("Inverse matrix (Key -1):\n",inv)

  message = str(input("Input the cipher text: "))
  message = message.upper()
  message = message.replace(" ","")

  print("CIPHER TEXT: ",message)

  print("PLAIN TEXT: ",end='  ')
  for i in range (0,len(message),2):
    locA = locindex(message[i])
    locB = locindex(message[i+1])
    A = locA[1] * inv[0][0]
    B = locB[1] * inv[1][0]
    C = locA[1] * inv[0][1]
    D = locB[1] * inv[1][1]
    plainA = ((A+B)%26)
    plainB = ((C+D)%26)
    print("{}{}".format(chr(65+plainA),chr(65+plainB)),end='')

e = 1    
while(e == 1):
    print("\n\nChoose an action to realize:")
    choice=int(input("\n 1.Encrytion \n 2.Decryption \n 3.Exit\n"))
    print("\n")

    if choice==1:
        encrypt()
    elif choice==2:
        decrypt()
    elif choice==3:
        e = 0
    else:
        print("Choose a correct answer\n")  
