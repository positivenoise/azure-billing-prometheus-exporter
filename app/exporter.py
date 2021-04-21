import time

from azure_ea import AzureEA
from config import *
from prometheus_client import Gauge, start_http_server

if __name__ == "__main__":
    start_http_server(8000)
    g = Gauge("total_usage", "Azure EA total costs for month")
    azure_ea = AzureEA(
        enrollment_number=ENROLLMENT_NUMBER,
        access_key=ACCESS_KEY,
    )
    while True:
        # g.set(azure_ea.get_total_usage())
        print(azure_ea.get_period_usage())
        time.sleep(60)
