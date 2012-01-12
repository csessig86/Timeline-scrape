import urllib2
from BeautifulSoup import BeautifulSoup

# Create a TSV where we'll save out data. We will later open it, make sure we removed all the commas and add new rows in we want. See further docs:
# http://propublica.github.com/timeline-setter/#csv
f = open('timeline_madison.csv', 'w')

# Make the header rows. These are based on headers recognized by TimelineSetter.
f.write("date" + "," + "link" + "," + "html" + "\n")

# URL of the XML file we will scrape
url = 'http://host.madison.com/cb61db52-3d43-11e1-9716-001871e3ce6c.xml?timelineRSS=1'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

# We'll first determine how many events appear in the XML document and then run a loop through each one, scraping our data along the way.
events = soup.findAll('event')
for x in events:
    
    # Tell us which event is being scraped
    print "Getting data for " + x['title']
	
    # Information within the XML file that we will scrape
    date = x['start']
    title = x['title']
    link = x['link']
    image = x['image']

    # Extract that information in strings
    date2 = str(date)
    link2 = str(link)
    title2 = str(title)
    image2 = str(image)
    
    # We'll replace commas with dashes so we don't screw up the CSV. You can change the dash to whatever character you want
    date3 = date2.replace(",", " -")
    link3 = link2.replace(",", " -")
    title3 = title2.replace(",", " -")
    image3 = image2.replace(",", " -")

    # Write the information to the file. The HTML code is based on coding recognized by TimelineSetter
    f.write(date3 + "," + link3 + "," + '<h2 class="timeline-img-hed">' + title3 + '</h2>' + '<img src="' + image3 + '" width="100">' + "\n")
	
#You're done! Close file.	
f.close()

