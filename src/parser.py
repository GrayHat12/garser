from html.parser import HTMLParser
from .element import Element

class Parser(HTMLParser):
    def __init__(self,convert_charrefs=True):
        HTMLParser.__init__(self,convert_charrefs=convert_charrefs)
        self.element = Element('document',[],None)
        self.chars = ' '
    def handle_starttag(self, tag, attrs):
        #print(self.chars+tag)
        self.chars = ' '*(len(self.chars)+1)
        if self.element == None:
            self.element = Element(tag,attrs,None)
        else:
            nElement = Element(tag,attrs,self.element)
            self.element.addElement(nElement)
            self.element = nElement     
    def handle_startendtag(self, tag, attrs):
        #print(self.chars+tag)
        if self.element != None:
            self.element.addElement(Element(tag,attrs,self.element))
    def handle_data(self, data):
        if self.element != None:
            self.element.addBody(data)  
    def handle_endtag(self, tag):
        self.chars = ' '*(len(self.chars)-1)
        #print(self.chars+tag)
        if self.element != None:
            while self.element.tag != tag and self.element.parent != None:
                self.element = self.element.parent
            self.element.close()
        if self.element.parent != None:
            self.element = self.element.parent
    def getParentElement(self):
        element = self.element
        while element.parent != None:
            element = element.parent
        return element
    def processElements(self):
        element = self.getParentElement()
        element.formatStructure()
        self.element = element
