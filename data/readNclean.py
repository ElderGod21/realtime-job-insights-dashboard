import pandas as pd
import numpy as np 

df = pd.read_csv("./data/internshala_jobs.csv")

'''cleaning null and redundant data '''

df = df.dropna(subset = ['Job Title','Company', 'Location', 'Salary', 'Experience', 'Posted'])

df.to_csv("./data/internshala_jobs.csv", index=False)

df.info()

