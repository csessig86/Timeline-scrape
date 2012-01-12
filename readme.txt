This scraper turns #timeline collections in the BLOX CMS into CSV files that can be read by ProPublica's Timeline-Setter:
http://propublica.github.com/timeline-setter/


Here's a quick walkthrough on how to set up your collection in BLOX:

1. Create a new collection and add any all stories/documents/videos/etc. you would like to have on the timeline.

2. Add the hashtag #timeline to the collection

3. View the timeline. Here's two examples (see output folder):
- http://wcfcourier.com/timeline-ryan-scott-investigation/collection_f13d220a-3c6c-11e1-835a-001871e3ce6c.html
- http://host.madison.com/online/local-election-news/collection_cb61db52-3d43-11e1-9716-001871e3ce6c.html

4. Click view source and look for the jQuery function that creates the timeline. It should start with:
jQuery(document).ready(function(){
	function onLoad()
	{ var eventSource = new Timeline.DefaultEventSource();
…

5. Look for: Timeline.loadXML(/f13d220a-3c6c-11e1-835a-001871e3ce6c.xml?timelineRSS=1) 

Grab the URL inside the parenthesis and paste it at the end of the website address that houses the timeline. Here's two examples:
- http://wcfcourier.com/f13d220a-3c6c-11e1-835a-001871e3ce6c.xml?timelineRSS=1
- http://host.madison.com/cb61db52-3d43-11e1-9716-001871e3ce6c.xml?timelineRSS=1

6. Paste the URL of the XML file into timeline.py after "url" (line 12):
url = 'http://wcfcourier.com/f13d220a-3c6c-11e1-835a-001871e3ce6c.xml?timelineRSS=1'
OR
url = 'http://host.madison.com/cb61db52-3d43-11e1-9716-001871e3ce6c.xml?timelineRSS=1'

7. If you haven't already, download BeautifulSoup. It's very easy to do:
http://www.crummy.com/software/BeautifulSoup/#Download

8. Go into your Terminal, navigate to the folder with Python script and run:
% python timeline.py

This will output a structured CSV file

9. If you haven't already, download Timeline-Setter. It's also really easy to do:
http://propublica.github.com/timeline-setter/

10. In your Terminal, run:
% timeline-setter -c timeline.csv (or whatever your CSV is called)

Note: Sometimes I have to bring the CSV into Excel and save it…Not sure what the problem is but it seems to work after I do that.

11. Tada! You now have Timeline-Setter timeline. See the output folder for a few examples.


- What's Next?
Timeline-Setter has additional customizations that you can add to the timeline:
http://propublica.github.com/timeline-setter/#csv

For instance, you can add descriptions and series to each event on the timeline by adding new columns in the CSV before running "timeline-setter -c timeline.csv".

You might also want to replace all photos in the timeline with large ones…The #timeline collection spits out images that are only 100 pixels wide.