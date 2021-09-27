FILE PRETAINING TO THE DETAILS AND INFORMATION ABOUT `hcsc.py`

# PLAN [How we want to scrape and grab data]
We want to grab the link, that is the title and the link of a story that has more than 127 points votes. 
Others we dont want. 
We filter them out.

1. We want grab the link and grab its votes{POINTS}.
   We want to grab the link that has a class of story link [class="storylink>]

2.   We want to grab the title of the link and the link['href] and combine them into one dictionary for making it more sensible.
We want only stories with votes. 
First, we want to convert the votes into numbers. If the story has more than 127 votes, we want to keep it and append to `hackernews`.
We want to sort the links from the highest number of votes, to the lowest number of votes.

We used enumerate() because we have two lists- the links and the subtext, and we're only enumerating over the `links` list and `subtext` is now being enumerate.
We need the index to access `subtext` within our loop; bcoz otherwise, if we don't enumerate, we can't grab both lists at the same time.

Then, we want to scrape the 3rd page of hackernews as well.


