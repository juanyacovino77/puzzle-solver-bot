from simpleai.search import SearchProblem, astar

tunel = [] # Aca guardamos los tuneles globalmente

def planear_escaneo(tuneles, robots):
    '''Tunel y robots que recibimos como parametros'''

    INITIAL_STATE = formular_estado(tuneles, robots)

    problema = MinaProblema(INITIAL_STATE)
    resultado = astar(problema, graph_search=False)

    # A partir de resultado contruir la estructura de dato de salida
    pass

def formular_estado(tuneles, robots):

    '''A partir de los parametros recibidos creamos el estado inicial'''
    global tunel
    tunel = tuneles

    robots_modificable = list(robot for robot in robots)

    for robot in robots_modificable:
        robot.append([5,0]) #Agregamos la posicion inicial de cada robot
        robot.append(1000)  #Agregamos la bateria inicial de cada robot

    state_modificable = [robots_modificable, () ]

    return tuple(state_modificable)
    
def convertir_a_lista(tupla):
    pass

def convertir_a_tupla(lista):
    pass


'''
INITIAL_STATE= ( ​("s1", "soporte", (5,0), 1000),("s2", "soporte", (5,0),1000)),  ()  )
                \____________________________________________________________/  \__/
                                        robots                                casilleros recorridos                                  
'''


class MinaProblema(SearchProblem):
    def actions(self,state):
        robots,casillerros_recorridos = state
        #for robot in robots
        #for robots: 
        #si es rSoporte o si es (rMapeo y bateria>0) ->  moverse entre tuneles 
        #
        #si es robot[i] == soporte y mismo lugar robot mapeo (con bateria <1000) -> recargar robot mapeo
        #if ROBOTS[robot[0]][1] == soporte
        #    for robot2 in robots
        #        if ROBOTS[robot[0]][1] == escaneador    
        #            if robot[1] == robot2[1]
                        #agregar action recargar
        pass

    def result(self, state, action):
        #si action = mover y rMapeo -> descontar bateria 100 y agregar en casilleros recorridos
        #si action = recargar -> recargar bateria a 1000
        pass

    def is_goal(self,state):
        #if (casilleros_recorridos == tuneles)
        pass

    def cost(self, state1, action, state2):
        accion = action[1]

        if accion == "mover":
            return 1
        elif accion == "cargar":
            return 5

    def heuristic(self, state):
        # cantidad de casilleros que faltan recorrer
        return len(tunel) - len(state[1])


