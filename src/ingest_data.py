from abc import ABC, abstractmethod

import pandas as pd
from zipfile import ZipFile

import os

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

        extracted_files = os.listdir('extracted_data')
        csv_files = [file for file in extracted_files if file.endswith('.csv')]

        if len(csv_files) == 0:
            raise FileNotFoundError("No csv files found in the extracted data.")
        
        if len(csv_files) > 1:
            raise ValueError("Multiple csv files found in the extracted data. Mention which one have to use")
        
        csv_file = csv_files[0]     
        df = pd.read_csv(f'extracted_data/{csv_file}')
        return df


class DataIngestorFactory:
    @staticmethod
    def get_ingestor(file_type: str) -> DataIngestion:
        """Factory method to get the appropriate data ingestor based on file type."""
        if file_type == 'zip':
            return ZipFileIngestor()
        else:
            raise ValueError(f"Unsupported file type: {file_type}")

if __name__ == '__main__':
    # DataIngestorFactory.get_ingestor('zip').ingest('Data/archive.zip')    
    pass