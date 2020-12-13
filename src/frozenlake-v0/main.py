import gym
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt

import sys; sys.path.append('..')
from q_agent import Qlearn
from common.policy import EpsilonGreedy

GAME_NAME = "FrozenLake-v0"


def show_plot(table, height, width):
    ch, cw = height * 3, width * 3
    reward_arr = np.zeros((ch, cw))

    keys = {
        0: (0, -1),
        1: (-1, 0),
        2: (0, 1),
        3: (1, 0),
    }

    for i in range(height):
        for j in range(width):
            state = (height - i - 1) * width + j
            if np.min(table[state]) - np.max(table[state]) == 0:
                continue
            coord_h = i * 3 + 1
            coord_w = j * 3 + 1
            reward_arr[coord_h][coord_w-1] = 1
            reward_arr[coord_h-1][coord_w] = 1
            reward_arr[coord_h][coord_w+1] = 1
            reward_arr[coord_h+1][coord_w] = 1
            actopt = np.argmax(table[state])

            coordx, coordy = keys[(actopt + 2) % 4]
            x, y = coordx + coord_h, coordy +coord_w
            reward_arr[x][y] = 0

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    plt.imshow(
        reward_arr,
        interpolation="bilinear",
        vmax=1,
        vmin=-1
    )
    ax.set_xlim(-0.5, height-0.5)
    ax.set_ylim(-0.5, width-0.5)
    ax.set_xticks(np.arange(-0.5, cw, 3))
    ax.set_yticks(np.arange(-0.5, ch, 3))
    ax.set_xticklabels(range(width + 1))
    ax.set_yticklabels(range(height + 1))
    ax.grid(which="both")
    plt.title("policy")
    plt.savefig("jpg/policy.jpg")
    plt.show()


def show_reward(rewards, step = 50):
    N = len(rewards)
    rewards = np.array(rewards)
    reward_mean = [0]
    reward_std  = [0]
    for i in range(1, (N + step - 1) // step + 1):
        reward_mean.append((np.mean(rewards[:i * step]) + 1) / 2)
        reward_std.append(np.std(rewards[:i * step]))

    plt.figure()
    x = np.arange(0, N + 1, step)
    mean = np.array(reward_mean)
    std = np.array(reward_std)
    plt.fill_between(
        x, mean - std, mean + std, alpha=.1, color="r"
    )
    plt.plot(x, reward_mean, label="mean")
    plt.legend()
    plt.title("Average reward")
    plt.savefig("jpg/mean_reward.jpg")
    plt.show()

def one_game(agent, gamma=0.9):
    env = gym.make(GAME_NAME)
    state = env.reset()

    rewards = 0
    done = False
    rate = 1

    while not done:
        act = agent.act_opt(state)
        state, reward, done, _ = env.step(act)
        if done:
            reward = 2 * reward - 1
        rewards += rate * reward
        rate *= gamma

    return (rewards + 1) / 2


def main():
    env = gym.make(GAME_NAME)
    q_agent = Qlearn()
    q_agent.init(
        env,
        EpsilonGreedy,
        seed = 0,
        prob = 0.1,
    )
    agent = q_agent.learn(episode=1000)
    show_plot(agent.table, 4, 4)
    show_reward(q_agent.log)
    mean = np.mean(q_agent.log)
    std = np.std(q_agent.log)
    print("reward : {:.2f} (+-{:.2f})".format(mean, std))

    reward_log = []
    bar = tqdm(total=100)
    bar.set_description("now game")
    for i in range(100):
        reward_log.append(one_game(agent))
        bar.update(1)
    print("Avarage reward :", np.mean(reward_log))


if __name__ == "__main__":
    main()
