from darknet import darknet
from src.Component import Component
from src import Alignment

result = darknet.performDetect(
    imagePath="/home/dsbaule/PycharmProjects/Sketch2AIA/Custom_Darknet_Files/TestImg/sample3.jpg",
    thresh=0.25,
    configPath="/home/dsbaule/PycharmProjects/Sketch2AIA/Custom_Darknet_Files/NewDatasetYolov3.cfg",
    weightPath="/home/dsbaule/PycharmProjects/Sketch2AIA/Custom_Darknet_Files/NewDatasetYolov3_18000.weights",
    metaPath="/home/dsbaule/PycharmProjects/Sketch2AIA/Custom_Darknet_Files/obj.data", showImage=False,
    makeImageOnly=False, initOnly=False)

# for component in result:
#     print(component[0] + ':')
#     print('\t' + str(component[2][0]))
#     print('\t' + str(component[2][1]))
#     print('\t' + str(component[2][2]))
#     print('\t' + str(component[2][3]))

componentList = list()

for component in result:
    print(component[0])
    if component[0] == 'Screen':
        screen = Component(component[0], component[1], component[2][0], component[2][1], component[2][2], component[2][3])
    else:
        componentList.append(Component(component[0], component[1], component[2][0], component[2][1], component[2][2], component[2][3]))

# Remove overlaps
for i in range(len(componentList)):
    for j in range(i+1, len(componentList)):
        if componentList[i].overlaps(componentList[j]):
            componentList.pop(i if (componentList[i].confidence < componentList[j].confidence) else j)


# Check what components are aligned in each axis
componentList.sort(key=lambda x: x.y1)
for i in range(len(componentList)):
    print(componentList[i].label + '(' + str(componentList[i].x1) + ',' + str(componentList[i].y1) + ')')
    componentList[i].getInLineComponents(componentList[i+1:])

#print(str(Alignment.align(componentList)))

import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(Alignment.align(componentList))