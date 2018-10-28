import xml.dom.minidom
document = "test3.xml"

dom = xml.dom.minidom.parse(document)

#Examines a node's contents and converts it to a string.
def getNodeText(node):

    nodelist = node.childNodes
    result = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            result.append(node.data)
    return ''.join(result)

#Returns a block's attribute
def handleBlockType(block):
    print(block.getAttribute("s"))

#Returns each block and its contents.
def handleBlocks(blocks):
    for block in blocks:
        handleBlockType(block)
        l = block.getElementsByTagName("l")
        if len(l) > 0:
            for node in l:
                handleLTagParameters(node)
        
#Returns text within a tag l
def handleLTagParameters(l):
    print(getNodeText(l))

#Parses XML to Python given dom input
def parseXML(xml):
    blocks = dom.getElementsByTagName("block")
    handleBlocks(blocks)

parseXML(dom)
