from dagster import op, job
import subprocess


@op
def scrape_telegram_data():
    print("Running Telegram scraper...")
    subprocess.run(
        ["python", "src/scraper.py"],
        check=True
    )


@op
def load_raw_to_postgres():
    print("Loading raw data into PostgreSQL...")
    subprocess.run(
        ["python", "src/load_to_postgres.py"],
        check=True
    )


@op
def run_dbt_models():
    print("Running dbt transformations...")
    subprocess.run(
        ["dbt", "run"],
        cwd="medical_warehouse",
        check=True
    )


@op
def run_yolo_detection():
    print("Running YOLO object detection...")
    subprocess.run(
        ["python", "src/yolo_detect.py"],
        check=True
    )


@job
def medical_pipeline():

    scrape = scrape_telegram_data()

    load = load_raw_to_postgres()

    dbt = run_dbt_models()

    yolo = run_yolo_detection()

    scrape >> load >> dbt >> yolo
