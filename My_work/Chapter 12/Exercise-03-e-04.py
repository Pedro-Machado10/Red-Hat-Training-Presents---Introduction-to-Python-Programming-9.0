"""Exercise 3
• Debug a program of your choice. Assign several breakpoints with the debugger by using the b command.
• Use the continue command to stop the execution at the breakpoints.
• Use the p command to print out the values of the variables available within the context of the current line.

Exercise 4
• Repeat Exercise 3, but start the debugger from the command line by using the -m option."""

def soma(a, b):
    resultado = a + b
    return resultado

def main():
    x = 10
    y = 5
    total = soma(x, y)
    print(total)

if __name__ == "__main__":
    main()