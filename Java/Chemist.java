/*PLEASE DO NOT EDIT THIS CODE*/
/*This code was generated using the UMPLE 1.35.0.7523.c616a4dce modeling language!*/



// line 64 "model.ump"
// line 130 "model.ump"
public class Chemist
{

  //------------------------
  // MEMBER VARIABLES
  //------------------------

  //Chemist Attributes
  private String chemist_id;
  private String name;
  private String address;
  private String email_id;
  private String phone;

  //------------------------
  // CONSTRUCTOR
  //------------------------

  public Chemist(String aChemist_id, String aName, String aAddress, String aEmail_id, String aPhone)
  {
    chemist_id = aChemist_id;
    name = aName;
    address = aAddress;
    email_id = aEmail_id;
    phone = aPhone;
  }

  //------------------------
  // INTERFACE
  //------------------------

  public boolean setChemist_id(String aChemist_id)
  {
    boolean wasSet = false;
    chemist_id = aChemist_id;
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

  public String getChemist_id()
  {
    return chemist_id;
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
            "chemist_id" + ":" + getChemist_id()+ "," +
            "name" + ":" + getName()+ "," +
            "address" + ":" + getAddress()+ "," +
            "email_id" + ":" + getEmail_id()+ "," +
            "phone" + ":" + getPhone()+ "]";
  }  
  //------------------------
  // DEVELOPER CODE - PROVIDED AS-IS
  //------------------------
  
  // line 71 "model.ump"
  void add_chemist() ;
// line 72 "model.ump"
  void delete_chemist() ;
// line 73 "model.ump"
  void edit_chemist() ;
// line 74 "model.ump"
  void medicine_delivery() ;

  
}