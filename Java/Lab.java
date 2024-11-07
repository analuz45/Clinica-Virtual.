/*PLEASE DO NOT EDIT THIS CODE*/
/*This code was generated using the UMPLE 1.35.0.7523.c616a4dce modeling language!*/



// line 77 "model.ump"
// line 135 "model.ump"
public class Lab
{

  //------------------------
  // MEMBER VARIABLES
  //------------------------

  //Lab Attributes
  private String lab_id;
  private String name;
  private String address;
  private String email_id;
  private String phone;

  //------------------------
  // CONSTRUCTOR
  //------------------------

  public Lab(String aLab_id, String aName, String aAddress, String aEmail_id, String aPhone)
  {
    lab_id = aLab_id;
    name = aName;
    address = aAddress;
    email_id = aEmail_id;
    phone = aPhone;
  }

  //------------------------
  // INTERFACE
  //------------------------

  public boolean setLab_id(String aLab_id)
  {
    boolean wasSet = false;
    lab_id = aLab_id;
    wasSet = true;
    return wasSet;
  }

  public boolean setName(String aName)
  {
    boolean wasSet = false;
    name = aName;
    wasSet = true;
    return wasSet;
  }

  public boolean setAddress(String aAddress)
  {
    boolean wasSet = false;
    address = aAddress;
    wasSet = true;
    return wasSet;
  }

  public boolean setEmail_id(String aEmail_id)
  {
    boolean wasSet = false;
    email_id = aEmail_id;
    wasSet = true;
    return wasSet;
  }

  public boolean setPhone(String aPhone)
  {
    boolean wasSet = false;
    phone = aPhone;
    wasSet = true;
    return wasSet;
  }

  public String getLab_id()
  {
    return lab_id;
  }

  public String getName()
  {
    return name;
  }

  public String getAddress()
  {
    return address;
  }

  public String getEmail_id()
  {
    return email_id;
  }

  public String getPhone()
  {
    return phone;
  }

  public void delete()
  {}


  public String toString()
  {
    return super.toString() + "["+
            "lab_id" + ":" + getLab_id()+ "," +
            "name" + ":" + getName()+ "," +
            "address" + ":" + getAddress()+ "," +
            "email_id" + ":" + getEmail_id()+ "," +
            "phone" + ":" + getPhone()+ "]";
  }  
  //------------------------
  // DEVELOPER CODE - PROVIDED AS-IS
  //------------------------
  
  // line 84 "model.ump"
  void add_lab() ;
// line 85 "model.ump"
  void delete_lab() ;
// line 86 "model.ump"
  void edit_lab() ;
// line 87 "model.ump"
  void collect_specimen() ;
// line 88 "model.ump"
  void generate_lab_report() ;
// line 92 "model.ump"
  Doctor * -- * Speciality ;
// line 93 "model.ump"
  Doctor * -- * Patient ;
// line 94 "model.ump"
  Doctor 1 -- * Consultation ;
// line 95 "model.ump"
  Patient 1 -- * Consultation ;
// line 96 "model.ump"
  Consultation 1 -- 1 Prescription ;
// line 97 "model.ump"
  Patient 1 -- * Prescription ;
// line 98 "model.ump"
  Chemist * -- * Prescription ;
// line 99 "model.ump"
  Consultation * -- * Lab ;

  
}