from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.properties import NumericProperty, ObjectProperty

from datetime import date
from dateutil.relativedelta import relativedelta

import string


LabelBase.register(name="DMSerif", 
    fn_regular='DMSerifText-Regular.ttf', fn_italic='DMSerifText-Italic.ttf'
    )

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
            if int(age.days) < 1:
                result = "Error: negative age. Please confirm birth date and try again."
            else:
                result = f"{age.years} years, {age.months} months,\n and {age.days} days"
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
        if substring in string.digits:
            col, row = self.cursor
            text = self._lines[row]
            new_text = text[:col] + substring + text[col:]
            if (int(new_text) < 1 or int(new_text) > 12):
                return
        
        super(MonthInput, self).insert_text(substring, from_undo=from_undo)

class DayInput(TextInput):

    def insert_text(self, substring, from_undo=False):
        if substring in string.digits:
            col, row = self.cursor
            text = self._lines[row]
            new_text = text[:col] + substring + text[col:]
            if (int(new_text) < 1 or int(new_text) > 31):
                return
        
        super(DayInput, self).insert_text(substring, from_undo=from_undo)

class YearInput(TextInput):

    def insert_text(self, substring, from_undo=False):
        if substring in string.digits:
            col, row = self.cursor
            text = self._lines[row]
            new_text = text[:col] + substring + text[col:]
            if (int(new_text) < 1 or len(new_text) > 4):
                return
        
        super(YearInput, self).insert_text(substring, from_undo=from_undo)

class NumericButton(Button):
    pass

class USAgeCalculatorApp(App):
    def build(self):
        return Interface()


if __name__ == "__main__":
    USAgeCalculatorApp().run()