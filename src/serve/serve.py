from flask import Flask, request, jsonify
from flask_cors import CORS  # Importer CORS
import os
import subprocess
import os
import subprocess

app = Flask(__name__)
CORS(app)  # Activer CORS pour toutes les routes

fake_db = [""]



def try_execute(command):
    try:
        # Get the cleaned command to execute
        cleaned_command = command.get('name', '').strip()
        print(f"Executing command: {cleaned_command}")

        # Handle 'cd' command separately (change directory in the current process)
        if cleaned_command.startswith("cd "):
            # Extract the directory from the command
            directory = cleaned_command[3:].strip()
            os.chdir(directory)  # Change the current working directory
            return f"Changed directory to {directory}"

        # Run other commands using subprocess (e.g., ls, touch)
        command_list = cleaned_command.split()
        result = subprocess.run(command_list, capture_output=True, text=True)

        if result.returncode != 0:
            return f"Error: {result.stderr}"

        print("Result:", result.stdout)
        return result.stdout

    except Exception as e:
        return str(e)


@app.route('/api/data', methods=['GET'])
def get_data():
    cleaned_data = [item.replace('(', '').replace(')', '') for item in fake_db]
    return jsonify(cleaned_data), 200

@app.route('/api/data', methods=['POST'])
def add_data():
    data = request.json
    execute_result = "Command not executed due to invalid characters."

    if data and 'name' in data:
        command = data['name']
        if '(' not in command and ')' not in command:
            execute_result = try_execute(data)

    response = {
        "message": "Data added successfully",
        "data": execute_result
    }
    if (execute_result == "Command not executed due to invalid characters."):
        fake_db.append(data)
    return jsonify(response), 201

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
