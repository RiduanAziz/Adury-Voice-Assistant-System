// Adury Smart Home Controller
// Receives commands from Adury Voice Assistant via Serial Communication with Python

char command;

const int bedroomLight = 2; // Pin for Bedroom Light
const int table_lamp = 3;   // Pin for Table Lamp
const int fan = 4;          // Pin for Fan
const int tv = 5;           // Pin for TV

void setup() {
    Serial.begin(9600);
    
    pinMode(bedroomLight, OUTPUT);
    pinMode(table_lamp, OUTPUT);
    pinMode(fan, OUTPUT);
    pinMode(tv, OUTPUT);
    
    // Initialize all devices to OFF state
    digitalWrite(bedroomLight, LOW);
    digitalWrite(table_lamp, LOW);
    digitalWrite(fan, LOW);
    digitalWrite(tv, LOW);
}

void loop() {
    if (Serial.available() > 0) {
        command = Serial.read();
        
        switch (command) {
            // turn Bedroom Light off
            case '1':
                digitalWrite(bedroomLight, HIGH);
                break;

            // turn Bedroom Light on
            case '2':
                digitalWrite(bedroomLight, LOW);
                break;

            // turn Table Lamp off
            case '3':
                digitalWrite(table_lamp, HIGH);
                break;
            // turn Table Lamp on
            case '4':
                digitalWrite(table_lamp, LOW);
                break;

            // turn Fan off
            case '5':
                digitalWrite(fan, HIGH);
                break;
            // turn Fan on
            case '6':
                digitalWrite(fan, LOW);
                break;
                
            // turn TV off
            case '7':
                digitalWrite(tv, HIGH);
                break;
            // turn TV on
            case '8':
                digitalWrite(tv, LOW);
                break;

            // everything off
            case '9':
                digitalWrite(bedroomLight, HIGH);
                digitalWrite(table_lamp, HIGH);
                digitalWrite(fan, HIGH);
                digitalWrite(tv, HIGH);
                break;

            // everything on
            case '0':
                digitalWrite(bedroomLight, LOW);
                digitalWrite(table_lamp, LOW);
                digitalWrite(fan, LOW);
                digitalWrite(tv, LOW);
                break;
        }
    }
}

