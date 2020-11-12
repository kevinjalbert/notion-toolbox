# notion-toolbox's server

> https://notion-server.herokuapp.com

This is the server component that communicates with Notion's API via [notion-py](https://github.com/jamalex/notion-py). The functionality is to provide CRUD (Create Read Update Delete) operations for blocks and collections. The server performs actions using your provided Notion token. This is a public server, and if needed, rate limiting will be used as this server will be running on a free [Heroku](https://heroku.com/) dyno.

## Authentication

By default, this server expects a `Notion-Token` to be sent in the request headers. This will be your own `token_v2` from [Notion's cookies](https://www.notion.so/). This will allow you to access your own private content. Tokens are not to be logged or stored anywhere, although if you have concerns you can always host your own server component.

If needed you can also send a `notion_token` in the JSON body payload, or even as a query parameter. I will mention that using the query parameter approach will expose the token in the Heroku logs.

## Endpoint Documentation

The endpoints are documented in a [Postman](https://www.postman.com/) collection. You can view the documentation online [here](https://documenter.getpostman.com/view/37310/TVYGdddF). There are free limitations to views, and thus if the monthly limit has been exceeded, you can import the documentation into your own instance of Postman using this [snapshot](https://www.postman.com/collections/9d5e9843e907c1820dcd).

