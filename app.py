from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

def get_latest_data():
    # Example: get average wealth
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT AVG(wealth) FROM citizens;")
    avg_wealth = c.fetchone()[0]
    conn.close()
    return f"Average Wealth: {avg_wealth:.2f}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_data')
def update_data():
    latest_value = get_latest_data()
    return jsonify({"html": latest_value})

if __name__ == '__main__':
    app.run(debug=True)
