from notion.store import RecordStore


def noSaveCache(self, attribute):
    return()


def noLoadCache(self, attributes=("_values", "_role", "_collection_row_ids")):
    return()


# Prevents the cache from being written and loaded
# Provides a massive speed boost for short lived commands
RecordStore._save_cache = noSaveCache
RecordStore._load_cache = noLoadCache
