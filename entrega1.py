from simpleai.search import SearchProblem, astar

tunel = [] # Aca guardamos los tuneles globalmente

def planear_escaneo(tuneles, robots):
    '''
    A partir de los tuneles y robots recibidos
    como parametros, formulamos un estado,corremos
    el problema con ese estado y devolvemos la estructura
    de salida requerida
    '''

    INITIAL_STATE = formular_estado(robots, tuneles)

    problema = MinaProblema(INITIAL_STATE)
    resultado = astar(problema, graph_search=True)

    salida = []

    for action, state in resultado.path():
        if action is not None:
            salida.append(tuple(action))

    return salida

def formular_estado(robots,tuneles):
    '''A partir de los parametros recibidos creamos el estado inicial'''
    global tunel
    tunel = tuneles
    
    robots_modificable = list(list(robot) for robot in robots)

    for robot in robots_modificable:
        robot.append((5,0)) #Agregamos la posicion inicial de cada robot
        robot.append(1000)  #Agregamos la bateria inicial de cada robot
    
    robots = tuple(tuple(robot) for robot in robots_modificable)
    
    pendientes = tuneles
    state = (robots, pendientes)

    return state
    

'''
INITIAL_STATE= ( ​("s1", "soporte", (5,0), 1000),("s2", "soporte", (5,0),1000)),  ()  )
                                        robots                                recorridos                                  
'''

class MinaProblema(SearchProblem):

    def cost(self, state1, action, state2):
        accion = action[1]

        if accion == "mover":
            return 1
        elif accion == "cargar":
            return 5

    def is_goal(self, state):
        _ , pendientes = state
        
        if len(pendientes) == 0:
            return True
        else:
            return False     

    def actions(self,state):
        robots, _ = state
        actions = []
        
        for robot in robots:
            if robot[3] >= 100:
                #moverse dentro de tablero y si existe en tuneles
                fila_robot, colu_robot = robot[2]

                if (fila_robot-1,colu_robot) in tunel:
                    actions.append((robot[0],"mover",(fila_robot-1,colu_robot)))

                if (fila_robot+1,colu_robot) in tunel:
                    actions.append((robot[0],"mover",(fila_robot+1,colu_robot)))

                if (fila_robot,colu_robot-1) in tunel:
                    actions.append((robot[0],"mover",(fila_robot,colu_robot-1)))
    
                if (fila_robot,colu_robot+1) in tunel:
                    actions.append((robot[0],"mover",(fila_robot,colu_robot+1)))

            #si es robot Soporte recargar si hay robot Mapeadores en mismo ubicacion
            if robot[1] == "soporte":
                for robotMapeo in robots:
                    if robotMapeo[1] == "escaneador" and robot[2] == robotMapeo[2] and robotMapeo[3]<1000:
                        actions.append((robot[0],"cargar",robotMapeo[0]))
        return actions

    def result(self, state, action):
        
        
        robots, pendientes = state
        robot_origen, action_name, robot_destino = action
        
        robots_m = list(list(robot) for robot in robots)
        pendientes_m = list(pendientes)
        
        if action_name == "mover":
            robot = [robot for robot in robots_m if robot[0] == robot_origen][0]
            robot[2] = robot_destino
            if robot[1] == "escaneador":
                robot[3] = robot[3] - 100
                if robot[2] in pendientes_m:
                     pendientes_m.remove(robot[2])
        else:
            robot = [robot for robot in robots_m if robot[0] == robot_destino][0]
            robot[3] = 1000
        
                
        robots = tuple(tuple(robot) for robot in robots_m)
        pendientes = tuple(pendientes_m)

        nuevo_state = (robots, pendientes)
        

        '''
        Este codigo tarda 2 minutos menos que el de arriba. al final la compresion de listas
        gasta mas que un for comun!!!!

        if action_name == "mover":
            # si action = mover y rMapeo -> descontar bateria 100 y agregar en casilleros recorridos, si es rSoporte solo cambiar posicion
            for robot in robots_m:
                if robot[0] == robot_origen:
                    robot[2] = robot_destino
                    if robot[1] == "escaneador":
                        robot[3] = robot[3] - 100
                        if robot[2] in pendientes_m:
                            pendientes_m.remove(robot[2])
                        break
                    break
        else: # si action = recargar -> recargar bateria de robot especificado a 1000 
            for robot in robots_m:
                if robot[0] == robot_destino:
                    robot[3] = 1000
                    break

        
        robots = tuple(tuple(robot) for robot in robots_m)
        pendientes = tuple(pendientes_m)

        nuevo_state = (robots, pendientes)
        '''
                    
        return nuevo_state

    def heuristic(self, state):
        '''   
        Distancia minima a la que se encuentra el robot
        mas cercano a cada posicion pendiente de recorrer.
        Si un robot tiene mas de una posicion pendiente
        cerca, tomamos la mas lejana.
        
        robots = state[0]
        recorrido_m = list(state[1])
        faltan_recorrer = list(set(tunel)-set(recorrido_m))
        
        robots_m = list(list(robot)for robot in robots)

        for robot in robots_m:
            robot.append([])
            
        for x_c, y_c in faltan_recorrer:
            min = 999
            robot_min = ""
            for robot in robots_m:
                if robot[1] is not "soporte":
                    x_r, y_r = robot[2]
                    diferencia = (abs((x_c-x_r)+(y_c-y_r)))
                    if diferencia<min:
                        min=diferencia
                        robot_min=robot

            robot_min[4].append(min)

        suma = 0
        for robot in robots_m:
            id,nombre, pos, bat, mins = robot
            if len(mins)>0:
                suma = suma + max(mins)

        return suma
        '''

        _ , pendientes = state
        return len(pendientes)


