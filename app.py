from flask import Flask, render_template, request, redirect, url_for, g
from flask_mysqldb import MySQL
import os
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = os.urandom(24)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'flaskpia'
app.config['MYSQL_PASSWORD'] = '12345pass'
app.config['MYSQL_DB'] = 'basketball_team'

mysql = MySQL(app)

table_created = False

# Show all players
@app.route('/')
def index():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM players")
    players = cursor.fetchall()
    return render_template('index.html', players=players)

# Add new player
@app.route('/add', methods=['GET', 'POST'])
def add_player():
    if request.method == 'POST':
        name = request.form['name']
        height = request.form['height']
        weight = request.form['weight']
        age = request.form['age']
        years_playing = request.form['years_playing']
        salary = request.form['salary']
        points_per_game = request.form['points_per_game']
        rebounds_per_game = request.form['rebounds_per_game']
        steals_per_game = request.form['steals_per_game']
        blocks_per_game = request.form['blocks_per_game']
        turnovers_per_game = request.form['turnovers_per_game']
        
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO players (name, height, weight, age, years_playing, salary, points_per_game, rebounds_per_game, steals_per_game, blocks_per_game, turnovers_per_game) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (name, height, weight, age, years_playing, salary, points_per_game, rebounds_per_game, steals_per_game, blocks_per_game, turnovers_per_game)
        )
        mysql.connection.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

# Edit player
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_player(id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        name = request.form['name']
        height = request.form['height']
        weight = request.form['weight']
        age = request.form['age']
        years_playing = request.form['years_playing']
        salary = request.form['salary']
        points_per_game = request.form['points_per_game']
        rebounds_per_game = request.form['rebounds_per_game']
        steals_per_game = request.form['steals_per_game']
        blocks_per_game = request.form['blocks_per_game']
        turnovers_per_game = request.form['turnovers_per_game']
        
        cursor.execute(
            "UPDATE players SET name=%s, height=%s, weight=%s, age=%s, years_playing=%s, salary=%s, points_per_game=%s, rebounds_per_game=%s, steals_per_game=%s, blocks_per_game=%s, turnovers_per_game=%s WHERE id=%s",
            (name, height, weight, age, years_playing, salary, points_per_game, rebounds_per_game, steals_per_game, blocks_per_game, turnovers_per_game, id)
        )
        mysql.connection.commit()
        return redirect(url_for('index'))
    else:
        cursor.execute("SELECT * FROM players WHERE id = %s", (id,))
        player = cursor.fetchone()
        return render_template('edit.html', player=player)

# Delete player
@app.route('/delete/<int:id>', methods=['GET'])
def delete_player(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM players WHERE id = %s", (id,))
    mysql.connection.commit()
    return redirect(url_for('index'))

# Create table if it doesn't exist
@app.before_request
def create_tables():
    global table_created
    if not table_created:
        with mysql.connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS players (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    height FLOAT,
                    weight FLOAT,
                    age INT,
                    years_playing INT,
                    salary FLOAT,
                    points_per_game FLOAT,
                    rebounds_per_game FLOAT,
                    steals_per_game FLOAT,
                    blocks_per_game FLOAT,
                    turnovers_per_game FLOAT
                );
            """)
            mysql.connection.commit()
        table_created = True

if __name__ == '__main__':
    app.run(debug=True)
