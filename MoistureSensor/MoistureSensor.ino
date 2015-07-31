#include "TrinketFakeUsbSerial.h"

void setup()
{
  TFUSerial.begin();
}

void loop()
{
  unsigned long time_stamp = millis();
  unsigned long wait = 1000;

  while(millis() < (time_stamp + wait)) {
    TFUSerial.task();
  }
  
  analogWrite(1, 0);
  delay(250);

  if(analogRead(1) < 200)
    analogWrite(1, 1023);    
  
  TFUSerial.println(analogRead(1));
}
