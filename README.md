# Ubuntu_Requests

✨ Features

📥 Fetch images from the web using URLs

📂 Automatically saves images in a Fetched_Images directory

🛡️ Handles errors gracefully (bad links, timeouts, invalid images)

🔄 Supports multiple URLs at once

🚫 Prevents duplicate downloads

🧾 Generates safe filenames if not provided by the URL

✅ Checks content type to confirm it’s an image

🛠 Installation

Clone this repository:

git clone https://github.com/your-username/Ubuntu_Requests.git
cd Ubuntu_Requests


Install dependencies:

pip install requests

▶️ Usage

Run the program:

python ubuntu_fetcher.py


Example interaction:

🌍 Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter image URL(s) (separated by spaces): https://example.com/pic1.jpg https://example.com/pic2.png

✓ Successfully fetched: pic1.jpg
✓ Image saved to Fetched_Images/pic1.jpg
⚠ Image already exists: pic2.png

Connection strengthened. Community enriched. ✨

🔒 Precautions Implemented

Timeout to avoid hanging requests

Skips non-image responses by checking Content-Type headers

Prevents duplicate image downloads

Graceful error handling with clear feedback

🌐 Ubuntu Principles in Action

Community → Connects to the global internet to fetch shared resources

Respect → Handles errors gracefully, without crashing

Sharing → Organizes collected images for reuse

Practicality → Simple, real-world tool that solves a useful problem

📌 Requirements

Python 3.7+

requests library
