import numpy as np

class Policy:
    def _action(self, state):
        raise Exception("行動が定義されていません")

    def __call__(self, state):
        return self._action(state)


class QAgent(Policy):
    def __init__(
        self,
        Qtable,
        isDecision = True
    ):
        """
            Parameter
            ---------
                Qtable: Qtable
                    Q-table 関数
                isDecision: True
                    決定的に行動するか非決定的に行動するか（非決定的の場合は未実装）
        """
        self.table = Qtable
        self.isDecision = isDecision

    def _action(self, state):
        return self.table.act_opt(state)
