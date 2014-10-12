#!/usr/bin/env python
# -*- coding: utf-8 -*-

#How to use lxml: http://lxml.de/tutorial.html
from lxml import etree
from StringIO import StringIO
import file_process as f

def exportToXML(etreeRootTag, filename):
	f.writeInFile(filename,etree.tostring(etreeRootTag, pretty_print=True))

def importFromXML(filename):
	fileContent = f.readWholeFile(filename)
	tree = etree.parse(StringIO(fileContent))
	return tree

def createFile(etreeParentTag, name_string="New URL", url_string=""):
	etree.SubElement(etreeParentTag, "file", name=name_string, url=url_string)

def createFolder(etreeParentTag, name_string="New Folder"):
	etree.SubElement(etreeParentTag, "folder", name=name_string)

def createNewTree(etreeRootTag):
	return etree.Element(etreeRootTag)

def printTree(etreeRootTag):
	print etree.tostring(etreeRootTag, pretty_print=True)

test = createNewTree("test")
for i in range(4):
	createFolder(test, str(i))
	createFile(test)
print test
print test[1]
createFile(test[1])

printTree(test)
exportToXML(test,"test.xml")

print "plop ++++++++++++++++++++"

tree = importFromXML("test.xml")
printTree(tree)
