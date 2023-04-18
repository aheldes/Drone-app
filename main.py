from datetime import datetime

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.texture import Texture
from kivy.clock import Clock


import random


class MyUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.start_time = 0

        Clock.schedule_interval(self._update_battery, 1)
        Clock.schedule_interval(self._update_temperature, 1 / 2)

    def button_handler(self):
        if self.button.text == "Start":
            self._start()
        elif self.button.text == "Stop":
            self._stop()
        else:
            print("Unknown button pressed")

    def _start(self):
        print("Start button pressed")
        self._update_buttons()
        self.start_time = datetime.now()
        Clock.schedule_interval(self._update_flight_time, 1 / 100)

    def _stop(self):
        self._update_buttons()
        Clock.unschedule(self._update_flight_time)

    def _update_battery(self, dt):
        self.battery.text = f"Battery: {random.randint(1, 100)}%"
        # batery = self.drone.get_battery()
        # self.battery.text = f"Battery: {batery}%"

    def _update_flight_time(self, dt):
        self.flight_time.text = f"Flight time: {datetime.now() - self.start_time}"
        # self.flight_time.text = f"Flight time: {self.drone.get_flight_time()}"

    def _update_temperature(self, dt):
        self.temperature.text = f"Temperature: {random.randint(1, 100)}"
        # self.temperature.text = f"Temperature: {self.drone.get_temperature()}"

    def _update_buttons(self):
        if self.button.text == "Start":
            self.button.text = "Stop"
        else:
            self.button.text = "Start"


class MainApp(App):
    def build(self):
        return MyUI()


if __name__ == "__main__":
    MainApp().run()
