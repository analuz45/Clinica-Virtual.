#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.35.0.7523.c616a4dce modeling language!
#*

#   * Definici??n de la clase Prescription

#   
# line 66 "model.ump"
# line 138 "model.ump"

class Prescription():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Prescription Attributes
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aPrescription_id, aDiagnosis, aMedicine_name, aMedicine_potency, aMedicine_frequency, aRemarks, aLab_test, aInstructions_lab, aPrescription_delivered, aLab_requests_performed, aInvoice_amount):
        self._invoice_amount = None
        self._lab_requests_performed = None
        self._prescription_delivered = None
        self._instructions_lab = None
        self._lab_test = None
        self._remarks = None
        self._medicine_frequency = None
        self._medicine_potency = None
        self._medicine_name = None
        self._diagnosis = None
        self._prescription_id = None
        self._prescription_id = aPrescription_id
        self._diagnosis = aDiagnosis
        self._medicine_name = aMedicine_name
        self._medicine_potency = aMedicine_potency
        self._medicine_frequency = aMedicine_frequency
        self._remarks = aRemarks
        self._lab_test = aLab_test
        self._instructions_lab = aInstructions_lab
        self._prescription_delivered = aPrescription_delivered
        self._lab_requests_performed = aLab_requests_performed
        self._invoice_amount = aInvoice_amount

    #------------------------
    # INTERFACE
    #------------------------
    def setPrescription_id(self, aPrescription_id):
        wasSet = False
        self._prescription_id = aPrescription_id
        wasSet = True
        return wasSet

    def setDiagnosis(self, aDiagnosis):
        wasSet = False
        self._diagnosis = aDiagnosis
        wasSet = True
        return wasSet

    def setMedicine_name(self, aMedicine_name):
        wasSet = False
        self._medicine_name = aMedicine_name
        wasSet = True
        return wasSet

    def setMedicine_potency(self, aMedicine_potency):
        wasSet = False
        self._medicine_potency = aMedicine_potency
        wasSet = True
        return wasSet

    def setMedicine_frequency(self, aMedicine_frequency):
        wasSet = False
        self._medicine_frequency = aMedicine_frequency
        wasSet = True
        return wasSet

    def setRemarks(self, aRemarks):
        wasSet = False
        self._remarks = aRemarks
        wasSet = True
        return wasSet

    def setLab_test(self, aLab_test):
        wasSet = False
        self._lab_test = aLab_test
        wasSet = True
        return wasSet

    def setInstructions_lab(self, aInstructions_lab):
        wasSet = False
        self._instructions_lab = aInstructions_lab
        wasSet = True
        return wasSet

    def setPrescription_delivered(self, aPrescription_delivered):
        wasSet = False
        self._prescription_delivered = aPrescription_delivered
        wasSet = True
        return wasSet

    def setLab_requests_performed(self, aLab_requests_performed):
        wasSet = False
        self._lab_requests_performed = aLab_requests_performed
        wasSet = True
        return wasSet

    def setInvoice_amount(self, aInvoice_amount):
        wasSet = False
        self._invoice_amount = aInvoice_amount
        wasSet = True
        return wasSet

    def getPrescription_id(self):
        return self._prescription_id

    def getDiagnosis(self):
        return self._diagnosis

    def getMedicine_name(self):
        return self._medicine_name

    def getMedicine_potency(self):
        return self._medicine_potency

    def getMedicine_frequency(self):
        return self._medicine_frequency

    def getRemarks(self):
        return self._remarks

    def getLab_test(self):
        return self._lab_test

    def getInstructions_lab(self):
        return self._instructions_lab

    def getPrescription_delivered(self):
        return self._prescription_delivered

    def getLab_requests_performed(self):
        return self._lab_requests_performed

    def getInvoice_amount(self):
        return self._invoice_amount

    # Code from template attribute_IsBoolean 
    def isPrescription_delivered(self):
        return self._prescription_delivered

    # Code from template attribute_IsBoolean 
    def isLab_requests_performed(self):
        return self._lab_requests_performed

    def delete(self):
        pass

    # line 79 "model.ump"
    def generate_invoice(self):
        

    def __str__(self):
        return str(super().__str__()) + "[" + "prescription_id" + ":" + str(self.getPrescription_id()) + "," + "diagnosis" + ":" + str(self.getDiagnosis()) + "," + "medicine_name" + ":" + str(self.getMedicine_name()) + "," + "medicine_potency" + ":" + str(self.getMedicine_potency()) + "," + "medicine_frequency" + ":" + str(self.getMedicine_frequency()) + "," + "remarks" + ":" + str(self.getRemarks()) + "," + "lab_test" + ":" + str(self.getLab_test()) + "," + "instructions_lab" + ":" + str(self.getInstructions_lab()) + "," + "prescription_delivered" + ":" + str(self.getPrescription_delivered()) + "," + "lab_requests_performed" + ":" + str(self.getLab_requests_performed()) + "," + "invoice_amount" + ":" + str(self.getInvoice_amount()) + "]"

