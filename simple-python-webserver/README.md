# Simple Python Webserver

This project is a simple web server built using Flask. It listens on port 5000 and provides a status page endpoint that returns the server's status.

## Project Structure

```
simple-python-webserver
├── app.py
├── requirements.txt
└── README.md
```

## Requirements

To run this project, you need to have Python installed on your machine. You also need to install the required dependencies listed in `requirements.txt`.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd simple-python-webserver
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Server

To start the Flask web server, run the following command:

```
python app.py
```

The server will start and listen on `http://localhost:5000`.

## Accessing the Status Page

Once the server is running, you can access the status page by navigating to:

```
http://localhost:5000/status
```

This will return the current status of the server.