import uuid


class Project:
    def __init__(self, Name, AppName):
        self.authURL = ["ai2.appinventor.mit.edu"]
        self.YaVersion = 206
        self.Source = "Form"
        self.Screen = Screen(Name, AppName)

    def toDict(self):
        return {
          "authURL": self.authURL,
          "YaVersion": str(self.YaVersion),
          "Source": self.Source,
          "Properties": self.Screen.toDict()
        }


class Screen:
    def __init__(self, Name, AppName):
        self.Name = Name
        self.Type = "Form"
        self.Version = "27"
        self.AppName = AppName
        self.Title = Name
        self.Uuid = 0
        self.Components = list()

    def addComponent(self, Component):
        self.Components.append(Component)

    def toDict(self):
        return {
            "$Name": self.Name,
            "$Type": self.Type,
            "$Version": str(self.Version),
            "AppName": self.AppName,
            "Title": self.Title,
            "Uuid": str(self.Uuid),
            "$Components": [x.toDict() for x in self.Components]
        }


class Component:
    def __init__(self, Name, Type, Version, AlignHorizontal=1, AlignVertical=1, Height=-1, Width=-1):
        self.Name = Name
        self.Type = Type
        self.Version = Version
        self.AlignHorizontal = AlignHorizontal
        self.AlignVertical = AlignVertical
        self.Height = Height
        self.Width = Width
        self.Uuid = uuid.uuid4()

    def toDict(self):
        return {
            "$Name": self.Name,
            "$Type": self.Type,
            "$Version": str(self.Version),
            "AlignHorizontal": str(self.AlignHorizontal),
            "AlignVertical": str(self.AlignVertical),
            "Height": str(self.Height),
            "Width": str(self.Width),
            "Uuid": str(self.Uuid)
        }


class Arrangement(Component):
    def __init__(self, Name, Type, Version, AlignHorizontal=1, AlignVertical=1, Height=-1, Width=-1, Components=None):
        super().__init__(Name, Type, Version, AlignHorizontal, AlignVertical, Height, Width)
        self.Components = list() if Components is None else Components

    def addComponent(self, Component):
        self.Components.append(Component)

    def toDict(self):
        return {
            "$Name": self.Name,
            "$Type": self.Type,
            "$Version": str(self.Version),
            "AlignHorizontal": str(self.AlignHorizontal),
            "AlignVertical": str(self.AlignVertical),
            "Height": str(self.Height),
            "Width": str(self.Width),
            "Uuid": str(self.Uuid),
            "$Components": [x.toDict() for x in self.Components]
        }

class HorizontalArrangement(Arrangement):
    def __init__(self, Name, AlignHorizontal=1, AlignVertical=1, Height=-1, Width=-1, Components=None):
        Type = "HorizontalArrangement"
        Version = "3"
        super().__init__(Name, Type, Version, AlignHorizontal, AlignVertical, Height, Width, Components)


class VerticalArrangement(Component):
    def __init__(self, Name, AlignHorizontal=1, AlignVertical=1, Height=-1, Width=-1, Components=None):
        Type = "VerticalArrangement"
        Version = "3"
        super().__init__(Name, Type, Version, AlignHorizontal, AlignVertical, Height, Width, Components)


class Button(Component):
    def __init__(self, Name, AlignHorizontal=1, AlignVertical=1, Height=-1, Width=-1):
        Type = "Button"
        Version = "6"
        super().__init__(Name, Type, Version, AlignHorizontal, AlignVertical, Height, Width)


class TextBox(Component):
    def __init__(self, Name, AlignHorizontal=1, AlignVertical=1, Height=-1, Width=-1):
        Type = "TextBox"
        Version = "6"
        super().__init__(Name, Type, Version, AlignHorizontal, AlignVertical, Height, Width)


class Label(Component):
    def __init__(self, Name, AlignHorizontal=1, AlignVertical=1, Height=-1, Width=-1):
        Type = "Label"
        Version = "5"
        super().__init__(Name, Type, Version, AlignHorizontal, AlignVertical, Height, Width)


class Switch(Component):
    def __init__(self, Name, AlignHorizontal=1, AlignVertical=1, Height=-1, Width=-1):
        Type = "Switch"
        Version = "1"
        super().__init__(Name, Type, Version, AlignHorizontal, AlignVertical, Height, Width)


class Slider(Component):
    def __init__(self, Name, AlignHorizontal=1, AlignVertical=1, Height=-1, Width=-1):
        Type = "Slider"
        Version = "2"
        super().__init__(Name, Type, Version, AlignHorizontal, AlignVertical, Height, Width)


class Map(Component):
    def __init__(self, Name, AlignHorizontal=1, AlignVertical=1, Height=-1, Width=-1):
        Type = "Map"
        Version = "5"
        super().__init__(Name, Type, Version, AlignHorizontal, AlignVertical, Height, Width)


class CheckBox(Component):
    def __init__(self, Name, AlignHorizontal=1, AlignVertical=1, Height=-1, Width=-1):
        Type = "CheckBox"
        Version = "2"
        super().__init__(Name, Type, Version, AlignHorizontal, AlignVertical, Height, Width)


class Image(Component):
    def __init__(self, Name, AlignHorizontal=1, AlignVertical=1, Height=-1, Width=-1):
        Type = "Image"
        Version = "4"
        super().__init__(Name, Type, Version, AlignHorizontal, AlignVertical, Height, Width)


class Spinner(Component):
    def __init__(self, Name, AlignHorizontal=1, AlignVertical=1, Height=-1, Width=-1):
        Type = "Spinner"
        Version = "1"
        super().__init__(Name, Type, Version, AlignHorizontal, AlignVertical, Height, Width)


class ListPicker(Component):
    def __init__(self, Name, AlignHorizontal=1, AlignVertical=1, Height=-1, Width=-1):
        Type = "VerticalArrangement"
        Version = "9"
        super().__init__(Name, Type, Version, AlignHorizontal, AlignVertical, Height, Width)