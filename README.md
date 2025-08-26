# DuckDB SQL IPython Extension

Loads JupySQL extension with DuckDB setup (incl. GCS auth).

## Setup

Use in a notebook as follows:

1. Install via pip if not yet installed:
    ```
    pip install git+https://github.com/grobgl/duckdb-sql-ipython-ext
    ```
2. (optional) Prepare GCS credentials:

    1. [Create HMAC keys](https://console.cloud.google.com/storage/settings;tab=interoperability) and store them as `GCS_KEY_ID` and `GCS_SECRET` environment variables.
    2. If using a `.env` file, these may have to be loaded into a notebook using [`python-dotenv`](https://github.com/theskumar/python-dotenv):
        ```
        %load_ext dotenv
        %dotenv /home/serenitydev/.env
        ```
3. Load extension:
    ```
    %load_ext duckdb_sql
    ```

## Usage

See [JupySQL](https://jupysql.ploomber.io/).
```
%sql select * from 'gs://example-bucket/**/*-example.parquet' limit 10;
```

Multi line:
```
%%sql
select *
from 'gs://example-bucket/**/*-example.parquet'
limit 10
```

Store result to variable:
```
%%sql example_df <<
select * from 'gs://example-bucket/**/*-example.parquet' limit 10;
```