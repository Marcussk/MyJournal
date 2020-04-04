import os

from myjournal import app
from myjournal.api import user


if __name__ == '__main__':
    port_number = int(os.environ.get('MYJOURNAL_PORT', 33507))
    app.run(host="0.0.0.0", port=port_number, threaded=True, debug=True)