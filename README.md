# Anstrengungs- und Müdigkeitsfeststellungssystem (AFS)

Ein eingebettetes System (Embedded System) zur Echtzeit-Erkennung von Sekundenschlaf bei Autofahrern. Entwickelt als Finalprojekt für das Modul "Eingebettete Systeme".

## 📌 Projektbeschreibung
Dieses Projekt nutzt Computer Vision (OpenCV) in Kombination mit Hardware-Sensorik, um den Fahrerzustand zu überwachen. Das System erkennt, wenn die Augen des Fahrers geschlossen sind, und misst simultan die Distanz des Kopfes zum Lenkrad, um sofortige Warnsignale auszugeben.

## ⚙️ Hardware-Komponenten
* Raspberry Pi (oder kompatibler SBC)
* USB-Kamera 
* HC-SR04 Ultraschallsensor
* Aktoren: Buzzer, LED (Rot, Gelb)
* Spannungsteiler (Voltage Divider) für den Echo-Pin

## 💻 Software & Abhängigkeiten
Das System erfordert Python 3 und die folgenden Bibliotheken:
* `OpenCV` (cv2) für die Haar-Cascade Gesichts- und Augenerkennung
* `RPi.GPIO` für die Hardware-Steuerung

## 🚀 Installation und Ausführung
1. Klonen Sie das Repository:
   ```bash
   git clone [https://github.com/DEIN_USERNAME/AFS-Embedded-System.git](https://github.com/efkuck/AFS-Embedded-System.git)
