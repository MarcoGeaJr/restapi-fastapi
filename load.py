import csv
import datetime

import Models
from Database import SessionLocal, engine

db = SessionLocal()

Models.Base.metadata.create_all(bind=engine)

with open("sars_2003_complete_dataset_clean.csv", "r") as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        db_record = Models.Record(
            date=datetime.datetime.strptime(row["date"], "%Y-%m-%d"),
            country=row["country"],
            cases=int(row["cases"]),
            deaths=int(row["deaths"]),
            recoveries=int(row["recoveries"])
        )
        db.add(db_record)

    db.commit()

db.close()
