#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.35.0.7523.c616a4dce modeling language!
#*

#   * Definici??n de la clase Patient

#   
# line 34 "model.ump"
# line 128 "model.ump"

class Patient():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Patient Attributes
    #Patient Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aPid, aName, aAge, aGender, aEmail_id, aPhone, aAddress):
        self._prescriptions = None
        self._consultations = None
        self._address = None
        self._phone = None
        self._email_id = None
        self._gender = None
        self._age = None
        self._name = None
        self._pid = None
        self._pid = aPid
        self._name = aName
        self._age = aAge
        self._gender = aGender
        self._email_id = aEmail_id
        self._phone = aPhone
        self._address = aAddress
        self._consultations = []
        self._prescriptions = []

    #------------------------
    # INTERFACE
    #------------------------
    def setPid(self, aPid):
        wasSet = False
        self._pid = aPid
        wasSet = True
        return wasSet

    def setName(self, aName):
        wasSet = False
        self._name = aName
        wasSet = True
        return wasSet

    def setAge(self, aAge):
        wasSet = False
        self._age = aAge
        wasSet = True
        return wasSet

    def setGender(self, aGender):
        wasSet = False
        self._gender = aGender
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

    def setAddress(self, aAddress):
        wasSet = False
        self._address = aAddress
        wasSet = True
        return wasSet

    def getPid(self):
        return self._pid

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def getGender(self):
        return self._gender

    def getEmail_id(self):
        return self._email_id

    def getPhone(self):
        return self._phone

    def getAddress(self):
        return self._address

    # Code from template association_GetMany 
    def getConsultation(self, index):
        aConsultation = self._consultations[index]
        return aConsultation

    #*
    
    #   * Asociaci??n con Consulta y Prescripci??n
    
    #   
    def getConsultations(self):
        newConsultations = tuple(self._consultations)
        return newConsultations

    def numberOfConsultations(self):
        number = len(self._consultations)
        return number

    def hasConsultations(self):
        has = len(self._consultations) > 0
        return has

    def indexOfConsultation(self, aConsultation):
        index = (-1 if not aConsultation in self._consultations else self._consultations.index(aConsultation))
        return index

    # Code from template association_GetMany 
    def getPrescription(self, index):
        aPrescription = self._prescriptions[index]
        return aPrescription

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
    def minimumNumberOfConsultations():
        return 0

    # Code from template association_AddUnidirectionalMany 
    def addConsultation(self, aConsultation):
        wasAdded = False
        if (aConsultation) in self._consultations :
            return False
        self._consultations.append(aConsultation)
        wasAdded = True
        return wasAdded

    def removeConsultation(self, aConsultation):
        wasRemoved = False
        if (aConsultation) in self._consultations :
            self._consultations.remove(aConsultation)
            wasRemoved = True
        return wasRemoved

    # Code from template association_AddIndexControlFunctions 
    def addConsultationAt(self, aConsultation, index):
        wasAdded = False
        if self.addConsultation(aConsultation) :
            if index < 0 :
                index = 0
            if index > self.numberOfConsultations() :
                index = self.numberOfConsultations() - 1
            self._consultations.remove(aConsultation)
            self._consultations.insert(index, aConsultation)
            wasAdded = True
        return wasAdded

    def addOrMoveConsultationAt(self, aConsultation, index):
        wasAdded = False
        if (aConsultation) in self._consultations :
            if index < 0 :
                index = 0
            if index > self.numberOfConsultations() :
                index = self.numberOfConsultations() - 1
            self._consultations.remove(aConsultation)
            self._consultations.insert(index, aConsultation)
            wasAdded = True
        else :
            wasAdded = self.addConsultationAt(aConsultation, index)
        return wasAdded

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
        self._consultations.clear()
        self._prescriptions.clear()

    # line 43 "model.ump"
    def create_patient_profile(self):
        

    # line 44 "model.ump"
    def edit_patient_profile(self):
        

    # line 45 "model.ump"
    def delete_patient_profile(self):
        

    # line 46 "model.ump"
    def request_consultation(self):
        

    def __str__(self):
        return str(super().__str__()) + "[" + "pid" + ":" + str(self.getPid()) + "," + "name" + ":" + str(self.getName()) + "," + "age" + ":" + str(self.getAge()) + "," + "gender" + ":" + str(self.getGender()) + "," + "email_id" + ":" + str(self.getEmail_id()) + "," + "phone" + ":" + str(self.getPhone()) + "," + "address" + ":" + str(self.getAddress()) + "]"

