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

#Returns a block tag's attribute, aka A block's type
def handleBlockType(block):
    print("            <block s = " + block.getAttribute("s")+">")
    
#Returns a variable block's variable name. To be distinguished from regular block types
def handleVariableBlock(block):
    print("            <block var =  " + block.getAttribute("var")+">")

#Returns the contents of a block tag
def handleBlock(block):
    if(block.hasAttribute("s")):
        handleBlockType(block)
    if(block.hasAttribute("var")):
        handleVariableBlock(block)
    ls = block.getElementsByTagName("l")
    for l in ls:
        if(not(l.parentNode.isSameNode(block))):
            ls.remove(l)
    if len(ls) > 0:
        for l in ls:
            handleLTagParameters(l)
#Returns the contents of a blocks tag
def handleBlocks(blocks):
    for block in blocks:
        handleBlock(block)
        
#Returns text within a tag l
def handleLTagParameters(l):
    print("               <l> "+ getNodeText(l))

#Returns everything within a "script" tag
def handleScript(script):
    print("         <Script>")
    blocks = script.getElementsByTagName("block")
    for block in blocks:
        if(not(block.parentNode.isSameNode(script))):
            blocks.remove(block)
        
    handleBlocks(blocks)
    print("         </Script>")
    
#Returns everything within a "scripts" tag
def handleScripts(scripts):
    print("      <Scripts>")
    for script in scripts:
        handleScript(script)
    print("      </Scripts>")
        
#Returns everything within a "sprite" tag
def handleSprite(sprite):
    print("   <Sprite>")
    print("      name: " + sprite.getAttribute("name"))
    print("      id: " + sprite.getAttribute("id"))
    print("      costume: " + sprite.getAttribute("costume"))
    handleScripts(sprite.getElementsByTagName("script"))
    print("   </Sprite>")
    
#Returns everything within a "sprites" tag
def handleSprites(sprites):
    print("<Sprites>")
    for sprite in sprites:
        handleSprite(sprite)
    print("</Sprites>")
        
#Parses XML to Python given dom input.
def parseXML(xml):
    sprites = dom.getElementsByTagName("sprite")
    handleSprites(sprites)

parseXML(dom)
