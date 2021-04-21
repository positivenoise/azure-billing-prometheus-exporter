from datetime import datetime

import requests


class AzureEA:
    def __init__(self, enrollment_number, access_key):
        self.base_url = (
            f"https://consumption.azure.com/v3/enrollments/{enrollment_number}"
        )
        self.header = {"Authorization": f"Bearer {access_key}"}

    def get_total_usage(self):
        uri = f"{self.base_url}/balancesummary"
        response = requests.get(url=uri, headers=self.header).json()
        return response[0]["totalUsage"]

    def get_period_usage(self, period=None):
        results = []
        if not period:
            period = datetime.now().strftime("%Y%m")
        uri = f"{self.base_url}/billingPeriods/{period}/usagedetails"
        response = requests.get(url=uri, headers=self.header).json()
        print(self._process_period_usage(response))

    def _process_period_usage(self, response):
        results = []
        for entry in response["data"]:
            results.append(
                [
                    entry["serviceName"],
                    entry["subscriptionName"],
                    entry["meterName"],
                    entry["cost"],
                ]
            )
        return results
