from flask import Flask, render_template, jsonify

from lib.stats import RedisMonitor
from settings import SERVERS

import simplejson, datetime

redis_monitor = RedisMonitor(SERVERS)

# initialize flask application
app = Flask(__name__)

# main view
@app.route('/')
def hello_world():
    stats = redis_monitor.getStats()
    return render_template('main.html', stats = stats)

# ajax view (json)
@app.route('/ajax')
def ajax():
    stats           = redis_monitor.getStats(True)
    datetimeHandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None
    return simplejson.dumps(stats, default = datetimeHandler)

# run the app.
if __name__ == '__main__':
    app.debug = True
    app.run()
