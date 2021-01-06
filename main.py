from Layer import Layer


# menu
def main_menu():
    print((' ' * 10) + "->  " + "WELCOME TO BRICKWORK""  <--")
    print("RULES: ")
    print("--> Each brick is 1x2 and it can be put vertical or horizontal")
    print("--> Enter values which are greater than 0 and not exceeding 100 !")
    print("--> Size of the RECTANGULAR must be NxM where N is number of rows and M is number of columns ")
    print("--> N and M must be positive and even numbers and not exceeding 100 ! ")
    print("--> If N is greater than M we assume the matrix to be M x N because it is the same as if we transpose N x M")
    print()
    print("IMPORTANT RULES : " + "!! ENJOY !!")
    print()


# Validating ROWS and COLS
def validate_rows_and_cols(rows_temp, cols_temp):
    return rows_temp > 0 and cols_temp > 0 and \
           rows_temp % 2 == 0 and cols_temp % 2 == 0 and \
           rows_temp < 100 and cols_temp < 100


def main():
    main_menu()
    print("Please enter ROWS")
    rows = int(input("Rows: "))
    print("Please enter COLS")
    cols = int(input("Cols: "))
    while not validate_rows_and_cols(rows, cols):
        print("INVALID ROWS and COLS")
        print("Please enter greater than zero, even and not exceeding 100 numbers for ROWS and COLS")
        print("Please enter ROWS")
        rows = int(input("Rows: "))
        print("Please enter COLS")
        cols = int(input("Cols: "))
    first_layer = Layer(rows, cols)
    second_layer = Layer(rows, cols)
    first_layer.filling_in()
    if second_layer.solution(first_layer, second_layer, 0, 0, 0, 0) == 0:
        print("\nThe SECOND wall should look like so:")
        second_layer.print()
    else:
        print("-1")
    return 0


main()
