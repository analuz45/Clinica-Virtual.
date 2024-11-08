#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.35.0.7523.c616a4dce modeling language!
#*

#   * Definici??n de la clase Chemist

#   
# line 83 "model.ump"
# line 143 "model.ump"

class Chemist():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Chemist Attributes
    #Chemist Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aChemist_id, aName, aAddress, aEmail_id, aPhone):
        self._prescriptions = None
        self._phone = None
        self._email_id = None
        self._address = None
        self._name = None
        self._chemist_id = None
        self._chemist_id = aChemist_id
        self._name = aName
        self._address = aAddress
        self._email_id = aEmail_id
        self._phone = aPhone
        self._prescriptions = []

    #------------------------
    # INTERFACE
    #------------------------
    def setChemist_id(self, aChemist_id):
        wasSet = False
        self._chemist_id = aChemist_id
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

    def getChemist_id(self):
        return self._chemist_id

    def getName(self):
        return self._name

    def getAddress(self):
        return self._address

    def getEmail_id(self):
        return self._email_id

    def getPhone(self):
        return self._phone

    # Code from template association_GetMany 
    def getPrescription(self, index):
        aPrescription = self._prescriptions[index]
        return aPrescription

    #*
    
    #   * Asociaci??n con Prescripci??n
    
    #   
    def getPrescriptions(self):
        newPrescriptions = tuple(self._prescriptions)
        return newPrescriptions

    def numberOfPrescriptions(self):
        number = len(self._prescriptions)
        return number

    def hasPrescriptions(self):
        has = len(self._prescriptions) > 0
        return has

    def indexOfPrescription(self, aPrescription):
        index = (-1 if not aPrescription in self._prescriptions else self._prescriptions.index(aPrescription))
        return index

    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfPrescriptions():
        return 0

    # Code from template association_AddUnidirectionalMany 
    def addPrescription(self, aPrescription):
        wasAdded = False
        if (aPrescription) in self._prescriptions :
            return False
        self._prescriptions.append(aPrescription)
        wasAdded = True
        return wasAdded

    def removePrescription(self, aPrescription):
        wasRemoved = False
        if (aPrescription) in self._prescriptions :
            self._prescriptions.remove(aPrescription)
            wasRemoved = True
        return wasRemoved

    # Code from template association_AddIndexControlFunctions 
    def addPrescriptionAt(self, aPrescription, index):
        wasAdded = False
        if self.addPrescription(aPrescription) :
            if index < 0 :
                index = 0
            if index > self.numberOfPrescriptions() :
                index = self.numberOfPrescriptions() - 1
            self._prescriptions.remove(aPrescription)
            self._prescriptions.insert(index, aPrescription)
            wasAdded = True
        return wasAdded

    def addOrMovePrescriptionAt(self, aPrescription, index):
        wasAdded = False
        if (aPrescription) in self._prescriptions :
            if index < 0 :
                index = 0
            if index > self.numberOfPrescriptions() :
                index = self.numberOfPrescriptions() - 1
            self._prescriptions.remove(aPrescription)
            self._prescriptions.insert(index, aPrescription)
            wasAdded = True
        else :
            wasAdded = self.addPrescriptionAt(aPrescription, index)
        return wasAdded

    def delete(self):
        self._prescriptions.clear()

    # line 90 "model.ump"
    def add_chemist(self):
        

    # line 91 "model.ump"
    def delete_chemist(self):
        

    # line 92 "model.ump"
    def edit_chemist(self):
        

    # line 93 "model.ump"
    def medicine_delivery(self):
        

    def __str__(self):
        return str(super().__str__()) + "[" + "chemist_id" + ":" + str(self.getChemist_id()) + "," + "name" + ":" + str(self.getName()) + "," + "address" + ":" + str(self.getAddress()) + "," + "email_id" + ":" + str(self.getEmail_id()) + "," + "phone" + ":" + str(self.getPhone()) + "]"

