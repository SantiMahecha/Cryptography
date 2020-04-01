#@Santiago Mahecha Pinzón
#smahechap@unal.edu.co

print("-------------------------------------------------------VIGENÈRE CIPHER ALGORITHM----------------------------------------------------------\n")
key = str(input("Intoduzca la clave (key): "))
key = key.replace(" ", "")
key = key.upper()

print("\n")
t = int(input("Introduzca t: "))
print("\n")

print("KEY: ",key)
print("t = ",t)
print("\n")

def create_matrix(rows,columns,initial):
    return [[initial for i in range(rows)]for j in range(columns)]

matrix=list()

c=0
i=65
while(c<=26): #Create a list with the 26x26 components (alphabet)
  if c == 0:
    for l in range(i,91):
        matrix.append(chr(l))
    c+=1

  else:
    for n in range(1,26):
       for l in range(i+n,91):
          matrix.append(chr(l))
       for m in range(65,i+n):
          matrix.append(chr(m))
    c+=1

k=0
main_matrix = create_matrix(26,26,0) #Create main matrix with the previus list
for i in range(0,26):
    for j in range(0,26):
        main_matrix[i][j] = matrix[k]
        k+=1

print("Matriz principal 26x26:\n",main_matrix,"\n")

def locindex(c): #Get location of each character.
    loc=list()
    for i ,j in enumerate(main_matrix):
        #print(i,j)
        for m,n in enumerate(j):
            #print(m,n)
            if c == n:
                loc.append(i)
                loc.append(m)
                return loc

def encrypt():#To encrypt
    message = str(input("Ingrese el PLAIN TEXT: "))
    message=message.upper()
    message=message.replace(" ", "")
    print("\n")
    print("Mensaje a encriptar:",end=' ')
    print(message)
    print("\n")
    print("FINAL PLAIN TEXT:",end=" ")

    m=0
    for i in range(0,len(message),t):
      for c in range(0,t):
        print(message[c+m],end="")
      m+=t
      print("",end=" ")

    print("\n")
    
    key_list=list()
    
    while(len(key_list)<len(message)):
      for l in range(0,len(key)):
        key_list.append(key[l])

    final_key = ''.join(key_list)
    final_key = final_key.upper()
    print("FINAL KEY:",end="        ")

    m=0
    for i in range(0,len(message),t):
      for c in range(0,t):
        print(final_key[c+m],end="")
      m+=t
      print("",end=" ")
    
    print("\n")
    print("CIPHER TEXT:      ",end='')

    i=0
    while i<len(message):
        locKEY=list()
        locKEY=locindex(final_key[i])
        locPLAIN=list()
        locPLAIN=locindex(message[i])
        print("{}".format(main_matrix[(locPLAIN[1])][locKEY[1]]),end='')
        if i%t==t-1 and i!=0:
          print("",end=' ')
        else: pass
        i+=1
        
    print("\n")   

def decrypt():#To encrypt
    message = str(input("Ingrese el CIPHER TEXT: "))
    message=message.upper()
    message=message.replace(" ", "")
    print("\n")
    print("Mensaje a desencriptar:",end=' ')
    print(message)
    print("\n")
    print("FINAL CIPHER TEXT:",end=" ")

    m=0
    for i in range(0,len(message),t):
      for c in range(0,t):
        print(message[c+m],end="")
      m+=t
      print("",end=" ")

    print("\n")
    
    key_list=list()
    
    while(len(key_list)<len(message)):
      for l in range(0,len(key)):
        key_list.append(key[l])

    final_key = ''.join(key_list)
    final_key = final_key.upper()
    print("FINAL KEY:",end="         ")

    m=0
    for i in range(0,len(message),t):
      for c in range(0,t):
        print(final_key[c+m],end="")
      m+=t
      print("",end=" ")
    
    print("\n")
    print("PLAIN TEXT:       ",end=' ')

    i=0
    while i<len(message):
        locKEY=list()
        locKEY=locindex(final_key[i])
        for j in range(0,26):
          if main_matrix[j][locKEY[1]] == message[i]:
            print("{}".format(main_matrix[j][0]),end='')
          else:pass
        if i%t==t-1 and i!=0:
          print("",end=' ')
        else: pass
        i+=1
        
    print("\n")   

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
