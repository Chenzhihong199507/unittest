# -*- coding:utf-8 -*-

from docx import Document
import json

def duqu(file):
    document = Document(file)
    ps = [paragraph.text for paragraph in document.paragraphs]
    str = ''
    for p in ps:
        str += p
    return str