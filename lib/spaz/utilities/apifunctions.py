
import requests
import json
from urllib3.exceptions import InsecureRequestWarning

# suppress verification warnings
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def get_data(url, verify=False):
    """ executes a get request and returns the data object """
    r = requests.get(url, verify=verify)
    return json.loads(r.text)['data']

