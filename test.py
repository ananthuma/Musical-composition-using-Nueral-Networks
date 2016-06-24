arr=['c','d#','f','g','a#','c','c','a#','a','g','f','d#','d','c']
inparr=[]
tunes=['c','c#','d','d#','e','f','f#','g','g#','a','a#','b','r','c#','d','d#','e','f','f#','g','g#','a','a#']
l=len(arr)
i=0
while (i<len(arr)-4):
	j=i;
	k=0
	inp=[];
	while (k<4):
		note=tunes.index(arr[j])
		inp.append(note)
		k+=1
		j+=1
	inparr.append(inp)
	i+=1;
	enote=tunes.index(arr[i+3]);
	
print inparr
	


