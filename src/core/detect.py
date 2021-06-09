from rich import print

from requests import get, exceptions

from urllib3 import disable_warnings
disable_warnings()

from src.core.manager import props
from src.core.info import *


def connect(args) -> None:

    url = args.u

    try:
        response = get(args.u, **props)
        status_code = response.status_code
        headers = response.headers

        verify = lambda success = 200: status_code == success
        (detect_magento(url, headers)) if verify() else (print(f"[red][ERR] Connection problems with {url} | {status_code} [/]"))

    except exceptions.ConnectionError as e:
        return print(f"[red][ERR] Connection problems with {url} | {e} [/]")
    
    except exceptions.MissingSchema:
        return print(f"[red][ERR] Invalid URL, did you mean https://{url}?")


def detect_magento(url, headers) -> str:

    cookie_header = 'X-Magento-Vary'
    tags_header = 'X-Magento-Tags'

    print(f"[green][INF] Connected successfully with [b]{url}[/] [/]\n")

    check_headers = lambda cookie = cookie_header, tag = tags_header : cookie or tag in headers
    (print(header_magento_detected), get_version(url)) if check_headers() else (print(not_detected))
    

def get_version(url) -> str:

    print(get_magento_version)

    path = f'{url}/magento_version'

    try:
        response = get(path, **props)
        status_code = response.status_code
        body = response.text

        verify = lambda success = 200, content = 'Magento/': status_code == success and content in body
        (print(f'[green][INF] Magento Version: {body}')) if verify() else (print(version_not_detect))

    except exceptions.ConnectionError as e:
        return print(f"[red][ERR] Connection problems with {url} | {e} [/]")