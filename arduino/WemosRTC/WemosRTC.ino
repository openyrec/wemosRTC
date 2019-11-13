#include "Wire.h"
#define DS1307_I2C_ADDRESS 0x68

bool in_settings_mode = false;
byte incomingByte;

//---------Convert functions-----------------------------------------
byte decToBcd(byte val)
{
  return ( (val/10*16) + (val%10) );
}

byte bcdToDec(byte val)
{
  return ( (val/16*10) + (val%16) );
}
//----------------------------------------------------------------------------

void setDateDs1307(byte second,        // 0-59
                   byte minute,        // 0-59
                   byte hour,          // 1-23
                   byte dayOfWeek,     // 1-7
                   byte dayOfMonth,    // 1-28/29/30/31
                   byte month,         // 1-12
                   byte year)          // 0-99
{
   Wire.beginTransmission(DS1307_I2C_ADDRESS);
   Wire.write(0);
   Wire.write(decToBcd(second));    
   Wire.write(decToBcd(minute));
   Wire.write(decToBcd(hour));     
   Wire.write(decToBcd(dayOfWeek));
   Wire.write(decToBcd(dayOfMonth));
   Wire.write(decToBcd(month));
   Wire.write(decToBcd(year));
   Wire.endTransmission();
}
//----------------------------------------------------------------------------
void getDateDs1307(byte *second,
          byte *minute,
          byte *hour,
          byte *dayOfWeek,
          byte *dayOfMonth,
          byte *month,
          byte *year)
{

  Wire.beginTransmission(DS1307_I2C_ADDRESS);
  Wire.write(0);
  Wire.endTransmission();

  Wire.requestFrom(DS1307_I2C_ADDRESS, 7);

  *second     = bcdToDec(Wire.read() & 0x7f);
  *minute     = bcdToDec(Wire.read());
  *hour       = bcdToDec(Wire.read() & 0x3f); 
  *dayOfWeek  = bcdToDec(Wire.read());
  *dayOfMonth = bcdToDec(Wire.read());
  *month      = bcdToDec(Wire.read());
  *year       = bcdToDec(Wire.read());
}
//----------------------------------------------------------------------------

void setTime(){
  Serial.println("Starten setTime function: ");
  digitalWrite(LED_BUILTIN, LOW); //Enable LED
  byte second, minute, hour, dayOfWeek, dayOfMonth, month, year;
  
  second = 45;
  minute = 3;
  hour = 7;
  dayOfWeek = 5;
  dayOfMonth = 17;
  month = 4;
  year = 8;
  setDateDs1307(second, minute, hour, dayOfWeek, dayOfMonth, month, year);
}

//------------------

void showTime(){
  
  byte second, minute, hour, dayOfWeek, dayOfMonth, month, year;
  
  getDateDs1307(&second, &minute, &hour, &dayOfWeek, &dayOfMonth, &month, &year);
  Serial.print(hour, DEC);
  Serial.print(":");
  Serial.print(minute, DEC);
  Serial.print(":");
  Serial.print(second, DEC);
  Serial.print("  ");
  Serial.print(month, DEC);
  Serial.print("-");
  Serial.print(dayOfMonth, DEC);
  Serial.print("-");
  Serial.print(year, DEC);
  Serial.print("  Day_of_week:");
  Serial.println(dayOfWeek, DEC);
}
//----------------------setup------------------------------------------------------

void setup()
{
  byte second, minute, hour, dayOfWeek, dayOfMonth, month, year;
  Wire.begin();
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH); //Disable LED

  second = 00;
  minute = 00;
  hour = 00;
  dayOfWeek = 00;
  dayOfMonth = 00;
  month = 00;
  year = 00;
  setDateDs1307(second, minute, hour, dayOfWeek, dayOfMonth, month, year);
}

//----------------------loop------------------------------------------------------


void loop()
{
  
  if (in_settings_mode == false){
    showTime();
  }
  
  if (Serial.available() > 0) {
    incomingByte = Serial.read();

                  if(incomingByte == '1'){
                    Serial.println("Here1");
                    in_settings_mode = true;
                    setTime();
              
                  }
                  else if (incomingByte == '0'){
                    Serial.println("Here0");
                    Serial.println("Finish settings");
                    digitalWrite(LED_BUILTIN, HIGH);
                    in_settings_mode = false;
                  }
    
      Serial.print("I received: ");
      Serial.println(incomingByte, DEC);
  }

  delay(1000);
}