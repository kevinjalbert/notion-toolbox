# notion-toolbox's server

This is the server component that communicates with Notion's API via [notion-py](https://github.com/jamalex/notion-py). The functionality is to provide CRUD (Create Read Update Delete) operations for blocks and collections.

## Authentication

This server expects a `Notion-Token` to be sent in the request headers. This will be your own `token_v2` from [Notion's cookies](https://www.notion.so/). This will allow you to access your own private content. Tokens are not to be logged or stored anywhere, although if you have concerns you can always host your own server component.

If needed, rate limiting will be used as this server will be running on a free [Heroku](https://heroku.com/) dyno.

## Endpoints

As of right now the following endpoints exist:

```python
@app.route('/blocks/<block_id>/append', methods=['POST'])
@app.route('/blocks/<block_id>/view', methods=['GET'])
@app.route('/collections/<collection_id>/<view_id>/append', methods=['POST'])
@app.route('/collections/<collection_id>/<view_id>/view', methods=['GET'])
```

More documentation will follow shortly for these, although you can take a look at the source code for more details.
