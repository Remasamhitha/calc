from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window


Window.size = (350,550)

Builder.load_file('calc.kv')

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

#creating a function which enables the user to press the button

    def button_press(self, button):

        #creating a variable which contains the number in the box

        prior = self.ids.calc_input.text
        #Test for error first
        if "Error" in prior:
            prior = ''

        #to determine whether 0 is there

        if prior == "0":

            prior = self.ids.calc_input.text
            self.ids.calc_input.text = f'{button}'

        else:

             self.ids.calc_input.text = f'{prior}{button}'

    #creating backspace function
    def remove(self):
        prior = self.ids.calc_input.text
    #to remove last character
        prior = prior[:-1]
    #to return output to the textbox
        self.ids.calc_input.text = prior

    #creating pos_neg function
    def pos_neg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f"-{prior}"
    #to create decimal point
    def dot(self):
        prior = self.ids.calc_input.text

        #split out text box in "+"
        num_list = prior.split("+")

        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior


        elif "." in prior:
            pass
        else:

            prior = f'{prior}.'
            self.ids.calc_input.text = prior


     #to create add function

    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        #slap a plus sign to the textbox
        self.ids.calc_input.text = f'{prior}{sign}'

     #create equals to function

    def equals(self):
        prior = self.ids.calc_input.text

         #Error handling
        try:
            #to evaluate the numbers
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"





class CalculatorApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    CalculatorApp().run()

