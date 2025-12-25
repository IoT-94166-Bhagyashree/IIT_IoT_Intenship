void setup() {
  pinMode(2, OUTPUT);
}

void loop() {
  digitalWrite(2, HIGH); // LED ON
  delay(1000);
  digitalWrite(2, LOW);  // LED OFF
  delay(1000);
}

