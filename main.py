"""
1 - Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área 
del rectángulo. 
"""
# class Rectangulo:
#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura

#     def calcular_area(self):
#         return self.base * self.altura
    
# base = int(input("Introduce la base del rectángulo: "))
# altura = int(input("Introduce la altura del rectángulo: "))

# rectangulo = Rectangulo(base, altura)
# print("El área del rectángulo es:", rectangulo.calcular_area())

"""
2 - Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. 
"""

# class Mate:
#     def __init__(self, cantidad):
#         self.cantidad = cantidad 
#         self.cebadas = cantidad
#         self.estado = True
    
#     def cebar(self):
#         if self.estado:
#             print("Esta Lleno!")
#         else:
#             self.estado = True
#             print("Mate cebado")
    
#     def beber(self):
#         if not self.estado:
#             print("El mate está vacio")
#         else:
#             self.estado = False
#             if self.cebadas > 0:
#                 self.cebadas -= 1
#                 print(f"Mate tomado faltan: {self.cebadas}.")
#             else:
#                 print("Mate está lavado.")

# mate = Mate(3)  # Crear un mate con 3 cebadas

# mate.cebar()    # llenar el mate
# mate.cebar()    # mate lleno

# # mate.beber()  # el mate está vacio
# # mate.cebar()  # llenr el mate
# # mate.beber()  # bebe el mate (2 cebadas)
# # mate.cebar()  # llena el mate de nuevo
# # mate.beber()  # bebe el mate (1 cebada)
# # mate.beber()  # intenta beber cuando está vacio
# # mate.cebar()  # llena el mate
# # mate.beber()  # bebe el mate (0 cebadas)
# # mate.cebar()  # llena el mate
# # mate.beber()  # bebe con el mate lavado

"""
3 - Botella y Sacacorchos
"""

"""
4 - Una heladería es un tipo especial de restaurante... 
"""

# class Restaurante:
#     def __init__(self, restaurante_nombre, tipo_comida):
#         self.restaurante_nombre = restaurante_nombre
#         self.tipo_comida = tipo_comida

#     def describir_restaurante(self):
#         print(f"Restaurante: {self.restaurante_nombre}")
#         print(f"Tipo de comida: {self.tipo_comida}")

#     def abrir_restaurante(self):
#         print(f"El restaurante {self.restaurante_nombre} está ahora abierto.")

# class Heladeria(Restaurante):
#     def mostrar_sabores(self):
#         print("Sabores disponibles:")
#         for sabor in self.sabores:
#             print(f"- {sabor}")

# mi_heladeria = Heladeria("Helados Ricos", "Postres")
# mi_heladeria.sabores = ["Vainilla", "Chocolate", "Fresa", "Mango"]

# mi_heladeria.describir_restaurante()
# mi_heladeria.abrir_restaurante()
# mi_heladeria.mostrar_sabores()

"""
5 - 
"""

"""
6 - Usuarios: Cree una clase Usuario...
"""

# class Usuario:
#     def __init__(self, nombre, apellido, edad, email, ciudad):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.email = email
#         self.ciudad = ciudad

#     def describir_usuario(self):
#         print(f"Usuario: {self.nombre} {self.apellido}")
#         print(f"Edad: {self.edad}")
#         print(f"Email: {self.email}")
#         print(f"Ciudad: {self.ciudad}")

#     def saludar_usuario(self):
#         print(f"Hola, {self.nombre} {self.apellido} Bienvenido.")


# # usuario1 = Usuario("Alvaro", "Martinez", 27, "amz@alvaromz.com.ar", "Salta")
# # usuario1.describir_usuario()
# # usuario1.saludar_usuario()

# # print()

# # usuario2 = Usuario("Carlos", "López", 35, "carlos.lopez@gmail.com", "Jujuy")
# # usuario2.describir_usuario()
# # usuario2.saludar_usuario()

# # print()

# # usuario3 = Usuario("Laura", "García", 22, "laura.garcia@hotmail.com", "Tucuman")
# # usuario3.describir_usuario()
# # usuario3.saludar_usuario()

"""
7 - Admin: Un administrador es un tipo de usuario con privilegios especiales...
"""
# class Admin(Usuario):
#     def __init__(self, nombre, apellido, edad, email, ciudad):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.email = email
#         self.ciudad = ciudad
#         self.privilegios = ["puede postear en el foro", "puede borrar un post", "puede banear usuario"]
        
    
#     def mostrar_privilegios(self):
#         print("Privilegios del administrador:")
#         for privilegio in self.privilegios:
#             print(f"- {privilegio}")

# admin1 = Admin("Alvaro", "Martinez", 27, "amz@alvaromz.com.ar", "Salta")
# admin1.describir_usuario()
# admin1.mostrar_privilegios()

"""
8 - Privilegios: Escriba una clase Privilegios...
"""

"""
9 - Restaurante importado...
"""
# from resto import Heladeria

# mi_heladeria = Heladeria("Helados Ricos", "Postres")
# mi_heladeria.sabores = ["Vainilla", "Chocolate", "Fresa", "Mango"]

# mi_heladeria.describir_restaurante()
# mi_heladeria.abrir_restaurante()
# mi_heladeria.mostrar_sabores()
