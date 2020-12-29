import os

SERVER_ADDRESS: str = os.getenv('SERVER_ADDRESS')
SERVER_PORT: str = int(os.getenv('SERVER_PORT') or -1)
SERVER_DEBUG_MODE: bool = bool(os.getenv('SERVER_DEBUG_MODE') == 'True')

API_KEY: str = os.getenv('API_KEY')