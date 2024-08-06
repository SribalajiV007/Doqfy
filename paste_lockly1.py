import requests

def create_snippet(text, api_key):
    url = "https://api.paste.ee/v1/pastes"
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": api_key
    }
    payload = {
        "description": "PasteLockly Snippet",
        "sections": [
            {
                "name": "Section",
                "syntax": "text",
                "contents": text
            }
        ]
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        return response.json()["link"]
    else:
        print(f"Failed to create snippet: {response.text}")
        return None

def shorten_url(url):
    response = requests.get(f"https://tinyurl.com/api-create.php?url={url}")
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to shorten URL: {response.text}")
        return None

def main():
    api_key = "aQeVZT1ar2putn0gawImTVYnpRMOWiflEaYoPvQXb"  # Replace with your Paste.ee API key
    text = input("Enter your text snippet: ")

    snippet_url = create_snippet(text, api_key)
    if snippet_url:
        print(f"Snippet URL: {snippet_url}")

        short_url = shorten_url(snippet_url)
        if short_url:
            print(f"Shortened URL: {short_url}")

if __name__ == "__main__":
    main()
