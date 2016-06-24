import simchk
f = open('selected', 'w')
files=["1.wav","2.wav","b.wav","a.wav"]
filetochk="a.wav"
for fi in files:
	f.write(fi+"\n")
f.write(filetochk)
f.close()
simchk.similarity()
with open("result") as f:
    content = f.readlines()
i=0;
for c in content:
	print "similarity between "+files[i] +" & "+ filetochk +":"+c;
	i=i+1

