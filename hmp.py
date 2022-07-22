#Hybrid profiling mechanism

def initialization_hadamard():
  qc.h(q[0]) 
  qc.h(q[1]) 
  qc.h(q[2])    
def grover_oracle_000():
  qc.x(q[0]) 
  qc.x(q[1])
  qc.x(q[2])
  qc.h(q[2])
  qc.ccx(q[0], q[1], q[2])
  qc.h(q[2])
  qc.x(q[0])
  qc.x(q[1])
  qc.x(q[2])
def grover_oracle_001():
  #qc.x(q[0]) 
  qc.x(q[1])
  qc.x(q[2])
  qc.h(q[2])
  qc.ccx(q[0], q[1], q[2])
  qc.h(q[2])
  #qc.x(q[0])
  qc.x(q[1])
  qc.x(q[2])
def grover_oracle_010():
  qc.x(q[0]) 
  #qc.x(q[1])
  qc.x(q[2])
  qc.h(q[2])
  qc.ccx(q[0], q[1], q[2])
  qc.h(q[2])
  qc.x(q[0])
  #qc.x(q[1])
  qc.x(q[2])
def grover_oracle_011():
  #qc.x(q[0]) 
  #qc.x(q[1])
  qc.x(q[2])
  qc.h(q[2])
  qc.ccx(q[0], q[1], q[2])
  qc.h(q[2])
  #qc.x(q[0])
  #qc.x(q[1])
  qc.x(q[2])
def grover_oracle_100():
  qc.x(q[0]) 
  qc.x(q[1])
  #qc.x(q[2])
  qc.h(q[2])
  qc.ccx(q[0], q[1], q[2])
  qc.h(q[2])
  qc.x(q[0])
  qc.x(q[1])
  #qc.x(q[2])
def grover_oracle_101():
  #qc.x(q[0]) 
  qc.x(q[1])
  #qc.x(q[2])
  qc.h(q[2])
  qc.ccx(q[0], q[1], q[2])
  qc.h(q[2])
  #qc.x(q[0])
  qc.x(q[1])
  #qc.x(q[2])
def grover_oracle_110():
  qc.x(q[0]) 
  #qc.x(q[1])
  #qc.x(q[2])
  qc.h(q[2])
  qc.ccx(q[0], q[1], q[2])
  qc.h(q[2])
  qc.x(q[0])
  #qc.x(q[1])
  #qc.x(q[2])
def grover_oracle_111():
  #qc.x(q[0]) 
  #qc.x(q[1])
  #qc.x(q[2])
  qc.h(q[2])
  qc.ccx(q[0], q[1], q[2])
  qc.h(q[2])
  #qc.x(q[0])
  #qc.x(q[1])
  #qc.x(q[2])
def selection_oracle(feature, T):
  if feature == "000":
    for t in range(T):
      grover_oracle_000()
      grover_amplification()
  if feature == "001":
    for t in range(T):
      grover_oracle_001()
      grover_amplification()
  if feature == "010":
    for t in range(T):
      grover_oracle_010()
      grover_amplification()
  if feature == "011":
    for t in range(T):
      grover_oracle_011()
      grover_amplification()   
  if feature == "100":
    for t in range(T):
      grover_oracle_100()
      grover_amplification()
  if feature == "101":
    for t in range(T):
      grover_oracle_101()
      grover_amplification()
  if feature == "110":
    for t in range(T):
      grover_oracle_110()
      grover_amplification()
  if feature == "111":
    for t in range(T):
      grover_oracle_111()
      grover_amplification()
def grover_amplification():
 	qc.h(q[0]) 
 	qc.h(q[1]) 
 	qc.h(q[2])
 	qc.x(q[0]) 
 	qc.x(q[1]) 
 	qc.x(q[2])
 	qc.h(q[2])
 	qc.ccx(q[0], q[1], q[2])
 	qc.h(q[2])
 	qc.x(q[0]) 
 	qc.x(q[1]) 
 	qc.x(q[2])
 	qc.h(q[0]) 
 	qc.h(q[1]) 
 	qc.h(q[2])	
def selection_genre(feature):
  if feature == "000":
    print("Genre: western")  
  if feature == "001":
    print("Genre: anime")
  if feature == "010":
    print("Genre: drama")
  if feature == "011":
    print("Genre: biography") 
  if feature == "100":
    print("Genre: history")
  if feature == "101":
    print("Genre: horror")
  if feature == "110":
    print("Genre: comedy")
  if feature == "111":
    print("Genre: sensational")
def selection_actor(feature):
  if feature == "000":
    print("Actor: Jack Nicholson")    
  if feature == "001":
    print("Actor: Leonardo DiCaprio")
  if feature == "010":
    print("Actor: Alan Rickman")
  if feature == "011":
    print("Actor: Robert Downey Jr.") 
  if feature == "100":
    print("Actor: Al Pacino")
  if feature == "101":
    print("Actor: Clint Eastwood")
  if feature == "110":
    print("Actor: Tom Hanks")
  if feature == "111":
    print("Actor: Kevin Spacey")
def selection_director(feature):
  if feature == "000":
    print("Director: Stanley Kubrick")
  if feature == "001":
    print("Director: Quentin Tarantino")
  if feature == "010":
    print("Director: Sergio Leone")
  if feature == "011":
    print("Director: Francis Ford Coppola") 
  if feature == "100":
    print("Director: Christopher Nolan")
  if feature == "101":
    print("Director: David Fincher")
  if feature == "110":
    print("Director: Wes Anderson")
  if feature == "111":
    print("Director: Miloš Forman")     
def selection_title(feature):
  if feature == "000":
    print("Film: Skazani na Shawshank")
  if feature == "001":
    print("Film: Nietykalni")
  if feature == "010":
    print("Film: Zielona mila")
  if feature == "011":
    print("Film: Ojciec chrzestny") 
  if feature == "100":
    print("Film: Dwunastu gniewnych ludzi")
  if feature == "101":
    print("Film: Forrest Gump")
  if feature == "110":
    print("Film: Lot nad kukułczym gniazdem")
  if feature == "111":
    print("Film: Joker")           

import getpass, time
from qiskit import ClassicalRegister, QuantumRegister
from qiskit import QuantumCircuit, available_backends, execute, register, get_backend
from qiskit.tools.visualization 
import plot_histogram, circuit_drawer
import numpy as np
import matplotlib.pyplot as plt
from qiskit import BasicAer, IBMQ
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from qiskit.tools.visualization import plot_histogram
q = QuantumRegister(3)
c = ClassicalRegister(3)
qc = QuantumCircuit(q, c)
T = 2
scales = 0    
user = "current" #user: new, current
preferences = "added" #preferences: added, top50
type_preferences = "genre" 
#type_preferences = "actor" 
#type_preferences = "director" 
status_film = "watched" 
status_film = "evaluated" 
liked = "yes" #"no"
how_scored = "good" #"badly" 
score = "5" #score: 5, 4, 3, 2, 1
feature = "010"  
if user == "new" :
  scales+=0.5
  print("New users")
if preferences == "added":
  scales+=0.5
  print("Added preferences")
if type_preferences == "genre":
  scales+=1/3
  scales+=1.0
  print("Added preferences for genre")
  print("Making a groover for of the genre indicated")
  initialization_hadamard()
  selection_oracle(feature, T)
  selection_genre(feature)
  print("Weight value =", + scales)
elif type_preferences == "actor":
  scales+=1/3
  scales+=0.5
  print("Added preferences for actor")
  print("Making a groover for of the sctor indicated")
  initialization_hadamard()
  selection_oracle(feature, T)
  selection_actor(feature)
  print("Scales =", + scales)
elif type_preferences == "director":
  scales+=1/3
  scales+=0.25
  print("Added preferences for director")
  print("Making a groover for of the indicated director")
  initialization_hadamard()
  selection_oracle(feature, T)
  selection_director(feature)
  print("Scales =", + scales)
elif preferences == "top50":
  scales+=0.5
  print("Favorite list from top50 list")
  print("Scales =", + scales)
elif user == "current":
  scales+=0.5
  print("Current user")
if status_film == "watched":
  scales+=0.5
  print("Watched film")
if liked == "yes":
  scales+=0.5
  scales+=1.0
  print("Liked film")
  print("Making a groover for of the indicated film")
  initialization_hadamard()
  selection_oracle(feature, T)
  selection_title(feature)
  print("Scales =", + scales)
elif liked == "no":
  scales+=0.5
  print("Not likedł film")
  print("Scales =", + scales)
elif status_film == "evaluated":
  scales+=0.5
  print("Evaluated film")
if how_scored == "good":
  scales+=0.5
  print("Good evaluated film")
if score == "5":
  scales+=1/3
  scales+=5.0
  print("Score for 5")
  print("Making a groover for of the indicated film for title")
  initialization_hadamard()
  selection_oracle(feature, T)
  selection_title(feature)
  print("Scales =", + scales) 
elif score == "4":
  scales+=1/3
  scales+=4.0
  print("Score for 4")
  print("Making a groover for
  			of the indicated film for title")
  initialization_hadamard()
  selection_oracle(feature, T)
  selection_title(feature)
  print("Scales =", + scales) 
elif score == "3":
  scales+=1/3
  scales+=3.0
  print("Score for 3")
  print("Making a groover for of the indicated film for title")
  initialization_hadamard()
  selection_oracle(feature, T)
  selection_title(feature)
  print("Scales =", + scales) 
elif how_scored == "badly":
  scales+=0.5
  print("Badly evaluated film")
if score == "2":
  scales+=0.5
  scales+=2.0
  print("Score for 2")
  print("Scales =", + scales)
elif score == "1":
  scales+=0.5
  scales+=1.0
  print("Score for 1")           
  print("Scales =", + scales) 
qc.measure(q, c)
backend = BasicAer.get_backend('qasm_simulator')
job = execute(qc, backend=backend, shots=10000)
result = job.result()
circuit_drawer(qc)
counts = result.get_counts(qc)
plot_histogram(counts)