import xml.etree.ElementTree as ET

data = ET.Element('employees')

element1 = ET.SubElement(data, 'employee')

s_elem1_1 = ET.SubElement(element1, 'name') 

fname = ET.SubElement(s_elem1_1,"firstname")
lname = ET.SubElement(s_elem1_1,"lastname")
fname.text = "Amar"
lname.text = "Joshi"

s_elem1_2 = ET.SubElement(element1, 'salary') 

#s_elem1_1.set('type', 'Manager') 
s_elem1_2.set('type', 'Monthly') 

#s_elem1_1.text = "Mr. ABCD"
s_elem1_2.text = "65000"

element2 = ET.SubElement(data, 'employee')

s_elem2_1 = ET.SubElement(element2, 'name') 
s_elem2_2 = ET.SubElement(element2, 'salary') 

s_elem2_1.set('type', 'Salesman') 
s_elem2_2.set('type', 'Comissionbases') 

s_elem2_1.text = "Mr. BCDE"
s_elem2_2.text = "75000"

b_xml = ET.tostring(data)

with open("xmldata.xml", "wb") as f: 
    f.write(b_xml) 