from flask import Flask
from helpers.assertions import AssertThat
from constants import Ns
from integral import sample

app = Flask(__name__)


@app.route("/integral/<lower>/<upper>")
def fetch(lower: float = None, upper: float = None):
    AssertThat(lower).isLessThan(upper)
    values = ','.join(map("{:10.10f}".format, sample(float(lower), float(upper), Ns)))
    file = "\n".join([values])
    return app.response_class(file, mimetype='text/csv')

if __name__ == "__main__":
    app.run()