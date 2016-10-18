from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, CircleAsset
PrettyColors={'Green':'0x00ff00', 'Red':'0xff000', 'Blue':'0x0000ff'}
class Circle(App):
    def __init__(self, radius):
         super().__init__(radius)
    radius=int(input("Radius?"))
    black=Color(0,1)
    red=Color(0xA62A2A)
    ogline=Linestyle(1, black)
    Circle_Asset=CircleAsset(radius, ogline, red)
    Circle=Sprite(Circle_Asset, (100,100))
        
myapp = App(Circle)
myapp.run()