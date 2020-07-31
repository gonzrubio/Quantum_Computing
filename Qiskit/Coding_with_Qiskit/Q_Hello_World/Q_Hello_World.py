# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 09:22:21 2020

@author: Gonzalo
"""
import qiskit as q


### Create circuit (1/sqrt(2))(|00>+|11>) ###

# A two qubit quantum register.
qr = q.QuantumRegister(2,'q') 

# Two classical bit register to take measurements from the quantum bits.
cr = q.ClassicalRegister(2,'c')

circuit = q.QuantumCircuit(qr, cr)

# Apply a Hadamard gate onto the first qubit.
circuit.h(qr[0])

# CNOT gate (When control == 1, target flips).
circuit.cx(qr[0],qr[1])

# Created entanglement between q0_0 and q0_1.
# Measure qubits and store in bits.
circuit.measure(qr,cr)


### Execute circuit ### 

# Simulate circuit locally
simulator = q.Aer.get_backend('qasm_simulator')
result = q.execute(circuit,backend=simulator).result()
q.visualization.plot_histogram(result.get_counts(circuit))

# Run on quantum computer at IBM
q.IBMQ.load_account()
provider = q.IBMQ.get_provider('ibm-q')
qcomp = provider.get_backend('ibmq_16_melbourne')
job = q.execute(circuit, backend=qcomp)
q.tools.monitor.job_monitor(job)
result = job.result()
q.visualization.plot_histogram(result.get_counts(circuit))


