import os

from sqlalchemy import Table, MetaData


def load_data(session, rows):
    target_table_name = os.getenv('TARGET_TABLE')
    metadata = MetaData()
    target_table = Table(target_table_name, metadata, autoload_with=session.bind)
    # Dynamically insert into the target table
    session.execute(target_table.insert(), rows)

    session.commit()
