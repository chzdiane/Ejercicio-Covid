from abc import ABC, abstractmethod

class Plotter(ABC):
    @abstractmethod
    def plot_data(self, data):
        pass