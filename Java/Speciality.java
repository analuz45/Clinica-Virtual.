/*PLEASE DO NOT EDIT THIS CODE*/
/*This code was generated using the UMPLE 1.35.0.7523.c616a4dce modeling language!*/



// line 2 "model.ump"
// line 105 "model.ump"
public class Speciality
{

  //------------------------
  // MEMBER VARIABLES
  //------------------------

  //Speciality Attributes
  private String ssd;
  private String name;
  private String description;

  //------------------------
  // CONSTRUCTOR
  //------------------------

  public Speciality(String aSsd, String aName, String aDescription)
  {
    ssd = aSsd;
    name = aName;
    description = aDescription;
  }

  //------------------------
  // INTERFACE
  //------------------------

  public boolean setSsd(String aSsd)
  {
    boolean wasSet = false;
    ssd = aSsd;
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

  public boolean setDescription(String aDescription)
  {
    boolean wasSet = false;
    description = aDescription;
    wasSet = true;
    return wasSet;
  }

  public String getSsd()
  {
    return ssd;
  }

  public String getName()
  {
    return name;
  }

  public String getDescription()
  {
    return description;
  }

  public void delete()
  {}


  public String toString()
  {
    return super.toString() + "["+
            "ssd" + ":" + getSsd()+ "," +
            "name" + ":" + getName()+ "," +
            "description" + ":" + getDescription()+ "]";
  }  
  //------------------------
  // DEVELOPER CODE - PROVIDED AS-IS
  //------------------------
  
  // line 7 "model.ump"
  void add_speciality(String ssd, String name, String description) ;
// line 8 "model.ump"
  void edit_speciality(String ssd, String name, String description) ;
// line 9 "model.ump"
  void delete_speciality() ;

  
}