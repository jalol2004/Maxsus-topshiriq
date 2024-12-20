# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19kWgkoKkR9OIAlFzMCB4XzuxIabZSII3
"""

import numpy as np
import matplotlib.pyplot as plt

# X qiymatlari
x = np.linspace(0, 10, 100)
# Y qiymatlari
y = np.sin(x)

# Grafikka chizish
plt.plot(x, y, label="Sinus(x)", color="blue")
plt.title("Sinus Funksiyasining Grafik")
plt.xlabel("X qiymatlari")
plt.ylabel("Y qiymatlari")
plt.grid(True)
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Tasodifiy nuqtalar yaratish
x = np.random.uniform(0, 10, 50)  # X qiymatlari (0 dan 10 gacha)
y = np.random.uniform(0, 10, 50)  # Y qiymatlari (0 dan 10 gacha)

# Scatter grafikka chizish
plt.scatter(x, y, color="blue", label="Nuqtalar")
plt.title("Tasodifiy Nuqtalar Scatter Grafiki")
plt.xlabel("X qiymatlari")
plt.ylabel("Y qiymatlari")
plt.grid(True)
plt.legend()
plt.show()