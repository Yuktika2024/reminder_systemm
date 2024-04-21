Set Up Flask Environment:Make sure you have Flask and other required libraries installed. You can install them using pip:

pip install Flask flask-cors pywhatkit
Directory Structure:Ensure your directory structure looks like this:
css
Copy code
├── your_project_folder/
│   ├── server.py (your Flask application code)
│   ├── index.html (the HTML file you want to serve)
│   └── uploaded_images/ (directory to store uploaded images)
Place your index.html in the same directory as app.py.
Run Flask Application:Navigate to your project folder in the terminal or command prompt and run:
Copy code
python server.py
You should see output indicating that the server is running, and it should be accessible at http://127.0.0.1:5000/.
Testing the Application:
Open a web browser and go to http://127.0.0.1:5000/ to access the web page.
Upload an image using the provided form.
The image will be saved in the uploaded_images directory.
The send_repeatedly function will start sending the image to the specified WhatsApp number repeatedly at the interval you set (in this case, every 5 minutes).
Stopping the Application:To stop the Flask application, you can press Ctrl + C in the terminal or command prompt where the Flask server is running.
Make sure to replace the placeholder WhatsApp number "+9191252 02135" with a valid number you want to send the images to.

That's it! You've set up a Flask application to serve an HTML page and send images via WhatsApp using pywhatkit.
