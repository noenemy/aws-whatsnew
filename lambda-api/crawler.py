import datetime
from lxml import html, etree
import requests

def get_whatsnew_url_list(year, month):

    url_list = []

    base_url = "https://aws.amazon.com/about-aws/whats-new"
    url = base_url + '/' + str(year) + '/' + "{:02}".format(month)

    whatsnew_list_page = requests.get(url)
    tree = html.fromstring(whatsnew_list_page.content)

    whatsnew_list = tree.xpath('//li[@class="directory-item text whats-new"]/h3/a/@href')

    for link in whatsnew_list:
        url_list.append('https:' + link)
    
    return url_list

def read_whatsnew_content(url):
    
    whatsnew_page = requests.get(url)
    tree = html.fromstring(whatsnew_page.content)

    title = tree.xpath('//div[@class="twelve columns"]/h1/a/text()')
    posted_date = tree.xpath('//span[@class="date"]/text()')
    content = ''
    content_section1 = tree.xpath('//div[@class="aws-text-box"]/div/p')
    content_section2 = tree.xpath('//div[@class="parsys content"]/div/div/p')

    for part in content_section1:
        content += etree.tostring(part, pretty_print=True)
    for part in content_section2:
        content += etree.tostring(part, pretty_print=True)

    print(title)
    print(posted_date)
    print(content)


year = datetime.datetime.now().year
month = datetime.datetime.now().month

# monthly
url_list = get_whatsnew_url_list(year, month)

for url in url_list:
    read_whatsnew_content(url)

print(len(url_list))