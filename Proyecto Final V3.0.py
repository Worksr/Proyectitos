import time
import datetime
import random

class SistemaArchivos:
    def __init__(self, usuario):
        self.usuario = usuario
        self.maquinas = { #Aqui los archivos que las instrucciones piden
            'Betty': MaquinaExcavadora('314', 'Mega Transporte', 150, 300, fechaAleatoria()),
            'Lola': MaquinaExcavadora('D77', 'Mega Transporte', 210, 450, fechaAleatoria()),
            'Marilyn': MaquinaExcavadora('D28', 'Mega Transporte', 50, 100, fechaAleatoria()),
            'Ava': MaquinaExcavadora('G53', 'Mega Transporte', 200, 800,fechaAleatoria()),
        }
        print(f"Hola {self.usuario}, este es mi proyecto final (Josue Alejandro)")

    def esperarCarga(self):
        print("Cargando programa")
        for i in range(5):
            time.sleep(1)
            print("Cargando programa"+("."*(i+1)))
        print("---Terminando carga---")

    def obtenerFecha(self): #Aqui le pedimos fecha en el formato solicitado
        while True:
            registrarFecha = input("Introduce la fecha en el siguiente formato:\ndia/mes/año: ")
            try:
                dia, mes, año = map(int, registrarFecha.split('/'))
                if 1 <= dia <= 31 and 1 <= mes <= 12:
                    return (dia, mes, año)
                else:
                    print("Esa fecha no existe")
            except ValueError:
                print("Formato mal hecho, asegurate de ingresar la fecha en formato dia/mes/año")

    def mostrarMenu(self): #Mostrar el menu, si uno espera aqui 10 minutos el programa pregunta si sigue ahi
        print("\n----------------------MENU PRINCIPAL----------------------")
        print("ESCRIBA LA PALABRA ENTRE COMILLAS PARA ELEGIR SU ACCION")
        print("Revisar maquina: 'revisar' ")
        print("Actualizar especificacion de una maquina: 'actualizar' ")
        print("Registrar nueva maquina: 'registrar' ")
        print("Cambiar de empresa: 'cambiar' ")
        print("Salir del programa: 'salir' ")
        #Iniciamos aqui el contador del tiempo
        empiezaTiempo = time.time()
        while True:
            #600 Segundos son 10 minutos entonces eso es el limite del contador
            if time.time() - empiezaTiempo > 600:
                respuesta = input("Tiempo de inactividad excedido, sigue ahi? ('si'/'no')")
                if respuesta.lower() == 'no':
                    return 'cambiar'
                else:
                    #Si el usuario dice que si entonces, reiniciamos el contador
                    empiezaTiempo = time.time()
            opcion = input("Eliga su opcion en minusculas porfavor: ").lower()
            if opcion:
                return opcion


    def registrarMaquina(self): #Aqui es donde se crean los archivos, cada archivo es una excavadora
        fecha = self.obtenerFecha()
        idMaquina = input("Escribe el ID de la nueva excavadora: ").lower()
        if idMaquina in self.maquinas:
            print("Ya existe la maquina en el programa, intente otro nombre")
        else:
            tipo = input("Introduce el tipo de maquina \nPersonal\nLigera\nMediana\nPesada\nMuy Pesada\nMega Transporte: ")
            horasUltimoMantenimiento = int(input("Introduce las horas desde el ultimo mantenimiento: "))
            horasTotales = int(input("Introduce las horas totales de uso: "))
            if horasUltimoMantenimiento > horasTotales:
                print("Las horas de ultimo mantenimiento no pueden ser mas que las horas totales de uso")
                return
            self.maquinas[idMaquina] = MaquinaExcavadora(idMaquina, tipo, horasUltimoMantenimiento, horasTotales, fecha)
            print(f"Maquina '{idMaquina}' registrada en el dia {fecha}")

    def actualizarMaquina(self):
        fecha = self.obtenerFecha()
        idMaquina = input("Escribe el ID de la maquina excavadora que deseas actualizar: ").lower()
        if idMaquina in self.maquinas:
            tipo = input("Escribe el nuevo tipo de maquinas: ")
            horasUltimoMantenimiento = int(input("Actualiza las horas desde el ultimo mantenimiento: "))
            horasTotales = int(input("Actualiza las horas desde el ultimo mantenimiento: "))
            maquina = self.maquinas[idMaquina]
            maquina.tipo = tipo
            maquina.horasUltimoMantenimiento = horasUltimoMantenimiento
            maquina.horasTotales = horasTotales
            print(f"Especificaciones actualizadas para la maquina {idMaquina}")
        else:
            print("Escribio el nombre mal, o esa maquina no existe")

    def mostrarMaquinas(self):
        if not self.maquinas:
            print("No hay maquinas registradas")
        else:
            for maquina in self.maquinas.values():
                maquina.revisarMaquina()

class MaquinaExcavadora:
    def __init__(self, id, tipo, horasUltimoMantenimiento, horasTotales, fecha):
        self.id = id
        self.tipo = tipo
        self.horasUltimoMantenimiento = horasUltimoMantenimiento
        self.horasTotales = horasTotales
        self.fecha = fecha

    def revisarMaquina(self):
        print(f"ID:{self.id}")
        print(f"Tipo de maquina:{self.tipo}")
        print(f"Horas desde el ultimo mantenimiento:{self.horasUltimoMantenimiento}")
        print(f"Necesita mantenimiento?:{self.necesitaMantenimiento()}")
        print(f"Estado de salud:{self.estadoSalud()}")
        print(f"Fecha de regstro: {self.fecha}")

    def necesitaMantenimiento(self):
        return "Si" if self.horasUltimoMantenimiento > 200 else "No"

    def estadoSalud(self):
        if self.horasTotales < 500:
            return "Excelente"
        elif 500 <= self.horasTotales <= 1000:
            return "Bueno"
        else:
            return "Critico"
def fechaAleatoria():
    hoy = datetime.date.today()
    diasPasados = random.randint(1, 900)
    fechaAleatoria = hoy - datetime.timedelta(days=diasPasados)
    return fechaAleatoria

def main():
    usuario = input("Introduce el nombre de su empresa (usuario): ") #La empresa funcionara como usuario
    sistema = SistemaArchivos(usuario)
    sistema.esperarCarga()
    while True: #While True requerido
        opcion = sistema.mostrarMenu()

        if opcion == "revisar":
            sistema.mostrarMaquinas()
        elif opcion == "actualizar":
            sistema.actualizarMaquina()
        elif opcion == "registrar":
            sistema.registrarMaquina()
        elif opcion == "salir":
            print("Saliendo del sistema")
            for i in range(5):
                time.sleep(1)
                print("Saliendo del sistema"+("."*(i+1)))
            print("---Terminando salida---")
            break
        else:
            print("Opcion no valida, recuerde escribir en minusculas...")
if __name__ == "__main__":
    main()