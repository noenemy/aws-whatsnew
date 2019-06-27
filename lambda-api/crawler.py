import sys
import urllib2

url = "https://aws.amazon.com/about-aws/whats-new/2018/11/"
whatsnew_page = urllib2.urlopen(url)

page_source = whatsnew_page.read()

elements = page_source.split('<')

prevUrl = ''

for element in elements:
    if element.startswith('a href'):
        
        newUrl = element[7:]
        if newUrl.startswith('"//aws.amazon.com/about-aws/whats-new'):
            cutoff ='">'
            newUrl = newUrl.split(cutoff, 1)[0]
            cutoff = '" '
            newUrl = newUrl.split(cutoff, 1)[0]
            newUrl = newUrl[1:]
            
            if prevUrl != newUrl:
                print newUrl
                prevUrl = newUrl
    else:
        pass
    
