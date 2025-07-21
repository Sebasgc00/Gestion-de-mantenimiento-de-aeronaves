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

class tecnico:
    def __init__(self, id, nombre, especialidad, ciudad):
        self.id = id
        self.especialidad = especialidad
        self.ciudad = ciudad
        self.nombre = nombre

    def status(self):
        print(f"id: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Ciudad: {self.ciudad}")

tecnico_1 = tecnico("75890345", "Joaquin","General", "Bogota")
tecnico_2 = tecnico("45632876", "Andres", "General", "Medellin")
tecnico_3 = tecnico("85740328", "Sofia", "Instrumentos", "Bogota")
tecnico_4 = tecnico("46328769", "Richard", "Instrumentos", "Medellin")
tecnico_5 = tecnico("47509779", "Sara", "Sensor de temperatura de aire", "Bogota")
tecnico_6 = tecnico("34572615", "Isabella", "Sensor de temperatura de aire", "Medellin")
tecnico_7 = tecnico("45087569", "Clara", "Sistema de aire acondicionado", "Bogota")
tecnico_8 = tecnico("1016593778", "Brandon Viejoski Enriquez", "Sistema de aire acondicionado", "Medellin")
tecnico_9 = tecnico("47507920", "Carlos", "Sistema Hidraulico", "Bogota")
tecnico_10 = tecnico("07896728", "Lizdi", "Sistema hidraulico", "Medellin")
tecnico_11 = tecnico("69574029", "Valeria", "Motor", "Bogota")
tecnico_12 = tecnico("03402840", "Hugo", "Motor", "Medellin")

if __name__ == "__main__":
    print("TÉCNICOS")
    tecnico_1.status()
    print()
    tecnico_2.status()
    print()
    tecnico_3.status()
    print()
    tecnico_4.status()
    print()
    tecnico_5.status()
    print()
    tecnico_6.status()
    print()
    tecnico_7.status()
    print()
    tecnico_8.status()
    print()
    tecnico_9.status()
    print()
    tecnico_10.status()
    print()
    tecnico_11.status()
    print()
    tecnico_12.status()
    print()

class hangar:
    def __init__(self, ubicacion, disponibilidad):
        self.ubicacion = ubicacion
        self.disponibilidad = disponibilidad

    def status(self):
        print(f"Ubicacion: {self.ubicacion}")
        print(f"Disponibilidad: {self.disponibilidad}")

if __name__ == "__main__":
    print("HANGARES")
    hangar_bog = hangar("Bogota", rnd.choice(["Ocupado", "Desocupado"]))
    hangar_mde = hangar("Medellin", rnd.choice(["Ocupado", "Desocupado"]))
    hangar_bog.status()
    print()
    hangar_mde.status()
    print()

if __name__ == "__main__":
    # Lista de aviones y fallas
    aviones = [Avion_1, Avion_2, Avion_3, Avion_4, Avion_5]
    fallas = [Falla_1, Falla_2, Falla_3, Falla_4, Falla_5]
    tecnicos = [tecnico_1, tecnico_2, tecnico_3, tecnico_4, tecnico_5, tecnico_6,
                tecnico_7, tecnico_8, tecnico_9, tecnico_10, tecnico_11, tecnico_12]

# Hangares
    hangares = [hangar_bog, hangar_mde]

    print("Mantenimiento por fallas inesperadas\n")

especialidades = {
        "Instrumentos defectuosos": "Instrumentos",
        "Falla del sensor de temperatura de aire": "Sensor de temperatura de aire",
        "Falla en aire acondicionado": "Sistema de aire acondicionado",
        "Perdida del sistema hidraulico": "Sistema hidraulico",
        "Falla total del motor": "Motor"
    }

for avion in aviones:
        falla_inesperada = rnd.choice(fallas)
        print(f"La aeronave {avion.matricula} - {avion.modelo} tuvo una falla inesperada")
        print(f"Falla: {falla_inesperada.descripcion} de gravedad {falla_inesperada.gravedad}")

        # Evaluar estado operativo
        if falla_inesperada.gravedad.lower() == "critica":
            print("Estado del avion: No operativo")
        else:
            print("Estado del avion: Operativo pero requiere revisión inmediata")

        # Buscar hangar disponible
        hangar_disponible = None
        for h in hangares:
            if h.disponibilidad == "Desocupado":
                hangar_disponible = h
                break

        if hangar_disponible:
            print(f"Enviando al hangar en {hangar_disponible.ubicacion}")

            especialidad_requerida = especialidades.get(falla_inesperada.descripcion, None)

            if especialidad_requerida:
                tecnico_encontrado = None
                for t in tecnicos:
                    if (t.especialidad == especialidad_requerida) and (t.ciudad in hangar_disponible.ubicacion):
                        tecnico_encontrado = t
                        break

                if tecnico_encontrado:
                    print(f"Técnico asignado: {tecnico_encontrado.nombre}")
        else:
            print("No hay hangares disponibles")

        print("-" * 50)

if __name__ == "__main__":
    # Lista de aviones 
    aviones = [Avion_1, Avion_2, Avion_3, Avion_4, Avion_5]

print("Mantenimiento por horras o ciclos de vuelo\n")

for avion in aviones:
    print(f"Aeronave {avion.matricula} - {avion.modelo}")
    print(f"Horas de vuelo: {avion.vhoras} / Ciclos de vuelo: {avion.vciclos}")

    if avion.vhoras >= 300 or avion.vciclos >= 600:
        print("Requiere mantenimiento general")

        # Filtrar hangares desocupados
        hangares_disponibles = [h for h in hangares if h.disponibilidad == "Desocupado"]

        if hangares_disponibles:
            # Elegir uno aleatorio si hay más de uno
            hangar_asignado = rnd.choice(hangares_disponibles)
            print(f"Enviando al hangar en {hangar_asignado.ubicacion}")

            # Buscar técnico de mantenimiento general en esa ciudad
            tecnico_general = None
            for t in tecnicos:
                if t.especialidad == "General" and t.ciudad == hangar_asignado.ubicacion:
                    tecnico_general = t
                    break

            if tecnico_general:
                print(f"Técnico asignado: {tecnico_general.nombre}")
        else:
            print("No hay hangares disponibles")
    elif 250 <= avion.vhoras < 300 or 500 <= avion.vciclos < 600:
        print("La aeronave está próxima a requerir mantenimiento general")
    else:
        print("La aeronave no necesita mantenimiento por horas ni ciclos")

    print("-" * 50)
