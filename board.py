from cell import Cell


class Board:
    def __init__(self, num_rows: int, num_columns: int, changed_cells: list):
        """
        During initilization we create the board and set the inital pattern
        """
        # the next two lines save the dimensions of the board so we can access them in other places
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.neighbors = [  # These are all the potential offsets of neighbors to a cell
            (0, 1),
            (1, 1),
            (1, 0),
            (-1, 1),
            (-1, 0),
            (-1, -1),
            (0, -1),
            (1, -1),
        ]
        final_grid = (
            []
        )  # the initilization of what will be an array full of Cell objects, forming the board
        for row in range(num_rows):  # start of forming a list for each row
            current_row = (
                []
            )  # creates current row which will be appended to final_grid later
            for column in range(
                num_columns
            ):  # creating a Cell object for every cell in a row
                current_row.append(Cell())  # create the Cell
                if (
                    row - 1,
                    column - 1,
                ) in changed_cells:  # check if the coordinates of the just created Cell are the coordinates of a cell that should be set as alive at initilization
                    changing_cell = current_row[
                        column
                    ]  # save Cell to be modified to a buffer
                    changing_cell.set_alive()  # modify Cell
                    current_row[column] = changing_cell  # update row with changed Cell
            final_grid.append(current_row)  # append the finalized row to the main grid
        self.grid = (
            final_grid  # set the class' grid variable to the final initilized grid
        )

    def __str__(self):
        """
        This method is used to get a visual representation of the board with a capital O as an alive cell and a space as the dead cell
        """
        output = ""  # this will contain the fully formated output string
        for row in self.grid:  # get each row in the board
            for cell in row:  # get each Cell in the current row
                if cell.status():  # if the cell is alive add an O to the row
                    output += "O"
                else:  # if the cell is dead add a space to the row
                    output += " "
            output += "\n"  # add the line breaks between each row
        return output

    def get_neighbors(self, cords: tuple):
        """
        This method takes a tuple with the coordinates of a cell within the board and returns...
        a list with tuple containing the coordinates of neighbors of that cell
        """
        x = cords[0]  # get x value of cell
        y = cords[1]  # get y value of cell
        neighbors = (
            []
        )  # will contain tuples containing coordinates of all neighbors of cell
        for (
            neighbor
        ) in self.neighbors:  # iterate through all possible offsets of neighbors
            x_cord = (
                x + neighbor[0]
            )  # get the x coordinate of the neighbor by offseting the x value of the cell with a potential offset of a neighbor
            y_cord = y + neighbor[1]  # do the same with the y coordinate
            if (
                x_cord >= 0
                and y_cord >= 0
                and x_cord < self.num_rows
                and y_cord < self.num_columns
            ):  # make sure the neighbor is not off the board (one of the cords is not negative or greater than the dimension of the board)
                neighbors.append(
                    (x_cord, y_cord)
                )  # add the neighbor to the list of neighbors
        return neighbors

    def iterate_board(self):
        """
        This method iterates the board once following the rules of Conway's Game of Life
        We have to iterate through the whole board and keep track of the changes were gonna make before actually making any of them...
        because if we change one cell and then move on to the nex cell the outcome of the iteration on that cell could change because...
        of the previous change
        """
        board = self.grid  # set a local variable for the current state of the board
        changes = (
            []
        )  # will contain a list of changes to the board which will then be made
        for row_index in range(
            len(board)
        ):  # get the index of each of the rows in the board
            for column_index in range(
                len(board[0])
            ):  # the index of each of columns in the board which when combined with a row index represent a single cell
                cell = board[row_index][
                    column_index
                ]  # get the current cell from the board
                cell_status = cell.status()  # get the status of the current cell
                neighbors = self.get_neighbors(
                    (row_index, column_index)
                )  # get all the neighbors of the current cell
                num_neighbors = (
                    0  # initilize a count of the neighbors of the current cell
                )
                for (
                    neighbor_cords
                ) in neighbors:  # iterate through all the neighbors of the
                    neighbor_status = board[neighbor_cords[0]][
                        neighbor_cords[1]
                    ].status()  # get the status of the current neighbor
                    if neighbor_status:  # trigger if the neigbor is alive
                        num_neighbors += (
                            1  # increment the number of neighbors of the current cell
                        )
                if (
                    cell_status == False and num_neighbors == 3
                ):  # if the cell is dead and it has three alive neighbors then change the cell to alive
                    changes.append((row_index, column_index, True))
                elif cell_status:  # trigger if the cell is alive
                    if (
                        num_neighbors == 2 or num_neighbors == 3
                    ):  # don't do anything if the cell has 2 or 3 alive neighbors
                        pass  # ok i know theres probably a way to set up these if statments so that it dosn't use pass but it works fine here
                    else:  # if the cell doesn't have 2 or 3 alive neighbors then kill the cell
                        changes.append((row_index, column_index, False))
        for change in changes:  # get each of the changes to make to the board
            cell = board[change[0]][change[1]]  # get the cell to change
            if change[
                2
            ]:  # if the cell should be made alive, change to be alive. otherwise set it dead
                cell.set_alive()
            else:
                cell.set_dead()
