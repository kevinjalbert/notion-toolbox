# Scriptable -- Notion Block View

This is a [Scriptable](https://scriptable.app/) widget that provides basic functionality for viewing/creating/deleting Notion blocks.

<img src="./images/widget.jpg" width="100%">

# Make README md 1611a8ff3dd64c2aae3124a5822142a2

# Description

This repository contains code and short instructions for creating a widget filled with data from your database in Notion.

«Scriptable» automatically updates the information inside the widget every 5-7 minutes.

## Brief description of the widget features:

1. Clicking on a widget - when clicked launches a main script branch that launches the Notion app
2. Text strings - contain text from one of the fields in your Notion database. When you click on the text, a branch of the main script is called, which opens the corresponding page in Notion
3. Circle before each entry - calls a script that transfers the task to the final status (for example: Done)
4. Square with a handle - The button calls Alert, with which you can create a task in the initial status.
5. Round Arrow - Forces a widget refresh.

# Installation

1. Create a new database or use [my template](https://www.notion.so/77bcd7e231d84566a2959e6abea33c2d).
    1. It should be understood that the database may have:
        1. Other structure
        2. Other field names
        3. Status names
        4. And so on.
    2. To do this, you will need to change the corresponding lines in the script code.
2. Follow the steps from [this instruction](https://developers.notion.com/docs)
    1. At this step, it is important to save
        1. Your API Token
        2. Your Database ID
3. [Install Scriptable](https://apps.apple.com/ru/app/scriptable/id1405459188) from the App Store 
4. Create 3 scripts in Scriptable (names are important and case-sensitive)
    1. [to-do](https://github.com/homerostov/notion-toolbox/blob/master/ios_widget/to_do.js)
    2. [task_done](https://github.com/homerostov/notion-toolbox/blob/master/ios_widget/task_done.js)
    3. [new_task](https://github.com/homerostov/notion-toolbox/blob/master/ios_widget/new_task.js)
5. Go to [to_do](https://github.com/homerostov/notion-toolbox/blob/master/ios_widget/to_do.js#:~:text=let%20notion_token%20%3D-,%3CYour_notion_token%3E,-%3B) script and paste your Token Notion API
6. Add widget
    1. Call the menu for changing the widget and specify the following parameters
        1. Script: to_do
        2. When interacting: Run Script
        3. Parameter: [Your Database ID]
    2. Click Done
7. After a few seconds, the widget will update and display pages from your Notion database
