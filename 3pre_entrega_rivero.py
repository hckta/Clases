import json
archivo_datos = 'datos.json'
dicc = {}
class Cliente():
    def __init__(self,usr,psw):
     self.nombre_usuario = str
     self.contrasenia_usuario = str
     self.edad = int
     self.tarjeta = int
     
    def ingresar(self):
        bandera1 = True
        while bandera1 != False:
            if input('Desea agregar un usuario nuevo? (si o no)') == 'si':
                self.registro()
            else:
                bandera1 = False
        bandera2 = True
        while bandera2 != False:
            bandera2 = self.loguearse()
    def registro(self,usr,psw):
        with open(Cliente.archivo_datos, 'r') as f:
            datos = json.load(f)
        usr = input('Ingrese numero de tarjeta del nuevo usuario: ')
        psw = input('Ingrese contrasenia del nuevo usuario: ')
        datos[usr] = psw
        
        with open(Cliente.archivo_datos, 'w') as f:
            json.dump(datos, f, indent = 4)
    def loguearse(self):
        nombre_usuario = input('Ingresar su usuario: ')
        contrasenia = input('Ingresar numero de contrasenia: ')
        if self.verificar(nombre_usuario, contrasenia):
            self.__menu()
        else:
            print('Los datos ingresados no son correctos. Vuelva a intentarlo.')
    def verificar(self,nombre_usuario,contrasenia):
        with open(Cliente.archivo_datos, 'r') as f:
            datos = json.load(f)
        for usuario_guardado, contrasenia_guardado in datos.items():
            if nombre_usuario == usuario_guardado and contrasenia == contrasenia_guardado:
                return True
        
    def comprar(self):
        ...
    def vender (self):
        ...

def menu_compras(self):
    ...
cliente1 = Cliente()
cliente1.ingresar()
# repetir_menu_ingreso = True
# while repetir_menu_ingreso: 
#     print('''
#     Menu principal
# 1. Registrarse
# 2. Usuarios guardados
# 3. Logear
# 4. Salir''')
#     opcion_elegida = input('Elija la operacion que desea realizar: ')
#     if opcion_elegida == '1':
#         nombre_usuario = usuario()
#         contrasenia_usuario = contrasenia()
#         if nombre_usuario in dicc:
#          print('El nombre de usuario ya existe')
#          continue
#         else: 
#          dicc.update({nombre_usuario: contrasenia_usuario})
#          with open ('archivo.json','w') as f:
#           json.dump(dicc , f, indent = 4)
#          print('Se ha registrado exitosamente')
#          continue
#     if opcion_elegida == '2':
#       nombres_usuarios = list(dicc.keys())
#       for solo_nombres in nombres_usuarios:
#        print(solo_nombres)
#       with open ('archivo.json', 'r') as f:
#         dicc = json.load(f)
#         continue
#     if opcion_elegida == '3':
#       usuario_login = input('Ingrese su usuario: ')
#       contrasenia_login = input('Ingrese su contrasenia: ')
#       if usuario_login in dicc or contrasenia_login in dicc:
#        print('Ha ingresado a su cuenta exitosamente')
#       else: print('Usuario o contraseña incorrecta')
#       continue
#     if opcion_elegida == '4': print('Hasta luego')
#     repetir_menu_ingreso = False
# else:
#     opcion_elegida != '1' or '2' or '3' or '4'
#     print('Por favor, ingrese un numero valido.')