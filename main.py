import json
from datetime import datetime

import pandas as pd
import routeros_api

__author = "ojpojao <ojpojao@gmail.com>"
__version__ = "0.1.0"

"""
Get all users PPPoE from RouterOS device and export to csv file
"""


def _setup_conn(
    host=None,
    username=None,
    password=None,
    api_port=8728,
):

    api = routeros_api.RouterOsApiPool(
        host=host, username=username, password=password, port=api_port
    )

    return api.get_api()


def _get_resource_get(conn=None, resource=None):

    """Execute get to RouterOS API on context of resource var"""

    r = conn.get_resource(resource)
    return r.get()


def _get_users_pppoe(
    conn=None,
):

    """Return all PPPoE Users on DB"""
    resource = "/ppp/secret"

    return _get_resource_get(conn, resource)


def save_to_csv(dataframe):
    """Save to CSV file"""

    # Get date and time
    now = datetime.now()
    d = now.strftime("%Y-%m-%d-%H%M")

    dataframe.to_csv(
        f"{d}-pppoe_users.csv",
        header=True, index=None,
        encoding="utf-8"
    )


def main():

    # Configure your connection
    setup_conn = _setup_conn(
        host="",
        username="",
        password="",
    )

    r = _get_users_pppoe(setup_conn)
    df = pd.read_json(json.dumps(r))
    save_to_csv(df)


if __name__ == "__main__":
    main()
