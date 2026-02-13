# Copyright (c) 2010-2024 openpyxl

from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.descriptors import (
    Typed,
    Integer,
    Bool,
    String,
    Sequence,
)
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.xml.constants import SHEET_MAIN_NS

class Slicer(Serialisable):
    tagname = "slicer"
    _path = "/xl/slicers/slicer{0}.xml"
    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.slicer+xml"
    rel_type = "http://schemas.microsoft.com/office/2007/relationships/slicer"

    name = String()
    cache = String()
    caption = String(allow_none=True)
    startItem = Integer(allow_none=True)
    columnCount = Integer(allow_none=True)
    showCaption = Bool(allow_none=True)
    rowHeight = Integer(allow_none=True)

    def __init__(self,
                 name=None,
                 cache=None,
                 caption=None,
                 startItem=None,
                 columnCount=None,
                 showCaption=None,
                 rowHeight=None,
                ):
        self.name = name
        self.cache = cache
        self.caption = caption
        self.startItem = startItem
        self.columnCount = columnCount
        self.showCaption = showCaption
        self.rowHeight = rowHeight


    @property
    def path(self):
        return self._path.format(self.id)


class SlicerCache(Serialisable):
    tagname = "slicerCache"

    name = String()
    listName = String(allow_none=True)

    def __init__(self,
                 name=None,
                 listName=None,
                ):
        self.name = name
        self.listName = listName
