''' The code is self explanatory, however why certain tasks are done cannot be interpreted
from the code itself and to fully understand a section,
one need to open the associated link from `sites_to_be_scraped`
and follow the code along with following the structure of the page '''



import bs4  # Have to import this to check a class instance further in code
from bs4 import BeautifulSoup as bs
import requests
from hashlib import sha256 as hs
import json



# Defining headers and creating a session for a successful request
with requests.Session() as se:
    se.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Language": "en-US,en;q=0.9",
    }
    sites_to_be_scraped = [
     'https://www.animenewsnetwork.com/', # animenewsnetwork
     'https://www.cbr.com/category/anime-news/', # cbr
     ]

    struct_ann = se.get(sites_to_be_scraped[0]) # Structure of anime news network news page
    struct_cbr = se.get(sites_to_be_scraped[1]) # Structure of cbr news page for anime

top_id = None # track the top id generated


data_generated = [None] # TODO: Asynch optimization here, instead of storing, directly pass onto the front end dynamically
data_generated[0] = [{'top_id': top_id}]
# Section 1

# scraping section for Anime News Network
struct_ann = bs(struct_ann.text, 'html5lib') # parse the structure into a bs instance
struct_ann_b = struct_ann.find_all('span') # Taking all span tags for further analysis. This is stored into a new instance

# Unique ID Gen and store
id_store = set()
def idgen(link):
    id = hs(link.encode('utf-8')).hexdigest()

    return id



n = 0
for i in struct_ann_b:
    data_obj = {} # A dictionary to store extracted data

    # `i` is one tag opening and closure for span and contains its elements as present in the DOM. `i` is a part of bs object

    # bs4 for time tag is not working so custom handling function for time,
    # hardcode the tracing assuming consistency
    # TODO: Optimize the time scraping here or maybe make bs4 work for this somehow

    str_i = str(i) # Converting the bs object into a string object so that we can perform string operations onto it

    s_index, e_index = 0, 0 # starting and end index variables for time tag gap

    if '<time' in str_i: # TODO: Optimize here the string search. (Check if a custom loop is fast or the current method)
        s_index = str_i.index('<time') + len('<time')  # Find the starting index, add the length of the string to find at what index the string ends + 1
        e_index = str_i.index('</time>')  # Find the starting index, to include the index where the string start
        time = str_i[s_index + 11 : e_index - 7] # The gap analysis and getting the time assuming consistency of the code flow
        time = str(time)
        messed_up_time_type = '2020-06-02T13:00:00-04:00\"'
        if len(time) == len(messed_up_time_type):  # Inconsistency in the time string fix
            time = time[:-1]



    text = i.text # Get the text heading from `i`
    link = i.a # Get links from `i`

    if type(link) == bs4.element.Tag: # This is because some `i` may not have a link and hence it won't  be an instance of `tag`(bs4), in this case, we check if its an instance or not.
        link = link['href'] # If its an instance then we get the link
        link = 'https://www.animenewsnetwork.com' + str(link) # Link modification from source so it opens the page directly

    cite = i.cite # citation tag

    if len(text) > 40 and len(str(link)) > 20: # ignore really short headings, these won't be news headings in general, also remove short hyperlinks
        n += 1  # We need to take 10 such news, this keeps in track of that
        data_obj['_id'] = str(idgen(link))

        if n == 1:  # Set top_id
            data_generated[0] = {'top_id': data_obj['_id']}

        data_obj['time'] = time # Allot the variables
        data_obj['heading'] = str(text)
        data_obj['summary'] = None
        data_obj['link'] = str(link)
        data_obj['cite'] = str(cite)
        data_generated.append(data_obj) # Put every verified object into our main list

    if n == 40: # `10` objects found hence break
        break

print (type(data_generated))

# NOTE: Shuffle output on Node
with open('data.json', 'w') as f:

    # for i in range(len(data_generated)): # Convert every object of type tag to dict (Skipped, handled by object conversion)
    #     data_generated[i] = dict(data_generated[i])

    json.dump(data_generated, f)

# # Section 2
# print (struct_cbr.text)
# struct_cbr = bs(struct_cbr.content, 'xml') # parse the structure into a bs instance
# print (struct_cbr)
#
# for i in data_generated:
#     print (i)
#     print ('\



# struct_ann = list(struct_ann)
#
# for i in range(len(struct_ann)):
#     struct_ann[i] = str(struct_ann[i])
# # for i in range(10):
# #     print (struct_ann[i])
# # print (type(struct_ann))
# with open('li.txt','w', encoding = 'utf-8') as f:
#     f.writelines(struct_ann)
#
# struct_ann = struct_ann.find_all('li')
# print (struct_ann[0])
# with open('li.txt', 'r', encoding = 'utf-8') as f:
#     k = f.read()
#     struct_ann = bs(f, 'html5lib')
#
# print (struct_ann)
