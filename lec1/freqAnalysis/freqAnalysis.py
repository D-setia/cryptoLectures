import matplotlib.pyplot as plt
import numpy as np

ipFile = open("input.txt", 'r')
contents = ipFile.read()
contents = contents.lower()

alphabet = [chr(i+97) for i in range(26)]
frequencies = [0 for i in range(26)]
chars = 0

for i in range(len(contents)):
    index = ord(contents[i]) - 97
    if index in range(0, 26):
        frequencies[index] += 1
        chars += 1

for i in range(26):
    frequencies[i] = round(frequencies[i]/chars*100, 2)

y_pos = np.arange(len(alphabet))
plt.bar(y_pos, frequencies, align='center', alpha=0.5)
plt.xticks(y_pos, alphabet)
plt.ylabel('Frequencies')
plt.show()

