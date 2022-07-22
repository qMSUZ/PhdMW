#Part of initialization profiling simulator

#The process of initializing the hybrid mechanism of profiling users of the recommendation system should begin with the definition of the size of the classical and quantum register.
#Then define the user's preferences by answering the questions included in the profiling process.
#The presented example concerns simulation on the QASM quantum computer simulator.
	
	
import getpass, time
import numpy as np
import matplotlib.pyplot as plt
from qiskit import ClassicalRegister, QuantumRegister
from qiskit.tools.visualization import plot_histogram, circuit_drawer
from qiskit import BasicAer, IBMQ
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from qiskit.tools.visualization import plot_histogram
from qiskit import IBMQ, assemble, transpile
from qiskit.circuit.random import random_circuit
%matplotlib inline
provider = IBMQ.load_account()
backend = BasicAer.get_backend('qasm_simulator')
q = QuantumRegister(3)
c = ClassicalRegister(3)
qc = QuantumCircuit(q, c)
T = 2	
scales = 0    
user = "current" #new
preferences = "added" #top50
type_preferences = "genre" # actor, director
status_film = "evaluated" #watched
liked = "yes" #"no"
how_scored = "good" #"badly" 
score = "5" #5,4,3,2,1
feature = "010"  
qc.measure(q, c)
job = execute(qc, backend, shots=1000)
result = job.result()
counts = result.get_counts(qc)
print("\nCount:",counts)
qc.draw()
plot_histogram(counts)
