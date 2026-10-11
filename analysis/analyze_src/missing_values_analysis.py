from abc import ABC, abstractmethod

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class MissingValuesAnalysisTemplate(ABC):
    def analyze(self, data: pd.DataFrame):
        pass

    @abstractmethod
    def identify_missing_values(self, data: pd.DataFrame) -> pd.DataFrame:
        pass

    @abstractmethod
    def visualize_missing_values(self, data: pd.DataFrame):
        pass


class SimpleMissingValuesAnalysis(MissingValuesAnalysisTemplate):
    def identify_missing_values(self, data: pd.DataFrame) -> pd.DataFrame:
        """Identify missing values in the DataFrame and return their counts."""
        missing_values = data.isnull().sum()
        return missing_values[missing_values > 0]

    def visualize_missing_values(self, data: pd.DataFrame):
        """Visualize missing values using a heatmap."""
        plt.figure(figsize=(20, 12))
        sns.heatmap(data.isnull(), cbar=False, cmap='viridis')
        plt.title('Missing Values Heatmap')
        plt.show()

    def analyze(self, data: pd.DataFrame):
        missing_values = self.identify_missing_values(data)
        print("Missing Values Count:\n", missing_values)
        self.visualize_missing_values(data)