import threading 
import time

def saludos(people):
    for i in people:
        print("Hola "+ i )
        time.sleep(0.5)

def asignar_id(people):
    i = 1
    for person in people:
        print("Persona: " + person + " Tu id es: " + str(i))
        i = i + 1
        time.sleep(0.5)

        
people = ["Diego", "Jose", "Bruno", "Miguel"]
t = time.time()
saludos(people)
asignar_id(people)
print("Me tomo: "+ str(time.time() - t))

print("----------------")
### Threads
t = time.time()
t1 = threading.Thread(target=saludos, args=(people,))
t2 = threading.Thread(target=asignar_id, args=(people,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Me tomo: "+ str(time.time() - t))
