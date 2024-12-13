from vehiculo import *
import csv

#Funcion para escribir el archivo .CSV
def guardar_datos_csv(vehiculos):
    try:
        with open('vehiculos.csv', 'w', newline='') as archivo:
            writer = csv.writer(archivo)
            for vehiculo in vehiculos:
                writer.writerow([vehiculo.__class__, vehiculo.__dict__])
    except Exception as e:
        print(f"Error al guardar datos: {str(e)}")

#Funcion para leer datos desde un .CSV
def leer_datos_csv():
    try:
        with open('vehiculos.csv', 'r') as archivo:
            reader = csv.reader(archivo)
            print("Lista de Vehiculos Particular")
            for linea in reader:
                if "Particular" in linea[0]:
                    print(linea[1])
            
            archivo.seek(0)
            print("\nLista de Vehiculos Carga")
            for linea in reader:
                if "Carga" in linea[0]:
                    print(linea[1])
            
            archivo.seek(0)
            print("\nLista de Vehiculos Bicicleta")
            for linea in reader:
                if "Bicicleta" in linea[0] and "Motocicleta" not in linea[0]:
                    print(linea[1])
            
            archivo.seek(0)
            print("\nLista de Vehiculos Motocicleta")
            for linea in reader:
                if "Motocicleta" in linea[0]:
                    print(linea[1])
    except Exception as e:
        print(f"Error al leer datos: {str(e)}")

def main():
    # Crear instancias de vehiculos
    particular = Particular("Ford", "Fiesta", "4", "180", "500", "5")
    carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    # Guardar en .CSV
    vehiculos = [particular, carga, bicicleta, motocicleta]
    guardar_datos_csv(vehiculos)

    # Verificar instancias de Motocicleta
    print("Motocicleta es instancia con relación a Vehículo:", isinstance(motocicleta, Vehiculo))
    print("Motocicleta es instancia con relación a Automovil:", isinstance(motocicleta, Automovil))
    print("Motocicleta es instancia con relación a Vehículo particular:", isinstance(motocicleta, Particular))
    print("Motocicleta es instancia con relación a Vehículo de Carga:", isinstance(motocicleta, Carga))
    print("Motocicleta es instancia con relación a Bicicleta:", isinstance(motocicleta, Bicicleta))
    print("Motocicleta es instancia con relación a Motocicleta:", isinstance(motocicleta, Motocicleta))

    # Leer y mostrar datos del CSV
    print("\nLeyendo datos del archivo CSV:")
    leer_datos_csv()

if __name__ == "__main__":
    main()