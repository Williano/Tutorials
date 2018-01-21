from bs4 import BeautifulSoup
import requests


with open('simple.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# Prints the whole html file.
print(soup.prettify())

# Prints a blank space.
print()
print()

# Prints the title of the html file.
match = soup.title.text
print(match)

# Prints a blank space.
print()
print()

# Prints the element with class footer of the html file.
match = soup.find('div', class_='footer')
print(match)

# Prints a blank space.
print()
print()

# Prints the element with class article of the html file.
article = soup.find('div', class_='article')
print(article)

# Prints a blank space.
print()
print()

# Prints the sub text of the class article elment of the html file.
headline = article.h2.a.text
print(headline)


# Prints a blank space.
print()
print()

# Prints the sub text of the class article elment of the html file.
summary = article.p.text
print(summary)

# Prints a blank space.
print()
print()

# Prints all elements with class article of the html file.
for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()





