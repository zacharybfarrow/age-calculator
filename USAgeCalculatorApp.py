from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen

class Interface(ScreenManager):
    pass

class MonthScreen(Screen):
    pass

class DayScreen(Screen):
    pass

class YearScreen(Screen):
    pass

class ResultScreen(Screen):
    pass

class USAgeCalculatorApp(App):
    def build(self):
        return Interface()

if __name__ == "__main__":
    USAgeCalculatorApp().run()