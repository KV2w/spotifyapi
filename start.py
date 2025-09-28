import requests

#Authenticate
client_id = ""
client_secret = ""

url = "https://accounts.spotify.com/api/token"

payload = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret
}

headers ={
    "Content-Type": "JAYR/x-www-form-urlencoded"
}

try:
    response = requests.post(url, data=payload, headers=headers)
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

    token_data = response.json()
    print("Access token retrieved successfully.")
    print("Token:", token_data["access_token"])
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")


# site = requests.get("https://api.spotify.com")

# data = site.json()
# print(data)