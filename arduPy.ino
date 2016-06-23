int pin,setTo;

void setup() {
    Serial.begin(9600);     // Baud rate.
    Serial.setTimeout(5);
    int val = readData();
    while (val==0){
      pin =readData();
      setTo = readData()==0? INPUT : OUTPUT;
      pinMode(pin, setTo);
      val=readData();
    }
    action(val);
}

void loop() {
    action(readData());   // Take action accordingly.
}

char readData() {
    Serial.println("w");      // It is read by python program after which it sends the data.
    while(1) {                // Loop until something is sent via port.
        if(Serial.available() > 0) {
            return Serial.parseInt();
        }
    }
}

void action(int val) {
  switch (val) {
        case 1 :
            // set digital value
            pin =readData();
            setTo = readData()==0? LOW : HIGH;
            digitalWrite(pin, setTo); break;
        case 2 :
            //get digital value
            pin =readData();
            Serial.println(digitalRead(pin)); break;
        case 3 :
            // set analog value
            pin =readData();
            setTo=readData();
            analogWrite(pin, setTo); break;
        case 4 :
            //read analog value
            pin =readData();
            Serial.println(analogRead(pin)); break;
        case 99:
            //just dummy to cancel the current read, needed to prevent lock 
            //when the PC side dropped the "w" that we sent
            break;
        default:
            break;
    }
}

