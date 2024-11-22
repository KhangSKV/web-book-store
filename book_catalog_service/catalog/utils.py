import requests

USER_SERVICE_URL = "http://user-management-service-url/api/users/"

def get_user_details(user_id):
    try:
        response = requests.get(f"{USER_SERVICE_URL}{user_id}/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
