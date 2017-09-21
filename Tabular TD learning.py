#Input the policy pi to be evaluated
#Output the value function V
from State import *
import random

n = 10 # the number of states
T = 10 # the total episodes
gamma = 0.5 # a discounted factor
alpha = 0.5 #learning rate
S = list() # state space
A = [0,1,2,3,4,5,6,7,8,9] # Action space
#Initialization of state values to be 0
def value(s):
	return s.value

def reward(s,a):
	reward = random.random()
	return reward

def takeAction(s,a):

	return S[random.randint(0,9)]

def initialize(S):
	return S[0]

def policy(s): #this one should be given

	#some logic
	return A[random.randint(0,9)]


for i in range(n):
	S.append(State(i))

for t in range(T):
	s = initialize(S)
	print 'Episode ',t
	print s.id, s.value
	while s.id != 9:
		a = policy(s)
		r = reward(s,a)
		new_state = takeAction(s,a)
		new_value = s.value + alpha*(r + gamma*new_state.value - s.value)
		s.updateValue(new_value)
		s = new_state
		print s.id, s.value

print 'Finally'
for i in range(n):
	print S[i].id, S[i].value

print 'done'


