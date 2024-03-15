import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to list tar files in a folder
def list_tar_files(folder_path):
    tar_files = []
    for file in os.listdir(folder_path):
        if file.endswith('.tar'):
            tar_files.append(file)
    return tar_files

@app.route('/')
def index():
    # Folder containing tar files
    folder_path = '/home/pc4/Documents/develop/worker-django/media/storage'
    # Get the list of tar files
    tar_files = list_tar_files(folder_path)
    return render_template('index.html', tar_files=tar_files)

@app.route('/transfer', methods=['POST'])
def transfer_file():
    # Get the selected tar file
    selected_file = request.form['selected_file']
    # Execute SCP command to transfer the file
    os.system(f'scp /home/pc4/Documents/develop/worker-django/media/storage/{selected_file} jetson@172.28.235.251:/home/jetson/Desktop')
    return 'File transferred successfully'

if __name__ == '__main__':
    app.run(debug=True)
