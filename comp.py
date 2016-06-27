from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
from pybrain.tools.validation    import testOnSequenceData
import pickle
import pysynth_s,pysynth
import random,math
def composer(filename,narray,bpmd,raganum,outfilename):
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
	raganum=2
	for r in test:
		newarr.append(int(round(abs(r))))
	i=i+1;
	tunes=['r','c3','d#3','f3','g3','a#3','c3','c3','a#3','a3','g3','f3','d#3','d3','c3','c3']
	tunes2=['c5','d#5','f5','g5','a#5','c5','c5','a#5','a5','g5','f5','d#5','d5','c5','c5']
	mayamg=['c', 'c#', 'e', 'f', 'g', 'g#', 'b','c', 'b', 'g#', 'g', 'f', 'e','c#','c']
	shanmukhapriya=['c', 'd', 'd#', 'f#', 'g', 'g#', 'a#', 'c5', 'a#', 'g#', 'g', 'f#', 'd#','d','c']
	anandab=['r','c', 'd#', 'd', 'd#', 'f', 'g', 'a', 'g', 'c', 'a#', 'a', 'g', 'f', 'd#','c']
	abhogi=['c', 'd', 'd#', 'f', 'a', 'c5', 'a', 'f', 'd#', 'd', 'c', 'd', 'd#', 'f','a', 'c5', 'a']
	sree=['c', 'd', 'f', 'g', 'a#', 'c5', 'a#', 'a', 'g', 'f', 'd#', 'd', 'c', 'd','c', 'd', 'f',]
	sankara=['c', 'd', 'e', 'f', 'g', 'a', 'b', 'c5', 'c5', 'b', 'a', 'g', 'f', 'e','c', 'd']
	if(raganum==1):
		raga=sree;
	elif(raganum==2):
		raga=sankara;
	elif(raganum==3):
		raga=mayag;
	elif(raganum==4):
		raga=anandab;
	else:
		raga=sree;
	

	t=()
	t2=();
	t3=();
	t4=();
	inc =1;
	for r in newarr:
		rx=int(abs(round(math.sin(inc)*10)))%4
		print rx
		if(rx==0):
			m=-1
			l=2
		elif(rx==3):
			m=1
			l=8
		elif(rx==2):
			m=-1
			l=4
		elif(rx==1):
			m=1
			l=4
			if(newarr.index(r)>10):
				r=r-int(abs(round(math.sin(inc)*10)))
		
		inc+=1;
		
		
		t=t+((raga[r],l),)
		t3=t3+((raga[r*-1],l/2),)
		t2=t2+((raga[r],l*2),)
		t4=t2+((raga[r*-1],l),)
	pysynth.make_wav(t, bpm=bpmd, fn = "f"+outfilename)
	pysynth.make_wav(t3, bpm=bpmd, fn = "s"+outfilename)
	pysynth_s.make_wav(t2, bpm=bpmd, fn = "l"+outfilename)
	pysynth_s.make_wav(t4, bpm=bpmd, fn = "l2"+outfilename)
	pysynth.mix_files("f"+outfilename,"s"+outfilename,"k"+outfilename);
	pysynth.mix_files("l"+outfilename,"l2"+outfilename,"k2"+outfilename);
	pysynth.mix_files("k"+outfilename,"k2"+outfilename,outfilename);
	return t


