import ctypes as c
mus = c.CDLL("libmus.so")
#mus.similarityCheck.argtypes = (ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)),ctypes.POINTER(ctypes.c_char))
prototype = c.CFUNCTYPE(c.c_int,c.c_char,c.c_char)
files = ["1.wav","2.wav","a.wav"]
filetochk = "b.wav"
similarityCheck=prototype(('similarityCheck',mus))
filesp=c.POINTER(c.c_char);
filespp=c.POINTER(filesp);
files2p=c.POINTER(c.c_char);

mus.similarityCheck(c.c_int(3),files,filetochk);
