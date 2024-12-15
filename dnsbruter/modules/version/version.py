import requests

def version():
    url = f"https://api.github.com/repos/sanjai-AK47/Dnsbruter/releases/latest"
    try:
        response = requests.get(url, verify=True, timeout=10)
        if response.status_code == 200:
            data = response.json()
            latest = data.get('tag_name')
            return latest
    except KeyboardInterrupt as e:
        exit(1)
    except Exception as e:
        pass