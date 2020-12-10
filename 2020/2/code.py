# Advent of code Year 2020 Day 2 solution
# Author = Jayascript
# Date = December 2020

import re
import numpy as np
import pandas as pd


df = pd.read_csv("input.txt", sep=" ", header=None)
df = df.rename(columns={
    0:'Freqs',
    1:'Char',
    2:'Pass',
})

df['Char'] = df['Char'].apply(lambda x: x.replace(':', ''))

df[['First', 'Second']] = df['Freqs'].str.split(
    '-', 1, expand=True)

df['First'] = df['First'].astype('int')
df['Second'] = df['Second'].astype('int')

count = 0
for index, row in df.iterrows():
    result = len(re.findall(row['Char'], row['Pass']))
    if row['First'] <= result <= row['Second']:
        count += 1


print("Part One : "+ str(count))

count = 0
for index, row in df.iterrows():
    a = row['Pass'][row['First'] - 1] == row['Char']
    b = row['Pass'][row['Second'] - 1] == row['Char']
    if bool(a) ^ bool(b):
        count +=1

print("Part Two : "+ str(count))
