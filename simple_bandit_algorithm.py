import random

k = 10 #number of arms for k-arms bandit problem
Q = list()
N = list()
epsilon = 0.1 # a probability to choose a random action
A = 0 # to store action

for a in range(k):
	Q[a] = 0
	N[a] = 0
	
def bandit(A):

	return reward(A)

while True:
	if random.random() < epsilon:
		A = random.randint(0, k - 1)
	else:
		A = Q.index(max(Q))

	R = bandit(A)
	N[A] = N[A] + 1
	Q[A] = Q[A] + 1/N[A] * (R - Q[A])



