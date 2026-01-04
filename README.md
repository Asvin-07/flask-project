🚀 Flask REST API with Docker

A containerized RESTful API built with Python and Flask. This project demonstrates backend development fundamentals including API design, containerization, and dynamic configuration.

Live Demo: [[Link to your Render App Will Go Here](https://flask-project-tzzq.onrender.com/)]

✨ Features

REST Architecture: Clean GET, POST, and DELETE endpoints.

Dockerized: Fully portable container setup.

Configurable: Supports configuration via CLI flags and Environment variables.

🛠️ Tech Stack

Python 3.11

Flask

Docker

Git

🚀 How to Run Locally

Clone the repo

git clone [https://github.com/YOUR_USERNAME/flask-personal-project.git](https://github.com/YOUR_USERNAME/flask-personal-project.git)


Build the Image

docker build -t flask-app .


Run the Container

docker run -p 5000:5000 -e PORT=5000 flask-app


🔌 Endpoints

GET /: Health check.

GET /items: Fetch all items.

POST /items: Create item ({"id": "1", "name": "Test"}).

DELETE /items/<id>: Delete item.
