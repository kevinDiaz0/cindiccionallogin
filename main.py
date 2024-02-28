userBD  = "hidrotech123"
passwordBD = "admin123*"


print("software tech hidroituango")
print("**************************")
userName = input("Digita tu usuario: ")
userPassword = input("ingrese su contraseña: ")

 
if(userBD == userName and passwordBD==userPassword):
    print("exito en su usuario")
else:
    print("fallaste")

    #print("exito en su usuario")  if userBD == userName and passwordBD==userPassword else print("fallaste")
