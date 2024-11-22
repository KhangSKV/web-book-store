# My website book store Microservices

This repository contains two microservices:
- **Book Catalog Service**: Manages book data.
- **User Management Service**: Handles user accounts.

## Setup Instructions
1. Clone the repository:
  git clone 'https://github.com/KhangSKV/web-book-store'

2. Navigate to the project directory and create a virtual environment:
  python -m venv venv source venv/bin/activate

3. Install dependencies:
  pip install -r requirements.txt

4. Run each service:
- Book Catalog Service:
  ```
  cd book_catalog_service
  python manage.py runserver
  ```
- User Management Service:
  ```
  cd user_management_service
  python manage.py runserver 8001
  ```

## API Endpoints
- **Book Catalog Service**:
- `/catalog/`: Lists all books.
- **User Management Service**:
- `/api/users/`: Lists and creates users.


