import pickle
import numpy as np
with open("pickle",'rb') as f:
    w=pickle.load(f)
n=np.array([1.54])
n=n.reshape(1,-1)
r=w.predict(n)
print(r)
