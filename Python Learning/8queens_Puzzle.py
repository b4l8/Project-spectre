#! /usr/bin/env python

# state save the state of queen , state[row-1] = col-1 


def conflict(state,nextX):
    """ (nextX,nextY) tell position of the next queen, Y = row , x = col
    this function check if this queen has conflict with the previous queens
    state[i] - nextX == 0 means in the same col
    state[i] - nextX == nextY-i means in the same diagonal
    one state in one row so no worry about same row issue"""
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0,nextY-i):
            return True
    return False
#counter = 0
def queens(num=8,state=()):
    """
    find position for the last queen
    """
    #global counter
    for pos in range(num):
        if not conflict(state,pos):
            #print state
            if len(state) == num-1:# final recursion 
                #counter+=10
                #print "%d:"%counter + str((pos,))
                yield (pos,)
            else:# give all solution
                for result in queens(num,state+(pos,)):
                    #state +(pos,)  state tree traveled form:
                    """
                        ()
                        (0,)        (1,)        (2,)        (3,)
                        (0,0..3,)   (1,0..3,)   (2,0..3,)   (3,0..3,)
                        ......      .....       .....       .....
                        ......      .....       .....       .....
                    """
                    #counter+=1
                    #print "%d:"%counter+ str((pos,)+result)
                    yield (pos,)+result


"""
given this :
||   | x |   |   ||
||   |   |   | x ||
|| x |   |   |   ||
|| ? | ? | ? | ? ||
"""
#print list(queens(4,(1,3,0)))

print list(queens(4))
