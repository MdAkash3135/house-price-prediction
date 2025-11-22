from abc import ABC, abstractmethod
import pandas as pd

class BasicDataInspectionInterface(ABC):
    @abstractmethod
    def inspect(self, data: pd.DataFrame) -> pd.DataFrame:
        pass

class InfoInspector(BasicDataInspectionInterface):
    def inspect(self, data: pd.DataFrame) -> pd.DataFrame:
        """Inspect the DataFrame and return its info as a DataFrame."""
        data.info()
        return data

class SummaryInspector(BasicDataInspectionInterface):
    def inspect(self, data: pd.DataFrame) -> pd.DataFrame:
        """Return the summary statistics of the DataFrame."""
        return data.describe()

class NullInspector(BasicDataInspectionInterface):
    def inspect(self, data: pd.DataFrame) -> pd.DataFrame:
        """Return the count of null values in each column of the DataFrame."""
        return data.isnull().sum()



class DataInspection:
    def __init__(self):
        pass

    def set_strategy(self, strategy: BasicDataInspectionInterface):
        self.strategy = strategy

    def inspect(self, data: pd.DataFrame) -> pd.DataFrame:
        return self.strategy.inspect(data)