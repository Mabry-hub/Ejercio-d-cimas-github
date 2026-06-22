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