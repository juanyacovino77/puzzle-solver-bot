from simpleai.search import CspProblem
from simpleai.search.csp import backtrack
from itertools import combinations

variables = list(range(1,4)) # 1 por cada tipo de mejora posible

#limitar a una variable para cada tipo de mejora
dominios = {
    0: [("baterias_chicas",5000,10),("baterias_medianas",7500,20),("baterias_grandes",10000,50)],
    1: [("patas_extras",0,15),("mejores_motores",0,25),("orugas",0,50)],
    2: [("caja_superior",0,10),("caja_trasera",0,10)],
    3: [("radios",0,5),("video_llamadas",0,10)]
}


mejoras_disponibles = {
    'baterias_chicas':(5000,10),
    'baterias_medianas':(7500,20),
    'baterias_grandes':(10000,50),
    'patas_extras':(0,15),
    'mejores_motores':(0,25),
    'orugas':(0,50),
    'caja_superior':(0,10),
    'caja_trasera':(0,10),
    'radios':(0,5),
    'video_llamadas':(0,10),
}

restricciones = []

# --------------Restricciones binarias---------
# bateria grande necesita sistema de oruga
def baterias_grandes_si_oruga(vars, vals):
    return "baterias_grandes" in vals and "orugas" not in vals

# caja_trasera no es compatible con patas_extras
def caja_trasera_o_patas_extras(vars, vals):
    return not("caja_trasera" in vals and "patas_extras" in vals)

# sistema de radio no compatible con mejores_motores
def radio_o_mejores_motores(vars,vals):
    return not("radios" in vals and "mejores_motores" in vals)

# video_llamadas necesita orugas o patas_extras
def videollamadas_si_orugas_o_patas_extras(vars, vals):
    return "mejores_motores" in vals and "video_llamadas" in vals
    

#---------------Restricciones generales -------------
# mayor o igual a autonomia 50 minutos
def autonomia(variables, values):
    var0,var1,var2,var3 = variables
    autonomia = 0
    consumo_por_minuto = 0
    
    carga_bateria,consumo_bateria = mejoras_disponibles[var0]
    carga = carga_bateria
    consumo_por_minuto =+ consumo_bateria

    carga_mov, consumo_mov = mejoras_disponibles[var1]
    consumo_por_minuto =+ consumo_mov

    carga_caja, consumo_caja = mejoras_disponibles[var2]
    consumo_por_minuto =+ consumo_caja

    carga_comunic, consumo_comunic = mejoras_disponibles[var3]
    consumo_por_minuto =+ consumo_comunic

    autonomia = carga / consumo_por_minuto

    return (autonomia >= 50)

for var1, var2 in combinations(variables,2):
    restricciones.append((var1,var2,baterias_grandes_si_oruga))
    restricciones.append((var1,var2,caja_trasera_o_patas_extras))
    restricciones.append((var1,var2,radio_o_mejores_motores))
    restricciones.append((var1,var2,videollamadas_si_orugas_o_patas_extras))

restricciones.append((variables,autonomia))


def rediseñar_robot():
    problema = CspProblem(variables, dominios, restricciones)
    solucion = backtrack(problema)

    return solucion
    

