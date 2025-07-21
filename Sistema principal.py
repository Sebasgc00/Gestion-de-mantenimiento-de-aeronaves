# Sistema principal
"""Este sistema estara encargado de gestionar el mantenimiento de aeronaves y coordinar tecnicos y hangares para dicha tarea""" 

# Extensiones
import random as rnd

class avion:
    # Simula un avion con los atibutos: id, modelo, horas de vuelo, ciclos de vuelo, estado, ultimo mantenimiento e historial de fallas
    def __init__(self, matricula, modelo, vhoras, vciclos, umantenimiento, ufalla,):
        self.matricula = matricula
        self.modelo = modelo
        self.vhoras = vhoras
        self.vciclos = vciclos
        self.umantenimiento = umantenimiento # Fecha en formato dia/mes/año
        self.ufalla = ufalla

    def status(self):
        print(f"Matricula: {self.matricula}")
        print(f"Modelo: {self.modelo}")
        print(f"Horas de vuelo: {self.vhoras}")
        print(f"Ciclos de vuelo: {self.vciclos}")
        print(f"Ultimo mantenieminto: {self.umantenimiento}")
        print(f"Ultima falla: {self.ufalla}")

Avion_1 = avion("HK-101", "A 320", rnd.randint(100,400), rnd.randint(200,700), "09/02/2025", "15/01/2025")
Avion_2 = avion("HK-202", "B 737", rnd.randint(100,400), rnd.randint(200,700), "01/01/2025", "23/12/2024")
Avion_3 = avion("HK-303", "ATR 42", rnd.randint(100,400), rnd.randint(200,700), "03/12/2024", "5/11/2024")
Avion_4 = avion("A6-EEY", "A 380",  rnd.randint(100,400),  rnd.randint(200,700), "29/11/2024", "3/11/2024")
Avion_5 = avion("F-HT00", "A 350", rnd.randint(100,400), rnd.randint(200,700), "18/02/2025", "27/01/2025")

if __name__ == "__main__":
    print("Estado de aviones")
    Avion_1.status()
    print()
    Avion_2.status()
    print()
    Avion_3.status()
    print()
    Avion_4.status()
    print()
    Avion_5.status()
    print()

class falla:
    # Simula si una aeronave tuvo una falla reciente
    def __init__(self, descripcion, gravedad):
        self.descripcion = descripcion
        self.gravedad = gravedad # La gravedad puede ser: leve, medio o critico

    def status(self):
        print(f"Descripcion: {self.descripcion}")
        print(f"Gravedad: {self.gravedad}")

Falla_1 = falla("Instrumentos defectuosos", "Leve")
Falla_2 = falla("Falla del sensor de temperatura de aire", "Media")
Falla_3 = falla("Falla en aire acondicionado", "Media")
Falla_4 = falla("Perdida del sistema hidraulico", "Critica")
Falla_5 = falla("Falla total del motor", "Critica")

if __name__ == "__main__":
    print("FALLAS")
    Falla_1.status()
    print()
    Falla_2.status()
    print()
    Falla_3.status()
    print()
    Falla_4.status()
    print()
    Falla_5.status()
    print()

class mantenimiento:
    # Simula los mantenimientos hechos a las aeronaves
    def __init__(self, tipo):
        self.tipo = tipo # el tipo puede ser: programado o no programado

    def status(self):
        print(f"Tipo: {self.tipo}")

Mantenimiento_1 = mantenimiento("General")
Mantenimiento_2 = mantenimiento("Instrumentos")
Mantenimiento_3 = mantenimiento("Sensor de temperatura de aire")
Mantenimiento_4 = mantenimiento("Sistema de aire acondicionado")
Mantenimiento_5 = mantenimiento("Sistema hidraulico")
Mantenimiento_6 = mantenimiento("Motores")

if __name__ == "__main__":
    print("MANTENIMIENTOS")
    Mantenimiento_1.status()
    print()
    Mantenimiento_2.status()
    print()
    Mantenimiento_3.status()
    print()
    Mantenimiento_4.status()
    print()
    Mantenimiento_5.status()
    print()
    Mantenimiento_6.status()
    print()

