# Kanban Project

This is a Dockerized Kanban board application that includes a **React frontend**, **FastAPI backend**, and a **PostgreSQL database**. The application allows users to manage tasks with features like task creation, updating, and deletion, while ensuring data integrity and secure access.

## Features
- User authentication and authorization
- Task management (create, read, update, delete tasks)
- Boards for organizing tasks
- Frontend built with React and styled components
- Backend API powered by FastAPI
- Database integration with PostgreSQL
- Nginx as a reverse proxy and static file server

## Project Structure
```
├── README.md
├── backend
│   ├── Dockerfile
│   ├── auth
│   │   ├── auth_utils.py
│   │   └── dependencies.py
│   ├── db
│   │   └── connection.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── board_model.py
│   │   ├── task_model.py
│   │   └── user_model.py
│   ├── requirements.txt
│   ├── routes
│   │   ├── board_routes.py
│   │   ├── task_routes.py
│   │   └── user_routes.py
│   └── schemas
│       ├── board_schemas.py
│       ├── task_schemas.py
│       └── user_schemas.py
├── docker-compose.yml
└── frontend
    ├── Dockerfile
    ├── nginx.conf
    ├── package.json
    ├── public
    │   └── index.html
    └── src
        ├── App.js
        ├── Auth
        │   ├── Login.js
        │   ├── Register.js
        │   └── auth.css
        ├── Boards
        │   ├── Board.js
        │   ├── BoardList.js
        │   └── boards.css
        ├── Context
        │   └── AuthContext.js
        ├── Navbar.css
        ├── Navbar.js
        ├── ProtectedRoute.js
        ├── Tasks
        │   ├── Task.js
        │   ├── TaskList.js
        │   └── tasks.css
        ├── Utils
        │   └── axiosInstance.js
        ├── config.js
        ├── index.css
        └── index.js
```

## Prerequisites
- Docker and Docker Compose installed
- Node.js (for local frontend development)
- Python 3.9+ (for local backend development)

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/kanban.git
cd kanban
```

### 2. Build and Run the Application
Using Docker Compose:
```bash
docker-compose up --build
```

The application will be available at:
- Frontend: [http://localhost:3000](http://localhost:3000)
- Backend API: [http://localhost:8000/api](http://localhost:8000/api)

### 3. Environment Variables
Configure the following environment variables in a `.env` file:
```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=yourpassword
POSTGRES_DB=kanban
POSTGRES_HOST=db
POSTGRES_PORT=5432
```



## API Endpoints
Base URL: `/api`

### Authentication
- `POST /api/auth/login`: Login a user
- `POST /api/auth/register`: Register a new user

### Tasks
- `GET /api/tasks`: Get all tasks for the logged-in user
- `POST /api/tasks`: Create a new task
- `PUT /api/tasks/{task_id}`: Update a task
- `DELETE /api/tasks/{task_id}`: Delete a task

### Boards
- `GET /api/boards`: Get all boards
- `POST /api/boards`: Create a new board

## Technology Stack
- **Frontend**: React, Axios
- **Backend**: FastAPI, SQLAlchemy
- **Database**: PostgreSQL
- **Web Server**: Nginx
- **Testing**: Pytest (backend), Jest (frontend)
- **Containerization**: Docker, Docker Compose

## Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

## License
This project is licensed under the MIT License. See the LICENSE file for details.

