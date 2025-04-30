const int relayPin = 7;

void setup() {
  pinMode(relayPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char cmd = Serial.read();
    if (cmd == '1') {
      digitalWrite(relayPin, HIGH);
    } else if (cmd == '0') {
      digitalWrite(relayPin, LOW);
    }
  }
}
