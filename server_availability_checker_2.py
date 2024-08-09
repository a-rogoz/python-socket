import requests
import sys


if len(sys.argv) not in [2, 3]:
    print("Improper number of arguments: at least one is required and not more than two are allowed:")
    exit(code=1)

port_no = 80

if len(sys.argv) == 3:
    try:
        user_port = int(sys.argv[2])
    except Exception as e:
        print("Incorrect port number")
        exit(code=2)

    if user_port >= 1 and user_port <= 65535:
        port_no = user_port
    else:
        print("Incorrect port number")
        exit(code=2)

try:
    if port_no == 80:
        res = requests.head(f"http://{sys.argv[1]}", timeout=5)
    elif port_no == 443:
        res = requests.head(f"https://{sys.argv[1]}", timeout=5)
    else:
        res = requests.head(f"http://{sys.argv[1]}", timeout=5)
except requests.exceptions.Timeout:
    print("Timeout")
    exit(3)
except requests.exceptions.ConnectionError:
    print("Sorry, connection error")
    exit(3)
except requests.exceptions.InvalidURL:
    print("Invalid URL")
    exit(3)
except Exception as e:
    print(f"Something went wrong: {e}")
    exit(3)

if res.status_code == requests.codes.ok:
    print(res.headers)
    print(res.text)
    # print(res.json())
elif res.status_code == requests.codes.moved:
    print("Redirected...")
    print(res.headers)
    exit(4)
elif res.status_code == requests.codes.not_found:
    print("Page Not found")
    exit(4)
else:
    print(f"Something went wrong: {res.status_code}")
    exit(4)