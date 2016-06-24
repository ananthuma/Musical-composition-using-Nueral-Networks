alay="GDGAbACDCBAAbAGGDGAbACDCBAAbAGGDGAbACDCBAAbAGGDGAbACDCBAAbAGGbAbAGGGGFFFAAGGGGbAbAGGGGFFFAAGGGGDCDAbCCFFEbEbEbDCCDDAAGbAbAGGGGFFFAAGGGFFGbbAFFGAFbAGGFFG"
naly=[]
i=0;
tune=["c","d","e","f","g","a","b"]

while(i<len(alay)-1):
	if(alay[i]!=' '):
		if alay[i+1]=='b':
			x=tune.index(alay[i].lower())
			naly.append(tune[x-1]+'#')
			i+=1;
		else:
			naly.append(alay[i].lower())
		
	else:
		naly.append('r');

	i+=1
import random
naly=['c', 'r', 'r', 'd#', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'd', 'd#', 'r', 'f', 'r', 'r', 'r', 'd#', 'd', 'r', 'r', 'r', 'c', 'r', 'r', 'd#', 'r', 'r', 'r', 'r', 'r', 'd', 'd#', 'r', 'f', 'r', 'd#', 'r', 'd', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'c', 'r', 'r', 'd#', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'd', 'd#', 'r', 'r', 'f', 'r', 'r', 'r', 'r', 'r', 'r', 'a#', 'a', 'r', 'r', 'f', 'r', 'r', 'r', 'r', 'r', 'r', 'g', 'r', 'g', 'f', 'r', 'd#', 'r', 'r', 'd', 'r', 'c', 'r', 'r', 'r', 'd#', 'r', 'r', 'r', 'r', 'r', 'r', 'd', 'r', 'd#', 'r', 'r', 'f', 'r', 'r', 'r', 'r', 'r', 'd#', 'd', 'r', 'r', 'r', 'c', 'r', 'r', 'd#', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'd', 'r', 'd#', 'r', 'r', 'f', 'r', 'r', 'd#', 'r', 'd', 'r', 'r', 'c', 'r', 'r', 'r', 'd#', 'r', 'd', 'r', 'r', 'd#', 'r', 'f', 'r', 'r', 'r', 'a#', 'r', 'a', 'r', 'r', 'f', 'r', 'r', 'g', 'r', 'r', 'f', 'r', 'r', 'd#', 'r', 'd', 'r', 'r', 'r', 'd', 'd#', 'c', 'r', 'c', 'r', 'c', 'r', 'r', 'r', 'c', 'r', 'c', 'r', 'r', 'r', 'c', 'r', 'r', 'r', 'r', 'r', 'a#', 'r', 'a#', 'a', 'r', 'a', 'f', 'r', 'r', 'r', 'r', 'r', 'r', 'd', 'f', 'd', 'f', 'r', 'g', 'r', 'g', 'r', 'r', 'a#', 'r', 'a#', 'c', 'r', 'c', 'r', 'c', 'r', 'c', 'r', 'r', 'r', 'r', 'c', 'r', 'r', 'a#', 'r', 'a#', 'r', 'a', 'r', 'r', 'a', 'f', 'r', 'r', 'r', 'r', 'f', 'd', 'f', 'r', 'r', 'r', 'g', 'r', 'g', 'f', 'r', 'r', 'd#', 'r', 'r', 'd', 'r', 'c', 'r', 'r', 'd#', 'r', 'd', 'd#', 'r', 'f', 'r', 'r', 'r', 'r', 'd#', 'd', 'r', 'c', 'r', 'r', 'd#', 'r', 'r', 'r', 'd', 'd#', 'r', 'f', 'r', 'd#', 'd', 'r', 'r', 'r', 'c', 'r', 'r', 'd#', 'r', 'd', 'r', 'd#', 'r', 'f', 'r', 'r', 'r', 'a#', 'a', 'r', 'f', 'r', 'r', 'r', 'r', 'g', 'r', 'f', 'r', 'd#', 'd', 'r', 'd#', 'd', 'r', 'r', 'r', 'c', 'r', 'r', 'd#', 'r', 'r', 'r', 'd', 'r', 'd#', 'r', 'f', 'r', 'd#', 'd', 'r', 'r', 'r', 'c', 'd#', 'r', 'r', 'r', 'd', 'r', 'd#', 'r', 'f', 'r', 'd#', 'd', 'r', 'r', 'r', 'c', 'd#', 'r', 'd', 'r', 'd#', 'r', 'r', 'r', 'r', 'f', 'r', 'a#', 'r', 'a', 'r', 'r', 'f', 'r', 'r', 'r', 'g', 'r', 'f', 'r', 'd#', 'd', 'd#', 'r', 'c', 'r', 'd', 'f', 'd', 'f', 'r', 'g', 'r', 'f', 'r', 'g', 'r', 'g', 'f', 'r', 'r', 'd#', 'r', 'f', 'r', 'g', 'r', 'r', 'f', 'r', 'f', 'r', 'g', 'r', 'f', 'r', 'f', 'r', 'r', 'a#', 'r', 'a#', 'r', 'r', 'a#', 'r', 'a#', 'f', 'r', 'a#', 'r', 'r', 'r', 'c', 'r', 'a#', 'r', 'r', 'r', 'r', 'c', 'r', 'd#', 'r', 'f', 'r', 'r', 'g', 'r', 'r', 'f', 'r', 'r', 'f', 'r', 'g', 'r', 'r', 'r', 'd#', 'r', 'f', 'r', 'g', 'r', 'r', 'f', 'r', 'r', 'f', 'r', 'r', 'g', 'r', 'f', 'f', 'r', 'r', 'a#', 'r', 'a#', 'r', 'r', 'r', 'a#', 'r', 'a#', 'a', 'f', 'r', 'f', 'r', 'r', 'r', 'f', 'r', 'a#', 'r', 'r', 'a#', 'r', 'c', 'r', 'c', 'r', 'd#', 'r', 'd', 'r', 'd#', 'r', 'r', 'r', 'f', 'r', 'r', 'r', 'd#', 'r', 'd', 'r', 'r', 'r', 'r', 'c', 'r', 'r', 'c', 'r', 'r', 'c', 'r', 'd#', 'd', 'd#', 'c', 'r', 'c', 'r', 'c', 'r', 'd#', 'd', 'r', 'd#', 'r', 'r', 'f', 'r', 'd#', 'r', 'd', 'r', 'r', 'r', 'r', 'r', 'r', 'c', 'r', 'r', 'c', 'r', 'r', 'c', 'r', 'd#', 'd', 'r', 'd#', 'c', 'r', 'c', 'c', 'r', 'r', 'r', 'd#', 'r', 'd', 'd#', 'r', 'f', 'd', 'f', 'r', 'd#', 'r', 'd', 'r', 'c', 'r', 'r', 'a#', 'r', 'r', 'a#', 'a', 'f', 'r', 'f', 'r', 'r', 'd#', 'r', 'd']

t=()
for r in range(0,100):
	if(naly[r]=='r'):
		l=32
	else:
		l=4
	t=t+((naly[r],l),)
print t
import pysynth
pysynth.make_wav(t, bpm=300 ,fn = "output2.wav")
