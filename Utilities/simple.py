import ctypes

testlib = ctypes.CDLL('./testlib.so')
testlib.similarityCheck()