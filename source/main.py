class Human:
    """
    Human is a class that has is made up of atrributes

    Attributes
    ----------
    Human_1: str
        This is the first object of Human class. [Explain what it does]
    Human_2: str
        This is the second object of Human class. [Explain what it does]
    """

    def __init__(self, name_human, occupation_human):
        """
        The __init__ method is the special method that let the class initialize the object's attributes.
        This method uses the self keyword that is used to define all the instances in a pyhton class.
       
        Parameters [Explain what it does]
        ----------
            name_human : str
                    pass the name
            occupation_human : str
                    Pass the occupation    

        Attributes  [Explain what it does]
        -----------
        name : str
            Pass the name

        occupation : str
            Pass the occupation
       
        """

        self.name =name_human
        self.occupatoin=occupation_human


    def do_work(self):
        """
        do-work is a method that is called by the objects, that tells you the kind of work you need to do.

        Notes
        -----
        Do not include the `self` parameter in the ``Parameters`` section.

        Attributes [Explain what it does]
        ----------
        occupation : str
            pass the occupation of Human attribute 

        name : str
            Give the name of the Human attribute 


        Raises
        ------
        AttributeError
            The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError
            The player is only Maria

        """

        if self.occupation =="Player":
            print(self.name,"Play")

            if self.name == "Maria":
                pass
            else:
                raise ValueError('The player is only Maria')
            return True

    def speaks(self):

        """
        speak is a method, that is called by the objects,that tells you to do your work 

        Attributes   [Explain what it does]
        ----------
        occupation : str
            Tells the occupation of the Human
        name : str
            Pass the name of the Human_1
        
        """
        
        if self.occupation == "Doctor":
            print(self.name,"Treat Patients")

    def errors(self):
        pass

Human_1 = Human("Andrew", "Doctor")  
# Human_1.do_work()
# Human_1.speaks()


Human_2 = Human("Maria", "Player")
# Human_2.do_work()
# Human_2.speaks()






    
