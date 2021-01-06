class Layer:
    def __init__(self, rows_temp, cols_temp):
        self.max_bricks = 0
        self.rows = 0
        self.cols = 0
        self.already_set_the_matrix = False
        self.set_rows_and_cols(rows_temp, cols_temp)
        self.rectangular = []
        self.init_rectangular()

# Making validation after setting their values (encapsulating the data in private fields)
    def set_rows_and_cols (self, rows_temp, cols_temp):
        # make the wall transposed
        ###########################
        #  1 1
        #  2 2   -->   1 2 3 4
        #  3 3         1 2 3 4
        #  4 4
        ###########################
        if rows_temp > cols_temp:
            self.rows = cols_temp
            self.cols = rows_temp
        else:
            self.rows = rows_temp
            self.cols = cols_temp
        self.max_bricks = (self.rows * self.cols) // 2

    def init_rectangular(self):
        self.rectangular = [[0] * self.cols for _ in range(self.rows)]

    # Properties but done with the old good way with getters :)
    def get_rows(self):
        return self.rows

    def get_cols(self):
        return self.cols

    def get_layer(self):
        return self.rectangular

    def get_max_brick(self):
        return self.max_bricks

    def decrease_max_brick(self):
        self.max_bricks -= 1

    def increase_max_brick(self):
        self.max_bricks += 1

    # Printing the solution
    def print(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.rectangular[i][j], end=' ')
            print()

    # Checking if bricks are validated
    def validate_the_bricks(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if i + 2 < self.rows and self.rectangular[i][j] == self.rectangular[i + 2][j]:
                    print("INVALID brick. One brick is Nx1! (where N is > 2)")
                    print("Enter again the values of the matrix !")
                    return False

                elif j + 2 < self.cols and self.rectangular[i][j] == self.rectangular[i][j + 2]:
                    print("INVALID brick. Found a brick that is 1xM (where M is > 2)")
                    print("Enter again the values of the matrix !")
                    return False
        return True

    # Entering values for the first wall and validating
    def filling_in(self):
        if self.already_set_the_matrix:
            print("It is not allowed to set another wall on the same wall ")
            return
        print("Enter the first wall: ")
        while True:
            for i in range(self.rows):
                for j in range(self.cols):
                    # Validating value in cells
                    # Stop if the user enters INVALID value and continue when the value in cell i, j is correct
                    while self.rectangular[i][j] <= 0:
                        self.rectangular[i][j] = int(input(f'[{i}][{j}]='))
                        if self.rectangular[i][j] <= 0:
                            print(f"INVALID value in position! {i} {j}")
                            print(f"Please enter greater than zero value in cell with positions {i} {j}."
                                  "Press ENTER and then continue filling in the wall")
            # if first wall INVALID --> user enters again the whole wall
            if self.validate_the_bricks():
                break
            else:
                self.init_rectangular()
                self.filling_in()

        self.already_set_the_matrix = True

    # if there is no zeros in the second wall -- > we found a solution
    def is_filled_second_layer(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.rectangular[i][j] == 0:
                    return False
        return True

    # BACKTRACKING !!!
#     def solution(self, first,
#                  first_rows, first_cols,
#                  second_rows, second_cols):
#         # if we filled the second layer ---> we are on the last col and last row
#         # so we return zero for TRUE
#         if second_cols >= self.cols - 1 and second_rows >= self.rows - 1:
#             return 0
# ############## REGULATION FOR FIRST WALL ##############
#         # getting on the next row if row index is out of range
#         if first_cols >= self.cols:
#             first_rows += 1
#             first_cols = 0
#         # if we already found two different number --> we change the values in their cells in the first wall with -1
#         # here we skip these cells
#         while first.get_layer()[first_rows][first_cols] == -1:
#             first_cols += 1
#             if first_cols >= self.cols:
#                 first_rows += 1
#                 first_cols = 0
#             if first.get_rows() >= self.rows:
#                 break
# ########################################################
#
# ############## REGULATION FOR SECOND WALL ##############
#         # Only if one of these is TRUE we make regulation for row or col index
#         while second_cols >= self.cols or second_rows >= self.rows or self.rectangular[second_rows][second_cols] != 0:
#             if second_cols + 1 >= self.cols:
#                 second_rows += 1
#                 second_cols = 0
#             else:
#                 second_cols += 1
#             if second_cols >= self.cols or second_rows >= self.rows:
#                 break
#
#         if first_cols + 1 < self.cols and first.get_layer()[first_rows][first_cols] != first.get_layer()[first_rows][first_cols + 1]:
#             self.rectangular[second_rows][second_cols] = self.max_bricks
#             self.rectangular[second_rows][second_cols + 1] = self.max_bricks
#             # Saving their values in need to be restored
#             temp1 = first.get_layer()[first_rows][first_cols]
#             temp2 = first.get_layer()[first_rows][first_cols + 1]
#             # make it -1 because it needs to be skipped (in the REGULATIONS)
#             first.get_layer()[first_rows][first_cols] = -1
#             first.get_layer()[first_rows][first_cols + 1] = -1
#             # we start with max number of brick and getting down to ZERO
#             self.max_bricks -= 1
#             # if solution returns -1 it means that we start going back
#             # to find the best solution
#             # that's why i'm reestablishing the old values of the first wall
#             # and making the changed values of the second wall again zeros
#             if self.solution(first, first_rows, first_cols + 2, second_rows, second_cols + 2) == -1:
#                 self.rectangular[second_rows][second_cols] = 0
#                 self.rectangular[second_rows][second_cols + 1] = 0
#                 first.get_layer()[first_rows][first_cols] = temp1
#                 first.get_layer()[first_rows][first_cols + 1] = temp2
#                 self.max_bricks += 1
#
#         if second_rows + 1 < self.rows and first.get_layer()[first_rows][first_cols] != first.get_layer()[first_rows + 1][first_cols]:
#             self.rectangular[second_rows][second_cols] = self.max_bricks
#             self.rectangular[second_rows + 1][second_cols] = self.max_bricks
#             temp1 = first.get_layer()[first_rows][first_cols]
#             temp2 = first.get_layer()[first_rows + 1][first_cols]
#             first.get_layer()[first_rows][first_cols] = -1
#             first.get_layer()[first_rows + 1][first_cols] = -1
#             self.max_bricks -= 1
#             if self.solution(first, first_rows, first_cols + 1, second_rows, second_cols + 1) == -1:
#                 self.rectangular[second_rows][second_cols] = 0
#                 self.rectangular[second_rows][second_cols + 1] = 0
#                 first.get_layer()[first_rows][first_cols] = temp1
#                 first.get_layer()[first_rows + 1][first_cols] = temp2
#                 self.max_bricks += 1
#
#         if self.is_filled_second_layer():
#             return 0
#         else:
#             return -1
    # BACKTRACKING !!!!
    def solution(self, first, second, first_rows, first_cols, second_rows, second_cols):
        # if we filled the second layer ---> we are on the last col and last row
        # so we return zero for TRUE
        if second_cols >= self.cols - 1 and second_rows >= self.rows - 1:
            return 0
############## REGULATION FOR FIRST WALL ##############
        # getting on the next row if row index is out of range
        if first_cols >= self.cols:
            first_rows += 1
            first_cols = 0
        # if we already found two different number --> we change the values in their cells in the first wall with -1
        # here we skip these cells
        while first.get_layer()[first_rows][first_cols] == -1:
            first_cols += 1
            if first_cols >= self.cols:
                first_rows += 1
                first_cols = 0
            if first.get_rows() >= self.rows:
                break
########################################################

############## REGULATION FOR SECOND WALL ##############
        # Only if one of these is TRUE we make regulation for row or col index
        while second_cols >= self.cols or second_rows >= self.rows or second.get_layer()[second_rows][second_cols] != 0:
            if second_cols + 1 >= self.cols:
                second_rows += 1
                second_cols = 0
            else:
                second_cols += 1
            if second_cols >= self.cols or second_rows >= self.rows:
                break

        if first_cols + 1 < self.cols and first.get_layer()[first_rows][first_cols] != first.get_layer()[first_rows][first_cols + 1]:
            helper_for_backtracking(first, second, first_rows, first_cols,second_rows, second_cols, 2, 1, 0)
        if second_rows + 1 < self.rows and first.get_layer()[first_rows][first_cols] != first.get_layer()[first_rows + 1][first_cols]:
            helper_for_backtracking(first, second, first_rows, first_cols,second_rows, second_cols, 1, 0, 1)

        if self.is_filled_second_layer():
            return 0
        else:
            return -1


def helper_for_backtracking(first, second, first_rows, first_cols, second_rows, second_cols, _, first_if, second_if):
    second.get_layer()[second_rows][second_cols] = second.get_max_brick()
    second.get_layer()[second_rows + second_if][second_cols + first_if] = second.get_max_brick()
    temp1 = first.get_layer()[first_rows][first_cols]
    temp2 = first.get_layer()[first_rows + second_if][first_cols + first_if]
    first.get_layer()[first_rows][first_cols] = -1
    first.get_layer()[first_rows + second_if][first_cols + first_if] = -1
    second.decrease_max_brick()
    if second.solution(first, second, first_rows, first_cols + _, second_rows, second_cols + _) == -1:
        second.get_layer()[second_rows][second_cols] = 0
        second.get_layer()[second_rows + first_if][second_cols + second_if] = 0
        first.get_layer()[first_rows][first_cols] = temp1
        first.get_layer()[first_rows + second_if][first_cols + first_if] = temp2
        second.increase_max_brick()
