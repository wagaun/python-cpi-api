import psycopg2

from datetime import datetime
from typing import List


connection_string = "dbname=postgres " \
                    "user=postgres " \
                    "password=postgres " \
                    "host=localhost"


class CpiData:
    def __init__(self, date: datetime, value: float):
        self.date = date
        self.value = value


def find_cpi_data() -> List[CpiData]:
    # Connect to your postgres DB
    conn = psycopg2.connect(connection_string)
    cur = conn.cursor()
    cur.execute(
        query="SELECT ref_date, index_value "
              "FROM public.cpi_series "
              "ORDER BY ref_date")
    output = [CpiData(date=row[0], value=row[1]) for row in cur.fetchall()]
    cur.close()
    conn.close()
    return output


def create_cpi_data(dt: datetime, value: float) -> None:
    # Connect to your postgres DB
    conn = psycopg2.connect(connection_string)
    cur = conn.cursor()
    # This is not subject to sql injection
    cur.execute(
        query="INSERT INTO public.cpi_series(ref_date, index_value) "
              "VALUES (%s, %s)",
        vars=(dt, value))
    conn.commit()
    cur.close()
    conn.close()
