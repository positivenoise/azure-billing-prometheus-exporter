import time

from azure_ea import AzureEA
from config import *
from prometheus_client import Gauge, start_http_server

if __name__ == "__main__":
    start_http_server(8000)
    g = Gauge(
        "total_usage",
        "Azure EA total costs for month",
        ["serviceName", "subscriptionName", "meterName"],
    )
    azure_ea = AzureEA(
        enrollment_number=ENROLLMENT_NUMBER,
        access_key=ACCESS_KEY,
    )
    while True:
        groups = azure_ea.get_period_usage()
        for labels, values in groups.iterrows():
            g.labels(
                serviceName=labels[0],
                subscriptionName=labels[1],
                meterName=labels[2],
            ).set(values.cost)
        time.sleep(300)
