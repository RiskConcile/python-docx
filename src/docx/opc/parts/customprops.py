"""
Custom properties part, corresponds to ``/docProps/custom.xml`` part in package.
"""

from docx.opc.constants import CONTENT_TYPE as CT
from docx.opc.customprops import CustomProperties
from docx.opc.packuri import PackURI
from docx.opc.part import XmlPart
from docx.oxml.customprops import CT_CustomProperties
from docx.oxml.parser import ct_parse_xml


class CustomPropertiesPart(XmlPart):
    """
    Corresponds to part named ``/docProps/custom.xml``, containing the custom
    document properties for this document package.
    """

    @classmethod
    def default(cls, package):
        """
        Return a new |CustomPropertiesPart| object initialized with default
        values for its base properties.
        """
        return cls._new(package)

    @property
    def custom_properties(self):
        """
        A |CustomProperties| object providing read/write access to the custom
        properties contained in this custom properties part.
        """
        return CustomProperties(self.element)

    @classmethod
    def load(cls, partname, content_type, blob, package):
        element = ct_parse_xml(blob)
        return cls(partname, content_type, element, package)

    @classmethod
    def _new(cls, package):
        partname = PackURI('/docProps/custom.xml')
        content_type = CT.OPC_CUSTOM_PROPERTIES
        customProperties = CT_CustomProperties.new()
        return CustomPropertiesPart(
            partname, content_type, customProperties, package
        )
