

# Building a webscraper to go fetch data from a website that contains the price difference between cost of commodities in two different places
import requests
from bs4 import BeautifulSoup
url = 'https://www.numbeo.com/cost-of-living/compare_cities.jsp?country1=Nepal&country2=United+States&city1=Kathmandu&city2=Lynchburg%2C+VA'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

# Extracting only the required information from the soup
difference = soup.find_all(style="vertical-align : middle; text-align: right")
difference_list = []
for item in difference:
    difference_list.append(item.text.strip().rstrip("%"))
  
# Formatting the list properly to allow for arithmetic operations.
diff_list = [i.replace(",", "") for i in difference_list]
d_list = [float(x) for x in diff_list if x]

# Work in progress
