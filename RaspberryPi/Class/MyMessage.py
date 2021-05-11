

class mymessage:
    def __init__(self, hum, temp):
        self.content = {
            'hum' : hum,
            'temp' : temp,
        }

    def __str__(self):
        return "메세지출력! hum: %d, temp: %d" %(self.content['hum'], self.content['temp']);