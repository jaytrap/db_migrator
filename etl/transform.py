import os

# Parse the column mappings from the environment
def get_column_mappings():
    mappings = os.getenv('COLUMN_MAPPINGS').split(',')
    mapping_dict = {}
    for mapping in mappings:
        source_col, target_col = mapping.split('=')
        mapping_dict[source_col] = target_col
    return mapping_dict

def transform_data(row, column_mappings):
    transformed_row = {}
    for source_col, target_col in column_mappings.items():
        # Map source column data to target column name
        transformed_row[target_col] = row[source_col]
    return transformed_row
