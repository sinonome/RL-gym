import numpy as np

class EpsilonGreedy:
    def __init__(self, num_of_act, epsilon=0.1, seed=0):
        """
            Parameters
            ----------
                num_of_act: int
                    number of actions
                
                epsilon: float
                    ランダム行動の確率
                
                seed: int
                    乱数のシード
        """
        self.num_of_act = num_of_act
        self.random = np.random.RandomState(seed)
        self.epsilon = epsilon

    def action(self, state, q_table):
        if self.random.random() >= self.epsilon:
            return q_table.act_opt(state)
        else:
            return self.random.randint(0, self.num_of_act)