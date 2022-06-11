
# Solving Boolean SAT Problem using Grover’s Algorithm

Solve k-SAT problem with grover's algorithm in quantum computer using qiskit
- Created own *Oracle* based on given equation and displayed its circuit
- Using *Phase Estimation* to find repetitions of Oracle
- Simulating final circuit in *Qasm Simulator* and *StateVector Simulator*
- Showing Histogram and printing StateVector

# REQUIREMENTS
- using pipenv
```bash
pipenv install
```

# Usage/Examples
### Problem Statement [🔗](https://app.simplenote.com/p/Pbbh5y)
Frank wants to throw a dinner party to celebrate Alice and Bob’s engagement. He is also considering inviting their mutual friends Charles, Dave and Eve. However, he is aware that Charles will come to the party only if Dave comes without Eve. Frank wants to know what possible combinations of invitations he can write for his friends Alice, Bob, Charles, Dave and Eve.

Help Frank calculate all the possible combinations using Grover’s algorithm.

```cmd
python3 main.py "(a & b) & (~c | (c & d & ~e))"
```

![cmd](https://github.com/adityabadhiye/grover-sat/blob/master/images/sample.png)
### Results

![circuit](https://github.com/adityabadhiye/grover-sat/blob/master/images/circuit.png)

![histogram](https://github.com/adityabadhiye/grover-sat/blob/master/images/qasmhist.png)
