# To-Do List Telegram Bot

This is a Telegram bot for managing a to-do list, built using Python and the Pyrogram library. Users can add, view, edit, and delete their daily tasks using this bot.

## 🚀 Features

  * **Automatic Registration and Login**: Users are automatically registered the first time they use the bot.
  * **Add New Task**: Users can add new tasks with a title and description to their list.
  * **View To-Do List**: Displays all the tasks registered for the user.
  * **Edit Tasks**: Allows editing the title and description of existing tasks.
  * **Delete Tasks**: Removes tasks from the list.
  * **Database**: Uses SQLite to store user information and tasks.

## 🛠️ Technologies Used

  * **Python**: The main programming language.
  * **Pyrogram**: A modern, elegant, and asynchronous framework for building Telegram bots.
  * **SQLAlchemy**: For interacting with the SQLite database.
  * **Pyromod**: To simplify user interactions in Pyrogram.

## ⚙️ Setup and Run

To run this project, follow these steps:

1.  First, clone the project:

    ```bash
    git clone <URL_REPOSITORY>
    ```

2.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3.  Replace the `BOT_TOKEN`, `APP_ID`, and `API_HASH` values in the `__main__.py` file with your actual values.

    ```python
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN")
    APP_ID = os.environ.get("APP_ID", "YOUR_APP_ID")
    API_HASH = os.environ.get("API_HASH", "YOUR_API_HASH")
    ```

4.  Run the application:

    ```bash
    python -m __main__
    ```

## 📂 Project Structure

```
.
├── __main__.py         # Application entry point
├── database/
│   ├── models.py       # Database models (User, Todo)
│   └── database.db     # SQLite database file
├── plugins/
│   ├── start.py        # /start command and main buttons
│   ├── login_check.py  # User check and registration
│   └── Todo/
│       ├── create_todo.py    # Logic for adding a new task
│       └── todo_list_view.py # View, edit, and delete tasks
├── .gitignore          # Files to be ignored by Git
└── README.md           # This file
