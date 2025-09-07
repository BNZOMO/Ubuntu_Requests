import requests
import os
from urllib.parse import urlparse
import hashlib

def fetch_image(url):
    """
    Fetches an image from the given URL and saves it into the Fetched_Images directory.
    Returns the filename if successful, or None if an error occurred.
    """

    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)

        # Fetch the image
        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()  # Raises an HTTPError for bad status codes

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename, generate one using a hash
        if not filename:
            filename = f"image_{hashlib.md5(url.encode()).hexdigest()[:8]}.jpg"

        filepath = os.path.join("Fetched_Images", filename)

        # Prevent duplicate downloads
        if os.path.exists(filepath):
            print(f"⚠ Image already exists: {filename}")
            return None

        # Save the image in binary mode
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        return filename

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

    return None


def main():
    print("🌍 Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Allow multiple URLs separated by spaces
    urls = input("Please enter image URL(s) (separated by spaces): ").split()

    for url in urls:
        fetch_image(url)

    print("\nConnection strengthened. Community enriched. ✨")


if __name__ == "__main__":
    main()
