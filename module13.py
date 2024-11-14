import mysql.connector
from flask import Flask, request, jsonify

# 1. Implement a Flask backend service that tells whether a number received as a parameter is a prime number or not.
# Use the prior prime number exercise as a starting point.
# For example, a GET request for number 31 is given as: http://127.0.0.1:5000/prime_number/31.
# The response must be in the format of {"Number":31, "isPrime":true}.
'''
app = Flask(__name__)
@app.route('/prime/<int:num>', methods=['GET'])
def calculate_prime(num):
    try:
        if num<2:
            return jsonify({"Number": num, "isPrime": False})
        isPrime = True
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
              isPrime = False
              break
        return jsonify({"Number": num, "isPrime": isPrime})
    except(TypeError, ValueError):
        return "Invalid Input: *Please enter a valid number", 400
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=False)
'''
# 2. Implement a backend service that gets the ICAO code of an airport and then returns
# the name and location of the airport in JSON format.The information is fetched from the airport
# database used on this course.
# For example, the GET request for EFHK would be: http://127.0.0.1:5000/airport/EFHK.
# The response must be in the format of: {"ICAO":"EFHK", "Name":"Helsinki-Vantaa Airport", "Location":"Helsinki"}.

app = Flask(__name__)

database = mysql.connector.connect(
user = 'sailesh',
    password = 'sailesh1103',
    host = 'localhost',
    port = '3306',
    database = 'flight_game',
    autocommit = True,
    charset = 'utf8mb4',
    collation = 'utf8mb4_unicode_ci'
)
def fetch_airports(icao_code):
    # Fetch airport information by icao code from the database.
    cursor = database.cursor()
    sql = "select name,municipality from airport where ident = %s"
    cursor.execute(sql,(icao_code,))
    result = cursor.fetchone()
    cursor.close()
    # check if an airport was found with the given icao code
    try:
        if result:
            return {
                "ICAO": icao_code,
                "Name": result[0],
                "Location": result[1]
            }
    except(TypeError, ValueError):
        return "Invalid Input: *Please enter a valid icao code", 400

@app.route('/airport/<string:icao_code>', methods=['GET'])
def get_airport_info(icao_code):
    airport = fetch_airports(icao_code.upper())
    try:
        if airport:
            return jsonify(airport)
    except(TypeError, ValueError):
        return "Invalid Input: *Please enter a valid icao code", 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port= 5000, debug=True, use_reloader=False)