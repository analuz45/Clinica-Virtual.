#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.35.0.7523.c616a4dce modeling language!
#*

#   * Definici??n de la clase Consultation

#   
# line 54 "model.ump"
# line 133 "model.ump"
import os

class Consultation():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Consultation Attributes
    #Consultation Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aOnline_appointment, aRequest_date, aSymptoms, aRequest_status, aPrescription):
        self._labs = None
        self._prescription = None
        self._request_status = None
        self._symptoms = None
        self._request_date = None
        self._online_appointment = None
        self._online_appointment = aOnline_appointment
        self._request_date = aRequest_date
        self._symptoms = aSymptoms
        self._request_status = aRequest_status
        if not self.setPrescription(aPrescription) :
            raise RuntimeError ("Unable to create Consultation due to aPrescription. See https://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")
        self._labs = []

    #------------------------
    # INTERFACE
    #------------------------
    def setOnline_appointment(self, aOnline_appointment):
        wasSet = False
        self._online_appointment = aOnline_appointment
        wasSet = True
        return wasSet

    def setRequest_date(self, aRequest_date):
        wasSet = False
        self._request_date = aRequest_date
        wasSet = True
        return wasSet

    def setSymptoms(self, aSymptoms):
        wasSet = False
        self._symptoms = aSymptoms
        wasSet = True
        return wasSet

    def setRequest_status(self, aRequest_status):
        wasSet = False
        self._request_status = aRequest_status
        wasSet = True
        return wasSet

    def getOnline_appointment(self):
        return self._online_appointment

    def getRequest_date(self):
        return self._request_date

    def getSymptoms(self):
        return self._symptoms

    def getRequest_status(self):
        return self._request_status

    # Code from template attribute_IsBoolean 
    def isOnline_appointment(self):
        return self._online_appointment

    # Code from template association_GetOne 
    def getPrescription(self):
        return self._prescription

    # Code from template association_GetMany 
    def getLab(self, index):
        aLab = self._labs[index]
        return aLab

    def getLabs(self):
        newLabs = tuple(self._labs)
        return newLabs

    def numberOfLabs(self):
        number = len(self._labs)
        return number

    def hasLabs(self):
        has = len(self._labs) > 0
        return has

    def indexOfLab(self, aLab):
        index = (-1 if not aLab in self._labs else self._labs.index(aLab))
        return index

    # Code from template association_SetUnidirectionalOne 
    def setPrescription(self, aNewPrescription):
        wasSet = False
        if not (aNewPrescription is None) :
            self._prescription = aNewPrescription
            wasSet = True
        return wasSet

    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfLabs():
        return 0

    # Code from template association_AddUnidirectionalMany 
    def addLab(self, aLab):
        wasAdded = False
        if (aLab) in self._labs :
            return False
        self._labs.append(aLab)
        wasAdded = True
        return wasAdded

    def removeLab(self, aLab):
        wasRemoved = False
        if (aLab) in self._labs :
            self._labs.remove(aLab)
            wasRemoved = True
        return wasRemoved

    # Code from template association_AddIndexControlFunctions 
    def addLabAt(self, aLab, index):
        wasAdded = False
        if self.addLab(aLab) :
            if index < 0 :
                index = 0
            if index > self.numberOfLabs() :
                index = self.numberOfLabs() - 1
            self._labs.remove(aLab)
            self._labs.insert(index, aLab)
            wasAdded = True
        return wasAdded

    def addOrMoveLabAt(self, aLab, index):
        wasAdded = False
        if (aLab) in self._labs :
            if index < 0 :
                index = 0
            if index > self.numberOfLabs() :
                index = self.numberOfLabs() - 1
            self._labs.remove(aLab)
            self._labs.insert(index, aLab)
            wasAdded = True
        else :
            wasAdded = self.addLabAt(aLab, index)
        return wasAdded

    def delete(self):
        self._prescription = None
        self._labs.clear()

    def __str__(self):
        return str(super().__str__()) + "[" + "online_appointment" + ":" + str(self.getOnline_appointment()) + "," + "symptoms" + ":" + str(self.getSymptoms()) + "," + "request_status" + ":" + str(self.getRequest_status()) + "]" + str(os.linesep) + "  " + "request_date" + "=" + str((((self.getRequest_date().__str__().replaceAll("  ", "    ")) if not self.getRequest_date() == self else "this") if not (self.getRequest_date() is None) else "null")) + str(os.linesep) + "  " + "prescription = " + ((format(id(self.getPrescription()), "x")) if not (self.getPrescription() is None) else "null")

