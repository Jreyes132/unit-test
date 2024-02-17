def login(username, password):
    if username == "admin" and password == "password":
        return True
    else:
        return False

username = input("Ingrese su nombre de usuario: ")
password = input("Ingrese su contraseña: ")

if login(username, password):
    print("Inicio de sesión exitoso")
else:
    print("Nombre de usuario o contraseña incorrectos")
