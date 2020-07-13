##
##  UNIVERSIDAD DEL VALLE DE GUATEMALA
##  GRÁFICAS POR COMPUTADORA
##  SECCIÓN 20
##
##  SR1: Points
##  AUTOR:  LUIS PEDRO CUÉLLAR - 18220
##

##  import gl library for drawing
from gl import Render, color

title = "---    ESCRITOR DE IMÁGENES BMP    ---\n"
intro_msg = "\nPrimero, hay que definir el tamaño de la imagen!"
set_width = "\nIngrese el número de pixeles de largo (width): "
set_height = "Ingrese el número de pixeles de alto (height): "

menu = """\nOpciones:
        1. Modificar el color al fondo de la imagen
        2. Modificar ViewPort
        3. Dibujar un punto en la imagen
        4. Guardar imagen
        5. Salir

        Ingrese la opcion que desea realizar: """

wants_to_continue = True
wants_to_change_size = True
width = 0
height = 0
red = 0
green = 0
blue = 0

print(title)
input("Apache enter para continuar...")

print(intro_msg)
input("Apache enter para continuar...")

while(wants_to_continue):
    if(wants_to_change_size):
        width = input(set_width)
        height = input(set_height)
        wants_to_change_size = False

    print(menu)
    option = input()
    option = int(option)

    if(option == 1):
        red = input(int("Ingrese el valor r del color deseado (de 0 a 255): "))
        green = input(int("Ingrese el valor g del color deseado (de 0 a 255): "))
        blue = input(int("Ingrese el valor b del color deseado (de 0 a 255): "))

    elif(option == 2):
        print("Opcion 2")
    elif(option == 3):
        print("Opcion 3")
    elif(option == 4):
        print("Opcion 4")
    elif(option == 5):
        wants_to_continue = False
    else:
        print("Por favor escoja una opción válida!")

print("BYEEEEE")
