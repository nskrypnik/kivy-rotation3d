
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *

class Renderer(Widget):
    
    def __init__(self, *args, **kw):
        super(Renderer, self).__init__(*args, **kw)
        with self.canvas:
            Color(1, 0.5, 1, 1)
            PushMatrix()
            Rotate(45, 0, 0, 1)
            Translate(400, -300, 0)
            Rectangle(pos=(0, 0), size=(300, 300))
            PopMatrix()
            
            PushMatrix()
            Color(0.5, 1, 0.5, 1)
            Rectangle(pos=(100, 100), size=(200, 200))
            PopMatrix()
            
            PushMatrix()
            Color(0.0, 0.5, 0.5, 1)
            Translate(300, 300, 0)
            Rotate(75, 0, 0, 1)
            Rectangle(pos=(0, 0), size=(250, 250))
            PopMatrix()

class TestApp(App):
    
    def build(self):
        return Renderer()

if __name__ == "__main__":
    TestApp().run()