from machine import Pin, PWM
from time import sleep
import random

# Pin donde está conectado el servo
servo = PWM(Pin(15))   # cambia el pin si necesitas
servo.freq(50)         # los servos usan 50 Hz

# Función para mover el servo a un ángulo
def mover_servo(angulo):
    # Conversión aproximada 0°–180°
    duty = int(1638 + (angulo / 180) * 6553)
    servo.duty_u16(duty)

# Movimiento infinito
while True:
    
    # Centro
    mover_servo(90)
    sleep(1)

    # Extremo izquierdo
    mover_servo(0)
    sleep(1)

    # Extremo derecho
    mover_servo(180)
    sleep(1)

    # Posición aleatoria
    angulo = random.randint(0, 180)
    mover_servo(angulo)
    sleep(1)
