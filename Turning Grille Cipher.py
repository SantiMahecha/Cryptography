#@Santiago Mahecha Pinzón
#smahechap@unal.edu.co

print("----------------------Turning Grille Cipher Algotihm---------------------------\n")

def create_matrix(rows,columns,initial):
    return [[initial for i in range(rows)]for j in range(columns)]

size = int(input("Input the size of the grille: "))
print("\n")

m = size-1
num_hole = 0

while(m>=2):
  num_hole = num_hole+m
  m = m-2
num_hole+=1  

print("Number of holes: ",num_hole)
print("\n")

grille = create_matrix(size,size,0) #Create main matrix

hole = create_matrix(2,num_hole,0)

print("Define the holes positions, make sure there won´t be collisions.\n")
print("1 if there is a hole and 0 if there is not:\n")

cont = 0
for i in range(0,size):
    for j in range(0,size):
        h = bool(int(input(f"Input the {i} element of the {j} row of the grille: ")))

        if h==1:
          hole[cont][0] = i
          hole[cont][1] = j
          cont+=1

        grille[i][j] = h

print("\n")
print("Holes positions:\n")
print(hole)

print("\n")
print(grille)

main_matrix = create_matrix(size,size,0)
for i in range(0,size):
    for j in range(0,size):
        main_matrix[i][j] = 0

#print("\n")
#print(main_matrix)

mov = create_matrix(size,size,0)
for i in range(0,size):
    for j in range(0,size):
        mov[i][j] = 0

def pos_hole():
    cont = 0
    for i in range(0,size):
      for j in range(0,size):
          if grille[i][j]==True:
            hole[cont][0] = i
            hole[cont][1] = j
            cont+=1
    #print("\n")
    #print("Holes positions updated:\n")
    #print(hole)

def turn_left():
    p = size-1
    for i in range(0,size):
      for j in range(0,size):
        mov[p-j][i] = grille[i][j]

    for i in range(0,size):
      for j in range(0,size):
        grille[i][j] = mov[i][j]

def turn_right():
    p = size-1
    for i in range(0,size):
      for j in range(0,size):
        mov[j][p-i] = grille[i][j]

    for i in range(0,size):
      for j in range(0,size):
        grille[i][j] = mov[i][j]

def encrypt():
    message = str(input("Input PLAIN TEXT: "))
    message=message.upper()
    message=message.replace(" ", "")
    print("\n")
    print("Messaje a encriptar:",end=' ')
    print(message)
    print("\n")
    print("FINAL PLAIN TEXT:",end=" ")

    m=0
    for i in range(0,len(message),size):
      for c in range(0,size):
        print(message[c+m],end="")
      m+=size
      print("",end=" ")

    z = 1    
    while(z == 1):
      print("\n\nChoose the direction to crypt: ")
      choice=int(input("\n 1.Left \n 2.Right \n 3.Exit\n\n"))

      if choice==1:
          m=0
          n=0
          while(m<4):
            i=0
            for j in range(0,num_hole): 
              main_matrix[hole[j][0]][hole[j][1]]=message[i+n]
              i+=1
            n+=num_hole
            turn_left()
            pos_hole()
            m+=1

          print("\nCIPHER TEXT:\n")
          print(main_matrix)

      elif choice==2:
          m=0
          n=0
          while(m<4):
            i=0
            for j in range(0,num_hole): 
              main_matrix[hole[j][0]][hole[j][1]]=message[i+n]
              i+=1
            n+=num_hole
            turn_right()
            pos_hole()
            m+=1

          print("\nCIPHER TEXT:\n")
          print(main_matrix)
      
      elif choice==3:
        z = 0

      else:
          print("Choose a correct option\n")  

def decrypt():

  for i in range(0,size):
    for j in range(0,size):
        main_matrix[i][j] = str(input(f"Input the {i} element of the {j} row of the CIPHER TEXT: "))

  print("\n")      
  print(main_matrix)
  print("\n") 

  pos_hole()
  
  m=0
  z = 1  

  while(z == 1):

      print("\n\nChoose the direction to decrypt: ")
      choice=int(input("\n 1.Left \n 2.Right \n 3.Exit\n\n"))

      if choice==1:
        print("\nPLAIN TEXT:\n")  
        while(m<4):
          for j in range(0,num_hole):
            print("{}".format(main_matrix[hole[j][0]][hole[j][1]]),end='')
            i+=1
          turn_left()
          pos_hole()
          m+=1
        print("\n")

      elif choice==2:
        print("\nPLAIN TEXT:\n")  
        while(m<4):
          for j in range(0,num_hole):
            print("{}".format(main_matrix[hole[j][0]][hole[j][1]]),end='')
            i+=1
          turn_right()
          pos_hole()
          m+=1
        print("\n")
        
      elif choice==3:
        z = 0
    
      else:
          print("Choose a correct option\n")  


e = 1    
while(e == 1):
    print("\n Choose an action to realize: ")
    choice=int(input("\n 1.Encrytion \n 2.Decryption \n 3.Exit\n\n"))
    print("\n")

    if choice==1:
        encrypt()
    elif choice==2:
        decrypt()
    elif choice==3:
        e = 0
    else:
        print("Choose a correct option\n")
