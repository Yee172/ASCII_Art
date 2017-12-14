#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Yee_172'
__date__ = '2017/12/10'


import sys
import cv2
import numpy as np


PATH = sys.path[0]


level = 3
[colF, ftSize, ftWidth] = [level + 2, (level + 2) * 0.15, 1 + int((level + 2) / 5)]
img = np.zeros((500, 400), dtype=np.uint8) + 255
outImg = img
print(cv2.getTextSize('h', cv2.FONT_HERSHEY_SIMPLEX, ftSize, ftWidth))
for i in range(colF, 50, colF):
    for j in range(0, 40, colF):
        cv2.putText(outImg, 'h', (j * 4, i * 4), cv2.FONT_HERSHEY_SIMPLEX, ftSize, (0, 0, 0), ftWidth)
# cv2.putText(img, 'asdfdaascddssaadf', (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
cv2.imshow('test1', outImg)
cv2.waitKey(0)
