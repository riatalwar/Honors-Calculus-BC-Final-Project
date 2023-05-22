def eulers_method(x, y, numSteps, end):
    dx = (end - x) / numSteps
    while x < end:
        # Automatic dydx is y^x, can be changed manually
        dydx = y ** x
        dy = dx * dydx
        x += dx
        y += dy

    return (round(x, 2), round(y, 2))

def right_riemann(points):
    sum = 0
    for i in range(len(points) - 1):
        dist = points[i + 1][0] - points[i][0]
        h = points[i + 1][1]
        sum += dist * h
    return sum

def left_riemann(points):
    sum = 0
    for i in range(len(points) - 1):
        dist = points[i + 1][0] - points[i][0]
        h = points[i][1]
        sum += dist * h
    return sum

def mid_riemann(points):
    sum = 0
    for i in range(len(points) - 1):
        dist = points[i + 1][0] - points[i][0]
        h = (points[i + 1][1] + points[i][1]) / 2
        sum += dist * h
    return sum

def trap_riemann(points):
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

def riemann_sums():
    points = []
    inp = get_point()
    if inp:
        points.append(inp)
    cont = 'y'
   
    while cont.lower() == 'y':
        inp = get_point()
        if inp:
            points.append(inp)

        cont = input('Enter \'y\' if you would like to continue: ')

    points.sort()
    print(points)

    print('Options\n1. Left Riemann Sum\n2. Right Riemann Sum\n3. Midpoint Riemann Sum\n4. Trapezoid Riemann Sum')
    invalid = True
    option = 0
    while invalid:
        try:
            option = int(input('Which Riemann sum would you like to apply (1-4)?'))
            if option > 4 or option < 1:
                print('ERROR: Invalid input: input must be between 1 and 4 inclusive.')
            else:
                invalid = False
        except:
            print('ERROR: Invalid input: Input must be an integer between 1 and 4 inclusive.')
    
    if option == 1:
        sum = left_riemann(points)
    elif option == 2:
        sum = right_riemann(points)
    elif option == 3:
        sum = mid_riemann(points)
    else:
        sum = trap_riemann(points)
    return sum

def euler_input():
    print('This will calculate Euler\'s Method with dy/dx of y ** x')
    
    # get starting point from user
    point = get_point()
    while not point:
        point = get_point()
    
    # get number of steps from user
    invalid = True
    while invalid:
        try:
            numSteps = int(input('Enter the number of steps: '))
            invalid = False
        except:
            print('ERROR: Invalid input: dx must be an integer value.')
    
    # get final x-coord from user
    invalid = True
    while invalid:
        try:
            end = float(input('Enter the final x-coordinate: '))
            invalid = False
        except:
            print('ERROR: Invalid input: end value must be a decimal value.')
    
    return point, numSteps, end

def main():
    print('This program can calculate the value of a point using Euler\'s method or find the area under the curve using any of the Riemann sums.')
    print('Options\n1. Euler\'s Method\n2. Riemann Sum')
    
    invalid = True  # to validate user choice for Euler's/Riemann
    while invalid:
        try:
            option = int(input('Which option would you like to select (1-2)? '))
            if option > 2 or option < 1:
                print('ERROR: Invalid input: input must be between 1 and 2 inclusive.')
            else:
                invalid = False
        except:
            print('ERROR: Invalid input: Input must be an integer between 1 and 2 inclusive.')
    
    print()

    if option == 1:
        # execute Euler's method
        inp = euler_input()
        print('\nSolution:')
        point = eulers_method(inp[0][0], inp[0][1], inp[1], inp[2])
        print(point)
    else:
        # execute riemann sums
        riemann = riemann_sums()
        print('\nSolution:')
        print(riemann)

main()