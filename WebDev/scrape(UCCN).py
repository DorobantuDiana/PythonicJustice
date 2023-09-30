from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://en.unesco.org/creative-cities').text

soup = BeautifulSoup(html_text, 'lxml')

contents = soup.find_all('div', class_='row-content')
for content in contents:
        city = content.find('h4', class_='title')
        category = content.find('div', class_='category')
        print(f''' 
            City Name: {city.text}
            Category Name: {category.text}
        ''')

# descriptions = soup.find_all('div', class_='field-item even')

# for description in descriptions:
#     text = description.find_all('p')
#     for p in text:
#         print(p.text)