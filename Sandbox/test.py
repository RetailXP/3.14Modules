void setup()
{
    Serial.begin(9600);
    Serial.setTimeout(5000);

    pinMode(8, OUTPUT);
    digitalWrite(8, HIGH);
}

int num = 0;

int reciBytes[15] = {0x80, 0xd, 0x1, 0x1, 0x1, 0x2, 0x3, 0x4, 0x0, 0x5, 0x0, 0x6, 0x0, 0x7, 0x0};
const int c_receiBytesLen = 15;
int retBytes[5] = {0x80, 0x3, 0x1, 0x1, 0x2};
const int c_retBytesLen = 5;


void flash(int num)
{
  for(int i=1; i<=num; i++)
  {
    digitalWrite(8, HIGH);
    delay(200);
    digitalWrite(8, LOW);
    delay(200); 
  }
}

void loop()
{
    flash(3);

    int numByteReceived = 0;
    while(numByteReceived < c_receiBytesLen)
    {
      int byteReceived = -1;
      if(Serial.available())
      {
        int byteReceived = Serial.read();
        flash(1);
      }
      else
        continue;
      
      if(byteReceived == reciBytes[numByteReceived])
      {
        ++numByteReceived;
      }
      delay(500);
    }

    for(int i=0; i<c_retBytesLen; i++)
    {
      Serial.write(retBytes[i]);
    }

    delay(1000);
}

