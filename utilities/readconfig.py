from pathlib import Path
import configparser

# Create config parser
config = configparser.RawConfigParser()

# Get absolute path to config.ini
from pathlib import Path
base_dir = Path(__file__).resolve().parent.parent
config_path = base_dir / "Configuration" / "config.ini"

# Read the config file
config.read(config_path)



class ReadConfig:

    @staticmethod
    def get_login_url():
        login_url = config.get('application url', 'login_url')
        return login_url

    @staticmethod
    def get_username():
        username = config.get('login data', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('login data', 'password')
        return password

