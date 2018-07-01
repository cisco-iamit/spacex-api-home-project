"""
Functionality related to SpaceX API
"""

import requests


def get_launches() -> list:
    """
    Return the list of all past launches.

    :return:
    """
    url = 'https://api.spacexdata.com/v2/launches/'
    response = requests.get(url)
    # status code 200 means everything is ok
    # see https://httpstatuses.com/200
    if response.status_code == 200:
        # JSON is a special format that most APIs use
        return response.json()
    else:
        # print an error message and exit the programme
        print("SpaceX API is unavailable")
        exit()


def recent_launches(n: int = 0,
                    launches: list = None):
    """
    Generator. Returns last n launches.

    :param int n: How many recent launches are required. n >= 0.
    :param list launches: If passed, will reuse the data and not make a REST call.
    :return:
    """

    # if not specified, load launch data from the server
    if launches is None:
        launches = get_launches()

    # count how many launches have taken place
    n_launches = len(launches)

    # if n is too big, start from the first element
    if n > n_launches or n < 0:
        offset = 0
    # otherwise, start from n'th element from the end
    else:
        offset = -n

    for launch in launches[offset:]:
        # 'yield' allows returning List items one by one
        # unlike 'return' which returns the whole thing at once
        # it may be more useful where you are going to read them in that manner
        yield launch
