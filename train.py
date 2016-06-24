from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
import pickle
import random
from pybrain.tools.validation    import testOnSequenceData
from pybrain.datasets import SupervisedDataSet
def convertNotesToInt(note):
	if(note in tunes):
		return tunes.index(note);
	else:
		print "Error converting ",note
newFile=False
if (newFile==True):
	fileObject = open('filename','r')
	net = pickle.load(fileObject)
else:
	n = FeedForwardNetwork()
	inLayer = LinearLayer(8)
	hiddenLayer = SigmoidLayer(500)
	outLayer = LinearLayer(1)
	n.addInputModule(inLayer)
	n.addModule(hiddenLayer)
	n.addOutputModule(outLayer)
	in_to_hidden = FullConnection(inLayer, hiddenLayer)
	hidden_to_out = FullConnection(hiddenLayer, outLayer)
	out_to_hidden = FullConnection(outLayer,hiddenLayer)
	n.addConnection(in_to_hidden)
	n.addConnection(hidden_to_out)
	n.sortModules()
inp=[]
out=[]

ds = SupervisedDataSet(8,1)

arra=[]

tunes=['c','c#','d','d#','e','f','f#','g','g#','a','a#','b','r','c#','d','d#','e','f','f#','g','g#','a','a#']
unes=['c','d#','f','g','a#','c','c','a#','a','g','f','d#','d','r','c']
arra1=['e', 'f#', 'g', 'f#', 'e', 'd#', 'e', 'f#', 'b', 'c#', 'd#', 'e', 'd', 'c', 'b', 'a', 'g', 'f#', 'g', 'a', 'b', 'a', 'g', 'f#', 'e', 'e', 'f', 'g', 'f#', 'e', 'd#', 'e', 'f#', 'b', 'c#', 'd#', 'e', 'd', 'c', 'b', 'a', 'g', 'g', 'f#', 'g', 'f#', 'g', 'f#', 'g', 'f#', 'g', 'g']
arra2=['g', 'e', 'c', 'e', 'g', 'c', 'e', 'd', 'c', 'e', 'f', 'g', 'g', 'g', 'e', 'd', 'c', 'b', 'a', 'b', 'c', 'c', 'g', 'e', 'c']
arra3=['c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'r', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'r', 'c', 'd', 'c', 'c', 'c', 'e', 'c#', 'c']
arra4=['c', 'c', 'r', 'r', 'd', 'r', 'g', 'r', 'f', 'r', 'd#', 'r', 'r', 'd#', 'r', 'f', 'd#', 'f', 'g', 'd', 'r', 'r', 'd#', 'f', 'r', 'd', 'c', 'r', 'r', 'r', 'r', 'c', 'c', 'r', 'r', 'a#', 'a', 'c', 'g', 'r', 'r', 'g', 'c', 'c', 'r', 'r', 'r', 'a#', 'g', 'g', 'r', 'r', 'r', 'f', 'a#', 'g', 'r', 'f', 'd#', 'f', 'd', 'c', 'c', 'c', 'r', 'r', 'd', 'r', 'a#', 'r', 'g', 'f', 'd#', 'r', 'd#', 'r', 'f', 'd#', 'f', 'g', 'd', 'r', 'r', 'd#', 'f', 'r', 'd', 'c', 'r', 'r', 'r', 'r', 'c', 'c', 'r', 'r', 'a#', 'a', 'c', 'c', 'd', 'r', 'd', 'f', 'r', 'd', 'c', 'r', 'r', 'a#', 'r', 'g', 'g', 'r', 'r', 'f', 'a#', 'g', 'r', 'f', 'd#', 'f', 'd', 'c', 'c', 'c', 'r', 'r', 'd', 'r', 'g', 'r', 'f', 'r', 'd#', 'r', 'd#', 'r', 'f', 'd#', 'f', 'g', 'd', 'r', 'd#', 'f', 'r', 'd', 'c', 'r', 'r', 'r', 'r', 'c', 'c', 'r', 'r', 'a#', 'a']
arra5=['c', 'r', 'r', 'd#', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'd', 'd#', 'r', 'f', 'r', 'r', 'r', 'd#', 'd', 'r', 'r', 'r', 'c', 'r', 'r', 'd#', 'r', 'r', 'r', 'r', 'r', 'd', 'd#', 'r', 'f', 'r', 'd#', 'r', 'd', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'c', 'r', 'r', 'd#', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'd', 'd#', 'r', 'r', 'f', 'r', 'r', 'r', 'r', 'r', 'r', 'a#', 'a', 'r', 'r', 'f', 'r', 'r', 'r', 'r', 'r', 'r', 'g', 'r', 'g', 'f', 'r', 'd#', 'r', 'r', 'd', 'r', 'c', 'r', 'r', 'r', 'd#', 'r', 'r', 'r', 'r', 'r', 'r', 'd', 'r', 'd#', 'r', 'r', 'f', 'r', 'r', 'r', 'r', 'r', 'd#', 'd', 'r', 'r', 'r', 'c', 'r', 'r', 'd#', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'd', 'r', 'd#', 'r', 'r', 'f', 'r', 'r', 'd#', 'r', 'd', 'r', 'r', 'c', 'r', 'r', 'r', 'd#', 'r', 'd', 'r', 'r', 'd#', 'r', 'f', 'r', 'r', 'r', 'a#', 'r', 'a', 'r', 'r', 'f', 'r', 'r', 'g', 'r', 'r', 'f', 'r', 'r', 'd#', 'r', 'd', 'r', 'r', 'r', 'd', 'd#', 'c', 'r', 'c', 'r', 'c', 'r', 'r', 'r', 'c', 'r', 'c', 'r', 'r', 'r', 'c', 'r', 'r', 'r', 'r', 'r', 'a#', 'r', 'a#', 'a', 'r', 'a', 'f', 'r', 'r', 'r', 'r', 'r', 'r', 'd', 'f', 'd', 'f', 'r', 'g', 'r', 'g', 'r', 'r', 'a#', 'r', 'a#', 'c', 'r', 'c', 'r', 'c', 'r', 'c', 'r', 'r', 'r', 'r', 'c', 'r', 'r', 'a#', 'r', 'a#', 'r', 'a', 'r', 'r', 'a', 'f', 'r', 'r', 'r', 'r', 'f', 'd', 'f', 'r', 'r', 'r', 'g', 'r', 'g', 'f', 'r', 'r', 'd#', 'r', 'r', 'd', 'r', 'c', 'r', 'r', 'd#', 'r', 'd', 'd#', 'r', 'f', 'r', 'r', 'r', 'r', 'd#', 'd', 'r', 'c', 'r', 'r', 'd#', 'r', 'r', 'r', 'd', 'd#', 'r', 'f', 'r', 'd#', 'd', 'r', 'r', 'r', 'c', 'r', 'r', 'd#', 'r', 'd', 'r', 'd#', 'r', 'f', 'r', 'r', 'r', 'a#', 'a', 'r', 'f', 'r', 'r', 'r', 'r', 'g', 'r', 'f', 'r', 'd#', 'd', 'r', 'd#', 'd', 'r', 'r', 'r', 'c', 'r', 'r', 'd#', 'r', 'r', 'r', 'd', 'r', 'd#', 'r', 'f', 'r', 'd#', 'd', 'r', 'r', 'r', 'c', 'd#', 'r', 'r', 'r', 'd', 'r', 'd#', 'r', 'f', 'r', 'd#', 'd', 'r', 'r', 'r', 'c', 'd#', 'r', 'd', 'r', 'd#', 'r', 'r', 'r', 'r', 'f', 'r', 'a#', 'r', 'a', 'r', 'r', 'f', 'r', 'r', 'r', 'g', 'r', 'f', 'r', 'd#', 'd', 'd#', 'r', 'c', 'r', 'd', 'f', 'd', 'f', 'r', 'g', 'r', 'f', 'r', 'g', 'r', 'g', 'f', 'r', 'r', 'd#', 'r', 'f', 'r', 'g', 'r', 'r', 'f', 'r', 'f', 'r', 'g', 'r', 'f', 'r', 'f', 'r', 'r', 'a#', 'r', 'a#', 'r', 'r', 'a#', 'r', 'a#', 'f', 'r', 'a#', 'r', 'r', 'r', 'c', 'r', 'a#', 'r', 'r', 'r', 'r', 'c', 'r', 'd#', 'r', 'f', 'r', 'r', 'g', 'r', 'r', 'f', 'r', 'r', 'f', 'r', 'g', 'r', 'r', 'r', 'd#', 'r', 'f', 'r', 'g', 'r', 'r', 'f', 'r', 'r', 'f', 'r', 'r', 'g', 'r', 'f', 'f', 'r', 'r', 'a#', 'r', 'a#', 'r', 'r', 'r', 'a#', 'r', 'a#', 'a', 'f', 'r', 'f', 'r', 'r', 'r', 'f', 'r', 'a#', 'r', 'r', 'a#', 'r', 'c', 'r', 'c', 'r', 'd#', 'r', 'd', 'r', 'd#', 'r', 'r', 'r', 'f', 'r', 'r', 'r', 'd#', 'r', 'd', 'r', 'r', 'r', 'r', 'c', 'r', 'r', 'c', 'r', 'r', 'c', 'r', 'd#', 'd', 'd#', 'c', 'r', 'c', 'r', 'c', 'r', 'd#', 'd', 'r', 'd#', 'r', 'r', 'f', 'r', 'd#', 'r', 'd', 'r', 'r', 'r', 'r', 'r', 'r', 'c', 'r', 'r', 'c', 'r', 'r', 'c', 'r', 'd#', 'd', 'r', 'd#', 'c', 'r', 'c', 'c', 'r', 'r', 'r', 'd#', 'r', 'd', 'd#', 'r', 'f', 'd', 'f', 'r', 'd#', 'r', 'd', 'r', 'c', 'r', 'r', 'a#', 'r', 'r', 'a#', 'a', 'f', 'r', 'f', 'r', 'r', 'd#', 'r', 'd']
arra6=['f', 'g', 'r', 'r', 'g', 'r', 'r', 'r', 'g', 'r', 'r', 'r', 'f', 'g', 'r', 'r', 'd#', 'r', 'r', 'd', 'r', 'd#', 'r', 'c', 'r', 'r', 'f', 'f', 'g', 'r', 'g', 'r', 'r', 'f', 'g', 'r', 'r', 'g', 'r', 'r', 'r', 'g', 'g', 'r', 'd#', 'r', 'd', 'r', 'd#', 'r', 'c', 'r', 'r', 'f', 'c', 'c', 'r', 'c', 'r', 'c', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'c', 'c', 'r', 'r', 'c', 'r', 'r', 'r', 'c', 'r', 'r', 'd#', 'r', 'r', 'd', 'r', 'a#', 'r', 'r', 'r', 'f', 'r', 'r', 'g', 'c', 'c', 'r', 'c', 'r', 'c', 'r', 'r', 'r', 'r', 'r', 'r', 'c', 'r', 'r', 'r', 'c', 'r', 'c', 'r', 'r', 'r', 'c', 'r', 'r', 'd#', 'r', 'r', 'r', 'd', 'r', 'a#', 'r', 'r', 'r', 'f', 'r', 'r', 'g', 'g', 'g#', 'r', 'a#', 'b', 'r', 'a#']
arra7=['f', 'c#', 'c', 'g#', 'g#', 'a#', 'g', 'f', 'c#', 'c', 'g#', 'a#', 'g#', 'g', 'f', 'c', 'g#', 'f', 'g#', 'f', 'c', 'g#', 'd#', 'c#', 'a#', 'g#', 'a#', 'a#', 'g', 'c', 'a#', 'g#', 'g#', 'a#', 'c#', 'c', 'c', 'g#', 'f', 'c#', 'g', 'd#', 'c', 'a#', 'c#', 'g', 'a#', 'g', 'd#', 'a#', 'd#', 'c', 'a#', 'g#', 'g#', 'f', 'c#', 'f', 'c#', 'c#', 'c', 'g#', 'g', 'f', 'd#', 'f', 'g#', 'f', 'c#', 'c', 'g#', 'a#', 'g', 'c', 'g#', 'f', 'g#', 'f', 'f', 'c#', 'c', 'g#', 'g#', 'c', 'g#', 'f', 'a#', 'c#', 'c', 'c', 'g#', 'd#', 'c#', 'c#', 'c', 'g', 'a#', 'g', 'd#', 'g#', 'f', 'c#', 'a#', 'd#', 'c', 'a#', 'a#', 'g#', 'f', 'c#', 'g', 'd#', 'c', 'a#', 'g#', 'a#', 'a#', 'g#', 'g', 'f', 'd#', 'f', 'g#', 'f', 'c#', 'c', 'g#', 'f', 'g#', 'f', 'c#', 'f', 'd#', 'c', 'd#', 'c#', 'a#', 'g', 'd#', 'a#', 'a#', 'g#', 'a#', 'a#', 'g#', 'a#', 'a#', 'g#', 'g', 'g', 'c', 'g#', 'f', 'f', 'd#', 'g#', 'a#', 'g#', 'a#', 'g#', 'c', 'a#', 'a#', 'g#', 'g', 'c', 'c', 'a#', 'c', 'f', 'g', 'a#', 'g#', 'f', 'd#', 'g#', 'a#', 'g', 'a#', 'g#', 'a#', 'g#', 'g', 'f', 'a#', 'g', 'd#', 'a#', 'g#', 'g#', 'f', 'c#', 'g', 'd#', 'c', 'c', 'g#', 'f', 'g#', 'f', 'c#', 'g', 'd#', 'c', 'a#', 'g#', 'g', 'g', 'f', 'f', 'd#', 'f', 'g#', 'f', 'c#', 'f', 'c', 'c#', 'a#', 'c', 'g#', 'f', 'f', 'g#', 'f', 'c#', 'a#', 'g#', 'g#', 'f', 'c#', 'a#', 'g', 'd#', 'g#', 'f', 'c#', 'c', 'c', 'g', 'd#', 'c', 'a#', 'c', 'c#', 'd#', 'd#', 'c#', 'c#', 'c', 'a#', 'g#', 'a#', 'c#', 'c', 'c', 'a#', 'g', 'd#', 'c', 'g#', 'f', 'g#', 'f', 'c#', 'g', 'd#', 'c', 'f', 'a#', 'a#', 'a#', 'g#', 'a#', 'g#', 'g', 'f', 'd#', 'a#', 'c#', 'a#', 'g#', 'c', 'c', 'a#', 'c#', 'a#', 'c#', 'c', 'g#', 'f', 'c#', 'g', 'd#', 'c', 'a#', 'g#', 'a#', 'g#', 'g', 'f', 'd#', 'f', 'f', 'd#', 'c', 'g#', 'a#', 'g', 'd#', 'c#', 'g', 'f', 'g', 'f', 'g', 'c#', 'f', 'c', 'c', 'g', 'f', 'e', 'c', 'a#', 'g', 'd#', 'f', 'c', 'c', 'a#', 'a#', 'c', 'g#', 'f', 'g#', 'a#', 'g#', 'a#', 'g#', 'g#', 'f', 'c#', 'g#', 'a#', 'c', 'c', 'g#', 'f', 'a#', 'g#', 'g', 'a#', 'g', 'd#', 'g#', 'f', 'c#', 'a#', 'c', 'a#', 'g#', 'f', 'c#', 'g', 'e', 'c', 'g', 'd#', 'c', 'd#', 'f', 'a#', 'g', 'd#', 'g#', 'f', 'c#', 'c', 'd#', 'c', 'a#', 'g#', 'a#', 'g', 'a#', 'g#', 'g', 'f', 'g#', 'f', 'c#', 'g', 'c', 'g#', 'f', 'g#', 'f', 'c#', 'g', 'd#', 'c', 'f', 'd#', 'a#', 'g', 'd#', 'g', 'c', 'a#', 'g#', 'g', 'f', 'g#', 'g', 'f', 'g', 'a#', 'g#', 'a#', 'g#', 'a#', 'c', 'a#', 'g#', 'a#', 'g#', 'f', 'c#', 'g', 'd#', 'c', 'a#', 'g#', 'f', 'c#', 'f', 'd#']

inparr=[]


for arr in (arra5,arra6,arra1,arra2,arra3,arra4,arra7):
	l=len(arr)
	i=0
	while (i<len(arr)-8):
		j=i;
		k=0
		inp=[];
		while (k<8):
			note=convertNotesToInt(arr[j])
			inp.append(note)
			k+=1
			j+=1
		inparr.append(inp)
		i+=1;
		enote=convertNotesToInt(arr[i+7]);
		ds.addSample(inp,enote)



from pybrain.supervised.trainers import BackpropTrainer
print len(ds)
trainer = BackpropTrainer(n, ds, verbose=True )
for i in range(1000):
    trainer.trainEpochs(2)

fileObject = open('filename', 'w')
pickle.dump(n, fileObject)
fileObject.close()

