#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

from notion.collection import CollectionRowBlock, CollectionView
from notion.block import DividerBlock


class BlockPresenter(dict):

    def __init__(self, block):
        self.block = block
        if isinstance(block, CollectionRowBlock):
            dict.__init__(self, **{"id": block.id.replace("-", ""), **block.get_all_properties()})
        elif isinstance(block, CollectionView):
            dict.__init__(self, **{"collection_id": block.parent.id.replace("-", ""), "view_id": block.id.replace("-", ""),
                                   "collection_title": block.parent.title, "view_title": block.name})
        elif isinstance(block, DividerBlock):
            dict.__init__(self, **{"id": block.id.replace("-", "")})
        else:
            dict.__init__(self, **{"id": block.id.replace("-", ""), "title": block.title})
