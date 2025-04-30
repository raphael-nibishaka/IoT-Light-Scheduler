import paho.mqtt.client as mqtt
import time

SCHEDULE_TOPIC = "light/schedule"

# Sample simulation (prints instead of serial comm)
def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"[MQTT] Schedule received: {payload}")
    on_time, off_time = payload.split(',')

    while True:
        now = time.strftime('%H:%M')
        if now == on_time:
            print("[SIM] Sending '1' to Arduino → Light ON")
        elif now == off_time:
            print("[SIM] Sending '0' to Arduino → Light OFF")
        time.sleep(30)

client = mqtt.Client()
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.subscribe(SCHEDULE_TOPIC)
print(f"[MQTT] Subscribed to {SCHEDULE_TOPIC}")
client.loop_forever()
