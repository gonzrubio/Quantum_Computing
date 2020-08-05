# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 11:26:36 2020

@author: Gonzalo
"""
import qiskit as q
from qiskit.tools.visualization import plot_bloch_multivector

circuit = q.QuantumCircuit(1,1) # Quantum circuit with one quibit and one bit
circuit.x(0) # Aplly an X-gate to the quibit

# Simulate circuit and see what the output is
simulator = q.BasicAer.get_backend('statevector_simulator')
job = q.execute(circuit, backend=simulator)
statevector = job.result().get_statevector()
print(statevector)

# Plot in Bloch sphere
plot_bloch_multivector(statevector)

# Apply measurement
circuit.measure([0],[0])
backend = q.BasicAer.get_backend('qasm_simulator')
result = q.execute(circuit, backend=backend, shots=1024).result()
counts = result.get_counts()
q.visualization.plot_histogram(counts)

# Matrix representation of the circuit
circuit = q.QuantumCircuit(1,1) 
circuit.x(0) 
simulator = q.BasicAer.get_backend('unitary_simulator')
job = q.execute(circuit, backend=simulator)
unitary = job.result().get_unitary()
print(unitary)