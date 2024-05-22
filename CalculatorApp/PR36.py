import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

kivy.require('1.9.1')



class Calculator(BoxLayout):
    def on_button_press(self, value):
        input_box = self.ids.input_box
        if input_box.text == "0":
            input_box.text = value
        else:
            input_box.text += value

    def on_clear_press(self):
        input_box = self.ids.input_box
        input_box.text = "0"

    def on_solution(self):
        input_box = self.ids.input_box
        try:
            input_box.text = str(eval(input_box.text))
        except Exception:
            input_box.text = "Error"

class CalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == '__main__':
    CalculatorApp().run()
