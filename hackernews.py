# A MORE NICER VERSION OF HACKER NEWS

import requests
# requests allows us to download the initial HTML
from bs4 import BeautifulSoup  # imported beautifulsoup from bs4
# beautifulsoup allows us to use the HTML file and grab different data
# it alllows us to use that data we've gathered to scrape it
import pprint
# pretty print- organises the way we print stuff in the terminal


# res--> response variable to get the response(information) from the webpage
res = requests.get('https://news.ycombinator.com/news')
# to get the third page
res2 = requests.get('https://news.ycombinator.com/news?p=2')
# using the getrequests to  get the information we want from the page
# --print(res)  # output--> <Response [200]>

# displays the entire HTML file that displays the text of the webpage.
# --print(res.text)  # we recieved all the HTML inforamtion in String format.
# We will use beautifulsoup to convert it from a string to an actual object that we can manipulate.

soup_obj = BeautifulSoup(res.text, 'html.parser')  # creates soup object
soup_obj2 = BeautifulSoup(res2.text, 'html.parser')
# gave string with all data
# now we parse it; we tell it to modify the string data to HTML that we can use

# --print(soup_obj)
# --print(soup_obj.body)
# --print(soup_obj.body.contents)
# --print(soup_obj.find_all('div'))
# --print(soup_obj.find_all('a'))  # --> prints all links of the site
# --print(soup_obj.title)
# --print(soup_obj.a) #--> prints first <a> tag the interpreter gets to
# --print(find('a')) #--> prints first <a> tag encountered by interpreter
# --print(soup_obj.find(id="score_27708411"))  # --> prints the exact score

# SELECTORS
# --print(soup_obj.select())
# CSS Selector allows us to access the DOM data of teh HTML page
# --print(soup_obj.select('.score')) #to grab all class scores
# --print(soup_obj.select('#score_27708411'))  # gets specific id

# STARTING THE MAIN SCRAPPING WORK.

# We grab the link and grab its votes{POINTS}.
# We want to grab the link that has a class of story link--> [class ="storylink >]
# --print(soup_obj.select('.storylink')[0]) #grabs the first item on hackernews; We get a ton of list that are <a> tags

links = soup_obj.select('.storylink')  # grabs all class links
subtext = soup_obj.select('.subtext')
links2 = soup_obj2.select('storylink')
subtext2 = soup_obj2.select('.subtext')
# now we combine both to one[links and subtext]
mega_links = links + links2
mega_subtext = subtext + subtext2
# we want the subtext instead of points. It's what comes underneath the titles
# all the links have subtext, but no all have scores

# *--votes = soup_obj.select('.score')  # grabs all class votes{scores}
# *--print(votes[0])  # print votes of first story
# *--print(votes[0].get('id'))  # prints the actual id value
# With beautifulsoup, we can keep changing these, we can keep selecting whatever we can
# Now we have the information that we need
# Now we will combine all them to make it more useful


def sort_stories_by_votes(hackernews_list):
    # to sort the stories from highest voted to lowest voted
    # we want to sort it by votes
    return sorted(hackernews_list, key=lambda k: k['votes'], reverse=True)
    # key = votes bcoz that is what by which we want to sort the votes


def create_custom_hackernews(links, subtext):
    # this will receive links and votes of above.
    hackernews = []
    # within the hackernews[], we only want to add the text and none of the HTML.
    # we want to loop through somethings.

    for index, item in enumerate(links):
        # here, we will grab the title of each link
        # we are grabbing the index of each link.
        title = links[index].getText()
        # .getText() gets us the text inside of the tag. It's an bs4 feature

        # in href, we want to get the attribute, not the text. so we use .get() & set a default param
        href = links[index].get('href', None)  # we are grabbing 'href'.

        vote = subtext[index].select('.score')
        # we are selecting the class scores, that is the vote we want

        # sometimes, there are no votes
        # if there are votes, or has length, then do the below
        if len(vote):
            # now we have the votes-->
            points = int(vote[0].getText().replace(' points', ''))
            # we are getting an array and we want to grab the first element in the array.
            # here above, anytime we see any space, replace it with an empty string
            # we are grabbing the subtext

            # now, we want only those news with more than 127 votes
            if points > 126:
                # --print(points)

                # we now combine href and title with a dictionary
                # we append a dictionary in our list which will have our title and link
                hackernews.append(
                    {'title': title, 'link': href, 'votes': points})
                # now, we will have a dictionary that has a link and a title

    return sort_stories_by_votes(hackernews)


pprint.pprint(create_custom_hackernews(mega_links, mega_subtext))
# makes the printed data or prints the output in a neat way
