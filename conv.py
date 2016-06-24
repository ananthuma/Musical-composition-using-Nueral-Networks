tunes=[' ','c','c#','d','d#','e','f','f#','g','g#','a','a#','b']
arr=[]
tune = tune.split()
i=0
for t in tune:
	if t in tunes:
		i=tunes.index(t);
		arr.append(i)
print arr
