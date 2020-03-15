import pandas as pd
from scipy.stats import mstats

# reading employee data
res = pd.read_csv('student.csv',header=0,names=["id","Marks"],delimiter=",")
# calculate quantiles

res['grade'] = pd.qcut(res['Marks'],q=[0,0.5,0.6,0.7,0.8,0.9,1],labels=["F","E","D","C","B","A"])

res.to_csv('graded.csv', index = False, header=True)

# calculating mean

mean = res['Marks'].mean()

# calculating median

median = res['Marks'].median()

# winsorized mean

m10 = mstats.winsorize(res['Marks'].astype(float), limits=[0.05, 0.05]).mean() # mean without 10% points
m20 = mstats.winsorize(res['Marks'].astype(float), limits=[0.1, 0.1]).mean() # mean without 20% points

with open('means.dat','w') as f:
	f.write("Mean mark is {}\n".format(mean))
	f.write("Median mark is {}\n".format(median))
	f.write("10% winsorized mean mark is {}\n".format(m10))
	f.write("20% winsorized mean mark is {}\n".format(m20))

