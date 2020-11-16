#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

from notion.collection import CollectionRowBlock, CollectionView
from notion.block import DividerBlock


class BlockPresenter(dict):

    def __init__(self, block):
        self.block = block

        default_attributes = {"id": block.id.replace("-", ""), "block_type": block.type}

        if isinstance(block, CollectionRowBlock):
            dict.__init__(self, **{**default_attributes, **block.get_all_properties()})
        elif isinstance(block, CollectionView):
            dict.__init__(self, **{"collection_id": block.parent.id.replace("-", ""), "view_id": block.id.replace("-", ""),
                                   "collection_title": block.parent.title, "view_title": block.name})
        elif isinstance(block, DividerBlock):
            dict.__init__(self, **{**default_attributes})
        else:
            dict.__init__(self, **{**default_attributes, "title": block.title})
