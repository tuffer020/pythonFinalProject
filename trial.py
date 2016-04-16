import psutil, time

#l = psutil.pids()
#for pid in l:
#	p = psutil.Process(pid)
#	print p.name()
f = open('tempFile', 'a')
f.write(psutil.test())
f.close()

