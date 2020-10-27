#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

from notion.collection import CollectionRowBlock


class BlockPresenter(dict):

    def __init__(self, block):
        self.block = block
        if isinstance(block, CollectionRowBlock):
            dict.__init__(self, **{"id": block.id, **block.get_all_properties()})
        else:
            dict.__init__(self, **{"id": block.id, "title": block.title})
