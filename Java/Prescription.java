/*PLEASE DO NOT EDIT THIS CODE*/
/*This code was generated using the UMPLE 1.35.0.7523.c616a4dce modeling language!*/



// line 48 "model.ump"
// line 125 "model.ump"
public class Prescription
{

  //------------------------
  // MEMBER VARIABLES
  //------------------------

  //Prescription Attributes
  private String prescription_id;
  private String diagnosis;
  private String medicine_name;
  private String medicine_potency;
  private String medicine_frequency;
  private String remarks;
  private String lab_test;
  private String instructions_lab;
  private boolean prescription_delivered;
  private boolean lab_requests_performed;
  private double invoice_amount;

  //------------------------
  // CONSTRUCTOR
  //------------------------

  public Prescription(String aPrescription_id, String aDiagnosis, String aMedicine_name, String aMedicine_potency, String aMedicine_frequency, String aRemarks, String aLab_test, String aInstructions_lab, boolean aPrescription_delivered, boolean aLab_requests_performed, double aInvoice_amount)
  {
    prescription_id = aPrescription_id;
    diagnosis = aDiagnosis;
    medicine_name = aMedicine_name;
    medicine_potency = aMedicine_potency;
    medicine_frequency = aMedicine_frequency;
    remarks = aRemarks;
    lab_test = aLab_test;
    instructions_lab = aInstructions_lab;
    prescription_delivered = aPrescription_delivered;
    lab_requests_performed = aLab_requests_performed;
    invoice_amount = aInvoice_amount;
  }

  //------------------------
  // INTERFACE
  //------------------------

  public boolean setPrescription_id(String aPrescription_id)
  {
    boolean wasSet = false;
    prescription_id = aPrescription_id;
    wasSet = true;
    return wasSet;
  }

  public boolean setDiagnosis(String aDiagnosis)
  {
    boolean wasSet = false;
    diagnosis = aDiagnosis;
    wasSet = true;
    return wasSet;
  }

  public boolean setMedicine_name(String aMedicine_name)
  {
    boolean wasSet = false;
    medicine_name = aMedicine_name;
    wasSet = true;
    return wasSet;
  }

  public boolean setMedicine_potency(String aMedicine_potency)
  {
    boolean wasSet = false;
    medicine_potency = aMedicine_potency;
    wasSet = true;
    return wasSet;
  }

  public boolean setMedicine_frequency(String aMedicine_frequency)
  {
    boolean wasSet = false;
    medicine_frequency = aMedicine_frequency;
    wasSet = true;
    return wasSet;
  }

  public boolean setRemarks(String aRemarks)
  {
    boolean wasSet = false;
    remarks = aRemarks;
    wasSet = true;
    return wasSet;
  }

  public boolean setLab_test(String aLab_test)
  {
    boolean wasSet = false;
    lab_test = aLab_test;
    wasSet = true;
    return wasSet;
  }

  public boolean setInstructions_lab(String aInstructions_lab)
  {
    boolean wasSet = false;
    instructions_lab = aInstructions_lab;
    wasSet = true;
    return wasSet;
  }

  public boolean setPrescription_delivered(boolean aPrescription_delivered)
  {
    boolean wasSet = false;
    prescription_delivered = aPrescription_delivered;
    wasSet = true;
    return wasSet;
  }

  public boolean setLab_requests_performed(boolean aLab_requests_performed)
  {
    boolean wasSet = false;
    lab_requests_performed = aLab_requests_performed;
    wasSet = true;
    return wasSet;
  }

  public boolean setInvoice_amount(double aInvoice_amount)
  {
    boolean wasSet = false;
    invoice_amount = aInvoice_amount;
    wasSet = true;
    return wasSet;
  }

  public String getPrescription_id()
  {
    return prescription_id;
  }

  public String getDiagnosis()
  {
    return diagnosis;
  }

  public String getMedicine_name()
  {
    return medicine_name;
  }

  public String getMedicine_potency()
  {
    return medicine_potency;
  }

  public String getMedicine_frequency()
  {
    return medicine_frequency;
  }

  public String getRemarks()
  {
    return remarks;
  }

  public String getLab_test()
  {
    return lab_test;
  }

  public String getInstructions_lab()
  {
    return instructions_lab;
  }

  public boolean getPrescription_delivered()
  {
    return prescription_delivered;
  }

  public boolean getLab_requests_performed()
  {
    return lab_requests_performed;
  }

  public double getInvoice_amount()
  {
    return invoice_amount;
  }
  /* Code from template attribute_IsBoolean */
  public boolean isPrescription_delivered()
  {
    return prescription_delivered;
  }
  /* Code from template attribute_IsBoolean */
  public boolean isLab_requests_performed()
  {
    return lab_requests_performed;
  }

  public void delete()
  {}


  public String toString()
  {
    return super.toString() + "["+
            "prescription_id" + ":" + getPrescription_id()+ "," +
            "diagnosis" + ":" + getDiagnosis()+ "," +
            "medicine_name" + ":" + getMedicine_name()+ "," +
            "medicine_potency" + ":" + getMedicine_potency()+ "," +
            "medicine_frequency" + ":" + getMedicine_frequency()+ "," +
            "remarks" + ":" + getRemarks()+ "," +
            "lab_test" + ":" + getLab_test()+ "," +
            "instructions_lab" + ":" + getInstructions_lab()+ "," +
            "prescription_delivered" + ":" + getPrescription_delivered()+ "," +
            "lab_requests_performed" + ":" + getLab_requests_performed()+ "," +
            "invoice_amount" + ":" + getInvoice_amount()+ "]";
  }  
  //------------------------
  // DEVELOPER CODE - PROVIDED AS-IS
  //------------------------
  
  // line 61 "model.ump"
  void generate_invoice() ;

  
}