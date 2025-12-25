#include<WiFi.h>
#include<WebServer.h>

const char *ssid = "SUNBEAM";
const char *password = "1234567890";

WebServer server(80);

void welcome(){
  server.send(200, "text/html", "<html><body><h1>This is welcome page<\h1><body><\html>");
}

void ledon(){
  digitalWrite(2, HIGH);
  server.send(200, "text/html", "<html><body><h1>LED is turned ON<\h1><body><\html>");
}

void ledoff(){
  digitalWrite(2, LOW);
  server.send(200, "text/html", "<html><body><h1>LED is turned OFF<\h1><body><\html>");
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  pinMode(2, OUTPUT);

  Serial.print("Connecting to WiFi ");
  while(WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }
  Serial.println("Connected to WiFi");
  Serial.print("IP Address : ");
  Serial.println(WiFi.localIP());

  server.on("/welcome", HTTP_GET, welcome);
  server.on("/ledon", HTTP_GET, ledon);
  server.on("/ledoff", HTTP_GET, ledoff);

  server.begin();
  Serial.println("Server is listening to clients ....");
}

void loop() {
  // put your main code here, to run repeatedly:
  server.handleClient();
}







