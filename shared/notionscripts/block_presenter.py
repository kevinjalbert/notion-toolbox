#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

from notion.collection import CollectionRowBlock, CollectionView


class BlockPresenter(dict):

    def __init__(self, block):
        self.block = block
        if isinstance(block, CollectionRowBlock):
            dict.__init__(self, **{"id": block.id, **block.get_all_properties()})
        elif isinstance(block, CollectionView):
            dict.__init__(self, **{"collection_id": block.parent.id, "view_id": block.id, "collection_title": block.parent.title, "view_title": block.name})
        else:
            dict.__init__(self, **{"id": block.id, "title": block.title})
