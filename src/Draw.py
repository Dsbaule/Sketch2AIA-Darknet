from PIL import Image, ImageDraw
from src import Component

colorDict = {
    'Screen':       '#d50000',
    'Label':        '#c51162',
    'Button':       '#aa00ff',
    'TextBox':      '#6200ea',
    'CheckBox':     '#304ffe',
    'Image':        '#0091ea',
    'Switch':       '#00b8d4',
    'Slider':       '#00bfa5',
    'Map':          '#00c853',
    'ListPicker':   '#64dd17'
}

def initImage(xNum = 18, yNum = 32):
    global im
    global drawing
    im = Image.new('RGB', (xNum, yNum), (128, 128, 128))
    drawing = ImageDraw.Draw(im)

def drawComponent(component: Component):
    drawing.rectangle((component.x1, component.y1, component.x2, component.y2), fill = colorDict[component.label])

def saveImage():
    im.save('/home/dsbaule/PycharmProjects/Sketch2AIA/src/test.jpg', quality=95)
