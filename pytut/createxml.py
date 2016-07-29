
from xml.dom.minidom import Document

#create minidom-document
doc = Document()

# create base element
base = doc.createElement('Dictionary')
doc.appendChild(base)

# create an entry element
entry = doc.createElement('Entry')

# ... and append it to the base element
base.appendChild(entry)

# create another element 
german = doc.createElement('German')

# create content
german_content = doc.createTextNode('''Hund
Hund''')

# append content to element
german.appendChild(german_content)

# append the german entry to our entry element
entry.appendChild(german)

# now the same with an english entry
english = doc.createElement('English')
english_content = doc.createTextNode('dog')
english.appendChild(english_content)
entry.appendChild(english)

print doc.toxml(encoding='utf-8') 