"""Action Run The Application"""

# Libraries
from os import getenv
from dotenv import load_dotenv

# Modules
from src import create_server

load_dotenv()


if __name__ == '__main__':
    config_name = getenv('ENV', 'local')
    app = create_server('flask', config_name)
    app.run()
