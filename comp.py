from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
from pybrain.tools.validation    import testOnSequenceData
import pickle
import pysynth_s,pysynth
import random
def composer(filename,narray,bpmd,raga,outfilename):
	fileObject = open(filename,'r')
	net = pickle.load(fileObject)
	j=0;
	test=narray
	test[j:j+4]+test[j+1:j+5]
	ran=[]
	for i in xrange(8):	
		ran.append(random.randrange(0, 14, 1))
	while(j<50):
		ran.append(random.randrange(0, 14, 1))
		if(j<8):
			result=net.activate(test[j:j+3]+ran[j:j+5])
		else:
			result=net.activate(test[j-8:j-4]+ran[j:j+4])
		if(result>14):
			result=result%12;
		j+=1
		test.append(result)

	i=0
	newarr=[]

	for r in test:
		newarr.append(int(round(abs(r))))
	i=i+1;
	tunes=['c5','d#5','f5','g5','a#5','c5','c5','a#5','a5','g5','f5','d#5','d5','c5','c5']
	mayamg=['c', 'c#', 'e', 'f', 'g', 'g#', 'b','c', 'b', 'g#', 'g', 'f', 'e','c#','c']
	shanmukhapriya=['c', 'd', 'd#', 'f#', 'g', 'g#', 'a#', 'c5', 'a#', 'g#', 'g', 'f#', 'd#','d','c']
	anandab=['c', 'd#', 'd', 'd#', 'f', 'g', 'a', 'g', 'c', 'a#', 'a', 'g', 'f', 'd#','c']
	abhogi=['c', 'd', 'd#', 'f', 'a', 'c5', 'a', 'f', 'd#', 'd', 'c', 'd', 'd#', 'f','a', 'c5', 'a']
	sree=['c', 'd', 'f', 'g', 'a#', 'c5', 'a#', 'a', 'g', 'f', 'd#', 'd', 'c', 'd','c', 'd', 'f',]
	sankara=['c', 'd', 'e', 'f', 'g', 'a', 'b', 'c5', 'c5', 'b', 'a', 'g', 'f', 'e','c', 'd']
	

	t=()

	for r in newarr:
		rx=random.randrange(100, 1000, 1)%4
		if(rx==0):
			l=4
		elif(rx==3):
			l=2
		elif(rx==2):
			l=1
		elif(rx==1):
			l=4
		t=t+((anandab[r],l),)
	pysynth.make_wav(t, bpm=bpmd, fn = outfilename)
	return t


