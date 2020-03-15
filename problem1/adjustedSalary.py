import pandas as pd

# reading employee data
emp = pd.read_csv('emp.csv',header=0,names=["id","name","zip","salary"]) 

# reading tax rate data
tax = pd.read_csv('zip_tax.csv',header=0,names=["zip","tax"])

# calculating tax adjusted salaries
# add tax column to emp
emp['tax']=emp[['zip']].merge(tax,how='left').tax
# calculate adjusted salary
emp['adjSal'] = emp.salary*(100-emp.tax)/100
emp.adjSal = emp.adjSal.astype(int)

# sace emp
emp.to_csv('emp_updated.csv', index = False, header=True)

# calculating mean

meanSalary = emp['salary'].mean()
meanAdjSal = emp['adjSal'].mean()

# calculating median

medianSalary = emp['salary'].median()
medianAdjSal = emp['adjSal'].median()

with open('means.dat','w') as f:
	f.write("Mean salary is {}, mean of adjusted salary is {}\n".format(meanSalary,meanAdjSal))
	f.write("Median salary is {}, median of adjusted salary is {}".format(medianSalary,medianAdjSal))
