import json
import sys
from PySide.QtCore import *
from PySide.QtGui import *
import urllib.request

class Weather:
    def __init__(self):
        self.image = QImage("hw4/" + self.getWeather()[2] + ".png")
        self.x = 0
        self.y = 0
        self.w = 150
        self.h = 150

    def draw(self, p):
        p.drawImage(QRect(self.x, self.y, self.w, self.h), self.image)

    def move(self, w):
        self.x += 2
        if self.x >= w:
            self.x = 0

    def update(self):
        self.image = QImage("hw4/" + self.getWeather()[2] + ".png")

    def getWeather(self):
        url = "http://api.openweathermap.org/data/2.5/weather?q=bangkok&APPID=9680ef44760190ebc1c367468b4ed1c1"
        response = urllib.request.urlopen(url).read().decode('UTF-8')
        data = json.loads(response)
        weatherTemp = data['main']['temp'] - 273
        weatherStatus = data['weather'][0]['main']
        weatherDescription = data['weather'][0]['description']
        weatherHumidity = str(data['main']['humidity'])
        weatherPressure = str(data['main']['pressure'])
        return [str(format(weatherTemp, ".1f")), weatherStatus\
                , weatherDescription, weatherHumidity, weatherPressure]

class Animation_area(QWidget):
    def __init__(self, weather):
        QWidget.__init__(self, None)
        self.setMinimumSize(500,150)

        self.arena_w = 500
        self.weather = weather

        self.AnimationTimer = QTimer(self)
        self.connect(self.AnimationTimer, SIGNAL("timeout()"), self.update_value)
        self.AnimationTimer.start(100)

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        self.weather.draw(p)
        p.end()

    def update_value(self):
        self.weather.move(self.arena_w)
        self.update()

class Simple_animation_window(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

        self.weather = Weather()
        self.anim_area = Animation_area(self.weather)

        layout = QVBoxLayout()
        data = self.weather.getWeather()
        self.description = QLabel('Temperature: ' + data[0] + "°C\n" \
                           + "Status: " + data[1] \
                           + "\nCloudiness: " + data[2] \
                                  + "\nHumidity: " + data[3] \
                                  + "\nPressure: " + data[4])
        layout.addWidget(self.description)
        
        layout.addWidget(self.anim_area)

        update_button = QPushButton("Update")
        layout.addWidget(update_button)
        update_button.clicked.connect(self.update_data)
        
        self.setLayout(layout)
        self.setMinimumSize(50,200)

        self.timer = QTimer(self)
        self.connect(self.timer, SIGNAL("timeout()"), self.update_data)
        self.timer.start(30000)

    def update_data(self):
        data = self.weather.getWeather()
        self.description.setText('Temperature: ' + data[0] + "°C\n" \
                           + "Status: " + data[1] \
                           + "\nCloudiness: " + data[2] \
                                  + "\nHumidity: " + data[3] \
                                  + "\nPressure: " + data[4])
        QSound.play("hw4/update_sound.wav")

def main():
    app = QApplication(sys.argv)

    w = Simple_animation_window()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
