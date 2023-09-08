from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# Endpoint for retrieving information
@app.route('/info', methods=['GET'])
def get_info():
    # Retrieve query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get the current day of the week
    current_day = datetime.datetime.utcnow().strftime("%A")
    
    # Get the current UTC time as a formatted string
    current_utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    github_file_url = 'https://github.com/walescript/HNG-stage1/blob/main/Stage_1/main.py'
    github_repo_url = 'https://github.com/walescript/HNG-stage1/tree/main'


    # Create a response JSON
    response = {
        'slack_name': slack_name,
        'current_day': current_day,
        'current_utc_time': current_utc_time,
        'track': track,
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': 200
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
