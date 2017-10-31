import os
import subprocess
import shutil
path =  os.path.dirname(os.path.realpath(__file__))
book_name = os.path.basename(path)
dirs = [x[0] for x in os.walk(path)][1:]
filename = "temporary_file"
i=0
processes = []
for dir in dirs:
    print dir
    processes.append(subprocess.Popen(["merge.bat",dir,filename+str(i)]))
    i+=1
    
for p in processes:
    p.wait()
i=0
for dir in dirs:
    os.rename(filename+str(i),dir+".mp3")
    i+=1
subprocess.call(["merge.bat",".",filename])
os.rename(filename,book_name+".mp3")
for dir in dirs:
    os.remove(dir+".mp3")
    shutil.rmtree(dir)
