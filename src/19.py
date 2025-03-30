import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Example: print the title of a webpage
print(soup.title.string)

# Example: find an element by its tag and text
element = soup.find('h1', {'class': 'example-class'})
if element:
    print(f"The class 'example-class' element has the following text: {element.text}")
else:
    print("No element found with the given class.")
