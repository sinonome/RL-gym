import numpy as np

class Qtable:
    def __init__(
        self,
        num_of_env: int,
        num_of_act: int,
    ):
        """
            initialize

            Parameters
            ----------
                num_of_env: int
                    number of state
                num_of_act: int
                    number of action
        """
        self.noe = num_of_env
        self.noa = num_of_act
        self.table = None
        self.islearn = None

    def init(self):
        """
            学習をするときの初期化

            Parameters
            ----------
                None

            Return
            ------
                None1
        """
        self.table = np.zeros((self.noe, self.noa))
        self.islearn = False
    
    def finish_learn(self):
        if self.islearn is None:
            raise Exception("学習がはじまっていません。")
        elif self.islearn:
            raise Exception("既に学習が終了している関数です。")

        # 何かしらの設定
        self.islearn = True
    
    def act_opt(self, state):
        return np.argmax(self.table[state])

