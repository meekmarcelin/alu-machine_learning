def get_user_location(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        user_data = response.json()
        if 'location' in user_data:
            return user_data['location']
        else:
            return "Location not available"
    elif response.status_code == 404:
        return "Not found"
    elif response.status_code == 403:
        reset_time = int(response.headers['X-Ratelimit-Reset'])
        current_time = time.time()
        reset_in_seconds = reset_time - current_time
        reset_in_minutes = int(reset_in_seconds / 60)
        return f"Reset in {reset_in_minutes} min"
    else:
        return "Unexpected error"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 2-user_location.py <API_URL>")
        sys.exit(1)

    api_url = sys.argv[1]
    location = get_user_location(api_url)
    print(location)
