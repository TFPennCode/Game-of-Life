class Cell:
    """
    The object "Cell" has 3 methods:

    One to set the status of the cell to alive
    One to set the status of the cell to dead
    One that returns the status of the cell (Returns a Boolean. True for Alive and False for Dead)
    """

    def __init__(self):
        # Initalizes state of Cell. By default the cell is dead.
        self.alive = False

    def set_alive(self):
        # Changes the cell's "alive" property to True
        self.alive = True

    def set_dead(self):
        # Changes the cell's "alive" property to False
        self.alive = False

    def status(self):
        # Returns the current state of the cell (True or False depending)
        return self.alive
