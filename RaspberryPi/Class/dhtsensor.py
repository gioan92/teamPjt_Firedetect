import time;
import Adafruit_DHT as dht11;
from threading import Thread;
import RPi.GPIO as GPIO;
from flask import Flask, render_template, request, Response, jsonify;
from MyMessage import mymessage;

class DHT(Thread):
    global msg;
    def __init__(self, msg): #client):
        super().__init__();
        self.message = msg;
        #self.client = client;

    def run(self):
        while True:
            pin = 20;
            hum, temp = dht11.read_retry(dht11.DHT11, pin);
            GPIO.setmode(GPIO.BCM);

            if hum is not None and temp is not None:
                print("습도: %s, 온도: %s" %(str(hum), str(temp)))
                self.message.content['hum'] = hum;
                self.message.content['temp'] = temp;
            else:
                print("입력값 없음");

            time.sleep(1);

app = Flask(__name__);

@app.route("/upload")
def upload():
    global dht;
    content = dht.message.content;
    return jsonify(content);

if __name__ == "__main__":
    try:
        msg = mymessage(0, 0);
        dht = DHT(msg);
        dht.start();

        app.run(host = "0.0.0.0", debug = True, threaded = True);

    except KeyboardInterrupt:
        print("종료, GPIO Pin Clean");
        GPIO.cleanup();