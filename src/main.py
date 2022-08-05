''' 
Ale Gudiel - 19232
Proyecto 1 - Redes 
Uso de un protocolo existente (XMPP) para comunicar con un servidor de mensajes

Archivo main para ejecutar el programa y mostrar el UI al usuario
'''


menu = 0 # Variable para controlar el menu

print("----------------------------------------")
print("----------------------------------------")
print("Bienvenido al chat de ALUMCHAT v.20.22")
print("----------------------------------------")
print("----------------------------------------")
print("1. Sign up \n2. Log-in \n3. Exit app")

menu = int(input("Enter the option you want to use: "))

while menu != 3:
    if menu == 1:
        print("Crear cuenta")

        # Crear cuenta
        print("----------------------------------------")

    if menu == 2:
        print("Iniciar sesion")

        # Iniciar sesion
        print("----------------------------------------")

    else:
        print("Thank you for using ALUMCHAT v.20.22")
        quit()





