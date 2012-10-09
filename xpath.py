'''
Created on Sep 2, 2012

@author: timo
'''
from lxml import etree

f = open("/Users/timo/Downloads/Rohstoffe & Edelmetalle.html", "r")
parser = etree.HTMLParser()
tree = etree.parse(f, parser)
elements = tree.xpath("//a[contains(text(), 'Gold')]/../following-sibling::*[2]")
print(float(elements[0].text.strip().replace("'", "")))
f.close()
