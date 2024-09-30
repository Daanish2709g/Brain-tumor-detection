gelan-c


!python detect.py --weights {HOME}/weights/gelan-c.pt --conf 0.1 --source {HOME}/data/dog.jpeg --device 0

NOTE: By default, the results of each subsequent inference sessions are saved in {HOME}/yolov9/runs/detect/, 
in directories named exp, exp2, exp3, ... 
You can override this behavior by using the --name parameter.

from IPython.display import Image
Image(filename=f"{HOME}/yolov9/runs/detect/exp/dog.jpeg", width=600)

