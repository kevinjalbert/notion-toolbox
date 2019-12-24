from notion.store import RecordStore


def no_save_cache(self, attribute):
    return()


def no_load_cache(self, attributes=("_values", "_role", "_collection_row_ids")):
    return()


# Prevents the cache from being written and loaded
# Provides a massive speed boost for short lived commands
RecordStore._save_cache = no_save_cache
RecordStore._load_cache = no_load_cache
