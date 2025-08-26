import os
import duckdb


def _configure_duckdb():
    try:
        duckdb.sql("INSTALL httpfs")
        duckdb.sql("LOAD httpfs")
    except Exception as e:
        print(f"[duckdb_sql] Warning: failed to install httpfs extension: {e}")

    key_id = os.environ.get("GCS_KEY_ID")
    secret = os.environ.get("GCS_SECRET")
    if key_id and secret:
        try:
            duckdb.sql(f"CREATE OR REPLACE PERSISTENT SECRET (TYPE gcs, KEY_ID '{key_id}', SECRET '{secret}')")
        except Exception as e:
            print(f"[duckdb_sql] Warning: failed to create GCS secret: {e}")


def load_ipython_extension(ipython):
    _configure_duckdb()
    ipython.run_line_magic("load_ext", "sql")
    ipython.run_line_magic("sql", "conn --alias duckdb")
    ipython.run_line_magic("sql", "LOAD httpfs;")
    ipython.run_line_magic("config", "SqlMagic.autopandas = True")
    ipython.run_line_magic("config", "SqlMagic.feedback = False")
    ipython.run_line_magic("config", "SqlMagic.displaycon = False")
