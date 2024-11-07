/*PLEASE DO NOT EDIT THIS CODE*/
/*This code was generated using the UMPLE 1.35.0.7523.c616a4dce modeling language!*/



// line 12 "model.ump"
// line 110 "model.ump"
public class Doctor
{

  //------------------------
  // MEMBER VARIABLES
  //------------------------

  //Doctor Attributes
  private String docid;
  private String name;
  private int age;
  private String qualification;
  private int experience;
  private String registration_number;

  //------------------------
  // CONSTRUCTOR
  //------------------------

  public Doctor(String aDocid, String aName, int aAge, String aQualification, int aExperience, String aRegistration_number)
  {
    docid = aDocid;
    name = aName;
    age = aAge;
    qualification = aQualification;
    experience = aExperience;
    registration_number = aRegistration_number;
  }

  //------------------------
  // INTERFACE
  //------------------------

  public boolean setDocid(String aDocid)
  {
    boolean wasSet = false;
    docid = aDocid;
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

  public boolean setQualification(String aQualification)
  {
    boolean wasSet = false;
    qualification = aQualification;
    wasSet = true;
    return wasSet;
  }

  public boolean setExperience(int aExperience)
  {
    boolean wasSet = false;
    experience = aExperience;
    wasSet = true;
    return wasSet;
  }

  public boolean setRegistration_number(String aRegistration_number)
  {
    boolean wasSet = false;
    registration_number = aRegistration_number;
    wasSet = true;
    return wasSet;
  }

  public String getDocid()
  {
    return docid;
  }

  public String getName()
  {
    return name;
  }

  public int getAge()
  {
    return age;
  }

  public String getQualification()
  {
    return qualification;
  }

  public int getExperience()
  {
    return experience;
  }

  public String getRegistration_number()
  {
    return registration_number;
  }

  public void delete()
  {}


  public String toString()
  {
    return super.toString() + "["+
            "docid" + ":" + getDocid()+ "," +
            "name" + ":" + getName()+ "," +
            "age" + ":" + getAge()+ "," +
            "qualification" + ":" + getQualification()+ "," +
            "experience" + ":" + getExperience()+ "," +
            "registration_number" + ":" + getRegistration_number()+ "]";
  }  
  //------------------------
  // DEVELOPER CODE - PROVIDED AS-IS
  //------------------------
  
  // line 20 "model.ump"
  void add_doctor() ;
// line 21 "model.ump"
  void edit_doctor() ;
// line 22 "model.ump"
  void delete_doctor() ;
// line 23 "model.ump"
  void provide_consultation() ;

  
}