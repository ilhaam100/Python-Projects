'''Creating a URL shortener using TinyURL'''

import pyshorteners

# Create a Shortener object
shortener = pyshorteners.Shortener()

# Ask the user to input a URL
url = input("Enter a URL to shorten: ")

# Shorten the URL using the Shortener object
short_url = shortener.tinyurl.short(url)

# Print the shortened URL
print(f"Shortened URL: {short_url}")
