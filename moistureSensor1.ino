// Defining desired board pins
#define moisturePin A0
#define voltagePin A1
#define groundPin A2
#define lightPin A5
#include <SoftwareSerial.h>

// Variable declaration
int moistureStatus = 0;
int lightStatus = 0;

// Moisture sensing function; maps analog voltage to digital value
 int readMoisture() {
    int moistureValue = analogRead(moisturePin);
    int moutputValue = map(moistureValue, 0, 1023, 255, 0);
   return moutputValue;
  }

// Light sensing function
  float readLight() { 
    float lightValue = analogRead(lightPin);
    float loutputValue = lightValue / 204.8; // This converts the analog input value to a voltage value from 0-5V since 1023/5=204.8. 
    float photoresistance = (15000 * loutputValue) / (5 - loutputValue); // Calculates resistance of photoresistor for a more comprehensible value.
    return photoresistance;
  }

// Board setup
void setup() {
  pinMode(moisturePin, INPUT);
  pinMode(lightPin, INPUT);
  pinMode(voltagePin, OUTPUT);
  pinMode(groundPin, OUTPUT);
  digitalWrite(voltagePin, HIGH);
  digitalWrite(groundPin, LOW);
  Serial.begin(9600);
}

void loop() {
  // if/else if block to categorize moisture status based on input
  if (readMoisture() >= 150) { // Dry
    moistureStatus = 1;
  }
  else if (readMoisture() > 100 && readMoisture() < 150) { // Moist
    moistureStatus = 2;
  }
  else if (readMoisture() >= 70 && readMoisture() <= 100) { // Saturated
    moistureStatus = 3;
  }
  else if (readMoisture() < 70) { // Too wet
    moistureStatus = 4;
  }

  // if/else if block to categorize light status based on input
  if (readLight() > 3000) { // Dark
    lightStatus = 1;
  }
  else if (readLight() <= 3000 && readLight() >= 1000) { // Moderate
    lightStatus = 2;
  }
  else if (readLight() < 1000 && readLight() >= 700) { // Indirect Sunlight
    lightStatus = 3;
  }
  else if (readLight() < 700) { // Direct Sunlight
    lightStatus = 4;
  }

// Serial output sent to application
  Serial.print(moistureStatus);
  Serial.print(" ");
  Serial.println(lightStatus);

  delay(1000);
}

