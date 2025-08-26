import os
import duckdb


def _load_httpfs_ext():
    try:
        duckdb.sql("INSTALL httpfs")
        duckdb.sql("LOAD httpfs")
    except Exception as e:
        print(f"[duckdb_sql] Warning: failed to install httpfs extension: {e}")


def _get_conn():
    conn = duckdb.connect()
    key_id = os.environ.get("GCS_KEY_ID")
    secret = os.environ.get("GCS_SECRET")
    if key_id and secret:
      conn.execute(f"CREATE OR REPLACE PERSISTENT SECRET (TYPE gcs, KEY_ID '{key_id}', SECRET '{secret}')")
    return conn


def load_ipython_extension(ipython):
    _load_httpfs_ext()
    conn = _get_conn()
    ipython.push({'conn': conn})
    ipython.run_line_magic("load_ext", "sql")
    ipython.run_line_magic("sql", "conn --alias duckdb")
    ipython.run_line_magic("sql", "LOAD httpfs;")
    ipython.run_line_magic("config", "SqlMagic.autopandas = True")
    ipython.run_line_magic("config", "SqlMagic.feedback = False")
    ipython.run_line_magic("config", "SqlMagic.displaycon = False")
