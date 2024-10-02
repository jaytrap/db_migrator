import os
from sqlalchemy import text

def extract_data(session, chunk_size):
    source_table = os.getenv('SOURCE_TABLE')
    query = f"SELECT * FROM {source_table}"

    offset = 0
    while True:
        data = session.execute(text(f"{query} LIMIT {chunk_size} OFFSET {offset}")).mappings()
        rows = list(data)
        if not rows:
            break
        yield rows
        offset += chunk_size