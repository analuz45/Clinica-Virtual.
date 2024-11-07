/*PLEASE DO NOT EDIT THIS CODE*/
/*This code was generated using the UMPLE 1.35.0.7523.c616a4dce modeling language!*/


import java.sql.Date;

// line 41 "model.ump"
// line 120 "model.ump"
public class Consultation
{

  //------------------------
  // MEMBER VARIABLES
  //------------------------

  //Consultation Attributes
  private boolean online_appointment;
  private Date request_date;
  private String symptoms;
  private String request_status;

  //------------------------
  // CONSTRUCTOR
  //------------------------

  public Consultation(boolean aOnline_appointment, Date aRequest_date, String aSymptoms, String aRequest_status)
  {
    online_appointment = aOnline_appointment;
    request_date = aRequest_date;
    symptoms = aSymptoms;
    request_status = aRequest_status;
  }

  //------------------------
  // INTERFACE
  //------------------------

  public boolean setOnline_appointment(boolean aOnline_appointment)
  {
    boolean wasSet = false;
    online_appointment = aOnline_appointment;
    wasSet = true;
    return wasSet;
  }

  public boolean setRequest_date(Date aRequest_date)
  {
    boolean wasSet = false;
    request_date = aRequest_date;
    wasSet = true;
    return wasSet;
  }

  public boolean setSymptoms(String aSymptoms)
  {
    boolean wasSet = false;
    symptoms = aSymptoms;
    wasSet = true;
    return wasSet;
  }

  public boolean setRequest_status(String aRequest_status)
  {
    boolean wasSet = false;
    request_status = aRequest_status;
    wasSet = true;
    return wasSet;
  }

  public boolean getOnline_appointment()
  {
    return online_appointment;
  }

  public Date getRequest_date()
  {
    return request_date;
  }

  public String getSymptoms()
  {
    return symptoms;
  }

  public String getRequest_status()
  {
    return request_status;
  }
  /* Code from template attribute_IsBoolean */
  public boolean isOnline_appointment()
  {
    return online_appointment;
  }

  public void delete()
  {}


  public String toString()
  {
    return super.toString() + "["+
            "online_appointment" + ":" + getOnline_appointment()+ "," +
            "symptoms" + ":" + getSymptoms()+ "," +
            "request_status" + ":" + getRequest_status()+ "]" + System.getProperties().getProperty("line.separator") +
            "  " + "request_date" + "=" + (getRequest_date() != null ? !getRequest_date().equals(this)  ? getRequest_date().toString().replaceAll("  ","    ") : "this" : "null");
  }
}