import datetime
import requests
from lxml import html, etree
from datetime import datetime

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

def get_xpath_value_safe(tree, xpath_query, default_value):

    value = tree.xpath(xpath_query)
    if value is None:
        return default_value
    
    return value[0]

def read_whatsnew_article(url):
    
    article = {}

    whatsnew_page = requests.get(url)
    tree = html.fromstring(whatsnew_page.content)

    title = get_xpath_value_safe(tree, '//div[@class="twelve columns"]/h1/a/text()', '')
    posted_date = get_xpath_value_safe(tree, '//span[@class="date"]/text()', '')
    #if posted_date == '':
        #TODO: raise invalid datetime value exception here!
    posted_date = datetime.strptime(posted_date, '%b %d, %Y')
    content = ''
    content_section1 = get_xpath_value_safe(tree, '//div[@class="aws-text-box"]/div/p', '')
    content_section2 = get_xpath_value_safe(tree, '//div[@class="parsys content"]/div/div/p', '')

    for part in content_section1:
        content += etree.tostring(part, pretty_print=True)
    for part in content_section2:
        content += etree.tostring(part, pretty_print=True)

    article["url"] = url
    article["posted_date"] = posted_date.isoformat()
    article["title"] = title
    article["content"] = content
    
    return article


year = datetime.now().year
month = datetime.now().month

# monthly
url_list = get_whatsnew_url_list(year, month)

for url in url_list:
    article = read_whatsnew_article(url)
    print(article)
