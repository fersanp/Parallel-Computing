import sys, threading, multiprocessing, time

def countdown(n):
    while n > 0:
        n -= 1

COUNT = 100000000

t = time.time()

if sys.argv[1]=='serial':
	#run it serially
	countdown(COUNT)
        print("Me tomo: "+ str(time.time() - t))
elif sys.argv[1]=='parallel':
	#subdividing the work over two parallel threads
	t1 = threading.Thread(target=countdown,args=(COUNT//2,))
	t2 = threading.Thread(target=countdown,args=(COUNT//2,))
	t1.start(); t2.start()
	t1.join() ; t2.join()
        print("Me tomo: "+ str(time.time() - t))
elif sys.argv[1]=='process':
	#subdividing the work over two parallel process
	p1 = multiprocessing.Process(target=countdown,args=(COUNT//2,))
	p2 = multiprocessing.Process(target=countdown,args=(COUNT//2,))
	p1.start(); p2.start()
	p1.join() ; p2.join()
        print("Me tomo: "+ str(time.time() - t))
