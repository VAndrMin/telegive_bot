# telegive_bot

This is a Telegram bot that helps users subscribe to channels and keeps track of their subscriptions.

## Get Started

1. Clone the repository to your local machine:
   ```
   git clone git@github.com:<your-username>/<project-name>.git
   ```
2. Create a new virtual environment:
   ```
   python3 -m venv venv
   ```
3. Activate the virtual environment:
   ```
   source venv/bin/activate
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Create a new bot on Telegram using the BotFather and get your bot token.
6. Copy the `.env.example` file to `.env` and update the `TELEGRAM_BOT_TOKEN` variable with your bot token.
7. Run the bot:
   ```
   python bot.py
   ```

You're now ready to use the bot! Send a message to your bot and it will respond with instructions on how to use it.

## Adding New Packages

If you need to add a new Python package to this project, follow these steps:

1. Activate your virtual environment:
   ```
   source venv/bin/activate
   ```
2. Use `pip` to install the package:
   ```
   pip install <package-name>
   ```
3. Freeze the new requirements:
   ```
   pip freeze > requirements.txt
   ```
4. Commit the changes to `requirements.txt` and push to the remote repository.

Note: If you're working with others on this project, make sure to communicate any changes to the `requirements.txt` file
to avoid conflicts when merging changes. It's also a good idea to periodically update the `requirements.txt` file with
the latest package versions using `pip freeze --update`.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch for your changes
3. Make your changes and commit them
4. Push your changes to your fork
5. Submit a pull request

We welcome all contributions, big and small!

## License

This project is licensed under the [MIT License](LICENSE).
