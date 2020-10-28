import matplotlib.pyplot as plt
import numpy as np

"""
    TODO:
        エージェントの作成

        1. Q-table の作成
        2. learn関数の作成
            1. 環境をリセットしたり、Agent の状態をリセットする init 関数を定義
            2. Q-table を設定する関数 setQtable を定義
            3. 行動を決める action 関数 の定義
            4. 行動を実際に起こす move 関数を定義
            5. 学習状況をリアルタイムで表示する何かを作成する
                - idea
                    * 状態を matplotlib などを用いて表示
                    * 報酬の log 配列を作成
"""


"""
    TODO:
"""
class Qtable:
    def __init__(
        self,
        states: list,
        actions: list,
    ):
        """
            Parameters
            ----------
            states : list
                環境全体

            actions : list
                行動全体

            Returns
            -------
            None
        """
        pass


class Agent:
    def __init__(self):
        self.env = None
        self.Qtable = None
        self.istrain = False

    def learn(
        self,
        env,
        episode = 1000,
        gamma = .9
    ):
        """
            Agent の学習を行う

            Parameters
            ----------
            env :
                環境
            episode :
                エピソード数
            gamma : float
                0以上1以下

            Returns
            -------
            self :
                インスタンスを返す
        """
        return self


