#menu
from Layer import Layer
def mainManu():
    print((' ' * 10) + "->  " + "WELCOME TO BRICKWORK""  <--")
    print( "RULES: ")
    print("--> Each brick is 1x2 and it can be put vertical or horizontal")
    print( "--> Enter values which are greater than 0 and not exceeding 100 !")
    print( "--> Size of the RECTANGULAR must be NxM where N is number of rows and M is number of columns ")
    print( "--> N and M must be positive and even numbers and not exceeding 100 ! ")
    print()
    print( "IMPORTANT RULES : " + "!! ENJOY !!")
    print()


def main():
    mainManu()
    print("Please enter ROWS")
    rows = int(input("Rows: " ))
    print("Please enter COLS")
    cols = int(input("Cols: "))
    first_layer = Layer(rows, cols)
    second_layer = Layer(rows, cols)
    first_layer.filling_in()
    if second_layer.solution(first_layer, second_layer, 0, 0, 0, 0) == 0:
        second_layer.print()
    else:
        print("-1")
    return 0

main()