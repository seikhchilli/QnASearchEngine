from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users')
def get_users():
    users = [
        {
            'name': 'Alice',
            'email': 'alice@example.com'
        },
        {
            'name': 'Bob',
            'email': 'bob@example.com'
        }
    ]
    return jsonify(users)

if __name__ == '__main__':
    app.run()