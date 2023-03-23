class TextBox:
    def draw(self):
        print("TextBox")

class DropDownList:
    def Draw(self):
        print("DropDownList")

def draw(controls):
    for control in controls :
        control.draw()