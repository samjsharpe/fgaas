#!/usr/bin/env python

import os

from flask import Flask, jsonify

# initialization
app = Flask(__name__)

@app.route("/fucks/<int:fnumber>")
def fucks(fnumber):
    return jsonify(fucks=fnumber)


# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
