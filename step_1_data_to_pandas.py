import os
import re

import numpy as np
import pandas as pd
from nltk.corpus import stopwords

print("Please Enter the Exact Dataset Main Folder name")
folder_name = input()

labels = os.listdir ("Dataset/" + folder_name)
if ".DS_Store" in labels:
    labels.remove(".DS_Store")

all_data = []

# uncomment to debug
labels = labels[:5]
counter = 0

for i in labels:
    instances_in_a_label = os.listdir ("Dataset/" + folder_name + '/' + i)
    all_data_for_a_label = []
    for j in instances_in_a_label:
        # uncomment to debug
        if counter < 2:
            f = open("Dataset/" + folder_name + '/' + i + '/' + j, "r")
            raw_data = f.read()
            preprocessed_data = re.sub('[^a-zA-Z]', ' ', raw_data).lower()
            preprocessed_data = preprocessed_data.split()
            preprocessed_data = [word for word in preprocessed_data if word not in stopwords.words('english')]
            preprocessed_data = ' '.join(preprocessed_data)
            all_data.append([preprocessed_data, i])
            counter += 1
    counter = 0

all_data = np.asarray(all_data)
df = pd.DataFrame(all_data)

df.to_csv('pre_processed_' + folder_name + '.csv', index=False)
