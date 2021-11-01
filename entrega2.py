from simpleai.search import CspProblem
from simpleai.search.csp import backtrack
from itertools import combinations

variables = list(range(4)) # 1 por cada tipo de mejora posible

#limitar a una variable para cada tipo de mejora
dominios = {
    0: [("baterias_chicas",5000,10),("baterias_medianas",7500,20),("baterias_grandes",10000,50)],
    1: [("patas_extras",0,15),("mejores_motores",0,25),("orugas",0,50)],
    2: [("caja_superior",0,10),("caja_trasera",0,10)],
    3: [("radios",0,5),("video_llamadas",0,10)]
}

restricciones = []

# bateria grande necesita sistema de oruga
def baterias_grandes_si_oruga(vars, vals):
    if "batearias_grandes" in vals[0]:
        if "orugas" in vals[1]:
            return True
        else:
            return False

    return True
    

# caja_trasera no es compatible con patas_extras
def caja_trasera_o_patas_extras(vars, vals):
    if "caja_trasera" in vals[1]:
        if "patas_extras" not in vals[0]:
            return True
        else:
            return False
    
    return True

# sistema de radio no compatible con mejores_motores
def radio_o_mejores_motores(vars,vals):
    if "radios" in vals[1]:
        if "mejores_motores" not in vals[0]:
            return True
        else:
            return False
    
    return True
    

# video_llamadas necesita orugas o patas_extras
def videollamadas_si_orugas_o_patas_extras(vars, vals):
    if "video_llamadas" in vals[1]:
        if "orugas" in vals[0] or "patas_extras" in vals[0]:
            return True
        else:
            return False
    
    return True

# mayor o igual a autonomia 50 minutos
def autonomia(vars, vals):
    carga = vals[0][1]
    consumo_por_minuto = sum(value[2] for value in vals) + 100

    return (carga/consumo_por_minuto) >= 50

restricciones.append(((variables[0], variables[1]),baterias_grandes_si_oruga))
restricciones.append(((variables[1], variables[2]),caja_trasera_o_patas_extras))
restricciones.append(((variables[1], variables[3]),radio_o_mejores_motores))
restricciones.append(((variables[1], variables[3]),videollamadas_si_orugas_o_patas_extras))

restricciones.append(((variables),autonomia))


def rediseñar_robot():
    problema = CspProblem(variables, dominios, restricciones)
    solucion = backtrack(problema)

    resultados = [mejora[0] for mejora in solucion.values()]
    
    return resultados

