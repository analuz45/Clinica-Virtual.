#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.35.0.7523.c616a4dce modeling language!
#*

#   * Definici??n de la clase Speciality

#   
# line 3 "model.ump"
# line 118 "model.ump"

class Speciality():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Speciality Attributes
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aSsd, aName, aDescription):
        self._description = None
        self._name = None
        self._ssd = None
        self._ssd = aSsd
        self._name = aName
        self._description = aDescription

    #------------------------
    # INTERFACE
    #------------------------
    def setSsd(self, aSsd):
        wasSet = False
        self._ssd = aSsd
        wasSet = True
        return wasSet

    def setName(self, aName):
        wasSet = False
        self._name = aName
        wasSet = True
        return wasSet

    def setDescription(self, aDescription):
        wasSet = False
        self._description = aDescription
        wasSet = True
        return wasSet

    def getSsd(self):
        return self._ssd

    def getName(self):
        return self._name

    def getDescription(self):
        return self._description

    def delete(self):
        pass

    # line 8 "model.ump"
    def add_speciality(self, ssd, name, description):
        

    # line 9 "model.ump"
    def edit_speciality(self, ssd, name, description):
        

    # line 10 "model.ump"
    def delete_speciality(self):
        

    def __str__(self):
        return str(super().__str__()) + "[" + "ssd" + ":" + str(self.getSsd()) + "," + "name" + ":" + str(self.getName()) + "," + "description" + ":" + str(self.getDescription()) + "]"

