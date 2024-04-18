"""Saves the wildfires dataset as a CSV."""

import sqlite3
import pandas as pd

def save_csv() -> None:
    cnx = sqlite3.connect('data/FPA_FOD_20170508.sqlite')
    sql = "select * from fires"
    df = pd.read_sql_query(sql, cnx)
    df.to_csv("data/wildfires.csv", index=False)
    df.head(10000).to_csv("data/wildfires_lite.csv", index=False)


if __name__ == "__main__":
    save_csv()