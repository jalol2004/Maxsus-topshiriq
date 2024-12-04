# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gzOaaKE3-AR47wyCfA6vbBW6FC65LZxS
"""

import pandas as pd
# Yuklangan fayl nomini o'zgartiring
df = pd.read_csv('WHO COVID-19 cases.csv')
print(df)

filtered_df = df[df['Country'] == 'Afghanistan']
print(len(filtered_df))

filtered_df = df[df['Continent'] == 'Asia']
print(len(filtered_df))

filtered_df = df[df['Continent'] == 'North America']
print(len(filtered_df))

filtered_df = df[df['Country_code'] == 'AU']
print(len(filtered_df))

filtered_df = df[df['Continent'] == 'Europe']
print(len(filtered_df))

filtered_df = df[df['Country_code'] == 'AF']
print(len(filtered_df))