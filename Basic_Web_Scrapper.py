import requests
from bs4 import BeautifulSoup

print("===================================")
print("         BASIC WEB SCRAPER        ")
print("===================================")

# Website URL
url = "https://news.ycombinator.com/"

try:

    # Send GET request
    response = requests.get(url)

    # Check request status
    response.raise_for_status()

    # Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find headlines
    headlines = soup.find_all("span", class_="titleline")

    print("\n📰 Latest News Headlines:\n")

    # Display headlines
    for index, headline in enumerate(headlines[:10], start=1):

        title = headline.get_text()

        print(f"{index}. {title}")

except requests.exceptions.RequestException as e:
    print("❌ Error while accessing website:")
    print(e)

except Exception as e:
    print("❌ An unexpected error occurred:")
    print(e)

finally:
    print("\nProgram execution completed.")