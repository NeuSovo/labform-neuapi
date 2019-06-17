import sys
sys.path.append('utils')

from apps import create_app
import config

if __name__ == '__main__':
    app = create_app(config=config)
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=False)
