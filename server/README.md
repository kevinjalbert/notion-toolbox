# notion-toolbox's server

This is the server component that communicates with Notion's API via [notion-py](https://github.com/jamalex/notion-py). The functionality is to provide CRUD (Create Read Update Delete) operations for blocks and collections.

## Authentication

This server expects a `Notion-Token` to be sent in the request headers. This will be your own `token_v2` from [Notion's cookies](https://www.notion.so/). This will allow you to access your own private content. Tokens are not to be logged or stored anywhere, although if you have concerns you can always host your own server component.

If needed, rate limiting will be used as this server will be running on a free [Heroku](https://heroku.com/) dyno.

## Endpoints

As of right now the following endpoints exist:

```python
# Allows you to add a piece of text as a child of the specific block (i.e.,
# nesting under a text block, or inside a page)
@app.route('/blocks/<block_id>', methods=['POST'])

# Allows you to update the specified block with new values from the JSON body. Text blocks
# use "title", and collection rows (which are technically blocks) can also
# specify other columns.
@app.route('/blocks/<block_id>', methods=['PUT'])

# Allows you to view the content of the specified block. It will take the block's title and
# all of its children's titles and join them with newlines.
@app.route('/blocks/<block_id>', methods=['GET'])

# Allows you to delete the specified block. This also works for collection rows
# as they are technically blocks
@app.route('/blocks/<block_id>', methods=['DELETE'])

# Allows you to append a new row onto the specificed collection view with the
# values from the JSON body.
@app.route('/collections/<collection_id>/<view_id>', methods=['POST'])

# Allows you to view all the rows of the specified collection view with all the
# column values present.
@app.route('/collections/<collection_id>/<view_id>', methods=['GET'])
```

More documentation will follow shortly for these, although you can take a look at the source code for more details.
