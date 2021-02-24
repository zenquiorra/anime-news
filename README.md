# Anime News Generator

Anime News Generator Scrapes potential websites which contains `anime related` news and articles.
The `news.py` file scrapes websites and returns a 'list of dictionaries' object which is further stored as `data.json` for further use. It uses related packages and libraries such as `BeautifulSoup`, `requests` ,`hashlib` and `json`.


# The procedure highlights

  - Creating a session token and passing related headers into the `request` arguments
  - Read the object from 'requests' and convert it into a BeautifulSoup object using the BeautifulSoup library
  - Read the page structure and find potential sources of news on related tags.
  - Scrape those tags and process the output into a presentable format.
  - The data is generated onto a 'list of dictionaries' which is further processed into a 'json' file using the `json` library.

# Technicalities

  - The program has a dedicated section to each source of 'news'.
  > We assume consistency in the code structure of the website which is used as a source.
  > Periodic checks and verification of the source structure is required and relevant changes to related section
  > upon any change in source.
  - The program scrapes the websites and different instances of output can have similar objects in them, this is evaded by using an `id` parameter and stored into a dictionary with `id` as a key.
  > We want this 'id' to be unique and does not change on various instances of the output for same objects.
  > We generate this `id` using the `hashlib` library and sha256 algorithm.
  > We make the assumption that the sha256 algorithm will not likely give a collision, given the size of output is small.
  > Hashlib will likely to return the same hash value on a consistent environment.

  # Section 1 ('Anime News Network')
The program uses it primary source in section 1 at [AnimeNewsNetwork]('https://www.animenewsnetwork.com/')



  # TODO : UPDATE THE README WITH ALL DETAILS OF THE PROCEDURE, UPCOMING FEATURES AND REMAINING DOCUMENTATION
