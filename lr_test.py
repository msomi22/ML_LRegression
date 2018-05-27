import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear_model import LinearRegression

house_price = [245, 312, 279, 308, 199, 219, 405, 324, 319, 255]
size = [1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700]
size = np.array(size).reshape((-1, 1))


#fitting into the model
model = LinearRegression()
model.fit(size, house_price)
print('Coefficients: \n', model.coef_)
print('intercept: \n', model.intercept_)

#formula obtained for the trained model
def graph(formula):
   x = np.array(size) 
   print x 
   y = eval(formula)
   print y 
   plt.plot(x, y)

#plotting the prediction line 
graph('model.coef_*x + model.intercept_')
print model.score(size, house_price)


plt.scatter (size,house_price, color='black')
plt.ylabel('house price')
plt.xlabel('size of house')
#plt.show()