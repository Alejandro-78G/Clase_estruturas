
class Medicamento:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    def mostrar_info(self):
        print("Medicamento:", self.nombre, "| Cantidad:", self.cantidad)


medicamentos = []
pacientes = []


def agregar_medicamento():
    nombre = input("Ingrese el nombre del medicamento: ")
    cantidad = int(input("Ingrese la cantidad del medicamento: "))

    nuevo = Medicamento(nombre, cantidad)
    medicamentos.append(nuevo)

    print("El medicamento se ingresó correctamente")


def eliminar_medicamento():
    nombre = input("Ingrese el nombre del medicamento que desea eliminar: ")

    for med in medicamentos:
        if med.nombre.lower() == nombre.lower():
            medicamentos.remove(med)
            print("El medicamento fue eliminado exitosamente")
            return

    print("Medicamento no encontrado")


def mostrar_medicamentos():
    if not medicamentos:
        print("No hay medicamentos registrados")
    else:
        for med in medicamentos:
            med.mostrar_info()


def agregar_paciente():
    nombre = input("Ingrese el nombre del paciente: ")
    medicamento = input("Ingrese el nombre del medicamento asignado: ")
    dia = input("Ingrese el día que desea reclamar el medicamento: ")

    pacientes.append([nombre, medicamento, dia])
    print("Se agregó el paciente con éxito para el día", dia)


def consultar_paciente():
    nombre = input("Ingrese el nombre del paciente que desea consultar: ")

    for paciente in pacientes:
        if paciente[0].lower() == nombre.lower():
            medicamento_asignado = paciente[1]
            dia = paciente[2]

            for med in medicamentos:
                if med.nombre.lower() == medicamento_asignado.lower():
                    print("\nINFORMACIÓN")
                    print("Paciente:", paciente[0])
                    print("Medicamento:", medicamento_asignado)
                    print("Día de entrega:", dia)

                    if med.cantidad > 0:
                        print("El medicamento tiene disponibilidad")
                    else:
                        print("No hay disponibilidad del medicamento")
                    return

            print("El medicamento asignado no existe en el sistema")
            return

    print("Paciente no encontrado")


while True:
    print("\nBienvenido al sistema de medicamentos")
    print("1. Agregar medicamento")
    print("2. Eliminar medicamento")
    print("3. Mostrar información de medicamentos")
    print("4. Agregar paciente")
    print("5. Consultar paciente")
    print("6. Salir")

    opcion = input("Ingrese el número de la opción que desea: ")

    if opcion == "1":
        agregar_medicamento()
    elif opcion == "2":
        eliminar_medicamento()
    elif opcion == "3":
        mostrar_medicamentos()
    elif opcion == "4":
        agregar_paciente()
    elif opcion == "5":
        consultar_paciente()
    elif opcion == "6":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida")



























