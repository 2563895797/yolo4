import torch
from torch import nn
from nets.yolo4 import YoloBody
from yolo import YOLO

print(set(dir(YOLO))-set(dir(nn.Module)))