import collections
word_freq=collections.Counter()
from matplotlib import pyplot as plt
counts=list(zip(*word_freq.most_common()))[1]
plt.xlabel("word-frequency")
plt.ylabel("word-kinds")
plt.hist(counts,bins=20,range=(1,20),normed=True)
plt.xlim(xmin=1,xmax=20)
plt.grid(axis="y")
plt.show()
