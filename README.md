<h1 align="center">Welcome to notion-toolbox 👋</h1>
<p align="center">
  <a href="https://github.com/kevinjalbert/notion-toolbox/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-yellow.svg" target="_blank" />
  </a>
  <a href="https://twitter.com/kevinjalbert">
    <img alt="Twitter: kevinjalbert" src="https://img.shields.io/twitter/follow/kevinjalbert.svg?style=social" target="_blank" />
  </a>
</p>

A collection of [Notion](https://www.notion.so/) tools that work in tandem together. Most of these tools take advantage of a [specific weekly/daily tempalte](https://kevinjalbert.com/my-weekly-notion-setup/) that integrates with various tools and solutions present in this repository.

## Tools

The following are the set of tools. Each one has their own README in their sub-directory.

- [Alfred](alfred/) workflow
  - Enables a handful of ways to interact with template using shortcuts
- [Server](server/) application
  - Enables an online (and backgrounded) interface to interact with template
  - Useful to connect with webhooks (e.g., IFTTT)
  - Opens integrations with Google Assistant

## History

I created a [specific weekly/daily tempalte](https://kevinjalbert.com/my-weekly-notion-setup/) to satisfy some of my needs and give structure to Notion. I later created an integration with [Alfred](https://www.alfredapp.com/) called [`alfred-notion`](https://github.com/kevinjalbert/alfred-notion) (read more [here](https://kevinjalbert.com/integrating-notion-with-alfred/)). I also created a server web application called [`notion-heroku`](https://github.com/kevinjalbert/notion-heroku) that interacts with [IFTTT](https://ifttt.com/) and Google Assistant (read more [here](https://kevinjalbert.com/integrating-notion-with-google-assistant/)). Finally, I made a shared repository called [`notion-scripts`](https://github.com/kevinjalbert/notion-scripts) to further help the development of my tooling for Notion (read more [here](https://kevinjalbert.com/introducing-notion-scripts/).

To simplify my Notion tools I decided to merge them all into one single repository. This increases the size of the repository and some deployment/usage of individual tools. The goal is to increase cohesion to allows the tools to interact with each other better. Overall, I believe this decision will result in an easier way to use and develop with the Notion tools found here.

### The Merge

The great merge happened on December 27, 2019. `notion-heroku` and `notion-scripts` were merged into `alfred-notion` (this repository). To better represent the contents of this repository, we now use the name `notion-toolbox`.

## Author

👤 **Kevin Jalbert**

* Twitter: [@kevinjalbert](https://twitter.com/kevinjalbert)
* Github: [@kevinjalbert](https://github.com/kevinjalbert)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/kevinjalbert/notion-toolbox/issues).

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2019 [Kevin Jalbert](https://github.com/kevinjalbert).<br />
This project is [MIT](https://github.com/kevinjalbert/notion-toolbox/blob/master/LICENSE) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
