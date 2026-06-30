# Data Warehouse

## Staging Models

- stg_telegram_messages

## Dimension Tables

- dim_channels
- dim_dates

## Fact Table

- fct_messages

## Tests

- unique message_id
- not null message_id
- positive views
## Dagster Pipeline

The project uses Dagster to orchestrate the ELT workflow.

Pipeline steps:

1. Scrape Telegram data
2. Load raw JSON into PostgreSQL
3. Execute dbt transformations
4. Run YOLO object detection

Run the pipeline with:

```bash
dagster dev -f pipeline.py
```
