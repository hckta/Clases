# -*- coding: utf-8 -*-
"""Pre-entrega Rivero

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lwZ2Zv46HpfNuO93KmxtvFfJs5QFGMIZ
"""

def usuario():
    nombre_usuario = input('Ingrese su usuario: ')
    return nombre_usuario
    
def contrasenia():
    contrasenia_usuario = input('Ingrese una contraseña: ')
    return contrasenia_usuario



repetir_menu = True
#dicc = { nombre del usuario: contraseña del usuario}
dicc = {'octavio': '1234', 
       'pepito': '123',}
import json

while repetir_menu: 
    print('''
    Menu principal
1. Registrarse
2. Usuarios guardados
3. Logear
4. Salir''')
    opcion_elegida = input('Elija la operacion que desea realizar: ')
    if opcion_elegida == '1':
        nombre_usuario = usuario()
        contrasenia_usuario = contrasenia()
        if nombre_usuario in dicc:
         print('El nombre de usuario ya existe')
         continue
        else: 
         dicc.update({nombre_usuario: contrasenia_usuario})
         with open ('archivo.json','w') as f:
          json.dump(dicc , f, indent = 4)
         print('Se ha registrado exitosamente')
         continue
    if opcion_elegida == '2':
      nombres_usuarios = list(dicc.keys())
      for solo_nombres in nombres_usuarios:
       print(solo_nombres)
      with open ('archivo.json', 'r') as f:
        dicc = json.load(f)
        continue
    if opcion_elegida == '3':
      usuario_login = input('Ingrese su usuario: ')
      contrasenia_login = input('Ingrese su contrasenia: ')
      if usuario_login in dicc or contrasenia_login in dicc:
       print('Ha ingresado a su cuenta exitosamente')
      else: print('Usuario o contraseña incorrecta')
      continue
    if opcion_elegida == '4': print('Hasta luego')
    repetir_menu = False
else:
    opcion_elegida != '1' or '2' or '3' or '4'
    print('Por favor, ingrese un numero valido.')