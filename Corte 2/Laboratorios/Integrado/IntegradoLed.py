from machine import Pin
import network
import socket
import time

# Configuración WiFi
ssid = "Contru"
password = "Contru546*"

# Configuración de red (IP fija)
ip_fija = '10.63.36.5'
subred = '255.255.255.0'
gateway = '10.63.36.247'
dns = '8.8.8.8'

wifi = network.WLAN(network.STA_IF)

# Reiniciar interfaz WiFi para evitar errores de estado
wifi.active(False)
time.sleep(1)
wifi.active(True)

# IMPORTANTE: configurar IP antes de conectar
wifi.ifconfig((ip_fija, subred, gateway, dns))

wifi.connect(ssid, password)

print("Conectando...")

timeout = 10
inicio = time.time()

# Evita que el programa se quede bloqueado si no conecta
while not wifi.isconnected():
    if time.time() - inicio > timeout:
        print("No conecta WiFi")
        break
    time.sleep(1)

if wifi.isconnected():
    print("Conectado")
    print("IP fija:", ip_fija)

    # LED integrado (generalmente GPIO 2)
    led = Pin(2, Pin.OUT)

    # Crear servidor web en puerto 80
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    server = socket.socket()
    server.bind(addr)
    server.listen(1)

    print("Servidor activo")

    while True:
        conn, addr = server.accept()

        # Recibir petición HTTP
        request = conn.recv(1024)
        request = str(request)

        # Control del LED según la URL
        if '/on' in request:
            led.on()
        if '/off' in request:
            led.off()

        # Página web enviada al cliente
        html = f"""<!DOCTYPE html>
<html>
<head><title>ESP32</title></head>
<body>
<h1>Control LED ESP32</h1>
<p>IP: {ip_fija}</p>
<a href="/on"><button>ENCENDER</button></a>
<a href="/off"><button>APAGAR</button></a>
</body>
</html>
"""

        conn.sendall(html)
        conn.close()