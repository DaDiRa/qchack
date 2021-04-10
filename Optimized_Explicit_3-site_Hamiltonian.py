#!/usr/bin/env python
# coding: utf-8

from qiskit import *
import numpy as np

n=3 #3 spins
h=1 #ένταση εγκάρσιου μαγνητικού πεδίου
qc = np.empty(2*n-1, dtype=object) 
for i in range(0, 2*n-1): #2n-1=5 γιατί τόσους παράγοντες θα έχει η χαμιλτονιανή
    qr = QuantumRegister(n) 
    qc[i] = QuantumCircuit(qr) #δημιουργία κυκλωμάτων που αντιστοιχούν σε κάθε παράγοντα της χαμιλτονιανής
    #print(i)
    if (i<=n-2): #αν βρίσκομαι στο πρώτο μέρος της χαμιλτονιανής
        qc[i].z(i) #το σπιν της θέσης στην οποία βρίσκομαι
        qc[i].z(i+1) #και το γειτονικό του
    else: #αν βρίσκομαι στο δεύτερο μέρος της χαμιλτονιανής
        qc[i].x(2*n-2-i) #2*n-2=4 γιατί η αρίθμηση ξεκινάει από το 0
simulator = Aer.get_backend('unitary_simulator')
result = np.empty(2*n-1, dtype=object) 
unitary = np.empty(2*n-1, dtype=object) 
Hamiltonial=0
for i in range(0, 2*n-1):
    result[i] = execute(qc[i], backend=simulator).result()
    unitary[i] = result[i].get_unitary()
    print(unitary[i])
    if (i<=n-2):
        Hamiltonial=np.add(Hamiltonial,-unitary[i])
    else:
        Hamiltonial=np.add(Hamiltonial,-h*unitary[i])
print(Hamiltonial)