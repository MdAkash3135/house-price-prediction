from src.ingest_data import DataIngestorFactory
import pandas as pd
from zenml import step

@step
def data_ingestion_step(file_path: str) -> pd.DataFrame:
    """Step to ingest data from a given file path."""
    # Determine file type based on file extension
    if file_path.endswith('.zip'):
        file_type = 'zip'
    else:
        raise ValueError("Unsupported file type. Only zip files are supported.")
    
    # Get the appropriate ingestor using the factory
    ingestor = DataIngestorFactory.get_ingestor(file_type)
    
    # Ingest the data and return as DataFrame
    df = ingestor.ingest(file_path)
    return df