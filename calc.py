import math

# standard symbols that are supported by the keyboard
SYMBOLS = ['+', '-', '*', '/', '^', '(', ')', '!', '%']

# contains abbreviations for symbols not supported by the keyboard but also functions
FUNCTIONS = {
    '':lambda x: x, # called when standard parenthesis are used
    '-':lambda x: -x, # called when - is front of parenthesis
    'sqrt':lambda x : math.sqrt(x), # it doesn't support other roots such as cubed root but that's possible with ^(1/3)
    'log':lambda x : math.log(x, 10), # can calculate other logs with logB(A) = log(A) / log(B)
    'ln':lambda x : math.log(x),
    'sin':lambda x : math.sin(x),
    'cos':lambda x : math.cos(x),
    'tan':lambda x : math.tan(x),
    'pi':lambda x : math.pi * x,
    'e':lambda x : math.e * x,
    'tau':lambda x : math.tau * x
}

# contains all supported constants
CONSTANTS = {
    'pi':math.pi,
    #'-pi':-math.pi,
    'e':math.e,
    #'-e':-math.e,
    'tau':math.tau,
   #'-tau':-math.tau
}

# turns user input into a list containing both numbers and operators
# note that any values in a list throughout this program are kept as strings
def format_input(initialInput):
    modifiedInput = ''

    # converts users input into a more standardized form for the program to use
    for i in range(len(initialInput)):
        ch = initialInput[i]
        try: 
            # puts * between numbers, constants, and functions
            if i > 0 and modifiedInput[-1].isnumeric() and ch.isalpha():
                modifiedInput += ' * '
            
            # only applies to symbols # not (not initialInput[i - 1].isnumeric() and ch != '(') and
            elif i > 0 and ch in SYMBOLS:
                if ch == '(':
                    # converts '3(' to '3 * ('
                    if modifiedInput[-1].isnumeric() or modifiedInput[-1] == 'x' or initialInput[i - 1] == ')':
                        modifiedInput += ' * '
                # adds a space to seperate symbols and numbers
                else:
                    modifiedInput += ' '

        except IndexError:
            pass

        # this code is the result of an hour of debugging and I don't understand it
        # it's probably unneccesarily complicated but it works and I don't feel like fixing it
        if ch == '-' and initialInput[i + 1].isnumeric():
            if len(modifiedInput) != 0 and not modifiedInput[-2] in SYMBOLS:
                modifiedInput += '+ '
            modifiedInput += '-'

        elif ch == '-' and i == 0:
            modifiedInput += '0 - '
        
        elif ch == ' ':
            if not (modifiedInput[-1] == '-' and modifiedInput[-3] == '+'):
                modifiedInput += ch
        else:
            modifiedInput += ch
        
            try:
                if initialInput[i + 1] != ' ' and ch in SYMBOLS and not(ch == '-' and initialInput[i + 1] == '('):
                    modifiedInput += ' '
                if (initialInput[i + 1].isalpha() or initialInput[i + 1].isnumeric()) and ch == ')':
                    modifiedInput += '* '
            except IndexError:
                pass
        #print(modifiedInput)

    eq = modifiedInput.split(' ')

    # removes blank items
    while '' in eq:
        eq.remove('')

    # replaces constants with values, also applies factorial
    i = 0
    while i < len(eq):
        if eq[i].lower() in CONSTANTS.keys():
            eq[i] = str(CONSTANTS[eq[i].lower()])
        
        i += 1

    return eq

# given a list of operators (such as '+') and a corresponding list of functions (such as lambda a, b : a + b)
# goes through eq (equation) and performs any matching operations that it finds
def calculate(eq, operators, operations):
    i = 0
    while i < len(eq):
        if eq[i] in operators:
            #print(str(eq[i - 1]) + str(eq[i]) + str(eq[i + 1]))
            operator = operators.index(eq[i])
            operation = operations[operators.index(eq[i])]

            eq[i - 1] = str(operation(float(eq[i - 1]), float(eq.pop(i + 1))))
            eq.pop(i)
        else:
            i += 1

    return eq

# the main calculation method, recursively called for parenthesis
def calculate_all(eq):
    #print('calculating G ' + str(eq))
    I = 0
    while I < len(eq):
        # handles parenthesis and functions
        if '(' in eq[I]:
            func = eq[I][0 : len(eq[I]) - 1]
            
            balance = -1
            
            i1 = I
            i2 = 0

            # figures out when the chosen parenthesis end
            i = i1
            while balance != 0:
                i += 1
                if '(' in eq[i]:
                    balance -= 1
                elif eq[i] == ')':
                    balance += 1
                    i2 = i

            # calculates the parenthesis and replaces values
            val = calculate_all(eq[i1 + 1 : i2])
            for i in range(i2 - i1):
                eq.pop(i1 + 1)

            eq[I] = str(FUNCTIONS[func](val))

        I += 1
    # calculates factorial
    i = 0
    while i < len(eq):
        if eq[i] == '!':
            eq[i - 1] = str(math.factorial(float(eq[i - 1])))
            eq.pop(i)
        i += 1
    
    # finishes order of operations
    #print('calculating E ' + str(eq))
    eq = calculate(eq, ['^'], [lambda a, b : a ** b])
    #print('calculating M ' + str(eq))
    eq = calculate(eq, ['*', '/', '%'], [lambda a, b : a * b, lambda a, b : a / b, lambda a, b : a % b])
    #print('calculating A ' + str(eq))
    eq = calculate(eq, ['+', '-'], [lambda a, b : a + b, lambda a, b : a - b])

    return float(eq[0])

# replaces any 'x' with a chosen value
def replace_x(eq, x):
    for i in range(len(eq)):
        if 'x' in eq[i]:
            if eq[i] == 'x':
                eq[i] = str(x)
            else:
                eq[i] = str(float(eq[i][0:len(eq[i]) - 1]) * float(x))
    #print(eq)
    return eq
    
inp = input('equation: ')
equation = format_input(inp)
#print(equation)
results = []
max = 0
min = 0
for i in range(40 * 4):
    try:
        results.append(calculate_all(replace_x([] + equation, i / 4)))
    except:
        results.append(math.nan)
    if results[-1] > max:
        max = results[-1]
    elif results[-1] < min:
        min = results[-1]
    #print(results[-1])
    
scale = 1
if max > -min:
    scale = max // 20

    while max > scale * 20:
        scale += 1
elif min > -max:
    scale = min // 20
    
    while -min > scale * 20:
        scale += 1

if max < 5 and min > -5:
    scale = 0.25

map = []
for y in range(41):
    column = []
    for x in range(40):
        if y == 20:
            if x % 5 == 4:
                column.append('|')
            else:
                column.append('-')
        else:
            column.append(' ')
    map.append(column)

for i in range(len(results)):
    #print(results[i])
    if math.isnan(results[i]):
        map[20][i // 4] = '?'
    else:
        if i % 4 == 0:
            map[int(20 - results[i] // scale)][i // 4] = 'X'
        elif map[int(20 - results[i] // scale)][i // 4] != 'X':
            map[int(20 - results[i] // scale)][i // 4] = 'x'

print('y scale = ' + str(scale))
print('x scale = 1.0')
for y in range(len(map)):
    print(' '.join(map[y]))
