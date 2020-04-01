#@Santiago Mahecha Pinzón
#smahechap@unal.edu.co

print("-------------------------------------------------------PLAYFAIR CIPHER ALGORITHM----------------------------------------------------------\n")
key = str(input("Intoduzca la clave (key): "))
key = key.replace(" ", "")
key = key.upper()

print("\n")
print("KEY: ",key)
print("\n")

def create_matrix(rows,columns,initial):
    return [[initial for i in range(rows)]for j in range(columns)]

#print(list(key))
key_array=list()

for l in key: #Create matrix(key) that will be into main matrix.
    if l not in key_array:
        if l =='J' or l =='I':
          if 'IJ' in key_array:
            pass
          else:  
            key_array.append('IJ')
        else:
            key_array.append(l)

for l in range(65,91):#Fill matrix with key and alphabet.
  if chr(l) not in key_array:
    if l == 73 and 'IJ' not in key_array:
      key_array.append('IJ')
    elif l == 73 or l == 74:
      pass
    else: key_array.append(chr(l))

#print(key_array)

k=0
main_matrix = create_matrix(5,5,0) #Create main matrix
for i in range(0,5): #making main matrix
    for j in range(0,5):
        main_matrix[i][j] = key_array[k]
        k+=1

print("Matriz principal:\n",main_matrix,"\n")


def locindex(c): #Get location of each character.
    loc=list()
    if c == 'J' or c == 'I':
        c ='IJ'
    for i ,j in enumerate(main_matrix):
        #print(i,j)
        for m,n in enumerate(j):
            #print(m,n)
            if c == n:
                loc.append(i)
                loc.append(m)
                return loc


def encrypt():  #To encrypt
    message = str(input("Introduzca el PLAIN TEXT:"))
    message=message.upper()
    message=message.replace(" ", "")
    print("Mensaje a encriptar:\n")
    print(message)
    print("\n")

    for s in range(0,len(message)+1,2):
        if s<len(message)-1:
            if message[s]==message[s+1]:
                message=message[:s+1]+'X'+message[s+1:]
                
    if len(message)%2!=0:
        message=message[:]+'X'
    
    for i in range(0,len(message),2):
      print("{}{}".format(message[i],message[i+1]),end=' ')

    print("\n")
    print("CIPHER TEXT:\n")

    i=0
    while i<len(message):
        loc0=list()
        loc0=locindex(message[i])
        loc1=list()
        loc1=locindex(message[i+1])
        if loc0[1]==loc1[1]:
            print("{}{}".format(main_matrix[(loc0[0]+1)%5][loc0[1]],main_matrix[(loc1[0]+1)%5][loc1[1]]),end=' ')
        elif loc0[0]==loc1[0]:
            print("{}{}".format(main_matrix[loc0[0]][(loc0[1]+1)%5],main_matrix[loc1[0]][(loc1[1]+1)%5]),end=' ')  
        else:
            print("{}{}".format(main_matrix[loc0[0]][loc1[1]],main_matrix[loc1[0]][loc0[1]]),end=' ')    
        i=i+2
    print("\n")    


def decrypt():  #To decrypt
    message=str(input("Introduzca el CIPHER TEXT: "))
    message=message.upper()
    message=message.replace(" ", "")
    print("Mensaje a desencriptar:\n")

    if len(message)%2!=0:
        message=message[:]+'X'

    for i in range(0,len(message),2):
      print("{}{}".format(message[i],message[i+1]),end=' ')

    print("\n")
    print("PLAIN TEXT:\n")

    i=0
    msgfinal=list()
    while i<len(message):
        loc0=list()
        loc0=locindex(message[i])
        loc1=list()
        loc1=locindex(message[i+1])
        if loc0[1]==loc1[1]:
            print("{}{}".format(main_matrix[(loc0[0]-1)%5][loc0[1]],main_matrix[(loc1[0]-1)%5][loc1[1]]),end=' ')
            msgfinal.append(str(main_matrix[(loc0[0]-1)%5][loc0[1]]))
            msgfinal.append(str(main_matrix[(loc1[0]-1)%5][loc1[1]]))
        elif loc0[0]==loc1[0]:
            print("{}{}".format(main_matrix[loc0[0]][(loc0[1]-1)%5],main_matrix[loc1[0]][(loc1[1]-1)%5]),end=' ')
            msgfinal.append(str(main_matrix[loc0[0]][(loc0[1]-1)%5]))
            msgfinal.append(str(main_matrix[loc1[0]][(loc1[1]-1)%5]))
        else:
            print("{}{}".format(main_matrix[loc0[0]][loc1[1]],main_matrix[loc1[0]][loc0[1]]),end=' ')
            msgfinal.append(str(main_matrix[loc0[0]][loc1[1]]))
            msgfinal.append(str(main_matrix[loc1[0]][loc0[1]]))
        i=i+2
    print("\n")
    
    print(''.join(msgfinal))


e = 1    
while(e == 1):
    print("\n Elija la acción a realizar: \n")
    choice=int(input("\n 1.Encrytion \n 2.Decryption \n 3.Exit\n\n"))
    print("\n")

    if choice==1:
        encrypt()
    elif choice==2:
        decrypt()
    elif choice==3:
        e = 0
    else:
        print("Elija una opcion correcta\n")        
