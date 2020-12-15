# Object Oriented Programming
# TU856 & TU858
# Semester 1, 2020-21
# B. Schoen-Phelan
# class Document adapted from coding files available
# with Python 3 by Dusty Phillips, second edition,
# Packt Publishing
# LAB TEST SOLUTION
# 11-12-2020

class Document:
    """
    Class to handle file management for file writing.
    Class Document receives the file name at initialisation.
    """

    def __init__(self, file_name):
        self.__characters = []
        self.__cursor = 0
        self.__filename = file_name

    @property
    def characters(self):
        return self.__characters

    @characters.setter
    def characters(self, value):
        self.__characters = value

    @property
    def cursor(self):
        return self.__cursor

    @property
    def filename(self):
        return self.__filename

    def insert(self, character):
        """
        Method inserts a character at the current
        cursor position.
        Argument:
        ---------
        character : str
        the character to insert

        returns: no return
        -------
        """
        self.characters.insert(self.__cursor, character)
        self.__cursor += 1

    def delete(self):
        """
        Method deletes a character from the current
        cursor position.
        Arguments: none
        Returns: none
        Raises: IndexError
        """
        if self.__cursor >= len(self.characters):
            raise IndexError("Out of range. I am not deleting.")
        else:
            del self.characters[self.cursor]

    def save(self):
        """
        Method saves all characters in the characters list
        to a file.
        Arguments: none
        Returns: none
        Raises: FileNotFoundException
        """
        if self.__filename:
            with open(self.__filename, 'w') as f:
                f.write(''.join(self.__characters))
        else:
            raise FileNotFoundError("No file name provided.")

    def forward(self, steps):
        """
        Method fowards to a particular position in
        characters [].
        Arguments:
        ----------
        steps: int
            The amount of steps the cursor should be
            pushed forward by

        Returns: none.
        """
        self.__cursor += steps

    def backward(self, steps):
        """
        Method backward moves the cursor position to
        that specific location in the characters list.
        Arguments:
        ----------
        steps : int
            The amount of steps to go back

        Returns: none
        Raises: IndexError
        """
        # fix crashes
        # get the length of what's in the character list
        # fixes both behaviours: going into minus and
        # going from back to front
        char_length = len(self.__characters)
        if steps >= char_length:  # more than available indexes of []
            raise IndexError("Not big enough")
        else:
            self.__cursor -= steps


# initialising an object and using the class

doc = Document("lab_t2.txt")
characters = 'fake mews'

for letter in characters:
    doc.insert(letter)

try:
    doc.backward(4)
except IndexError as ie:
    print(ie)
except Exception as e:
    print("UNEXPECTED: ", e)

try:
    doc.delete()
except IndexError as ie:
    print(ie)
except Exception as e:
    print("UNEXPECTED: ", e)

print(doc.cursor)
doc.insert("n")

try:
    doc.save()
except FileNotFoundError as fnfe:
    print(fnfe)
except Exception as e:
    print("UNEXPECTED: ", e)
