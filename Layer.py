class Layer:

    def __init__(self, rows_temp, cols_temp):
        self.max_bricks = 0
        self.rows = 0
        self.cols = 0
        self.already_set_the_matrix = False
        self.set_rows_and_cols(rows_temp, cols_temp)
        self.rectangular = []
        self.init_rectangular()

# Validating ROWS and COLS
    def validate_rows_and_cols (self, rows_temp, cols_temp):
        return rows_temp > 0 and cols_temp > 0 and \
               rows_temp % 2 == 0 and cols_temp % 2 == 0 and \
               rows_temp < 100 and cols_temp < 100
    
# Making validation after setting their values (encapsulating the data in private fields)
    def set_rows_and_cols(self, rows_temp, cols_temp):
        while not self.validate_rows_and_cols(rows_temp, cols_temp):
            print("INVALID rows and cols.")
            print("Please enter greater than zero, not exceeding 100 and even numbers for rows and columns")
            rows_temp = int(input("Rows: "))
            cols_temp = int(input("Cols: "))
        # make the wall transposed
        # it is the same
        ###########################
        #  1 1
        #  2 2   -->   1 2 3 4
        #  3 3         1 2 3 4
        #  4 4
        ###########################
        if rows_temp > cols_temp :
            self.rows = cols_temp
            self.cols = rows_temp
        else:
            self.rows = rows_temp
            self.cols = cols_temp
        self.max_bricks = (self.rows * self.cols) // 2

    def init_rectangular(self):
        self.rectangular = [[0] * self.cols for _ in range(self.rows)]

    def get_rows(self):
        return self.rows

    def get_cols(self):
        return self.cols

    def get_layer(self):
        return self.rectangular

    def print(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.rectangular[i][j], end=' ')
            print()

    def validate_the_bricks(self, rect):
        for i in range(self.rows):
            for j in range(self.cols):
                if i + 2 < self.rows and rect[i][j] == rect[i + 2][j]:
                    print("INVALID brick. One brick is Nx1! (where N is > 2)")
                    print("Enter again the values of the matrix !")
                    return False

                elif j + 2 < self.cols and rect[i][j] == rect[i][j + 2]:
                    print("INVALID brick. Found a brick that is 1xM (where M is > 2)")
                    print("Enter again the values of the matrix !")
                    return False
        return True

    def filling_in(self):
        if self.already_set_the_matrix:
            print("It is not allowed to set another wall on the same wall ")
            return
        print("Enter the first wall: ")
        while True:
            for i in range(self.rows):
                for j in range(self.cols):
                    #Validating value in cells
                    while self.rectangular[i][j] <= 0:
                        self.rectangular[i][j] = int(input(f'[{i}][{j}]='))
                        if self.rectangular[i][j] <= 0:
                            print(f"INVALID value in position! {i} {j}")
                            print(f"Please enter greater than zero value in cell with positions {i} {j}."
                                 "Press ENTER and then continue filling in the wall")
            if self.validate_the_bricks(self.rectangular):
                break
        self.already_set_the_matrix = True

#if there is not zeros in the second wall -- > that means we found a solution

    def is_filled_second_layer(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.rectangular[i][j] == 0:
                    return False
        return True

    def solution(self, first, second,
                 first_rows, first_cols,
                 second_rows, second_cols):

        if second_cols >= self.cols - 1 and second_rows >= self.rows -1:
            return 0

        if first_cols >= self.cols:
            first_rows += 1
            first_cols = 0

        while first.get_layer()[first_rows][first_cols] == -1:
            first_cols += 1
            if first_cols >= self.cols:
                first_rows += 1
                first_cols = 0

        while  second_cols >= self.cols or second_rows >= self.rows or second.get_layer()[second_rows][second_cols] != 0:
            if second_cols + 1 >= self.cols:
                second_rows += 1
                second_cols = 0
            else:
                second_cols += 1

        if first_cols + 1 < self.cols and first.get_layer()[first_rows][first_cols] != first.get_layer()[first_rows][first_cols + 1]:
            second.get_layer()[second_rows][second_cols] = self.max_bricks
            second.get_layer()[second_rows][second_cols + 1] = self.max_bricks
            temp1 = first.get_layer()[first_rows][first_cols]
            temp2 = first.get_layer()[first_rows][first_cols + 1]
            first.get_layer()[first_rows][first_cols] = -1
            first.get_layer()[first_rows][first_cols + 1] = -1
            self.max_bricks -= 1
            if self.solution(first, second, first_rows, first_cols + 2, second_rows, second_cols + 2) == -1:
                second.get_layer()[second_rows][second_cols] = 0
                second.get_layer()[second_rows][second_cols + 1] = 0
                first.get_layer()[first_rows][first_cols] = temp1
                first.get_layer()[first_rows][first_cols + 1] = temp2
                self.max_bricks += 1

        if second_rows + 1 < self.rows and first.get_layer()[first_rows][first_cols] != first.get_layer()[first_rows + 1][first_cols]:
            second.get_layer()[second_rows][second_cols] = self.max_bricks
            second.get_layer()[second_rows + 1][second_cols] = self.max_bricks
            temp1 = first.get_layer()[first_rows][first_cols]
            temp2 = first.get_layer()[first_rows + 1][first_cols]
            first.get_layer()[first_rows][first_cols] = -1
            first.get_layer()[first_rows + 1][first_cols] = -1
            self.max_bricks -= 1
            if self.solution( first, second, first_rows, first_cols + 1, second_rows, second_cols + 1) == -1:
                second.get_layer()[second_rows][second_cols] = 0
                second.get_layer()[second_rows][second_cols + 1] = 0
                first.get_layer()[first_rows][first_cols] = temp1
                first.get_layer()[first_rows + 1][first_cols] = temp2
                self.max_bricks += 1
                
        if second.is_filled_second_layer():
            return 0
        else:
            return -1





