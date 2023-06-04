
class Cliente():
    def __init__(self,nombre,edad,dni,domicilio):
        
    
        
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.domicilio = domicilio
        self.mostrar_carrito
        self.comprar
        self.advertencia
        self.carrito = []
        
    def __str__(self):
        print(f'El nombre del cliente es {self.nombre}')
        
    def advertencia(self):
        print (f'''
                ADVERTENCIA
                Recuerde que el paquete enviado debera ser recibido por {self.nombre} presentando el siguiente documento {self.dni}''')
    
    def comprar(self):
        if self.edad < '18':
            print('Debe ser mayor de edad para realizar una compra')
        else:    
         print('Se ha realizado la compra extosamente')
         print(f'Gracias por su compra {self.nombre}')
         print(f'Su pedido sera despachado y destinado a {self.domicilio}')

    def agregar_al_carrito(self,producto):
        self.carrito.append(producto)
        print(f'Se ha agregado {producto} al carrito')
        ...
    def comprar_bucle(self): 
         if len(self.carrito) > 0: 
           print('Se ha realizado la compra extosamente')
           print(f'Gracias por su compra {self.nombre}')
           print(f'Su pedido sera despachado y destinado a {self.domicilio}')
         else: print('El carrito esta vacio')
     
    def mostrar_carrito(self):
        if len(self.carrito) > 0:
            print('Lista de productos en tu carrito')
            for producto in self.carrito:
                print(f'{producto}')
        else: print('El carrito esta vacio')
    

# cliente = Cliente (input('Ingrese su nombre completo: '), 
#                     input('Ingrese su edad: '), 
#                     input('Ingrese su dni: '), 
#                     input('Ingrese su domicilio: '))

# cliente1=Cliente('Irma Carbonel','32','22222','Cabildo 115, Bahía Blanca')
# print(cliente1.__str__())
# print(cliente1.comprar())
# print(cliente1.nombre)
# print(cliente1.edad)
# print(cliente1.dni)
# print(cliente1.domicilio)

#cliente2 = Cliente('Pepito Perez','11','99999','Av San Martin 1040, Capital federal')
#cliente3= Cliente('Luis Arias','23','44444','Florida 809, Mar del plata')

## Atributos de la clase cliente
# print(cliente2.nombre)
# print(cliente3.nombre)
# print(cliente2.edad)
# print(cliente3.edad)
# print(cliente2.dni)
# print(cliente3.dni)
# print(cliente2.domicilio)
# print(cliente3.domicilio)

##Funciones de los clientes
# cliente2.comprar()
# cliente3.comprar()
# cliente2.__str__() 
# cliente3.__str__()



# #IMPORTANTE:Este menu funciona si lo agregamos bajo las funciones de la clase cliente agregando los parametros nombre,edad,dni,domicilio a traves de los input
# bandera = True
# while bandera == True:
#     print('''
#           #### MENU ####
#           1. Comprar producto
#           2. Ver productos en el carrito
#           3. Finalizar compra
#           4. Salir
#           ''')
#     operacion = input('Ingrese la operacion que desea realizar: ')
    
#     if operacion == '1':
#      cliente.edad =(input('Ingrese su edad: '))
#      if cliente.edad < '18':
#          print ('Para realizar esta compra debes ser mayor de edad') 
#          break
#      else:
#          producto = input('Ingrese el producto que desea comprar: ')
#      cliente.agregar_al_carrito(producto)
    
#     if operacion == '2':
#         cliente.mostrar_carrito()
    
#     if operacion == '3':
#          cliente.comprar_bucle()
    
#     if operacion == '4':
#         print('Hasta luego!')
#         break
    

