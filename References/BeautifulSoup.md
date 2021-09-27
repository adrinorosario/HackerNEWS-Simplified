# BEAUTIFUL SOUP
We will use beautifulsoup to clean the data we have grabbed `res`, `res.text`. We want to remove all the information we don't need, such as stories that have less than <X> points.[here, less than 127]

## BASICS

1. BeautifulSoup(res.text, 'html.parser')
   * Creates a soup object
   * html.parser converts it from a string to something that we can use [here, we want to convertb it to an HTML that we can use].
   * We need to do `html.parser` bcoz BeautifulSoup also parses XML.

2. OF THE HTML FILE
   * print(soup_obj)
   * print(soup_obj.body)
   * print(soup_obj.body.contents)
   * print(soup_obj.find_all('div'))

   * print(soup_obj.find_all('a')) >------------------------------------------------->> prints all links of the site

   * print(soup_obj.title)
   * print(soup_obj.a) >---------------------------->> prints first <a> tag the interpreter gets to

   * print(find('a')) >------------------------------------->> prints first <a> tag encountered by interpreter

   * print(soup_obj.find(id="score_27708411")) >------------------->> prints the exact score

## BEAUTIFULSOUP- Selectors

print(soup_obj.select())
.select allows us to grab a peice of data from the soup that we downloaded and created using a CSS Selector.
