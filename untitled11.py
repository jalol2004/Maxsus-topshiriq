# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16iDh5oqMdFlqUZNUwnt8Db9bVHOfuild
"""

!pip install opencv-python

from google.colab.patches import cv2_imshow
import cv2
rasm= cv2.imread( "rasm.jpg")
cv2_imshow(rasm)

oqqora= cv2.cvtColor(rasm, cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

!pip install opencv-python

from google.colab.patches import cv2_imshow
import cv2
rasm= cv2.imread( "rasm3.jpg")
cv2_imshow(rasm)

oqqora= cv2.cvtColor(rasm, cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

!pip install opencv-python

from google.colab.patches import cv2_imshow
import cv2
rasm= cv2.imread( "rasm4.jpg")
cv2_imshow(rasm)

oqqora= cv2.cvtColor(rasm, cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)