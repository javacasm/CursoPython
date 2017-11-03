n=0
while(n==0)
  print("Bienvenido!")
  nom=input("Introduce tu nombre: ")
  if(nom=="Admin"):
    intentos=0
    while(intentos<4):
      passwd=input("Contraseña?")
      if(passwd=="nimdA"):
        while(n==0):
          com=input("#$>: ")
          if(com=="help"):
            print("help\tmuestra la ayuda")
            print("end\ttermina la consola")
          elif (com=="end"):
            n=2
            print("Exit!")
      else:
        intentos=intentos+1
  else:
    print("Hola "+nom)
  
