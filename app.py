# app.py
import os
from dotenv import load_dotenv
from utils.db import get_db_engine, get_db_session
from etl.etl_process import run_etl

# Load environment variables from .env file
load_dotenv()

if __name__ == "__main__":
    # Setup database connections
    source_engine = get_db_engine(os.getenv('DB_SOURCE_URI'))
    target_engine = get_db_engine(os.getenv('DB_TARGET_URI'))

    source_session = get_db_session(source_engine)
    target_session = get_db_session(target_engine)

    chunk_size = int(os.getenv('CHUNK_SIZE'))

    # Run the ETL process
    run_etl(source_session, target_session, chunk_size)
