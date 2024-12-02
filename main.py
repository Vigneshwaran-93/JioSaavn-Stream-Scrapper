import requests
from bs4 import BeautifulSoup
import re

# Function to get the track stream count
def get_stream_count(track_url):
    # Send a GET request to the track page
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(track_url, headers=headers)
    
    # Check if request is successful
    if response.status_code == 200:
        # Parse the content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the <p> tag with the specific class
        play_count_tag = soup.find('p', class_='u-centi u-deci@lg u-color-js-gray u-ellipsis@lg u-margin-bottom-tiny@sm')
        
        if play_count_tag:
            # Extract the text within the <p> tag, which contains the play count
            play_count_text = play_count_tag.text.strip()
            
            # Use regular expression to extract the number before the word 'Play'
            play_count_match = re.search(r'(\d{1,3}(?:,\d{3})*)\s*Play', play_count_text)
            
            if play_count_match:
                # Extract and return the formatted number
                stream_count = play_count_match.group(1)
                return stream_count
            else:
                return "Stream count not found."
        else:
            return "Play count element not found."
    else:
        return "Failed to fetch the page."

# Example usage
track_url = 'https://www.jiosaavn.com/song/song_url'  # Replace with the actual track URL
stream_count = get_stream_count(track_url)
print(f"Stream count: {stream_count}")
