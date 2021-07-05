from flask import Flask, request
from time import sleep
from random import randint
import sys
app = Flask(__name__)


@app.route("/")
def hello():
    user: str = request.args.get('user')
    sleep(randint(1,5))  # sleep for 5 seconds, to simulate delay in request
    return user.upper()

#  curl -X GET "http://127.0.0.1:5000/?user=arnabsudesh"


if __name__ == '__main__':
    app.run(port=int(sys.argv[1]))
