from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
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
        birthday = ''

        try:
            birthday = date(birth_year, birth_month, birth_day)
            today = date.today()
            age = relativedelta(today, birthday)
            result = f"Current age is {age.years} years, {age.months} months, and {age.days} days."
        except Exception as e:
            result = f"Error: {e}. Please confirm birth date and try again."

        return result

class MonthScreen(Screen):
    pass

class DayScreen(Screen):
    pass

class YearScreen(Screen):
    pass

class ResultScreen(Screen):
    pass

class MonthInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        if substring in range(1, 12):
            return super().insert_text(substring, from_undo=from_undo)
        else:
            return super().insert_text('', from_undo=from_undo)

class DayInput(TextInput):
    # Todo: implement min and max values
    pass

class YearInput(TextInput):
    # Todo: implement min and max values
    pass

class USAgeCalculatorApp(App):
    def build(self):
        return Interface()


if __name__ == "__main__":
    USAgeCalculatorApp().run()