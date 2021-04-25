from datetime import datetime

import requests
from pandas import DataFrame


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

        if not period:
            period = datetime.now().strftime("%Y%m")
        uri = f"{self.base_url}/billingPeriods/{period}/usagedetails"
        response = requests.get(url=uri, headers=self.header).json()
        df = DataFrame(response["data"])

        while response["nextLink"] is not None:
            response = requests.get(
                url=response["nextLink"], headers=self.header
            ).json()
            df = df.append(response["data"], ignore_index=True)

        df = df.reindex(
            ["serviceName", "subscriptionName", "meterName", "cost"], axis=1
        )

        groups = df.groupby(["serviceName", "subscriptionName", "meterName"]).sum()

        return groups
