from .hanoi_exception import HanoiException


class State:
    """
    Class for storing and managing Hanoi game states.
    """

    DISC_CHAR = '#'
    NON_DISC_CHAR = '.'
    ROD_CHAR = '|'

    def __init__(self, move_id, depth, moved_disc, source, target, towers, n_discs):
        """
        Initializes a state with all the information needed to represent it in the requested format.

        :param move_id: Identifier of the move. Ideally, the step number.
        :param depth: Recursion depth at which this state is generated.
        :param moved_disc: The disc moved to reach this state. Ideally, a disk is defined just by its size.
        :param source: Tower from which the disc is moved.
        :param target: Tower to which the disc is moved.
        :param towers: Towers of the game.
        :param n_discs: Number of discs of the game.
        """

        self.move_id = move_id
        self.depth = depth

        self.moved_disc = moved_disc
        self.source = source
        self.target = target
        self.n_discs = n_discs

        self.num_source, self.num_target, count = 0, 0, 1
        self.torres = []
        for tower in towers:
            self.torres.append(tower.as_list())
            if not isinstance(self.source, int):
                if self.source == tower:
                    self.num_source = count
                    count += 1
                elif self.target == tower:
                    self.num_target = count
                    count += 1
                else:
                    count += 1
        # How the towers will be stored? Directly? Is that a good idea?
        #raise NotImplementedError()

    def get_tower(self, idx):
        """
        Returns the tower corresponding to the idx. Depending on the implementation of the state, this method can be
        invalid. If so, raise an exception and justify it in the report.

        :param idx: Index of the tower.
        :return: The tower corresponding to the idx.
        """
        try:
            return self.torres[idx]
        except IndexError:
            raise HanoiException("La torre no se encuentra en el juego!")

    def __repr__(self):
        """
        Returns a string with the internal representation of the state. This method can be used to represent the state
        information in a different format than the requested.

        :return: A string with the internal representation of the state.
        """
        return str(self.torres)

    def __str__(self):
        """
        Returns a string with the representation of the state in the requested format.

        :return: A string with the representation of the state in the requested format
        """
        header = "Move id " + str(self.move_id) + " Rec Depth " + str(self.depth) + "\n"
        sub_header = "Last move: " + str(self.moved_disc) + " Disk, from " + str(self.num_source) + " to " + str(self.num_target) + "\n"
        rep_tow = ""
        TOWER_EMPTY = ((self.NON_DISC_CHAR)*self.n_discs + self.ROD_CHAR + (self.NON_DISC_CHAR)*(self.n_discs))
        for i in range(self.n_discs, -1, -1):
            for j in range(0, len(self.torres)):
                if i != 0:
                    if len(self.torres[j]) < i:
                        if j == len(self.torres)-1:
                            rep_tow = rep_tow + TOWER_EMPTY + " \n"
                        else:
                            rep_tow = rep_tow + TOWER_EMPTY + " "
                    else:
                        TOWER_NOT_EMPTY = ((self.NON_DISC_CHAR)*(self.n_discs-self.torres[j][i-1])+self.DISC_CHAR*self.torres[j][i-1] +
                        self.ROD_CHAR+self.DISC_CHAR*self.torres[j][i-1]+(self.NON_DISC_CHAR)*(self.n_discs-self.torres[j][i-1]))
                        if j == len(self.torres)-1:
                            rep_tow = rep_tow + TOWER_NOT_EMPTY + " \n"
                        else:
                            rep_tow = rep_tow + TOWER_NOT_EMPTY + " "
                else:
                    rep_tow = rep_tow + " "*(self.n_discs-3) +"Tower " + str(j+1) + " "*((self.n_discs-3)+1)
        if self.depth is not None:
            return header + sub_header + rep_tow + " \n"
        else:
            return "\n" + rep_tow + "\n"
