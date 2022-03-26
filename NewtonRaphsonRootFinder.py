# Defining Function
def f(x):
    return x**3 - 10**2 - 25*x - 250

# Defining derivative of function
def g(x):
    return 3*x**2 - 25

# Implementing Newton Raphson Method

def newtonRaphson(x0, e, N):
    print('\n\n*** NEWTON RAPHSON METHOD ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break
        
        x1 = x0 - f(x0)/g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1
        
        # Stop condition if amount of iteration exceeds maximum steps
        if step > N:
            flag = 0
            break
        
        # Stop condition if |f(x1)| > tolerable error
        condition = abs(f(x1)) > e
    
    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


# Input Section
x0 = input('Enter Guess: ')
e = input('Tolerable Error: ')
N = input('Maximum Step: ')

# Converting x0 and e to float
x0 = float(x0)
e = float(e)

# Converting N to integer
N = int(N)

# Driver code
newtonRaphson(x0, e, N)