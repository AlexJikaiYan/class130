import csv 
import pandas as pd
df=pd.read_csv("final.csv")
print (df.shape)
del df["pl_hostname"]
del df["pl_letter"]
del df["pl_name"]
del df["pl_discmethod"]
del df["pl_controvflag"]
del df["pl_pnum"]
del df["pl_orbper"]
del df["pl_orbpererr1"]
del df["pl_orbpererr2"]
del df["pl_orbperlim"]
del df["pl_orbsmax"]
del df["pl_orbsmaxerr1"]
del df["pl_orbsmaxerr2"]
del df["pl_orbsmaxlim"]
del df["pl_orbeccen"]
del df["pl_orbeccenerr1"]
del df[" pl_orbeccener2"]
del df["pl_orbincllim"]
del df["pl_bmassj"]
del df["pl_bmassjerr1"]
del df["pl_bmassjerr2"]
print(df.shape)
df.to_csv("newfile.csv")