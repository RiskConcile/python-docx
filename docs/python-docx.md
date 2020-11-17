# python-docx workflow

## Components

### Docx

Deals with the creation and addition of elements of a docx object.

### Parts

The middle man, will receive and redirect top level calls to specific domain implementation

### Oxml

Translates docx objects to docx files by converting them to appropriate XML.

## Implementation

Upon calling the creation of a document object api.py will handle this call. In turn docx>parts>document.py will create and return this document object<>
Document aanmaken

the module uses OPC (Open Packaging Convention) for the "flow of the program"

### Core properties

During the creation of a docx the core properties are also set.
docx>document.py core properties -> part core properties -> opc>part.py package (instance of object) -> opc>package.py core properties -> opc>package.py returns core properties

Next the root xml is location and a CoreProperties object is created. After all these steps are done modifying core properties is very simple. The CoreProperties object consists of several properties like author, and can easily be altered by accessing these properties
oxml>coreprops.py CT_CoreProperties has the properties, and when a property is changed in opc>core_properties the value of that property will also be set in CT_CoreProperties (which translates to the XML core properties)

```python
_coreProperties_tmpl = (
        '<cp:coreProperties %s/>\n' % nsdecls('cp', 'dc', 'dcterms')
    )
```

nsdecls goes to a dictionary where for each of the given arguments the matching link will be added to the XML file

### Custom properties

#### Initial

The general flow is very similar to core properties. Initially no CustomProperties exist so this object is created.
Document.py -> __parts -> package.custom_properties -> CustomPropertiesPart

opc>customprops.py The CustomPropertiesPart acts as a middle man for custom properties transactions. It also servers at the connection between the OXML and OPC custom properties. This way the custom properties can easily be converted to valid XML  
oxml>customprops.py CT_CustomProperties via de template creates and adds XML  
opc>customprops.py CustomProperties new property created via __setitem__. if the property already exists it is simply updated  
OPC package ales has different functionalities like forming relaties between objects

#### Create new Custom Property

document.py>custom properties  
parts>document.py custom properties  
opc>part.py package  
opc>package.py custom properties, custom properties part  
-> a custom properties will be returned and set through the setitem on custom properties. Finally in the XML a new element is added for this custom property.
