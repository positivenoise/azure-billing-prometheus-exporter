import datetime
import time

import requests
from config import *
from prometheus_client import Gauge, start_http_server

# Azure EA access details
g = Gauge("things", "stuff and things")
header = {"Authorization": f"Bearer {ACCESS_KEY}"}


def get_total_usage():
    uri = f"https://consumption.azure.com/v3/enrollments/{ENROLLMENT_NUMBER}/balancesummary"
    response = requests.get(url=uri, headers=header).json()
    g.set(response[0]["totalUsage"])


if __name__ == "__main__":
    start_http_server(8000)

    while True:
        get_total_usage()
        time.sleep(60)
