
from Application.Default_Object.DefaultObjectInformationForInanimateObjects import DefaultInformation

class Inanimate_Object(DefaultInformation):
    def __init__(self):
        DefaultInformation.__init__(self)
        self.color = None

    def set_color(self,color):
        self.color = color