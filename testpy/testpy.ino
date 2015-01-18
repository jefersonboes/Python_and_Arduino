
void setup() {
  Serial.begin(115200);
}

void loop() {
  while (Serial.available() > 0) {
  
    char a;
    
    Serial.readBytes(&a, 1);
    
    Serial.println(a);
  }
}

