#funciones validaciones
def validar_codigo(codigo):    #validar el codigo sin espacios
    return codigo.strip()!=""

def buscar_codigo(reservas, codigo):    #las funciones de validacion de codigo-(que no tenga espacios) y buscar el codigo-(si es que ya existe) pueden fusionarse en una sola funcion
    for indice, reserva in enumerate(reservas):
        if reserva["codigo"]==codigo:
            return indice, reserva
    return None, None

def validar_nombre(nombre):
    return nombre.strip()!=""

#funciones opciones y funcionales

def mostrar_menu():
    print("1. Registrar reserva")
    print("2. Buscar reserva")
    print("3. Actualizar reserva")
    print("4. Eliminar reserva")
    print("5. Mostrar reservas")
    print("6. Mostrar estadísticas")
    print("7. Salir")

#OPCION 1
def registrar_reserva(reservas):
    codigo=input("Ingrese codigo de reserva: ").strip()

    if not validar_codigo(codigo):
        print("Error: El código no puede estar vacio")
        return
    indice, reserva = buscar_codigo(reservas, codigo)

    if buscar_codigo(reservas, codigo) is not None:
        print("Error: El código de la reserva ya existe")
        return

    nombre=input("ingrese nombre del huésped: ").strip()
    if not validar_nombre(nombre):
        print("Error: el nombre no puede estar vacío")
        return
    
    try:
        noches=int(input("Ingrese la cantidad de noches de estadía:"))
        if noches<=0:
            print("Error: La cantidad ingresada tiene que ser mayor a 0.")
            return
    except ValueError:
        print("Error: Debe ingresar un numero entero")
        return
    
    try:
        valor_noche=int(input("Ingrese el valor de noche: "))
        if valor_noche<=0:
            print("Error: El valor por noche no puede ser 0")
            return
    except ValueError:
        print("Error: Debe ingresar un numero entero")

    total=valor_noche*noches

    if total<200000:
        categoria="economica"
    elif 200000<= total <=500000:
        categoria="estandar"
    else:
        categoria="premium"

    reserva={"codigo":codigo,
             "nombre":nombre,
             "noches":noches,
             "valor_noche":valor_noche,
             "total":total,
             "categoria":categoria}

    reservas.append(reserva)

#OPCION 2
def buscar_reserva(reservas, codigo):
    if len(reservas)==0:
        print("Error: No existen registros de reservas.")
        return
    indice, reserva = buscar_codigo(reservas, codigo)
    if reserva is None:
        print(f"No existe ninguna reserva con el código '{codigo}'.")
    else:
        print("Posición :", indice + 1)
        print("Código   :", reserva["codigo"])
        print("Nombre   :", reserva["nombre"])
        print("Noches   :", reserva["noches"])
        print("Valor    : $", reserva["valor_noche"])
        print("Total    : $", reserva["total"])
        print("Categoría:", reserva["categoria"])

#OPCION 3 
def actualizar_reserva(reservas):
    if len(reservas)==0:
        print("Error: No existen registros de reservas.")
        return
    
    codigo = input("Ingrese el código de la reserva a actualizar: ").strip()
    indice, reserva = buscar_codigo(reservas, codigo)
    if reserva is None:
        print("No existe ninguna reserva con el código", codigo)
        return
    nuevo_nombre=input("Ingrese nuevo nombre: ").strip()
    if not validar_nombre(nuevo_nombre):
        print("Error: el nuevo nombre no puede estar vacío.")
        return
    reserva["nombre"]=nuevo_nombre

    nuevas_noches=int(input("Ingrese nueva cantidad de noches: "))
    try:
        if nuevas_noches<=0:
            print("Error: la cantidad ingresada no uede ser negtiva.")
            return
        reserva["noches"]=nuevas_noches
    except ValueError:
        print("Error: Debe ingresar un numero entero.")
        return

    nuevo_valor=int(input("Ingrese nuevo valor por noche: "))
    try:
        if nuevo_valor<=0:
            print("Error: La cantidad ingresada no puede ser negativa")
            return
        reserva["valor"]=nuevo_valor
    except ValueError:
        print("Error  ingrese un numero entero.")
        return
    reserva["total"]=reserva["noches"]*reserva["valor_noche"]
    if reserva["total"]<200000:
        reserva["categoria"]="economica"
    elif 2000000 <= reserva["total"] <=500000:
        reserva["categoria"]="estandar"
    else:
        reserva["categoria"]="premium"
    print("reserva actualizada correctamente")

def main():

    reservas=[]

    while True:

        mostrar_menu()

        opcion=leer_opcion(reservas)

        if opcion==1:
            registrar_reserva(reservas)

        elif opcion==2:
            buscar_reserva(reservas)

        elif opcion==3:
            actualizar_reserva(reservas)

        elif opcion ==4:
            eliminar_reserva(reservas)
        
        elif opcion==5:
            mostrar_reservas(reservas)

        elif opcion==6:
            mostrar_estadisticas(reservas)
        
        elif opcion==7:
            print('*Programa finalizado*')
            break
        
main()

