__version__ = '0.1'

import PgDumpLoader


def load_database_schema(dump_file_name, ignore_slony_triggers=False):
    PgDumpLoader.load_database_schema(dump_file_name, ignore_slony_triggers)