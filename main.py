from flask import Flask, jsonify, request

app = Flask(__name__)

# This block is the error handler. It formats the error message
# into JSON, sets the status code to 400, then returns everything.
@app.errorhandler(ValueError)
def handle_value_exception(error):
    response = jsonify(message=str(error))
    response.status_code = 400
    return response

@app.route("/fibonacci")
# This little block returns the user input "n" as well as 
# the calculated result in JSON format.
def fib():
    n = request.args.get("n", None)
    return jsonify(n=n, result=calcfib(n))

# This block does the actual computation using user input
# "n", and returns an exception if the user input is outside
# the predetermined (and arbitrary) range of 1-90.
def calcfib(n):
    try:
        n = int(n)
        assert 1 <= n <= 90
    except (ValueError, AssertionError) as e:
        raise ValueError("n must be between 1 and 90") from e

    a, b = 0, 1  # a, b initialized as F(0), F(1)
    for _ in range(1, n):
        a, b = b, a+b  # a, b always store F(i-1), F(i)
    return a

# Runs the app on a predefined port. 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)