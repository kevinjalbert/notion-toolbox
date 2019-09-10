<h1 align="center">Welcome to notion_scripts 👋</h1>
<p align="center">
  <img alt="Version" src="https://img.shields.io/badge/version-v0.2.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/kevinjalbert/notion-scripts/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" target="_blank" />
  </a>
  <a href="https://twitter.com/kevinjalbert">
    <img alt="Twitter: kevinjalbert" src="https://img.shields.io/twitter/follow/kevinjalbert.svg?style=social" target="_blank" />
  </a>
</p>

> Shared collection of common Notion Scripts used in my projects

## Install

This package is using Python 3.

```sh
pip install git+https://github.com/kevinjalbert/notion-scripts
```

## Usage

Some quick usage is shown here:

```python
from notionscripts.notion_api import NotionApi

notion_api = NotionApi()
notion_api.current_day()
notion_api.append_to_current_day_notes("title of a note")
```

For more detailed usage I would recommend taking a look at [`alfred-notion`](https://github.com/kevinjalbert/alfred-notion) and [`notion-heroku`](https://github.com/kevinjalbert/notion-heroku).

A more completed set of features and instructions will be provided soon.

## Author

👤 **Kevin Jalbert**

* Twitter: [@KevinJalbert](https://twitter.com/KevinJalbert)
* Github: [@kevinjalbert](https://github.com/kevinjalbert)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/kevinjalbert/notion-scripts/issues).

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2019 [Kevin Jalbert](https://github.com/kevinjalbert).<br />
This project is [MIT](https://github.com/kevinjalbert/notion-scripts/blob/master/LICENSE) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
