from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)

@app.route('/ntop')
def ntop():
    try:
        # Get full name (replace with your actual name)
        full_name = "Sathvik S"  # Replace this with your actual name
        
        # Get system username (with error handling if it fails)
        try:
            system_username = "codespace"
        except Exception as e:
            system_username = f"Error fetching username: {e}"
        
        # Get server time in IST
        ist_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        
        # Run the 'top' command and capture its output (with error handling)
        try:
            top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
        except subprocess.CalledProcessError as e:
            top_output = f"Error running 'top' command: {e}"

        # Format the output
        output = f"""
        <h2>Name: {full_name}</h2>
        <h3>User: {system_username}</h3>
        <h3>Server Time (IST): {ist_time}</h3>
        <strong>TOP Output:</strong><br>
        <pre>{top_output}</pre>
        """
        return output
    
    except Exception as e:
        return f"An unexpected error occurred: {e}"

if __name__ == '__main__':
    # Make the app publicly visible with '0.0.0.0' host
    app.run(host='0.0.0.0', port=5000)
