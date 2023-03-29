import gym
import numpy as np
'''
  ### Action space A = {0, 1, 2, 3}
  {left, down, right, up}
  a = 0 -> left
  
  ### Observation space S = 4 x 4 grid
  Start at 0

  | 0 | 1 | 2 | 3 |
  | 4 | 5 | 6 | 7 |
  | 8 | 9 |10 |11 |
  |12 |13 |14 |15 |
  ------------------
  ------------------
  ------------------

  ### Rewards
  Reach goal(G)  +1
  Reach hole(H)   0
  Reach frozen(F) 0
  
  ### Slippery
  1/3 chance move in intended direction
  1/3 in either perpendicular directions
  
  ### Observation
  (observation, reward, terminated, truncated, done)
'''

env = gym.make('FrozenLake-v1', desc=None, map_name="4x4",
               is_slippery=True, render_mode="human")
observation, info = env.reset()

o1 = env.step(3)
print(env.action_space)
print(env.observation_space)
print(o1)
