import requests

def brute_force_directories(target_url, wordlist_file):
    try:
        with open(wordlist_file, 'r') as file:
            directories = file.read().splitlines()

        print(f"Starting directory brute force on: {target_url}")

        for directory in directories:
            url = f"{target_url}/{directory}"
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Found directory: {url}")
            else:
                print(f"Failed directory: {url} (Status code: {response.status_code})")

    except FileNotFoundError:
        print(f"Wordlist file not found: {wordlist_file}")
    except requests.RequestException as e:
        print(f"Request error: {e}")

if __name__ == "__main__":
    target_url = input("Enter the target URL (e.g., http://example.com): ").strip()
    wordlist_file = input("Enter the path to the wordlist file: ").strip()
    brute_force_directories(target_url, wordlist_file)
