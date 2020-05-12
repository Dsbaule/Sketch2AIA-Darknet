from darknet import darknet
from src.Component import Component

result = darknet.performDetect(
    imagePath="/home/dsbaule/PycharmProjects/Sketch2AIA/Custom_Darknet_Files/TestImg/NewLoginInterfaceScan.jpg",
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
    componentList.append(Component(component[0], component[1], component[2][0], component[2][1], component[2][2], component[2][3]))

print(str(componentList))
