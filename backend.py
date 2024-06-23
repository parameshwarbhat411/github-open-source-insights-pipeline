from flask import Flask, jsonify, request
import duckdb

app = Flask(__name__)


def get_latest_repos():
    # Connect to your database (update the connection string as needed)
    conn = duckdb.connect('file.db')
    cursor = conn.cursor()

    # Fetch the latest named repos
    query = """
    SELECT repo_id, repo_name
    FROM file.main.dim_repos
    WHERE end_date IS NULL
    """
    cursor.execute(query)
    repos = cursor.fetchall()

    # Convert to a list of dictionaries
    repo_list = [{'repo_id': row[0], 'repo_name': row[1]} for row in repos]

    conn.close()
    return repo_list


def get_repo_data(repo_id):
    # Connect to your database (update the connection string as needed)
    conn = duckdb.connect('file.db')
    cursor = conn.cursor()

    # Fetch data for the specific repo
    query = """
    SELECT * FROM file.main.fact_stars_monthly
    WHERE repo_id = ?
    """
    cursor.execute(query, (repo_id,))
    data = cursor.fetchall()

    conn.close()
    return data


@app.route('/repo_data', methods=['GET'])
def repo_data():
    repo_id = request.args.get('repo_id')
    data = get_repo_data(repo_id)
    return jsonify(data)

@app.route('/latest_repos', methods=['GET'])
def latest_repos():
    repos = get_latest_repos()
    return jsonify(repos)


if __name__ == '__main__':
    app.run(debug=True)