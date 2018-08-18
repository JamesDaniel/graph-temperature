#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>

#define DHTPIN 5

#define DHTTYPE DHT22

DHT_Unified dht(DHTPIN, DHTTYPE);

uint32_t delayMS;

void setup()
{
  Serial.begin(9500);

  dht.begin();
  sensor_t sensor;
  dht.temperature().getSensor(&sensor);
}

void loop()
{
  delay(5000);

  sensors_event_t event;  
  dht.temperature().getEvent(&event);
  if (isnan(event.temperature)) {
    Serial.println("0.00");
  } else {
    Serial.println(event.temperature, 1);
  }
}

