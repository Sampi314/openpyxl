# Copyright (c) 2010-2024 openpyxl

import pytest
from openpyxl.xml.functions import tostring, fromstring
from ..slicer import Slicer, SlicerCache

class TestSlicer:
    def test_slicer_to_tree(self):
        slicer = Slicer(name="Slicer1", cache="SlicerCache1")
        xml = tostring(slicer.to_tree())
        assert b'name="Slicer1"' in xml
        assert b'cache="SlicerCache1"' in xml

    def test_slicer_from_tree(self):
        xml = '<slicer name="Slicer1" cache="SlicerCache1" caption="My Slicer"/>'
        node = fromstring(xml)
        slicer = Slicer.from_tree(node)
        assert slicer.name == "Slicer1"
        assert slicer.cache == "SlicerCache1"
        assert slicer.caption == "My Slicer"

class TestSlicerCache:
    def test_slicer_cache_to_tree(self):
        cache = SlicerCache(name="SlicerCache1", listName="Table1")
        xml = tostring(cache.to_tree())
        assert b'name="SlicerCache1"' in xml
        assert b'listName="Table1"' in xml
