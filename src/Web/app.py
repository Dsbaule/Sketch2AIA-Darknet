from flask import Flask, render_template, request
import os
from darknet import darknet

__author__ = 'Daniel Baulé'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        file.save(destination)

        result = darknet.performDetect(
            imagePath='/home/dsbaule/PycharmProjects/Sketch2AIA/src/Web/images/' + filename,
            thresh=0.25,
            configPath="/home/dsbaule/PycharmProjects/Sketch2AIA/Custom_Darknet_Files/NewDatasetYolov3.cfg",
            weightPath="/home/dsbaule/PycharmProjects/Sketch2AIA/Custom_Darknet_Files/NewDatasetYolov3_18000.weights",
            metaPath="/home/dsbaule/PycharmProjects/Sketch2AIA/Custom_Darknet_Files/obj.data", showImage=True,
            makeImageOnly=True, initOnly=False)

        destination = "/".join([target, filename[:-4] + 'Generated.jpg'])

        import matplotlib
        matplotlib.image.imsave(destination, result['image'])

    return render_template("complete.html")

if __name__ == "__main__":
    app.run(port=4555, debug=True)