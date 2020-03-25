class Element:
    def __init__(self,tag,attributes,parent=None):
        self.children = []
        if parent == None:
            self.parent = None
        else:
            self.parent = parent
        self.bodyData = ''
        self.tag = tag
        self.attributes = {}
        self.open = True
        for attribute in attributes:
            self.attributes.update({attribute[0] : attribute[1]})
    def changeParent(self,newParent):
        """Change the Parent of this element"""
        self.parent = newParent
    def getChildrenWithAttribute(self,attr):
        """
        Get immediate children matching the provided attribute
        """
        out = []
        for child in self.children:
            if attr in child.attributes.keys():
                out.append(child)
        return out
    def getImmediateElementsByTag(self,tag):
        """
        Get immediate elements matching the provided tag
        Example - Tag to locate <h1>Text</h1>
        Syntax - getImmediateElementsByTag("h1")
        """
        out = []
        for child in self.children:
            if child.tag == tag:
                out.append(child)
        return out
    def getImmediateElementsByAttributes(self,attrs=[""]):
        """
        Get immediate elements matching the provided attributes
        Example - Element to locate <div id="id0" class="class0">Text</div>
        Syntax - getImmediateElementsByAttributes(['id=id0','class=class0'])
        """
        out = []
        for child in self.children:
            present = True
            for attr in attrs:
                att = attr.split('=')
                if att[0] in child.attributes.keys():
                    if child.attributes[att[0]]==att[1]:
                        pass
                    else:
                        present=False
                        break
                else:
                    present = False
                    break
            if present:
                out.append(child)
        return out
    def getElementsByTag(self,tag):
        """
        Get all child elements matching the provided tag
        Example - Tag to locate <h1>Text</h1>
        Syntax - getImmediateElementsByTag("h1")
        """
        out = []
        for child in self.children:
            if child.tag == tag:
                out.append(child)
            more = child.getElementsByTag(tag)
            out.extend(more)
        return out
    def getElementsByAttributes(self,attrs=[""]):
        """
        Get all child elements matching the provided attributes
        Example - Element to locate <div id="id0" class="class0">Text</div>
        Syntax - getImmediateElementsByAttributes(['id=id0','class=class0'])
        """
        out = []
        for child in self.children:
            present = True
            for attr in attrs:
                att = attr.split('=')
                if att[0] in child.attributes.keys():
                    if child.attributes[att[0]]==att[1]:
                        pass
                    else:
                        present=False
                        break
                else:
                    present = False
                    break
            more = child.getElementsByAttributes(attrs)
            out.extend(more)
            if present:
                out.append(child)
        return out
    def generateHtml(self):
        """
        Generate HTML format text from this element and available children
        """
        out = ""
        if self.parent != None:
            out = "<"+str(self.tag)+" "
            for key in self.attributes.keys():
                out += str(key)+"=\""+str(self.attributes.get(key))+"\" "
            out+=">"
        out+=self.bodyData
        for child in self.children:
            out += str(child.generateHtml())
        if self.parent != None:
            out+="</"+str(self.tag)+">"
        return out
    def addElement(self,element):
        """
        Add child Element
        """
        if self.open:
            self.children.append(element)
    def addBody(self,data):
        """
        Add text found between opening and closing tags
        """
        if self.open:
            self.bodyData = data
    def getData(self):
        """
        Generate JSON format data using current and child elements
        """
        data = {
            'tag' : self.tag,
            'attributes' : self.attributes,
            'body' : self.bodyData
        }
        children = []
        for child in self.children:
            children.append(child.getData())
        data.update({'children' : children})
        return data
    def formatStructure(self):
        """
        Format the structure of this and child elements
        """
        newchildren = []
        children = self.children
        for child in children:
            if child.open:
                tchildren = child.children
                for tchild in tchildren:
                    tchild.changeParent(newParent=self)
                newchildren.extend(tchildren)
                child.children = []
                child.close()
            else:
                child.formatStructure()
        self.children.extend(newchildren)
        if len(newchildren)>0:
            self.formatStructure()
    def close(self):
        """
        Close adding children and body
        """
        self.open=False