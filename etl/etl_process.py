from etl.extract import extract_data
from etl.transform import transform_data, get_column_mappings
from etl.load import load_data

def run_etl(source_session, target_session, chunk_size):
    column_mappings = get_column_mappings()

    for data_chunk in extract_data(source_session, chunk_size):
        transformed_data = [transform_data(row, column_mappings) for row in data_chunk]
        load_data(target_session, transformed_data)
