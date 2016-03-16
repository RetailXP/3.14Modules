void setup()
{
  Serial.begin(9600);
  Serial.setTimeout(2000);

  flash(3);
}

void flash(int num)
{
  for(int i=1; i<=num; i++)
  {
    digitalWrite(8, HIGH);
    delay(500);
    digitalWrite(8, LOW);
    delay(500); 
  }
}

void loop()
{ 
  if(Serial.available())
  {
    int val = Serial.read();
    flash(val);
  }
}
