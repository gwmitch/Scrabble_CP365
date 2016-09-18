import random
import numpy as np
import csv
#np.random.seed(42)

values = np.random.randint(2,size=(100,6489))


fileObj = open("sample.csv", "wb")

csv_file = csv.writer(fileObj)  

csv_file.writerows(values)
