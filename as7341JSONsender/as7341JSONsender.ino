#include <Adafruit_AS7341.h>

Adafruit_AS7341 as7341;

void setup() {
  Serial.begin(9600);

  // Wait for communication with the host computer serial monitor
  while (!Serial) {
    delay(1);
  }
  
  if (!as7341.begin()){
    Serial.println("Could not find AS7341");
    while (1) { delay(10); }
  }

  as7341.setATIME(100);
  as7341.setASTEP(100);
  as7341.setGain(AS7341_GAIN_256X);
}


void loop() {
  uint16_t readings[12];

  if (!as7341.readAllChannels(readings)){
    Serial.println("Error reading all channels!");
    return;
  }

  /*
  // These are 'out of order' so the colors match the default plotter
  // drawing colors :)
  // #1 blue
  Serial.print("{");
  Serial.print("\"ch3\": ");
  Serial.print(readings[2]);  // F3 Blue
  Serial.print(", ");
  // #2 red
  Serial.print("\"ch7\": ");
  Serial.print(readings[8]);  // F7 red
  Serial.print(", ");
  // #3 green
  Serial.print("\"ch4\": ");
  Serial.print(readings[3]); // F4 green
  Serial.print(", ");
  // #4 orange
  Serial.print("\"ch6\": ");
  Serial.print(readings[7]); // F6 orange
  Serial.print(", ");
  // #5 purple
  Serial.print("\"ch1\": ");
  Serial.print(readings[0]); // F1 violet
  Serial.print(" }");
  Serial.println();
  */
  
  Serial.print("{");
  Serial.print("\"ch0\": ");
  Serial.print(readings[0]);
  Serial.print(", ");
  Serial.print("\"ch1\": ");
  Serial.print(readings[1]);
  Serial.print(", ");
  Serial.print("\"ch2\": ");
  Serial.print(readings[2]);
  Serial.print(", ");
  Serial.print("\"ch3\": ");
  Serial.print(readings[3]);
  Serial.print(", ");
  Serial.print("\"ch4\": ");
  Serial.print(readings[4]);
  Serial.print(", ");
  Serial.print("\"ch5\": ");
  Serial.print(readings[5]);
  Serial.print(", ");
  Serial.print("\"ch6\": ");
  Serial.print(readings[6]);
  Serial.print(", ");
  Serial.print("\"ch7\": ");
  Serial.print(readings[7]);
  Serial.print(", ");
  Serial.print("\"ch8\": ");
  Serial.print(readings[8]);
  Serial.print(", ");
  Serial.print("\"ch9\": ");
  Serial.print(readings[9]);
  Serial.print(", ");
  Serial.print("\"ch10\": ");
  Serial.print(readings[10]);
  Serial.print(" }");
  Serial.println();

  
}
