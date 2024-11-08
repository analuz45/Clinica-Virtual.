#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.35.0.7523.c616a4dce modeling language!
#*

#   * Definici??n de la clase Doctor

#   
# line 14 "model.ump"
# line 123 "model.ump"

class Doctor():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Doctor Attributes
    #Doctor Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aDocid, aName, aAge, aQualification, aExperience, aRegistration_number):
        self._consultations = None
        self._patients = None
        self._specialities = None
        self._registration_number = None
        self._experience = None
        self._qualification = None
        self._age = None
        self._name = None
        self._docid = None
        self._docid = aDocid
        self._name = aName
        self._age = aAge
        self._qualification = aQualification
        self._experience = aExperience
        self._registration_number = aRegistration_number
        self._specialities = []
        self._patients = []
        self._consultations = []

    #------------------------
    # INTERFACE
    #------------------------
    def setDocid(self, aDocid):
        wasSet = False
        self._docid = aDocid
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

    def setQualification(self, aQualification):
        wasSet = False
        self._qualification = aQualification
        wasSet = True
        return wasSet

    def setExperience(self, aExperience):
        wasSet = False
        self._experience = aExperience
        wasSet = True
        return wasSet

    def setRegistration_number(self, aRegistration_number):
        wasSet = False
        self._registration_number = aRegistration_number
        wasSet = True
        return wasSet

    def getDocid(self):
        return self._docid

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def getQualification(self):
        return self._qualification

    def getExperience(self):
        return self._experience

    def getRegistration_number(self):
        return self._registration_number

    # Code from template association_GetMany 
    def getSpeciality(self, index):
        aSpeciality = self._specialities[index]
        return aSpeciality

    #*
    
    #   * Definici??n de asociaciones
    
    #   
    def getSpecialities(self):
        newSpecialities = tuple(self._specialities)
        return newSpecialities

    def numberOfSpecialities(self):
        number = len(self._specialities)
        return number

    def hasSpecialities(self):
        has = len(self._specialities) > 0
        return has

    def indexOfSpeciality(self, aSpeciality):
        index = (-1 if not aSpeciality in self._specialities else self._specialities.index(aSpeciality))
        return index

    # Code from template association_GetMany 
    def getPatient(self, index):
        aPatient = self._patients[index]
        return aPatient

    def getPatients(self):
        newPatients = tuple(self._patients)
        return newPatients

    def numberOfPatients(self):
        number = len(self._patients)
        return number

    def hasPatients(self):
        has = len(self._patients) > 0
        return has

    def indexOfPatient(self, aPatient):
        index = (-1 if not aPatient in self._patients else self._patients.index(aPatient))
        return index

    # Code from template association_GetMany 
    def getConsultation(self, index):
        aConsultation = self._consultations[index]
        return aConsultation

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

    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfSpecialities():
        return 0

    # Code from template association_AddUnidirectionalMany 
    def addSpeciality(self, aSpeciality):
        wasAdded = False
        if (aSpeciality) in self._specialities :
            return False
        self._specialities.append(aSpeciality)
        wasAdded = True
        return wasAdded

    def removeSpeciality(self, aSpeciality):
        wasRemoved = False
        if (aSpeciality) in self._specialities :
            self._specialities.remove(aSpeciality)
            wasRemoved = True
        return wasRemoved

    # Code from template association_AddIndexControlFunctions 
    def addSpecialityAt(self, aSpeciality, index):
        wasAdded = False
        if self.addSpeciality(aSpeciality) :
            if index < 0 :
                index = 0
            if index > self.numberOfSpecialities() :
                index = self.numberOfSpecialities() - 1
            self._specialities.remove(aSpeciality)
            self._specialities.insert(index, aSpeciality)
            wasAdded = True
        return wasAdded

    def addOrMoveSpecialityAt(self, aSpeciality, index):
        wasAdded = False
        if (aSpeciality) in self._specialities :
            if index < 0 :
                index = 0
            if index > self.numberOfSpecialities() :
                index = self.numberOfSpecialities() - 1
            self._specialities.remove(aSpeciality)
            self._specialities.insert(index, aSpeciality)
            wasAdded = True
        else :
            wasAdded = self.addSpecialityAt(aSpeciality, index)
        return wasAdded

    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfPatients():
        return 0

    # Code from template association_AddUnidirectionalMany 
    def addPatient(self, aPatient):
        wasAdded = False
        if (aPatient) in self._patients :
            return False
        self._patients.append(aPatient)
        wasAdded = True
        return wasAdded

    def removePatient(self, aPatient):
        wasRemoved = False
        if (aPatient) in self._patients :
            self._patients.remove(aPatient)
            wasRemoved = True
        return wasRemoved

    # Code from template association_AddIndexControlFunctions 
    def addPatientAt(self, aPatient, index):
        wasAdded = False
        if self.addPatient(aPatient) :
            if index < 0 :
                index = 0
            if index > self.numberOfPatients() :
                index = self.numberOfPatients() - 1
            self._patients.remove(aPatient)
            self._patients.insert(index, aPatient)
            wasAdded = True
        return wasAdded

    def addOrMovePatientAt(self, aPatient, index):
        wasAdded = False
        if (aPatient) in self._patients :
            if index < 0 :
                index = 0
            if index > self.numberOfPatients() :
                index = self.numberOfPatients() - 1
            self._patients.remove(aPatient)
            self._patients.insert(index, aPatient)
            wasAdded = True
        else :
            wasAdded = self.addPatientAt(aPatient, index)
        return wasAdded

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

    def delete(self):
        self._specialities.clear()
        self._patients.clear()
        self._consultations.clear()

    # line 22 "model.ump"
    def add_doctor(self):
        

    # line 23 "model.ump"
    def edit_doctor(self):
        

    # line 24 "model.ump"
    def delete_doctor(self):
        

    # line 25 "model.ump"
    def provide_consultation(self):
        

    def __str__(self):
        return str(super().__str__()) + "[" + "docid" + ":" + str(self.getDocid()) + "," + "name" + ":" + str(self.getName()) + "," + "age" + ":" + str(self.getAge()) + "," + "qualification" + ":" + str(self.getQualification()) + "," + "experience" + ":" + str(self.getExperience()) + "," + "registration_number" + ":" + str(self.getRegistration_number()) + "]"

