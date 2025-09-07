import gymnasium as gym
import numpy as np
import random
from tqdm import tqdm
import matplotlib.pyplot as plt

environment=gym.make("FrozenLake-v1",is_slippery=False,render_mode="ansi")
environment.reset()

nb_states=environment.observation_space.n
nb_actions=environment.action_space.n
qtable=np.zeros((nb_states,nb_actions))

print("Q-Table.:")
print(qtable)

''' 
action=environment.action_space.sample()

# sol:0
# asagi:1
# sag:2
# yukari:3 

#S1 -> (Action 1) ->S2
new_state,reward,done,info,_=environment.step(action)

'''

#q_learning
episodes=10000
alpha=0.5 #learning rate
gama=0.9 #discount parameter

outcomes=[]

#training

for _ in tqdm(range(episodes)):

    state,_ = environment.reset()
    done=False #ajanin basari durumu

    outcomes.append("Failure")

    while not done: #ajan basarili olana kadar state icerisinde hareket et

        if np.max(qtable[state]) > 0:
            action=np.argmax(qtable[state])
        else:
            action=environment.action_space.sample()
        
        new_state,reward,done,info,_=environment.step(action)

        #update qtable

        qtable[state,action]=qtable[state,action] + alpha*(reward+gama*np.max(qtable[new_state])-qtable[state,action])

        state=new_state

        if reward:
            outcomes[-1]="Success"

print("Q-Table after Training.:")
print(qtable)

plt.bar(range(episodes),outcomes)
plt.show()

#test
episodes=100
nb_success=0

for _ in tqdm(range(episodes)):

    state, _ =environment.reset()
    done=False

    while not done:
        if np.max(qtable[state]) >0:
            action=np.argmax(qtable[state])
        else:
            action=environment.action_space.sample()

        new_state,reward,done,info,_ =environment.step(action)

        state=new_state
        nb_success+=reward

print("Success rate.:",100*nb_success/episodes)