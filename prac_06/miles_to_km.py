from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesKilometerConverter(App):
    def build(self):
        self.title = "Miles to Kilometer Converter"
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def handle_calculation(self, text):
        value = self.check_value(text)
        result = value * MILES_TO_KM
        self.root.ids.output_km.text = str(result)

    def check_value(self, text):
        try:
            value = float(text)
            return value
        except ValueError:
            return 0

    def handle_increment(self, change):
        value = self.check_value(self.root.ids.input_miles.text)
        result = value + change
        self.root.ids.input_miles.text = str(result)


MilesKilometerConverter().run()
