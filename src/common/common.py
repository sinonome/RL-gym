import numpy as np
from typing import Union


class Qtable:
    def __init__(
        self,
        array: np.ndarray = None
    ):
        """
            initialize

            Parameters
            ----------
                array: np.ndarray
                    q-table
        """
        self.table = array

    def init(
        self,
        array: np.ndarray = None,
        num_of_env: int = None,
        num_of_act: int = None,
    ):
        """
            関数の初期化をする。

            Parameters
            ----------
                array: np.ndarray
                    特定の配列で初期化するときに指定する
                num_of_env: int
                    1以上の整数。0配列による初期化の時に選択
                num_of_act: int
                    1以上の整数。環境の大きさを指定しているのであればこれも指定しないとエラーを吐く
        """
        if array is not None:
            self.table = array

        if num_of_env is None:
            raise Exception("状態がセットされていません")
        if num_of_act is None:
            raise Exception("行動がセットされていません")

        self.table = np.zeros((num_of_env, num_of_act))
        self.islearn = False

    def act_opt(self, state):
        # 最適行動を出力
        return np.argmax(self.table[state])

    # その他
    def __getitem__(self, key):
        return self.table.__getitem__(key)

    def __setitem__(self, key, value):
        return self.table.__setitem__(key, value)

    def __repr__(self):
        return "Qtable" + self.table.__repr__()[5:]

if __name__ == "__main__":
    table = Qtable()
    table.init(num_of_env = 3, num_of_act = 3)
    import pdb; pdb.set_trace()