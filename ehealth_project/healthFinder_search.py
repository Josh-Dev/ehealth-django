__author__ = 'Ruxandra'
from bs4 import BeautifulSoup
import urllib, urllib2

# Add your BING_API_KEY

HEALTHFINDER_API_KEY = 'nolnuoubegzidkdu'  # !!!!! REGISTER ON AZURE !!!!!


def run_queryHF(search_terms):
    # Specify the base
    root_url = 'http://healthfinder.gov/developer/Search'

    # Wrap quotes around our query terms as required by the Bing API.
    # The query we will then use is stored within variable query.
    query = '{0}'.format(search_terms)
    query = urllib.quote(query)

    # Construct the latter part of our request's URL.
    # Sets the format of the response to JSON and sets other properties.
    search_url = "{1}.xml?api_key={2}&keyword={0}".format(
        query,
        root_url,
        HEALTHFINDER_API_KEY,

        )

    # Setup authentication with the Bing servers.
    # The username MUST be a blank string, and put in your API key!
    username = ''


    # Create a 'password manager' which handles authentication for us.
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, search_url, username, HEALTHFINDER_API_KEY)

    # Create our results list which we'll populate.
    results = []

    try:
        # Prepare for connecting to Bing's servers.
        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)

        # Connect to the server and read the response generated.
        response = urllib2.urlopen(search_url).read()

        # Convert the string response to a Python dictionary object.
        xml_soup = BeautifulSoup(response,"xml")

        # Loop through each page returned, populating out results list.
        for result in xml_soup.find_all("Topic"):
            cleantext = BeautifulSoup(result.Sections.Section.Description.text).text
            cleantitle = BeautifulSoup(result.Title.text).text
            results.append({
            'title': cleantitle,
            'link': result.AccessibleVersion.text,
            'summary': cleantext})
        for result in xml_soup.find_all("Tool"):
            cleantext = BeautifulSoup(result.Content.text).text
            cleantitle = BeautifulSoup(result.Title.text).text
            results.append({
            'title': cleantitle,
            'link': result.AccessibleVersion.text,
            'summary': cleantext[0:280]+"..."})

    # Catch a URLError exception - something went wrong when connecting!
    except urllib2.URLError as e:
        print "Error when querying the HealthFinder API: ", e

    # Return the list of results to the calling function.
    return results
