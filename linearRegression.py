from sklearn.linear_model import LinearRegression
from sklearn import svm 

import numpy as np
import matplotlib.pyplot as plt



'''
A simple numeric prediction based on some funny series 
'''
def numericPrediction():
	X = [1,2,3,4,5,6,7,8,9,10,11]
	X = np.array(X).reshape((-1, 1))

	Y = [10,20,30,40,50,60,70,80,90,100,110]

	model = LinearRegression()
	model.fit(X,Y)

	sy = eval('model.coef_*X + model.intercept_')  
	
	plt.scatter(X,  Y, color='red')   
	plt.plot(X, sy, color='blue', linewidth=3) 
	plt.xlabel("Pattern")
	plt.ylabel("Output") 
	plt.title("Linear Regression, Patter Prediction") 
	plt.savefig('numericPredictionGraph')  

    
	print "12 = %d" %model.predict(np.array([12]).reshape((-1, 1)))   
	print "13 = %d" %model.predict(np.array([13]).reshape((-1, 1)))   
	print "14 = %d" %model.predict(np.array([14]).reshape((-1, 1)))   
	print "15 = %d" %model.predict(np.array([15]).reshape((-1, 1)))    
	


#numericPrediction()


'''
Predict area of a circle 
Area = PI * (r * r)
PI = np.pi 

we will first write a simple method to return area of a circle given a particular radius 

'''
def getCircleArea(radius):
	return round(np.pi * radius * radius, 4)

def circleAreaPrediction(predRadius): 
	RADIUS_X = []  
	AREA_Y = []
	for num in range(1,47): 
		RADIUS_X.append([num])
		AREA_Y.append(long(getCircleArea(num)))#
	
    #Create and Train our model 
	model = LinearRegression()
	model.fit(RADIUS_X,AREA_Y) 
	print "LinearRegression: Circle r = ", predRadius ," A = " , model.predict([[predRadius]]) , " CA = ", getCircleArea(predRadius)

	'''
	use classifier 
	'''
	clf = svm.SVC() 
	clf.fit(RADIUS_X,AREA_Y)  
	print "SVM: Circle r = ", predRadius ," A = " ,clf.predict([[predRadius]])  , " CA = ", getCircleArea(predRadius)
	


	y = eval('model.coef_*RADIUS_X + model.intercept_') 
	
    # we plot the independent variable (radius) on the x-axis and dependent variable (area) on the y-axis
	plt.scatter(RADIUS_X, AREA_Y, color='red') 
	plt.plot(RADIUS_X, y, color='blue', linewidth=3) 
	plt.xlabel("Circle Radius")
	plt.ylabel("Cricle Area")
	plt.title("Linear Regression, Circle Area Prediction") 
	plt.savefig('circleAreaLineGraph')   

circleAreaPrediction(7)  
