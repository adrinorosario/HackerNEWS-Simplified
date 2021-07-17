###### Note:- I will review the pull requests. Once i fully review them, i will merge within the upcoming 5 days. Thank you all for your contributions :)

# HackerNEWS-Simplified

A more simplified and straightforward version of HackerNews. The project uses BeautifulSoup, a python web scraping framework to scrape the data from the hackernews website and take ony the most relevant news and displays it on your terminal. 

The Hackernews page has many stories, articles and news that are not that relevant and useful to the community. The page isn't arranged properly to put forward the stories that have the most votes or approval.

##### The news displayed on your terminal(after you run ``hackernews.py``) is sorted by the number of votes of that specific news/article on the site. Only the news having 127 or more votes are displayed systematically on your terminal. The stories are scrapped and collected from the first 2 pages of Hacker News.

##### Clone the repo and open the Terminal/CLI in the folder containing ``hackernews.py``. Into the terminal, type in: ``python3 hackernews.py``

The project code(``hackernews.py``) has been/ is filled with useful comments that can be used to assert the process of grabbing data from the web page.

In order to understand the flow of control and how the Script operates, you can refer to ``hackernews(py).md`` to understand the working of the Script and ``BeautifulSoup.md`` for information on what features/components of the framework are used in the scripts.

## A Glimpse into the program in action
![capture](https://user-images.githubusercontent.com/83050257/125961036-c2812364-4fac-4066-b44f-8d3c3d43f61c.gif)

## Requirements

autopep8==1.5.6 or above

beautifulsoup4==4.9.3 or above

pycodestyle==2.7.0 or above

pylint==2.8.2 or above

requests==2.25.1 or above

soupsieve==2.2.1 or above

pprint

### Installation 

You can either clone or fork this repo onto your device. Then again, make sure all the files are in a single directory/folder(just for safekeeping).

### Usage

After installation, open your Terminal/CLI in the directory/folder containing the script. Type in or copy/paste the following command: ```python3 hackernews.py```.

Then again, the output will have the stories with the most votes(>=127). When you check them on the hackernews page, they won't be at the top and you'll have to scroll down or sometimes, navigate to the 2nd page to find them.

## Support

Useful links:

https://news.ycombinator.com/ - Hacker News

https://www.excellarate.com/blogs/web-scraping-introduction-applications-and-best-practices/#:~:text=Web%20scraping%20typically%20extracts%20large,show%20data%20from%20a%20website. - Introduction to Web Scraping and best practices

https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors - CSS Selectors

https://pypi.org/project/beautifulsoup4/ - BeautifulSoup Docs.

## License 

MIT License 
