#!/usr/bin/env python
from ..Generic.word import GenericTemplate
from docx import Document


class Template(GenericTemplate):

    def __init__(self, arg=None):
        super(Template, self).__init__()
        self.arg = arg
