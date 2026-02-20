from abc import ABC

class ITreeNode(ABC):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value