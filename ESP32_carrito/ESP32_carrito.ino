#include "BluetoothSerial.h"

BluetoothSerial BT;

#define PIN_MOTOR_d_atras 18
#define PIN_MOTOR_d_adelante 19
#define PIN_MOTOR_i_atras 5
#define PIN_MOTOR_i_adelante 17      

unsigned long lapso;
unsigned long tiempo_actual = 500;
unsigned long tiempo_atras = 800;
unsigned long tiempo_adelante = 800;
unsigned long tiempo_derecha = 585;
unsigned long tiempo_izquierda = 585; 
unsigned long tiempo_parado = 500;

enum Comandos { 
  ATRAS = 'w', 
  ADELANTE = 's', 
  IZQUIERDA = 'd', 
  DERECHA = 'a', 
  PARA = 'q' 
}; 

void byteReceived() {
  if (BT.available() > 0) {
    char datos = BT.read();

    switch (datos) {
      case ATRAS:
        tiempo_actual = tiempo_atras;
        digitalWrite(PIN_MOTOR_d_atras, HIGH);
        digitalWrite(PIN_MOTOR_d_adelante , LOW);
        digitalWrite(PIN_MOTOR_i_atras, HIGH);
        digitalWrite(PIN_MOTOR_i_adelante, LOW);
        break;

      case ADELANTE:
        tiempo_actual = tiempo_adelante;
        digitalWrite(PIN_MOTOR_d_atras, LOW);
        digitalWrite(PIN_MOTOR_d_adelante, HIGH);
        digitalWrite(PIN_MOTOR_i_atras, LOW);
        digitalWrite(PIN_MOTOR_i_adelante, HIGH);
        break;

      case IZQUIERDA:
        tiempo_actual = tiempo_izquierda;
        digitalWrite(PIN_MOTOR_d_atras, LOW);
        digitalWrite(PIN_MOTOR_d_adelante, HIGH);
        digitalWrite(PIN_MOTOR_i_atras, HIGH);
        digitalWrite(PIN_MOTOR_i_adelante, LOW);
        break;

      case DERECHA:
        tiempo_actual = tiempo_derecha;
        digitalWrite(PIN_MOTOR_d_atras, HIGH);
        digitalWrite(PIN_MOTOR_d_adelante, LOW);
        digitalWrite(PIN_MOTOR_i_atras, LOW);
        digitalWrite(PIN_MOTOR_i_adelante, HIGH);
        break;

      case PARA:
        tiempo_actual = tiempo_parado;
        detenerMotores();
        break;

      default:
        break;
    }

    lapso = millis(); 
  }
}

void detenerMotores() {
  digitalWrite(PIN_MOTOR_d_atras, LOW);
  digitalWrite(PIN_MOTOR_d_adelante , LOW);
  digitalWrite(PIN_MOTOR_i_atras, LOW);
  digitalWrite(PIN_MOTOR_i_adelante, LOW);
}

void setup() {
  BT.begin("Carrito");

  pinMode(PIN_MOTOR_d_atras, OUTPUT);
  pinMode(PIN_MOTOR_d_adelante, OUTPUT);
  pinMode(PIN_MOTOR_i_atras, OUTPUT);
  pinMode(PIN_MOTOR_i_adelante, OUTPUT);

  detenerMotores(); 
  
  Serial.begin(115200);
  lapso = millis();
}

void loop() {
  byteReceived(); 

  if (millis() - lapso > tiempo_actual) {
    detenerMotores(); 
  }
}
