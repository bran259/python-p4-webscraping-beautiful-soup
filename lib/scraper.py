from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)

# Create Beautiful Soup object
doc = BeautifulSoup(html.text, 'html.parser')

# Extract main heading
heading = doc.select('.heading-financier')
if heading:
    print(heading[0].contents[0].strip())

# Extract course information
courses_html = requests.get("https://flatironschool.com/our-courses/", headers=headers)
courses_doc = BeautifulSoup(courses_html.text, 'html.parser')

courses = courses_doc.select('.heading-60-black.color-black.mb-20')
for course in courses:
    print(course.contents[0].strip())
