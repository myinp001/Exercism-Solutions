def ineq_vio(sides):
    if sides[1] <= sides[2]:
        if sides[2] <= sides[0]:
            value = sides[1] + sides[2]
            if value <= sides[0]:
                return True
        else:
            value = sides[1] + sides[0]
            if value <= sides[2]:
                return True
    else:
        if sides[1] >= sides[0]:
            value = sides[0] + sides[2]
            if value <= sides[1]:
                return True
        else:
            value = sides[1] + sides[2]
            if value <= sides[0]:
                return True
    return False


def equilateral(sides):
    if ineq_vio(sides) == False:
        if sides[0] == sides[1] and sides[1] == sides[2]:
            if sides[0] and sides[1] and sides[2] != 0:
                return True
            else:
                return False
        else:    
            return False
    else:    
            return False

def isosceles(sides):
    if ineq_vio(sides) == False:
        if sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
            if sides[0] and sides[1] and sides[2] != 0:
                return True
            else:
                return False
        else:    
            return False
    else:    
            return False

def scalene(sides):
    if ineq_vio(sides) == False:
        if sides[1] == sides[2] or sides[0] == sides[1] or sides[0] == sides[2]:
            if sides[0] and sides[1] and sides[2] != 0:
                return False
            else:
                return True
        else:    
            return True
    else:    
            return False