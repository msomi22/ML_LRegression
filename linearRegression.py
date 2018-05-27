from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 
import numpy as np
import matplotlib.pyplot as plt


'''
A simple numeric prediction based on some funny series 
'''
def numericPrediction():
	X = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10],[11,11]]
	Y = [10,20,30,40,50,60,70,80,90,100,110]
	model = LinearRegression()
	model.fit(X,Y)
	print "12 + 12 = %d" %model.predict([[12,12]])
	print "13 + 13 = %d" %model.predict([[13,13]])
	print "20 + 20 = %d" %model.predict([[20,20]])
	print "21 + 21 = %d" %model.predict([[21,21]]) 


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
	for num in range(1,14): 
		RADIUS_X.append([num])
		AREA_Y.append(getCircleArea(num))#
	
    #Train our model 
	model = LinearRegression()
	X_train, X_test, y_train, y_test = train_test_split(RADIUS_X, AREA_Y, test_size=0.2, random_state=0)   
	model.fit(X_train,y_train) 
	print X_train
	print y_train
	print '******************************************************************************************************'
	print "Circle r = ", predRadius ," A = " , model.predict([[predRadius]]) , " CA = ", getCircleArea(predRadius) 
	print '******************************************************************************************************'
	plt.scatter(RADIUS_X, AREA_Y, color='red') 
	plt.plot(RADIUS_X, AREA_Y, color='blue', linewidth=3) 
	#plt.xticks(())
	#plt.yticks(()) 
	plt.xlabel("Circle Radius")
	plt.ylabel("Cricle Area")
	plt.title("Linear Regression, Circle Area Prediction") 
	plt.savefig('circleAreaLineGraph')   
	#plt.show() 
	# we plot the independent variable (radius) on the x-axis and dependent variable (area) on the y-axis

circleAreaPrediction(7)  
