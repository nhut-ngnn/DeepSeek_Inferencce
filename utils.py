import requests

def check_vllm_status(url: str = "http://localhost:8000/health") -> bool:
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False