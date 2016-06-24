import pyaudio  
import wave,sys  
chunk = 2048  
f = wave.open(sys.argv[1],"rb")  
p = pyaudio.PyAudio()   
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
print  p.get_format_from_width(f.getsampwidth())
data = f.readframes(chunk)  
while data != '':  
    stream.write(data)  
    data = f.readframes(chunk)  
stream.stop_stream()  
stream.close()    
p.terminate()

