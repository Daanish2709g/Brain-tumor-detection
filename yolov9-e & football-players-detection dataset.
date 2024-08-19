yolov9-e

!python detect.py --weights {HOME}/weights/yolov9-e.pt --conf 0.1 --source {HOME}/data/dog.jpeg --device 0

from IPython.display import Image

Image(filename=f"{HOME}/yolov9/runs/detect/exp2/dog.jpeg", width=600)

#Authenticate and Download the Dataset

NOTE: The dataset must be saved inside the {HOME}/yolov9 directory, otherwise, the training will not succeed.

%cd {HOME}/yolov9

NOTE: 
In this tutorial, I will use the football-players-detection dataset. Feel free to replace it
with your dataset in YOLO format or use another dataset available on Roboflow Universe. 
Additionally, if you plan to deploy your model to Roboflow after training, make sure you are the
owner of the dataset and that no model is associated with the version of the dataset you are going
to training on.

!pip install roboflow
#dont change this code block
from roboflow import Roboflow
rf = Roboflow(api_key="Uf6CsoUf4Q2SVTMuGDdb")
project = rf.workspace("glioblastoma-multiforme-detection").project("glioblastoma-early-diagnosis-deaqt")
version = project.version(5)
dataset = version.download("yolov9")
