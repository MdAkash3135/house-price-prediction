from abc import ABC, abstractmethod

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data):
        pass

class DataAnalyzer(ABC):
    @abstractmethod
    def analyze(self, data):
        pass

class DataVisualizer(ABC):
    @abstractmethod
    def visualize(self, data):
        pass

ob1 = DataProcessor()
ob2 = DataAnalyzer()
ob3 = DataVisualizer()