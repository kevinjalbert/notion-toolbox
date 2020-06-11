Display your current task in the menubar. If you click on the bitbar area it will open the notion to that task.

# Installation

1. Have https://github.com/matryer/bitbar installed
2. hardlink `show_current_tasks.sh` to the bitbar plugin directory.
  `ln ./show_current_tasks.sh /Users/jalbert/bitbar`
  bitbar doesn't support symlinks (atleast I could get them to work)
3. Make sure that the required exports for Notion are sourced (e.g., in the default position they are in the `~/.secret` file)
  like:

  ```
  export NOTION_TOKEN=""
  export TASKS_DATABASE_URL=""
  ```
