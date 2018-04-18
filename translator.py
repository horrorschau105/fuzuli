def fuzuli(size, n, grid):
    # Open file
    out = open('prolog_output.pl', 'w')

    # Returns variable as string
    def X(i, j):
        return "X_%d_%d" % (i, j)

    # Writes new line to the file
    def writeln(s):
        out.write(s + '\n')

    # Useful flags and modules
    writeln(":- use_module(library(clpfd)).")
    writeln(":- set_prolog_flag(answer_write_options,[max_depth(0)]).")

    # Define variables and their domains
    vs = [X(i, j) for i in range(size) for j in range(size)]
    writeln("run([" + ','.join(vs) + "]) :-")
    writeln('[' + ','.join(vs) + '] ins 0..' + str(n) + ',')

    # Define rules how each row/column should look like
    variables = (['0' for i in range(size - n)] + [str(i) for i in range(1, n + 1)])
    writeln('Vs =[' + ','.join(variables) + '],')
    
    # Findall generate in prolog all possibilities for row/column
    writeln("findall(X, permutation(X, Vs), Permed),")
    for i in range(size):
        writeln('tuples_in([[' + ','.join([X(i, j) for j in range(size)]) + ']], Permed),')
        writeln('tuples_in([[' + ','.join([X(j, i) for j in range(size)]) + ']], Permed),')

    # Here we say no 2x2 square can be fully filled with digits <==> somewhere has to be zero
    for i in range(size - 1):
        for j in range(size - 1):
            writeln('*'.join([X(i, j), X(i, j + 1), X(i + 1, j), X(i + 1, j + 1)]) + " #= 0,")

    # Writes additional information got from grid
    for idx in range(len(grid)):
        i, j = idx // size, idx % size
        if grid[idx] in ['0', '-']:
            writeln(X(i, j) + ' #= 0,')
        elif grid[idx] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            writeln(X(i, j) + ' #= ' + grid[idx] + ',')

    # Closing terms
    writeln('labeling([\'ff\'], [' + ','.join(vs) + ']).')

    # Prolog magic for better look of output 
    writeln('solve(X) :- run(X), write_ln(X), fail.')
    writeln('solve(_).')
    writeln(':- solve(_), halt.')
    out.close()
