<h1 align="center">Welcome to notion-heroku 👋</h1>
<p align="center">
  <a href="https://github.com/kevinjalbert/notion-heroku/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-yellow.svg" target="_blank" />
  </a>
  <a href="https://twitter.com/kevinjalbert">
    <img alt="Twitter: kevinjalbert" src="https://img.shields.io/twitter/follow/kevinjalbert.svg?style=social" target="_blank" />
  </a>
</p>

> Heroku hosted application that performs [Notion](https://www.notion.so/) actions (i.e., new task, new note) based on voice requests via [IFTTT Webhooks](https://ifttt.com/maker_webhooks) and [Google Assistant](https://ifttt.com/google_assistant).

## Prerequisites

1. Have a [Notion](https://www.notion.so/) account
2. Have a [Heroku](https://heroku.com/) account
3. Have an [IFTTT](https://ifttt.com/) account (with Google Assistant service enabled)
4. Have [Specific Notion Template](https://www.notion.so/Week-Template-0a7ac4d03082417c929176b5ea1df07e) as described in [this blog post](https://kevinjalbert.com/my-weekly-notion-setup/)
5. Your Notion Token
6. URLs for Several Notion Object

## Install

_Note:_ The required environment variables mentioned in the below steps are outlined in [kevinjalbert/alfred-notion](https://github.com/kevinjalbert/alfred-notion)'s section on [finding your Notion Token](https://github.com/kevinjalbert/alfred-notion#finding-your-notion-token) and [finding your Notion URLs](https://github.com/kevinjalbert/alfred-notion#finding-your-notion-urls).

### With Heroku Deploy Button
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

1. Use above deploy button to create/launch application on [Heroku](https://heroku.com/)
2. Navigate to application settings page (i.e., https://dashboard.heroku.com/apps/your-notion-heroku/settings) and set required environment variables.

### Manually

1. Clone the repository via `git clone git@github.com:kevinjalbert/notion-heroku.git`
2. `heroku create`
3. `git push heroku master`
4. Set all required environment variables via `heroku config:set xxxx=yyyy`

## Author

👤 **Kevin Jalbert**

* Twitter: [@kevinjalbert](https://twitter.com/kevinjalbert)
* Github: [@kevinjalbert](https://github.com/kevinjalbert)

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
