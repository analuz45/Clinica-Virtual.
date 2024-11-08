#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.35.0.7523.c616a4dce modeling language!
#*

#   * Definici??n de la clase Lab

#   
# line 100 "model.ump"
# line 148 "model.ump"

class Lab():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Lab Attributes
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aLab_id, aName, aAddress, aEmail_id, aPhone):
        self._phone = None
        self._email_id = None
        self._address = None
        self._name = None
        self._lab_id = None
        self._lab_id = aLab_id
        self._name = aName
        self._address = aAddress
        self._email_id = aEmail_id
        self._phone = aPhone

    #------------------------
    # INTERFACE
    #------------------------
    def setLab_id(self, aLab_id):
        wasSet = False
        self._lab_id = aLab_id
        wasSet = True
        return wasSet

    def setName(self, aName):
        wasSet = False
        self._name = aName
        wasSet = True
        return wasSet

    def setAddress(self, aAddress):
        wasSet = False
        self._address = aAddress
        wasSet = True
        return wasSet

    def setEmail_id(self, aEmail_id):
        wasSet = False
        self._email_id = aEmail_id
        wasSet = True
        return wasSet

    def setPhone(self, aPhone):
        wasSet = False
        self._phone = aPhone
        wasSet = True
        return wasSet

    def getLab_id(self):
        return self._lab_id

    def getName(self):
        return self._name

    def getAddress(self):
        return self._address

    def getEmail_id(self):
        return self._email_id

    def getPhone(self):
        return self._phone

    def delete(self):
        pass

    # line 107 "model.ump"
    def add_lab(self):
        

    # line 108 "model.ump"
    def delete_lab(self):
        

    # line 109 "model.ump"
    def edit_lab(self):
        

    # line 110 "model.ump"
    def collect_specimen(self):
        

    # line 111 "model.ump"
    def generate_lab_report(self):
        

    def __str__(self):
        return str(super().__str__()) + "[" + "lab_id" + ":" + str(self.getLab_id()) + "," + "name" + ":" + str(self.getName()) + "," + "address" + ":" + str(self.getAddress()) + "," + "email_id" + ":" + str(self.getEmail_id()) + "," + "phone" + ":" + str(self.getPhone()) + "]"

