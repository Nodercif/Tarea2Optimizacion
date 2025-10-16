import time

from docplex.mp.model import Model

items = [
    "espada_hierro", "espada_diamante", "pico_hierro", "pico_diamante",
    "armadura_hierro", "armadura_oro", "hacha_piedra", "pala_madera", "arco", "escudo_hierro"
]

ganancias = {
    "espada_hierro": 25,
    "espada_diamante": 60,
    "pico_hierro": 30,
    "pico_diamante": 70,
    "armadura_hierro": 80,
    "armadura_oro": 50,
    "hacha_piedra": 10,
    "pala_madera": 5,
    "arco": 15,
    "escudo_hierro": 35
}

materiales = ["hierro", "oro", "diamante", "piedra", "madera"]

# Consumo de materiales por cada ítem:

# c[item][material]
c = {it: {m: 0 for m in materiales} for it in items}

c["espada_hierro"]["hierro"] = 3
c["espada_diamante"]["diamante"] = 2
c["pico_hierro"]["hierro"] = 3
c["pico_diamante"]["diamante"] = 3
c["armadura_hierro"]["hierro"] = 8
c["armadura_oro"]["oro"] = 4
c["hacha_piedra"]["piedra"] = 3
c["pala_madera"]["madera"] = 2
c["arco"]["madera"] = 3
c["escudo_hierro"]["hierro"] = 6

disp_semanal = {
    "hierro": 500,
    "oro": 200,
    "diamante": 50,
    "piedra": 300,
    "madera": 400
}

# Tiempos de horno por cada ítem:
# Cada ítem fabricado con hierro (espadas, picos, armaduras, escudos): 2 horas de fundición.
# Cada ítem fabricado con oro (armaduras): 1.5 horas de fundición.
# Cada ítem fabricado con piedra (hachas): 1 hora de fundición.
# Asumimos 0 si no usa ese material.

tiempo = {i: 0 for i in items}

for i in items:
  if c[i]["hierro"] > 0:
    t[i] += 2
  if c[i]["oro"] > 0:
    t[i] += 1.5
  if c[i]["piedra"] > 0:
    t[i] += 1.0
    
max_horno = 200
max_items = 150

items_trabajo = ["pico_hierro", "pico_diamante", "hacha_piedra", "pala_madera"]