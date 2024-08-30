!python detect.py --weights {HOME}/weights/yolov9-e.pt --conf 0.1 --source {HOME}/data/dog.jpeg --device 0

from IPython.display import Image

Image(filename=f"{HOME}/yolov9/runs/detect/exp2/dog.jpeg", width=600)

//Authenticate and Download the Dataset
//NOTE: The dataset must be saved inside the {HOME}/yolov9 directory, otherwise, the training will not succeed.

%cd {HOME}/yolov9
!pip install roboflow
#dont change this code block
from roboflow import Roboflow
rf = Roboflow(api_key="Uf6CsoUf4Q2SVTMuGDdb")
project = rf.workspace("glioblastoma-multiforme-detection").project("glioblastoma-early-diagnosis-deaqt")
version = project.version(5)
dataset = version.download("yolov9")


//Train the custom model

%cd {HOME}/yolov9

!python train.py \
--batch 16 --epochs 10 --img 640 --device 0 --min-items 0 --close-mosaic 15 \
--data {dataset.location}/data.yaml \
--weights {HOME}/weights/gelan-c.pt \
--cfg models/detect/gelan-c.yaml \
--hyp hyp.scratch-high.yaml
