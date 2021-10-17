from simpleai.search import SearchProblem, astar

#Initial_State:
#[[robots],[casilleros_recorridos]]
#id_robot,pos_robot,state_bateria = robots 
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
        #si es mover -> 1min
        #si recargar -> 5min
        pass

    def heuristic(self, state):
        # cantidad de tuneles que falta recorrer
        pass


