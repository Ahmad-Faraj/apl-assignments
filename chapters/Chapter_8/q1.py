2. In Pandas, which method is used to group data for aggregation?
4. Flask is considered a:
5. In Django ORM, a database table is typically represented as:
6. Which library uses tensors and is widely used for deep learning?
b) It is mainly used for scientific computing like NumPy.
d) It cannot be used for deep learning.
1. NumPy arrays are less efficient than Python lists for numerical computations. Answer=F
2. Pandas DataFrame is a two-dimensional labeled data structure. Answer=T
3. Seaborn is built on top of Matplotlib. Answer=T
4. Flask is heavier and more complex than Django. Answer=F
differentiation. Answer=T
6. Django ORM automatically creates SQL queries for models. Answer=T
1. Explain the difference between NumPy and SciPy. Answer: NumPy is used for basic array
operations, while SciPy provides advanced scientific and mathematical functions.
lightweight framework, while Django is a full-featured framework
Answer:
Matplotlib is used for basic plotting, while Seaborn provides advanced statistical
Problem 1:
import numpy as np
array = np.arange(1, 11)
print("Mean:", np.mean(array))
print("Median:", np.median(array))
print("Standard Deviation:", np.std(array))
Problem 2:
import pandas as pd
data={
df=pd.DataFrame(data)
result=df[df["Score"] > 80]
print(result)
Problem 3:
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [1,4,9,16,25]
Problem 4:
from flask import Flask
app = Flask(__name__)
def hello():
if __name__ == "__main__":
Problem 5:
import torch
tensor1 = torch.tensor([1,2,3])
tensor2 = torch.tensor([4,5,6])
dot = torch.dot(tensor1, tensor2)
mul = tensor1 * tensor2
print("Dot Product:", dot)
print("Element-wise Multiplication:", mul)