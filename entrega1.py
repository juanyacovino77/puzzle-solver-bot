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
        state = list(state)
        robot1, action_name, robot2_or_destiny = action
        if action_name == "mover":
            # si action = mover y rMapeo -> descontar bateria 100 y agregar en casilleros recorridos, si es rSoporte solo cambiar posicion
            for robot in state[0]:
                if robot[0] == robot1:
                    robot[2] = robot2_or_destiny
                    if robot[1] == "escaneador":
                        robot[3] = robot[3] - 100
                        state[1].append(robot[2])
                        break
        else:
            # si action = recargar -> recargar bateria de robot especificado a 1000
            for robot2 in state[0]:
                if robot2[0] == robot2_or_destiny:
                    robot2[2] = 1000
                    break
        return tuple(state)

    def is_goal(self, state):        
        #if (casilleros_recorridos == tuneles)
        if len(state[1]) == len(tunel):
            return true
        else:
            return false

    def cost(self, state1, action, state2):
        accion = action[1]

        if accion == "mover":
            return 1
        elif accion == "cargar":
            return 5

    def heuristic(self, state):
        # cantidad de casilleros que faltan recorrer
        return len(tunel) - len(state[1])


