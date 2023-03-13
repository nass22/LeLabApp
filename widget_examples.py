from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, BooleanProperty

Builder.load_file("widget_examples.kv")

class WidgetsExample(GridLayout):
    counter_click = 0
    mon_txt = StringProperty("0")
    counter_toggle = BooleanProperty(False) # Pour pouvoir utiliser cette variable dans le fichier kv, on est obligé de passer par un BooleanProperty!
    text_input_label = StringProperty("")
    # counter_slider = StringProperty("50")
    
    def on_slider_value(self, slider):
        pass
        # self.counter_slider = str(int(slider.value))
    
    def on_switch_state(self, switch_button):
        print("Switch: " + str(switch_button.active))
    
    def on_button_click(self):
        if self.counter_toggle == True:
            self.counter_click += 1
            self.mon_txt = str(self.counter_click)
    
    def on_toggle_button_state(self, toggle_button):        
        if toggle_button.state == "normal":
            toggle_button.text = "OFF"
            self.counter_toggle = False
        else :
            toggle_button.text = "ON"
            self.counter_toggle = True
            
    def on_text_validate(self, text_input):
        self.text_input_label = text_input.text