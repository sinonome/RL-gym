import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

import sys; sys.path.append('..')
from common.common import Qtable, Alpha
from common.policy import EpsilonGreedy
from common.agent  import QAgent


class Qlearn:
    def __init__(self):
        self.env = None
        self.table = Qtable()
        self.isInit = False

    def init(
        self,
        env,
        policy,
        seed = 0,
        prob = 0.1,
        array = None
    ):
        """
            Parameter
            ---------
                env:
                    環境
                policy:
                    学習するための行動規則(epsilon greedy のみに対応？)
                seed:
                    シード値
                prob:
                    ランダム行動する確率
                array:
                    Q-table を初期化するときに使う。指定しなければ0配列で初期化
        """
        self.env = env
        self.states  = self.env.observation_space.n
        self.actions = self.env.action_space.n
        if array is not None:
            self.table.init(array)
        else:
            self.table.init(num_of_env=self.states, num_of_act=self.actions)

        self.alpha  = Alpha(self.states)
        self.policy = policy(self.actions, prob, seed)
        self.isInit = True

    def learn(
        self,
        episode = 1000,
        max_iter = 10000,
        gamma = .9,
    ):
        """
            Agent の学習を行う

            Parameters
            ----------
            episode: int
                エピソード数
            max_iter: int
                一回のゲームにおける行動回数の上限
            gamma: float
                0以上1以下

            Returns
            -------
            self:
                インスタンスを返す
        """
        if not self.isInit:
            raise Exception("初期化されていません")

        self.log = []
        bar = tqdm(total = episode)
        for i in range(1, episode + 1):
            state = self.env.reset()
            done = False
            rewards = 0
            turn = 0
            rate = 1

            while not done and turn < max_iter:
                action = self.policy.action(state, self.table)
                next_state, reward, done, _ = self.env.step(action)
                if done:
                    reward = 2 * reward - 1
                rewards += rate * reward
                rate *= gamma
                delta = reward \
                            + gamma * np.max(self.table[next_state]) \
                            - self.table[state, action]
                self.table[state, action] += self.alpha[state] * delta
                state = next_state
                turn += 1

            self.log.append(rewards)
            bar.set_description("reward : {:1.2f} ".format(np.mean(self.log)))
            bar.update(1)

        self.env.close()
        return Qtable(self.table)
