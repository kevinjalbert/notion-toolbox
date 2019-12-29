<h1 align="center">Welcome to notion-toolbox 👋</h1>
<p align="center">
  <a href="https://github.com/kevinjalbert/notion-toolbox/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-yellow.svg" target="_blank" />
  </a>
  <a href="https://twitter.com/kevinjalbert">
    <img alt="Twitter: kevinjalbert" src="https://img.shields.io/twitter/follow/kevinjalbert.svg?style=social" target="_blank" />
  </a>
</p>

This is a collection of [Notion](https://www.notion.so/) tools that work in tandem together. All of these tools take advantage of a [specific weekly/daily template](https://kevinjalbert.com/my-weekly-notion-setup/) that integrates with various tools and solutions present in this repository.

## Tools

The following tools are available. Each tool has a README file present in its corresponding sub-directory.

- [Alfred](alfred/) workflow
  - Enables a handful of ways to interact with the template using shortcuts
- [Server](server/) application
  - Enables an online (and backgrounded) interface to interact with the template
  - Useful to connect with webhooks (e.g., IFTTT)
  - Opens integrations with Google Assistant

## History

For a good part of 2019, I focused heavily on my [Notion[Referral]](https://www.notion.so/?r=6b8d609eb50943419db4d87c67fa558e) setup. I personally feel that this was time well invested, akin to a craftsman refining his tools.

- I created a [specific weekly/daily template](https://kevinjalbert.com/my-weekly-notion-setup/) to satisfy some of my needs and give structure to Notion.
- I created an integration with [Alfred](https://www.alfredapp.com/) called [`alfred-notion`](https://github.com/kevinjalbert/alfred-notion) ([blog post](https://kevinjalbert.com/integrating-notion-with-alfred/)).
- I created a server web application called [`notion-heroku`](https://github.com/kevinjalbert/notion-heroku) that interacts with [IFTTT](https://ifttt.com/) and Google Assistant ([blog post](https://kevinjalbert.com/integrating-notion-with-google-assistant/)).
- I created a shared repository called [`notion-scripts`](https://github.com/kevinjalbert/notion-scripts) to further help the development of my tooling for Notion ([blog post](https://kevinjalbert.com/introducing-notion-scripts/)).

I recently made the decision to consolidate all my Notion related projects into a single repository. The goal is to increase cohesion to allow the tools to better interact with each other. It also puts everything in one place instead of spreading it out over multiple repositories. This approach does increase the size of the repository and the deployment/usage complexity for certain tools, but overall I feel that this decision will result in an easier way to use and develop with the Notion tools found there.

### The Great Merge

The great merge happened on December 27, 2019. On GitHub, `notion-heroku` and `notion-scripts` were merged into `alfred-notion`. I decided for `alfred-notion` to be the main repository as it had the most _stars_ on GitHub and was the longest-tenured repository I have for Notion tools. I did rename the repository to [`notion-toolbox`](https://github.com/kevinjalbert/notion-toolbox) to better represent the mission and contents of this project. Fortunately, GitHub automatically handles the redirects from `alfred-notion` to `notion-toolbox`.

I was able to retain the commit history of each project by following the approach mentioned in this article on _[How to merge two or multiple git repositories into one](https://medium.com/altcampus/how-to-merge-two-or-multiple-git-repositories-into-one-9f8a5209913f)_. This approach worked flawlessly for me, and was rather straightforward. The only thing I had to do was move each project's contents into subdirectories.

As for the merged repositories, I archived them following my approach listed in _[Archive Unused Repositories](https://kevinjalbert.com/archive-unused-repositories/)_ that I blogged about last year.

The only issue that I've hit right now is the _server_ (formerly `notion-heroku`) [expects certain files in the root directory to be deployable to Heroku](https://devcenter.heroku.com/articles/procfile#procfile-naming-and-location). I've temporarily restructured the repository so that it works, but it isn't ideal as the tool itself is bleeding outside of its sub-directory. A better solution will be found in the future.

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
