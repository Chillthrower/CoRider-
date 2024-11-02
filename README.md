## Getting Started

Follow the instructions below to get your local copy up and running.

### Prerequisites

Make sure you have Docker and Docker Compose installed on your machine.

### Installation

1. First, clone the repository:
   ```bash
   git clone https://github.com/Chillthrower/CoRider-.git

3. Navigate into the project directory:
   ```bash
   cd CoRider-
   
5. Build and start the Docker containers: 
   ```bash
   docker compose up --build -d

### Accessing the Application

- You can check the status of all running containers with:
  ```bash
  docker ps

- The Streamlit app can be accessed at: http://localhost:8501/

### Accessing the MongoDB Database:

- To access the MongoDB database, run the following command in your terminal:
  ```bash
  docker exec -it mongodb mongosh

- Once inside the MongoDB shell, switch to the desired database:
  ```bash
  use mydatabase

- You can view the users in the database with:
  ```bash
  db.users.find().pretty()
