import sys
import urllib2
import datetime

def get_whatsnew_urls(url):

    new_urls = []

    whatsnew_page = urllib2.urlopen(url)
    page_source = whatsnew_page.read()

    elements = page_source.split('<')

    prev_url = ''

    for element in elements:
        if element.startswith('a href'):
            
            new_url = element[7:]
            if new_url.startswith('"//aws.amazon.com/about-aws/whats-new'):
                cutoff ='">'
                new_url = new_url.split(cutoff, 1)[0]
                cutoff = '" '
                new_url = new_url.split(cutoff, 1)[0]
                new_url = new_url[1:]
                
                if prev_url != new_url:
                    new_urls.append(new_url)
                    prev_url = new_url
        else:
            pass
        
    return new_urls

base_url = "https://aws.amazon.com/about-aws/whats-new"

year = datetime.datetime.now().year
month = datetime.datetime.now().month

# yearly
#get_whatsnew_urls(base_url + '/' + str(year))

# monthly
new_urls = get_whatsnew_urls(base_url + '/' + str(year) + '/' + "{:02}".format(month))

print len(new_urls)
