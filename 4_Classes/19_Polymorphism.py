from abc import ABC, abstractmethod

class UIControl(ABC):
    @abstractmethod
    def draw (self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("TextBox")

class DropDownList(UIControl):
    def Draw(self):
        print("DropDownList")

def draw(controls):
    for control in controls:
        control.draw()

ddl = DropDownList()
print(isinstance(ddl,UIControl))
textbox = TextBox()
draw([ddl, textbox])