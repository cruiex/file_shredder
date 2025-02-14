from flask import Flask, request, jsonify, send_from_directory, redirect, url_for
import os
from flask_cors import CORS
import shutil
app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads/'
ENCRYPTED_FOLDER = 'encrypted/'
DECRYPTED_FOLDER = 'decrypted/'  # Folder for decrypted files
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ENCRYPTED_FOLDER, exist_ok=True)
os.makedirs(DECRYPTED_FOLDER, exist_ok=True)

# Helper function to encrypt files (simulated for now)
def encrypt_files(file_paths):
    encrypted_files = []
    for file_name in file_paths:
        file_path = os.path.join(UPLOAD_FOLDER, file_name)
        encrypted_file_path = os.path.join(ENCRYPTED_FOLDER, f"encrypted_{file_name}")
        
        # Simulated encryption by reversing file content
        with open(file_path, 'rb') as f_in, open(encrypted_file_path, 'wb') as f_out:
            data = f_in.read()
            f_out.write(data[::-1])  # Reverse content as "encryption"
        
        encrypted_files.append(f"encrypted_{file_name}")
    
    return encrypted_files

# Helper function to decrypt files (simulated for now)
def decrypt_files(file_paths):
    decrypted_files = []
    for file_name in file_paths:
        file_path = os.path.join(ENCRYPTED_FOLDER, file_name)
        decrypted_file_path = os.path.join(DECRYPTED_FOLDER, f"decrypted_{file_name}")
        
        # Simulated decryption by reversing the file content back
        with open(file_path, 'rb') as f_in, open(decrypted_file_path, 'wb') as f_out:
            data = f_in.read()
            f_out.write(data[::-1])  # Reverse content back to original
        
        decrypted_files.append(f"decrypted_{file_name}")
    
    return decrypted_files

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    files = request.files.getlist('files')
    saved_files = []
    
    for file in files:
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        saved_files.append(file.filename)

    return jsonify({'message': 'Files uploaded successfully', 'files': saved_files}), 200

@app.route('/encrypt', methods=['POST'])
def encrypt_endpoint():
    # Clear the encrypted folder before processing new files
    for filename in os.listdir(ENCRYPTED_FOLDER):
        file_path = os.path.join(ENCRYPTED_FOLDER, filename)
        if os.path.isfile(file_path):
            os.unlink(file_path)  # Delete old encrypted files

    # Fetch files from the upload folder for encryption
    uploaded_files = os.listdir(UPLOAD_FOLDER)
    
    if not uploaded_files:
        return jsonify({'error': 'No files available for encryption'}), 400

    # Encrypt the files
    encrypted_files = encrypt_files(uploaded_files)
    
    # Redirect to the first encrypted file to trigger download
    return redirect(url_for('get_encrypted_file', filename=encrypted_files[0]))

@app.route('/decrypt', methods=['POST'])
def decrypt_endpoint():
    # Clear the decrypted folder before processing new decryption
    for filename in os.listdir(DECRYPTED_FOLDER):
        file_path = os.path.join(DECRYPTED_FOLDER, filename)
        if os.path.isfile(file_path):
            os.unlink(file_path)  # Delete old decrypted files

    # Fetch encrypted files for decryption
    encrypted_files = os.listdir(ENCRYPTED_FOLDER)
    
    if not encrypted_files:
        return jsonify({'error': 'No files available for decryption'}), 400

    # Decrypt the files
    decrypted_files = decrypt_files(encrypted_files)
    
    # Return list of decrypted files (or you can redirect to the first one)
    return jsonify({'message': 'Files decrypted successfully', 'decrypted_files': decrypted_files}), 200

@app.route('/encrypted/<filename>', methods=['GET'])
def get_encrypted_file(filename):
    # Serve the encrypted file to trigger the download
    return send_from_directory(ENCRYPTED_FOLDER, filename)

@app.route('/decrypted/<filename>', methods=['GET'])
def get_decrypted_file(filename):
    # Serve the decrypted file to trigger the download
    return send_from_directory(DECRYPTED_FOLDER, filename)

@app.route('/list-encrypted', methods=['GET'])
def list_encrypted_files():
    # List the encrypted files after encryption
    encrypted_files = os.listdir(ENCRYPTED_FOLDER)
    return jsonify({'encrypted_files': encrypted_files}), 200

@app.route('/list-decrypted', methods=['GET'])
def list_decrypted_files():
    # List the decrypted files after decryption
    decrypted_files = os.listdir(DECRYPTED_FOLDER)
    return jsonify({'decrypted_files': decrypted_files}), 200

if __name__ == '__main__':
    app.run(debug=True)




@app.route('/shred', methods=['POST'])
def shred_files():
    # Delete all files in the upload, encrypted, and decrypted folders
    try:
        shutil.rmtree(UPLOAD_FOLDER)
        shutil.rmtree(ENCRYPTED_FOLDER)
        shutil.rmtree('decrypted/')  # Adjust the path if necessary

        # Recreate the folders to keep the structure intact
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        os.makedirs(ENCRYPTED_FOLDER, exist_ok=True)
        os.makedirs('decrypted/', exist_ok=True)

        return jsonify({'message': 'Files shredded successfully'}), 200
    except Exception as e:
        return jsonify({'error': f'Error shredding files: {str(e)}'}), 500
