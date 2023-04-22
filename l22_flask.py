# Lesson 1: Create a flask app

Flask is a web framework that allows you to create your own websites using Python. In this tutorial, we will create a simple website that displays a welcome message.

### What you'll need:

A computer with Python 3 installed. You can download Python from the official website: https://www.python.org/downloads/
A text editor to write code. You can use any text editor, such as Notepad or Visual Studio Code.

### Step 1: Install Flask
Open your computer's terminal or command prompt and type the following command to install Flask:

```
pip install Flask
```

Wait for the installation to complete.

### Step 2: Create a new folder
Create a new folder on your computer where you want to store your project files. Name it something like "flask_project".

### Step 3: Write the code
Open your text editor and create a new file called app.py in the "flask_project" folder. Write the following code in the file:

```
from flask import Flask #1

app = Flask(__name__) #2

@app.route('/') #4
def home(): #3
    return "Welcome to my website!"

if __name__ == '__main__': #5
    app.run(debug=True) #6
```

Save the file.

### Step 4: Understand the code
Let's break down the code we just wrote:

1. We imported Flask from the flask module.
2. We created a new Flask web app called app.
3. We created a function called home that returns the message "Welcome to my website!".
4. We used the @app.route('/') decorator to tell Flask to call the home function when someone visits the homepage of our website.
5. We used if __name__ == '__main__': to make sure our app only runs when we execute this file directly.
6. We used app.run(debug=True) to start our web app with debug mode enabled.

### Step 5: Run the app
Go back to your terminal or command prompt, navigate to the "flask_project" folder, and run the following command:

```
python app.py
```

You should see output similar to this:

```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 123-456-789
```

### Step 6: Visit your website
Open your web browser and go to the address displayed in your terminal (usually http://127.0.0.1:5000/). You should see the message "Welcome to my website!".

Congratulations! You've just created your first Flask web app. You can now explore more about Flask and create more advanced websites with different pages, forms, and user interactions. Good luck and have fun!
