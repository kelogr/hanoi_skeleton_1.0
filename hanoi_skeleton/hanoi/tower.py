from .hanoi_exception import HanoiException


class Tower:
    """
    Class for storing and managing Hanoi game towers.
    """

    def __init__(self):
        """
        Initializes the tower.
        """
        self.discs = []

    def is_empty(self):
        """
        Returns if a tower is empty or not, it is, if the tower has no discs.

        :return: True if is empty, it is, if the tower has no discs, False otherwise
        """
        if self.size() == 0:
            return True
        else:
            return False
        #raise NotImplementedError()

    def size(self):
        """
        Returns the size (number of discs) of the tower.

        :return: The size (number of discs) of the tower.
        """
        return int(len(self.discs))
        #raise NotImplementedError()

    def pop_disc(self):
        """
        Removes a disc from the top of the tower and returns it.
        Raises an HanoiException if the tower is empty.

        :return: The disc removed from the top of the tower.
        """
        try:
            return self.discs.pop()
        except IndexError:
            raise HanoiException("No puedes extraer un disco de una torre vacía!")
        #raise NotImplementedError()

    '''
        Inserta un disco encima de la torre.
    '''
    def push_disc(self, disc):
        """
        Adds a dis to the top of the tower.
        Raises an HanoiException if the disc is bigger that the disc at the top of the tower.

        :param disc: The disc to be added to the top of the tower.
        """
        if self.is_empty() == True:
            self.discs.append(disc)
        elif self.discs[-1] < disc:
            raise HanoiException("El disco es superior al que está en la torre. Movimiento invalido!")
        else:
            self.discs.append(disc)

    def as_list(self):
        """
        Returns the discs of the tower as a new list (it means that if the internal representation of the tower is a
        list, it should return a copy of it).

        :return: A list containing the discs of the tower.
        """
        return list(self.discs)
        #raise NotImplementedError()

    def __repr__(self):
        """
        Returns a string with the internal representation of the tower. This method can be used to represent the tower
        information in a different format than the requested.

        :return: A string with the internal representation of the state.
        """
        return str(self.discs)
        #raise NotImplementedError()

    def __str__(self):
        """
        Returns a string with the representation of the state in the requested format.

        :return: A string with the representation of the state in the requested format
        """
        return str(self.as_list())
        #raise NotImplementedError()
