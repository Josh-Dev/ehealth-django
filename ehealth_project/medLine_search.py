__author__ = 'Ruxandra'

from bs4 import BeautifulSoup
import urllib, urllib2


def run_queryMed(search_terms):
    # Specify the base
    root_url = 'https://wsearch.nlm.nih.gov/ws/query'

    # Specify how many results we wish to be returned in the xml document.
    # default is 10.
    #database used - healthTopics
    db = 'healthTopics'
    retmax='10'

    # Wrap quotes around our query terms as required by the Bing API.
    # The query we will then use is stored within variable query.
    query = '{0}'.format(search_terms)
    query = urllib.quote(query)

    # Construct the latter part of our request's URL.
    # Sets the format of the response to XML and sets other properties.
    search_url = "{1}?db={2}&term={0}&retmax={3}".format(
        query,
        root_url,
        db,
        retmax
        )

    # Setup authentication with the medLine servers.
    # The username MUST be a blank string, and put in your API key! - not needed for medLine
    username = ''


    # Create a 'password manager' which handles authentication for us.
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, search_url, username, None)

    # Create our results list which we'll populate.
    results = []

    try:
        # Prepare for connecting to meLine's servers.
        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)

        # Connect to the server and read the response generated.
        response = urllib2.urlopen(search_url).read()

        # Convert the string response to a BeautifulSoup object.
        xml_response = BeautifulSoup(response)

        # Loop through each page returned, populating out results list.
        keys = {'url'}
        for result in xml_response.find_all("document"):
            dict = ({key:value for key, value in result.attrs.iteritems() if key in keys})
            results.append({
            'title': BeautifulSoup(result.contents[1].text).text,
            'link': dict['url'],
            'summary': BeautifulSoup(result.contents[len(result.contents)-2].text).text})

    # Catch a URLError exception - something went wrong when connecting!
    except urllib2.URLError as e:
        print "Error when querying the medLine API: ", e

    # Return the list of results to the calling function.
    return results
