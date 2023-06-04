import json
archivo_datos = 'datos.json'

class Cliente():
    edad= int
    dni = str
    nro_tarjeta= str
    usuarios = {}
    datos_clientes = {}
    
    def __init__(self, edad, dni, nro_tarjeta):
        self.edad = edad
        self.dni = dni
        self.nro_tarjeta = nro_tarjeta
        self.agregar_usuario()
        
    def agregar_usuario(self):
        bandera = True
        while bandera != False:
            if input('Quiere agregar un usuario: (ingrese si en caso correcto)') != 'si':
                break
            ingreso_nuevo_usuario = input('Ingrese el usuario: ')
            ingreso_contrasenia_del_nuevo_usuario = input('Ingrese la contrasenia: ')
            self.usuarios[ingreso_nuevo_usuario] = ingreso_contrasenia_del_nuevo_usuario
            print ('Bienvenido, ingrese a su usuario!')
            bandera = False
        bandera2 = True
        while bandera2 != False:
         bandera2 = self.logear()
        
        
            
    def verificar(self, usuario, contrasenia):
        return self.usuarios.get(usuario) == contrasenia
        
    
    def logear(self):
        ingreso_de_usuario = input('Ingrese su usuario: ')
        ingreso_de_contrasenia = input('Ingrese su contrasenia: ')
        if self.verificar(ingreso_de_usuario, ingreso_de_contrasenia):
            print('Inicio sesion con exito!')
            self.menu()
        else:
            print('Error! Vuelva a intentarlo!')
            return False
    
    def inicio(self):
        repetir_autenticacion = True
        while repetir_autenticacion:
            conectado = self.logear()
            if conectado == False:
                continue
            elif conectado == None:
                break
            self.menu()
                
    def menu(self):
        repetir_menu = True # bandera/flag
        while repetir_menu:
            print('''
        ==============
            Menu
        ==============
        1. Comprar.
        2. Vender.
        3. Salir
        ''')
            opcion_elegida = input('Ingrese la operacion a realizar: ')
            if opcion_elegida == '1':
                self.comprar(self)
            elif opcion_elegida == '2':
                self.vender(self)
            elif opcion_elegida == '3':
                repetir_menu = False
                print('Hasta luego!')
            else:
                print('Vuelva a intentar con una opcion valida.')
    
    def vender(self):
        print('A publicado su producto a la venta')
    def comprar(self,edad):
        self.edad = edad
        self.dni = dni
        self.nro_tarjeta = nro_tarjeta
        super.__init__(dni,nro_tarjeta)
        self.edad = input('Ingrese su edad: ')
        if edad < '18':
            print('Para hacer esta compra debe ser mayor de edad')
            self.menu()
        dni = input('Ingrese su dni: ')
        nro_tarjeta = input('Ingrese su numero de tarjeta: ')
        if nro_tarjeta in self.datos_clientes and dni in self.datos_clientes:
         self.menu_compras()
        else: print ('Numero de tarjeta o dni invalido')
        
cliente1 = Cliente(input('Ingrese su nombre: '),
                   input('Ingrese su edad: '),
                   input('Ingrese su dni: '),
                   input('Ingrese su tarjeta: '))
cliente1.agregar_usuario()
cliente1.comprar(dni = input('Ingrese su dni: '), nro_tarjeta = (input('Ingrese su numero de tarjeta: ')))


print('hola')

 