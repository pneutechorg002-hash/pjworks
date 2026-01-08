import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label



class calculate(BoxLayout):
   def __init__(self):
       super(calculate,self).__init__()

   def calc_symbol(self,symbol):
       self.calc_field.text += symbol

   def  calc_clear(self):
       self.calc_field.text =" "

   def get_result(self):
       self.calc_field.text = str(eval(self.calc_field.text))       
           




class Mycalc(App):
    def build(self):
        return calculate()
        


app= Mycalc()
app.run()



