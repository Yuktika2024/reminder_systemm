from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import pywhatkit 
import time
import threading

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        files = request.files.getlist("images")
        
        if len(files) == 0:
            return jsonify({"success": False, "message": "No image uploaded"}), 400

        # Assuming only one image is uploaded
        file = files[0]
        filename = file.filename
        image_path = f"uploaded_images/{filename}"
        file.save(image_path)
        
        print(f"Image {filename} saved")
        
        # Start a thread to send the image repeatedly
        thread = threading.Thread(target=send_repeatedly, args=(["+9191252 02135", image_path, "NILI GOLI KHAOOOOOOOOO", 5]))
        thread.start()

        return jsonify({"success": True, "message": f"Image {filename} saved and will be sent repeatedly"}), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({"success": False, "message": str(e)}), 500

def send_repeatedly(MobileNo, imagePath, caption, interval_minutes):
    try:
        while True:
            pywhatkit.sendwhats_image(MobileNo, imagePath, caption, 20)
            print(f"Image sent to {MobileNo}")
            time.sleep(interval_minutes * 60)
    except KeyboardInterrupt:
        print("\nImage sending stopped.")

if __name__ == '__main__':
    if not os.path.exists("uploaded_images"):
        os.makedirs("uploaded_images")
    
    app.run(debug=True)
