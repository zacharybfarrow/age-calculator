from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, ObjectProperty

from datetime import date
from dateutil.relativedelta import relativedelta


class Interface(ScreenManager):

    month_input = ObjectProperty(None)
    day_input = ObjectProperty(None)
    year_input = ObjectProperty(None)

    def calculate_age(self):
        birth_month = int(self.month_input.text)
        birth_day = int(self.day_input.text)
        birth_year = int(self.year_input.text)
        birthday = date(birth_year, birth_month, birth_day)
        today = date.today()

        age = relativedelta(today, birthday)

        result = f"Current age is {age.years} years, {age.months} months, and {age.days} days."
        print(result)
        return result

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