void setup() 
{
 pinMode(LED_BUILTIN, OUTPUT); 
  Serial.begin(9600);
}

void loop() 
{
//  if(Serial.available() > 0)
//  {
//    ;
//  }
//    char val=Serial.read();
//
//if( val == 's' )               
//  {
//
//  digitalWrite(LED_BUILTIN, HIGH);  
//  }
//  if( val == 't' )               
//  {
//
//  digitalWrite(LED_BUILTIN, LOW);  
//  }
//    
// 
// delay(5);

int values=analogRead(A0);
Serial.print(values);
//Serial.write(values);
Serial.print("$");
}
