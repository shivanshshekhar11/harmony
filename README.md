# Harmony

Harmony is a Django-based discussion platform that allows users to create rooms, discuss various topics, and interact with each other in real-time. It provides a clean and organized way to host discussions on specific subjects.

## Features

- **User Authentication**: Users can register, login, and logout securely.
- **Rooms**: Users can create, update, and delete discussion rooms.
- **Topics**: Rooms are categorized by topics for better organization.
- **Messaging**: Real-time-like messaging within rooms.
- **Search**: Search functionality for rooms, topics, and users.
- **User Profiles**: View user profiles and their activity.
- **API**: A RESTful API to access room data programmatically.

## Tech Stack

- **Backend**: Python, Django
- **API**: Django REST Framework
- **Database**: SQLite (default, easy to switch to PostgreSQL/MySQL)

## Getting Started

Follow these steps to set up the project locally.

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd harmony
    ```

2.  **Create a virtual environment (optional but recommended):**

    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (optional):**

    To access the Django admin panel:

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the server:**

    ```bash
    python manage.py runserver
    ```

    The application will be available at `http://127.0.0.1:8000/`.

## Usage

1.  **Register/Login**: Create a new account or log in with existing credentials.
2.  **Explore Rooms**: Browse available rooms on the homepage or search for specific topics.
3.  **Join Discussion**: Enter a room to view messages and participate in the conversation.
4.  **Create Room**: Click on "Create Room" to start a new discussion topic.

## API Documentation

The project includes a basic API built with Django REST Framework.

-   **Base URL**: `api/`
-   **Get All Routes**: `GET /api/`
-   **Get All Rooms**: `GET /api/rooms/`

## License

This project is open source and available under the [MIT License](LICENSE).
