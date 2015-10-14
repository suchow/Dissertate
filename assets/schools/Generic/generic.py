from __future__ import print_function
from builtins import object
#!/usr/bin/env python
from docx import Document


class GenericTemplate(object):

    def __init__(self):
        self.document = Document('../assets/word-base/dissertate.docx')

    def fill(self):
        print("")

    def save(self):
        self.document.save('dissertation.docx')

    def clear_paragraph(self, paragraph):
        p_element = paragraph._p
        p_child_elements = [elm for elm in p_element.iterchildren()]
        for child_element in p_child_elements:
            p_element.remove(child_element)
