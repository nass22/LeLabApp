from kivy.app import App
from navigation_screen_manager import NavigationScreenManager
from kivy.properties import ObjectProperty
# from canvas_examples import CanvasExample1, CanvasExample2, CanvasExample3
from canvas_examples import * #permet de tout importer
class MyScreenManager(NavigationScreenManager):
    pass

class LeLabApp(App):
    manager = ObjectProperty(None)
    
    def build(self):
        self.manager = MyScreenManager()
        # return self.manager
        return CanvasExample3()

LeLabApp().run()