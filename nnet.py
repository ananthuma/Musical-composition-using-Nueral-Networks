import numpy as np
class nnetwork(object):
	def __init__(self):
		self.inputsize=2;
		self.outputsize=1;
		self.hiddensize=3;
		self.w1=np.random.randn(self.inputsize,self.hiddensize)
		self.w2=np.random.randn(self.hiddensize,self.outputsize)
		
	def forward(self, x):
		self.z2=np.dot(x,self.w1)
		self.a2=self.sigmoid(self.z2)
		self.z3=np.dot(self.a2,self.w2)
		yhat=self.sigmoid(self.z3)
		return yhat
	def sigmoid(self ,z):
		return 1/(1+np.exp(-z))
