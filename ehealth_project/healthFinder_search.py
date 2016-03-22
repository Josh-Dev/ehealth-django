__author__ = 'Ruxandra'
from bs4 import BeautifulSoup
import xml.etree.ElementTree
import urllib, urllib2

# Add your HEALTHFINDER_API_KEY

HEALTHFINDER_API_KEY = 'nolnuoubegzidkdu'  # !!!!! REGISTER ON AZURE !!!!!


def run_queryHF(search_terms):
    # Specify the base
    root_url = 'http://healthfinder.gov/developer/Search'

    # Wrap quotes around our query terms as required by the HealthFinder API.
    # The query we will then use is stored within variable query.
    query = '{0}'.format(search_terms)
    query = urllib.quote(query)

    # Construct the latter part of our request's URL.
    # Sets the format of the response to XML and sets other properties.
    search_url = "{1}.xml?api_key={2}&keyword={0}".format(
        query,
        root_url,
        HEALTHFINDER_API_KEY,

        )

    # Setup authentication with the HealthFinder servers.
    # The username MUST be a blank string, and put in your API key!
    username = ''


    # Create a 'password manager' which handles authentication for us.
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, search_url, username, HEALTHFINDER_API_KEY)

    # Create our results list which we'll populate.
    results = []

    try:
        # Prepare for connecting to HealthFinder's servers.
        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)

        # Connect to the server and read the response generated.
        request = urllib2.Request(search_url)
        response = urllib2.urlopen(request)
        # Convert the string response to a Python dictionary object.
        xml_soup = xml.etree.ElementTree.parse(response)
        root = xml_soup.getroot()

        # Loop through each page returned, populating out results list.
        for result in root.findall("Topics"):
            for data in result.findall("Topic"):
                title = BeautifulSoup(data.find("Title").text,"html.parser").text
                url = data.find("AccessibleVersion").text
                for data1 in data.findall("Sections"):
                    for data2 in data1.findall("Section"):
                        summary = BeautifulSoup(data2.find("Content").text,"html.parser").text

                results.append({
                'title': title,
                'link': url,
                'summary': summary[0:280]+"...",
                'source': 'Healthfinder'
                 })
        for result in root.findall("Tools"):
            for data in result.findall("Tool"):
                title = BeautifulSoup(data.find("Title").text,"html.parser").text
                url = data.find("AccessibleVersion").text
                summary = BeautifulSoup(data.find("Content").text,"html.parser").text
                results.append({
                'title': title,
                'link': url,
                'summary': summary[0:280]+"...",
                'source': 'Healthfinder'
                 })

    # Catch a URLError exception - something went wrong when connecting!
    except urllib2.URLError as e:
        print "Error when querying the HealthFinder API: ", e

    # Return the list of results to the calling function.
    return results
