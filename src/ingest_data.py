from abc import ABC, abstractmethod

import pandas as pd
from zipfile import ZipFile

class DataIngestion(ABC):
    @abstractmethod
    def ingest(self, file_path: str) -> pd.DataFrame:
        """Abstract method to ingest data from a given file."""
        pass

class ZipFileIngestor(DataIngestion):
    def ingest(self, file_path: str) -> pd.DataFrame:
        """Ingest data from a zip file."""

        #ensure file is a zip file
        if not file_path.endswith('.zip'):
            raise ValueError("File is not a zip file.")
        
        #extract zip file in extracted_data folder
        with ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall('extracted_data')
        