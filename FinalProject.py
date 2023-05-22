def eulers_method(startX, startY, dx):
    while x < 1.5:
        dydx = y ** x
        dy = dx * dydx
        print(round(x, 2), round(y, 2), round(dx, 2), round(dydx, 2), round(dy, 2))
        x += dx
        y += dy

    return (x, y)

def right_reimann(points):
    sum = 0
    for i in range(len(points) - 1):
        dist = points[i + 1][0] - points[i][0]
        h = points[i + 1][1]
        sum += dist * h
    return sum

def left_reimann(points):
    sum = 0
    for i in range(len(points) - 1):
        dist = points[i + 1][0] - points[i][0]
        h = points[i][1]
        sum += dist * h
    return sum

def mid_reimann(points):
    sum = 0
    for i in range(len(points) - 1):
        dist = points[i + 1][0] - points[i][0]
        h = (points[i + 1][1] + points[i][1]) / 2
        sum += dist * h
    return sum

def trap_reimann(points):
    sum = 0
    for i in range(len(points) - 1):
        dist = points[i + 1][0] - points[i][0]
        h = min(points[i + 1][1], points[i][1])
        dif = abs(points[i + 1][1] - points[i][1])
        sum += dist * h + dif * dist * 0.5
    return sum

def get_point():
    try:
        inpX = float(input('Enter X: '))
        inpY = float(input('Enter Y: '))
        return (inpX, inpY)
    except:
        print('ERROR: Invalid Input: input must be an integer or decimal value.')
        return False

def reimann_sums():
    points = []
    inp = get_point()
    if inp:
        points.append(inp)
    cont = "y"
   
    while cont.lower() == 'y':
        inp = get_point()
        if inp:
            points.append(inp)

        cont = input('Enter \'y\' if you would like to continue: ')

    points.sort()
    print(points)

    print('Options\n1. Left Reimann Sum\n2. Right Reimann Sum\n3. Midpoint Reimann Sum\n4. Trapezoid Reimann Sum')
    invalid = True
    option = 0
    while invalid:
        try:
            option = int(input('Which Reimann sum would you like to apply (1-4)?'))
            if option > 4 or option < 1:
                print('ERROR: Invalid input: input must be between 1 and 4 inclusive.')
            else:
                invalid = False
        except:
            print('ERROR: Invalid input: Input must be an integer between 1 and 4 inclusive.')
    
    if option == 1:
        sum = left_reimann(points)
    elif option == 2:
        sum = right_reimann(points)
    elif option == 3:
        sum = mid_reimann(points)
    else:
        sum = trap_reimann(points)
    return sum

def main():
    print('Options\n1. Euler\'s Method\n2. Reimann Sum')
    invalid = True
    option = 0
    while invalid:
        try:
            option = int(input('Which Reimann sum would you like to apply (1-2)? '))
            if option > 2 or option < 1:
                print('ERROR: Invalid input: input must be between 1 and 2 inclusive.')
            else:
                invalid = False
        except:
            print('ERROR: Invalid input: Input must be an integer between 1 and 2 inclusive.')
    if option == 1:
        # GET INPUT
        eulers_method()
    else:
        reimann = reimann_sums()
        print(reimann)

main()