import machine
import time
import network
import dht
import urequests

SSID = "odit"
PASSWORD = "kayabanget"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)


timeout = 15  
while not wlan.isconnected() and timeout > 0:
    print(f"Menghubungkan ke WiFi... ({timeout})")
    time.sleep(1)
    timeout -= 1

if wlan.isconnected():
    print("✅ WLAN is connected!")
else:
    print("❌ Gagal terhubung ke WiFi. Periksa SSID/PASSWORD!")
    machine.reset() 


UBIDOTS_ENDPOINT = "https://industrial.api.ubidots.com/api/v1.6/devices/esp32/"
FLASK_ENDPOINT = "http://192.168.115.68:7000/save"


dht_sensor = dht.DHT11(machine.Pin(14))


ldr_sensor = machine.ADC(machine.Pin(34))
ldr_sensor.atten(machine.ADC.ATTN_11DB)  


pir_sensor = machine.Pin(25, machine.Pin.IN)


led = machine.Pin(32, machine.Pin.OUT)

while True:
    try:
        dht_sensor.measure()
        time.sleep(1)
        suhu = dht_sensor.temperature()
        kelembaban = dht_sensor.humidity()

        ldr_value = ldr_sensor.read()  

        pir_status = pir_sensor.value() 

        if pir_status == 1:
            led.value(1) 
        else:
            led.value(0) 


        print(f"Suhu: {suhu}°C, Kelembaban: {kelembaban}%, LDR: {ldr_value}, PIR: {pir_status}")

        data = {
            "temperature": {"value": suhu},
            "humidity": {"value": kelembaban},
            "light": {"value": ldr_value}, 
            "motion": {"value": pir_status} 
        }

        headers_ubidots = {
            "Content-Type": "application/json",
            "X-Auth-Token": "BBUS-xbWvcWOvgOBXRTEEtB4VuqXr2NZuPC"
        }

        response = urequests.post(UBIDOTS_ENDPOINT, json=data, headers=headers_ubidots)
        print(f"📡 Status pengiriman ke Ubidots: {response.status_code}, {response.text}")
        response.close()
        
        headers = {"Content-Type":"application/json"}
        response = urequests.post(FLASK_ENDPOINT,json=data,headers=headers)
        
        print(f"response flask: {response.status_code}")
        response.close()
        time.sleep(1)

    except Exception as e:
        print("⚠️ Error:", e)

    time.sleep(1)