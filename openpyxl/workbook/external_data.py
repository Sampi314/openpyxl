# Copyright (c) 2010-2024 openpyxl

from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.descriptors import (
    Typed,
    Integer,
    Bool,
    String,
    Sequence,
    Set,
)
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.xml.constants import SHEET_MAIN_NS

class WebQueryProperties(Serialisable):
    tagname = "webPr"

    xml = Bool(allow_none=True)
    sourceData = Bool(allow_none=True)
    parseHtml = Bool(allow_none=True)
    consecutive = Bool(allow_none=True)
    firstRow = Bool(allow_none=True)
    xl97 = Bool(allow_none=True)
    textDates = Bool(allow_none=True)
    xl2000 = Bool(allow_none=True)
    url = String(allow_none=True)
    post = String(allow_none=True)
    htmlTables = Bool(allow_none=True)

    def __init__(self,
                 xml=None,
                 sourceData=None,
                 parseHtml=None,
                 consecutive=None,
                 firstRow=None,
                 xl97=None,
                 textDates=None,
                 xl2000=None,
                 url=None,
                 post=None,
                 htmlTables=None,
                ):
        self.xml = xml
        self.sourceData = sourceData
        self.parseHtml = parseHtml
        self.consecutive = consecutive
        self.firstRow = firstRow
        self.xl97 = xl97
        self.textDates = textDates
        self.xl2000 = xl2000
        self.url = url
        self.post = post
        self.htmlTables = htmlTables

class DatabaseProperties(Serialisable):
    tagname = "dbPr"

    connection = String()
    command = String(allow_none=True)
    commandType = Integer(allow_none=True)

    def __init__(self,
                 connection=None,
                 command=None,
                 commandType=None,
                ):
        self.connection = connection
        self.command = command
        self.commandType = commandType

class Connection(Serialisable):
    tagname = "connection"

    id = Integer()
    name = String(allow_none=True)
    description = String(allow_none=True)
    type = Integer(allow_none=True)
    background = Bool(allow_none=True)
    refreshOnLoad = Bool(allow_none=True)
    saveData = Bool(allow_none=True)
    dbPr = Typed(expected_type=DatabaseProperties, allow_none=True)
    webPr = Typed(expected_type=WebQueryProperties, allow_none=True)

    __elements__ = ('dbPr', 'webPr')

    def __init__(self,
                 id=None,
                 name=None,
                 description=None,
                 type=None,
                 background=None,
                 refreshOnLoad=None,
                 saveData=None,
                 dbPr=None,
                 webPr=None,
                ):
        self.id = id
        self.name = name
        self.description = description
        self.type = type
        self.background = background
        self.refreshOnLoad = refreshOnLoad
        self.saveData = saveData
        self.dbPr = dbPr
        self.webPr = webPr

class ConnectionList(Serialisable):
    tagname = "connections"
    _path = "/xl/connections.xml"
    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.connections+xml"

    connection = Sequence(expected_type=Connection)

    __elements__ = ('connection',)

    def __init__(self,
                 connection=(),
                ):
        self.connection = connection

    @property
    def path(self):
        return self._path
