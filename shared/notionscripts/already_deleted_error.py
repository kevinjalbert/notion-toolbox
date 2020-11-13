#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3


class AlreadyDeletedError(Exception):
    def __init__(self, block_id):
        super().__init__(f"Block {block_id} has already been deleted")
