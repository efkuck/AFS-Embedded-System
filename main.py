import cv2
import RPi.GPIO as GPIO
import time

#  GPIO PIN AYARLARI 
BUZZER_PIN = 17
TRIG_PIN = 23
ECHO_PIN = 24
YELLOW_LED_PIN = 27
RED_LED_PIN = 22   

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(YELLOW_LED_PIN, GPIO.OUT)
GPIO.setup(RED_LED_PIN, GPIO.OUT)


GPIO.output(BUZZER_PIN, GPIO.LOW)
GPIO.output(TRIG_PIN, GPIO.LOW)
GPIO.output(YELLOW_LED_PIN, GPIO.LOW)
GPIO.output(RED_LED_PIN, GPIO.LOW)

#  OPENCV HAAR CASCADE 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

#  PROJE PARAMETRELERİ 
CLOSED_EYE_FRAMES = 0
ALARM_TRIGGER_FRAMES = 10 
DISTANCE_THRESHOLD = 30  
frame_counter = 0     


def get_distance():

    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(ECHO_PIN) == 0:
        start_time = time.time()


    while GPIO.input(ECHO_PIN) == 1:
        stop_time = time.time()


    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2
    return distance


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

print("Gelişmiş Sürücü Koruma Sistemi Başlatıldı...")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_counter += 1 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(50, 50))
    eyes_detected = False

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=5, minSize=(15, 15))
        for (ex, ey, ew, eh) in eyes:
            eyes_detected = True
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)


    try:
        current_dist = get_distance()
    except:
        current_dist = 100

   
    cv2.putText(frame, f"Mesafe: {current_dist:.1f} cm", (10, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    #  ALARM SENARYOLARI
    if len(faces) > 0 and not eyes_detected:
        CLOSED_EYE_FRAMES += 1
        if CLOSED_EYE_FRAMES >= ALARM_TRIGGER_FRAMES:
            
    
            if current_dist < DISTANCE_THRESHOLD:
                GPIO.output(BUZZER_PIN, GPIO.HIGH)  
                GPIO.output(RED_LED_PIN, GPIO.HIGH)      
                GPIO.output(YELLOW_LED_PIN, GPIO.LOW) 
                cv2.putText(frame, f"KRITIK: KAFA DUSTU! ({int(current_dist)}cm)", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            

            else:
                GPIO.output(YELLOW_LED_PIN, GPIO.HIGH)
                GPIO.output(RED_LED_PIN, GPIO.LOW)
                

                if frame_counter % 10 < 5:
                    GPIO.output(BUZZER_PIN, GPIO.HIGH)
                else:
                    GPIO.output(BUZZER_PIN, GPIO.LOW)
                cv2.putText(frame, "UYARI: GOZLER KAPALI!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 165, 255), 2)
    else:

        CLOSED_EYE_FRAMES = 0
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        GPIO.output(YELLOW_LED_PIN, GPIO.LOW)
        GPIO.output(RED_LED_PIN, GPIO.LOW)

    cv2.imshow('Surucu Yorgunluk Tespiti', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


GPIO.output(BUZZER_PIN, GPIO.LOW)
GPIO.output(YELLOW_LED_PIN, GPIO.LOW)
GPIO.output(RED_LED_PIN, GPIO.LOW)
GPIO.cleanup()
cap.release()
cv2.destroyAllWindows()
