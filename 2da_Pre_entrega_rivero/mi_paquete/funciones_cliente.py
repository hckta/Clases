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
    print( f'El nombre del cliente es {self.nombre}')
    
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

        
    ##Funcinones del bucle (funcionan solo con el menu que esta en clase_cliente)
        
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