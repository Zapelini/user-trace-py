import os

from config.app import create_app

app = create_app('config.default.' + os.getenv("APP_ENV", 'Production'))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
