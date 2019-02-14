# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

nTrain = 4
nInputs = 2
a = 0.5

class data:
    inputs = []
    output = 0.0
    
class singlePerceptron:
    def computeSingle(self,inputs,weights):       #according to the number of inputs
        sum = 0.0
        for i in range(nInputs):
            sum += inputs[i]*weights[i]
        sum += 1.0*weights[nInputs]     #bias
        if sum >= 0.0:
            return 1
        else:
            return -1
        
    def train(self,tempData, weights):
        out = self.computeSingle(tempData.inputs, weights)
        out_real = tempData.output
        #print(out, tempData.output, end='\n')
        if out != int(tempData.output):
            for j in range(nInputs):
                #b = tempData.inputs[j]
                in_real = tempData.inputs[j]
                weights[j] += a*(tempData.output-out)*tempData.inputs[j]
            weights[nInputs] += a*(tempData.output-out)
            #global learningOK
            #learningOK = False
            
class polyPerceptron:
    def computePoly(self, inputs, weights):
        sum = 0.0
        for i in range(5):
            sum += inputs[i]*weights[i]
        sum += 1.0 * weights[5]
        if sum >= 0.0:
            return 1
        else:
            return -1
        
    def train(self, tempData, weights):
        out = self.computePoly(tempData.inputs, weights)
        if out != int(tempData.output):
            for j in range(5):
                #b = tempData.inputs[j]
                weights[j] += a*(tempData.output)*tempData.inputs[j]
            weights[5] += a*(tempData.output)
            global learningOK
            learningOK = False
        
'''            
if __name__ == "__main__" :

    #newData = [data()] * nTrain
    single = singlePerceptron()
    #newData = [[-1.0, -1.0, -1.0], [-1.0, 1.0, 1.0], [1.0, -1.0, 1.0], [1.0, 1.0, 1.0]]
    
    file=open('linear.txt')   
    newData = []
    testData = []
    c = 0
    for line in file.readlines():  
        if c < 200:
            c = c+1
            curLine=line.strip().split(",")    
            floatLine=curLine#这里使用的是map函数直接把数据转化成为float类型    
            if floatLine[-1] == 'g':
                floatLine[-1] = 1
            else:
                floatLine[-1] = -1
            newData.append(list(map(float,floatLine[0:35]))) 
        else:
            curLine=line.strip().split(",")    
            floatLine=curLine#这里使用的是map函数直接把数据转化成为float类型    
            if floatLine[-1] == 'g':
                floatLine[-1] = 1
            else:
                floatLine[-1] = -1
            testData.append(list(map(float,floatLine[0:35])))
        
            
    print(np.shape(newData))
    print(np.shape(testData))
    weights = [0.0]*(nInputs+1)
   # newLen = len(newData)
    #learningOK = False
    #while(learningOK != True):
        #learningOK = True
    for x in range(100):
        for i in newData:
            temp = data()
            temp.inputs = []
            for j in range(34):
                temp.inputs.append(i[j])
            #temp.inputs.append(i[1])
            ti = temp.inputs
            temp.output = i[34]
            single.train(temp, weights)
        
    for i in range(nInputs+1):
        print("weight ", i, "is", weights[i], sep = ' ', end = '\n')
        
correct = 0

for i in newData:         
    print("The correct output is: ", int(i[34]), sep = ' ', end = '\t')
    temp2 = data()
    temp2.inputs = []
    for j in range(34):
        temp2.inputs.append(i[j])
        temp2.output = i[34]
    #print("Calculate output is ", single.computeSingle(temp2.inputs, weights))
    if single.computeSingle(temp2.inputs, weights) == int(i[34]):
        correct += 1
    print("Calculate output is: ", correct/200)
      
    for i in range(nTrain):
        print("The correct output is ", newData[i][2], sep = ' ', end = '\t')
        temp2 = data()
        temp2.inputs = [newData[i][0], newData[i][1]]
        temp2.output = newData[i][2]
        print("The calculate ouput is ", single.computeSingle(temp2.inputs, weights))

  
    '''
    
if __name__ == "__main__":
    
    single = singlePerceptron()
    poly = polyPerceptron()

    file2 = open("poly1.txt")
    newData2 = []
    testData2 = []
    c = 0
    for line in file2.readlines():  
        if c <= 4092:
            c = c+1
            curLine=line.strip().split(",")    
            floatLine=curLine           #这里使用的是map函数直接把数据转化成为float类型    
            newData2.append(list(map(float,floatLine[0:3]))) 
        else:
            curLine=line.strip().split(",")    
            floatLine=curLine           #这里使用的是map函数直接把数据转化成为float类型    
            testData2.append(list(map(float,floatLine[0:3])))
        
    tempData = []
    finalData = []
    for i in newData2:
        tempData = []
        tempData.append(i[0])
        tempData.append(i[1])
        tempData.append(i[0]*i[0])
        tempData.append(i[0]*i[1])
        tempData.append(i[1]*i[1])
        tempData.append(i[2])
        #print(np.shape(tempData))
        finalData.append(tempData)
    weights3 = [0.0] * 6
    weights2 = [0.0] * 3
    print(np.shape(finalData))

    for x in range(1):
        for i in finalData:
            temp3 = data()
            temp3.inputs = []
            for j in range(5):
                temp3.inputs.append(i[j])
            #temp.inputs.append(i[1])
            ti = temp3.inputs
            temp3.output = i[5]
            poly.train(temp3, weights3)
            
    for x in range(1):
        for i in newData2:
            temp2 = data()
            temp2.inputs = []
            for j in range(2):
                temp2.inputs.append(i[j])
            #temp.inputs.append(i[1])
            ti2 = temp2.inputs
            temp2.output = i[2]
            single.train(temp2, weights2)
            
    fig = plt.figure()
    
    x1Draw = []
    y1Draw = []
    x2Draw = []
    y2Draw = []
    for i in newData2:
        if i[2] == 1.0:
            x1Draw.append(i[0])
            y1Draw.append(i[1])
        else:
            x2Draw.append(i[0])
            y2Draw.append(i[1])
            
    x1Draw = np.array(x1Draw)
    y1Draw = np.array(y1Draw)
    x2Draw = np.array(x2Draw)
    y2Draw = np.array(y2Draw)
    
            
    
    plt.scatter(x1Draw, y1Draw, marker = 'x', color = 'm', label='1.0', s = 30)
    plt.scatter(x2Draw, y2Draw, marker = '+', color = 'c', label='-1.0', s = 30)
    plt.legend(loc = 'upper right')
            
    
    x1 = []
    for i in newData2:
        x1.append(i[0])
    x1 = np.array(x1)
    y = (-weights2[0]*x1 - weights2[2])/weights2[1]
    
    plt.plot(x1,y)
    plt.show()
    
    print("The output should be: ", finalData[10][5])
    temp4 = data()
    for i in range(5):
        temp4.inputs.append(finalData[10][i])
        temp4.output = finalData[10][5]
    print("The calculate result is: ", poly.computePoly(temp4.inputs, weights3))
 

