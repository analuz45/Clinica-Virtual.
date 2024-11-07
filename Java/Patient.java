/*PLEASE DO NOT EDIT THIS CODE*/
/*This code was generated using the UMPLE 1.35.0.7523.c616a4dce modeling language!*/



// line 26 "model.ump"
// line 115 "model.ump"
public class Patient
{

  //------------------------
  // MEMBER VARIABLES
  //------------------------

  //Patient Attributes
  private String pid;
  private String name;
  private int age;
  private String gender;
  private String email_id;
  private String phone;
  private String address;

  //------------------------
  // CONSTRUCTOR
  //------------------------

  public Patient(String aPid, String aName, int aAge, String aGender, String aEmail_id, String aPhone, String aAddress)
  {
    pid = aPid;
    name = aName;
    age = aAge;
    gender = aGender;
    email_id = aEmail_id;
    phone = aPhone;
    address = aAddress;
  }

  //------------------------
  // INTERFACE
  //------------------------

  public boolean setPid(String aPid)
  {
    boolean wasSet = false;
    pid = aPid;
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

  public boolean setAge(int aAge)
  {
    boolean wasSet = false;
    age = aAge;
    wasSet = true;
    return wasSet;
  }

  public boolean setGender(String aGender)
  {
    boolean wasSet = false;
    gender = aGender;
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

  public boolean setAddress(String aAddress)
  {
    boolean wasSet = false;
    address = aAddress;
    wasSet = true;
    return wasSet;
  }

  public String getPid()
  {
    return pid;
  }

  public String getName()
  {
    return name;
  }

  public int getAge()
  {
    return age;
  }

  public String getGender()
  {
    return gender;
  }

  public String getEmail_id()
  {
    return email_id;
  }

  public String getPhone()
  {
    return phone;
  }

  public String getAddress()
  {
    return address;
  }

  public void delete()
  {}


  public String toString()
  {
    return super.toString() + "["+
            "pid" + ":" + getPid()+ "," +
            "name" + ":" + getName()+ "," +
            "age" + ":" + getAge()+ "," +
            "gender" + ":" + getGender()+ "," +
            "email_id" + ":" + getEmail_id()+ "," +
            "phone" + ":" + getPhone()+ "," +
            "address" + ":" + getAddress()+ "]";
  }  
  //------------------------
  // DEVELOPER CODE - PROVIDED AS-IS
  //------------------------
  
  // line 35 "model.ump"
  void create_patient_profile() ;
// line 36 "model.ump"
  void edit_patient_profile() ;
// line 37 "model.ump"
  void delete_patient_profile() ;
// line 38 "model.ump"
  void request_consultation() ;

  
}