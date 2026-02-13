# Copyright (c) 2010-2024 openpyxl

import pytest
from openpyxl.xml.functions import tostring, fromstring
from ..external_data import Connection, ConnectionList, DatabaseProperties

class TestConnection:
    def test_connection_to_tree(self):
        db_pr = DatabaseProperties(connection="Provider=Microsoft.ACE.OLEDB.12.0;Data Source=C:\\data.xlsx")
        conn = Connection(id=1, name="Conn1", type=1, dbPr=db_pr)
        xml = tostring(conn.to_tree())
        assert b'name="Conn1"' in xml
        assert b'<dbPr connection="Provider=Microsoft.ACE.OLEDB.12.0;Data Source=C:\\data.xlsx"/>' in xml

    def test_connection_list_to_tree(self):
        conn1 = Connection(id=1, name="Conn1")
        conn2 = Connection(id=2, name="Conn2")
        clist = ConnectionList(connection=[conn1, conn2])
        xml = tostring(clist.to_tree())
        assert b'<connection id="1" name="Conn1"/>' in xml
        assert b'<connection id="2" name="Conn2"/>' in xml
