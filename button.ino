#define btnEnter 8
 int sender=LOW;
void setup() 
{
 pinMode(LED_BUILTIN, OUTPUT); 
  pinMode(btnEnter, INPUT);
  Serial.begin(9600);
}

void loop() 
{
 
  int values=5;
    int valuess=0;
if(digitalRead(btnEnter)==HIGH)                //DETECTION OF BUTTON INTERFACE TO HIGH
  {   
      delay(10);                               //DELAY FOR ELIMANATING EDGE JITTER(bounce)
      if(digitalRead(btnEnter)==HIGH)            //CONFIRM BUTTON IS PRESSED
      {     
        while(digitalRead(btnEnter)==HIGH);    //WAIT FOR KEY INTERFACE TO HIGH
        delay(10);                         //DELAY FOR ELIMANATING EDGE JITTER
        while(digitalRead(btnEnter)==HIGH);  //Confirm button release
 if(sender==HIGH){
Serial.print(values);
Serial.print("$");
Serial.print(values);
Serial.print("$");
 }
if(sender==LOW){
Serial.print(valuess);
Serial.print("$");
Serial.print(valuess);
Serial.print("$");
}
sender=!sender;
//Serial.println(values);
//Serial.println("$");

    }
  }

}
