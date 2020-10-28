import gym
import random as rand
from time import sleep

def one_game(gamma=0.9):
    env = gym.make("FrozenLake-v0")
    state = env.reset()

    all_reward = 0
    done = False

    print(env.render())
    while not done:
        act = rand.randint(0, 3)
        state, reward, done, _ = env.step(act)
        env.render()
        all_reward = all_reward * gamma + reward
        sleep(.5)

    print("reward :", all_reward)

def main():
    one_game()

if __name__ == "__main__":
    main()