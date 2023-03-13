from kivy.app import App
from navigation_screen_manager import NavigationScreenManager
from kivy.properties import ObjectProperty
from canvas_examples import CanvasExample1
from canvas_examples import CanvasExample2

class MyScreenManager(NavigationScreenManager):
    pass

class LeLabApp(App):
    manager = ObjectProperty(None)
    
    def build(self):
        self.manager = MyScreenManager()
        # return self.manager
        return CanvasExample2()

LeLabApp().run()