from flask import Flask, jsonify
from math import isqrt

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/alkuluku/<int:number>', methods=['GET'])
def check_prime(number):
    result = {"Number": number, "isPrime": is_prime(number)}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
