# REST Backend Project

## Steps to Run This Project

1. **Download the project directory**
2. **Open the directory in a terminal**
3. **Run the server**
   ```sh
   python manage.py runserver
   ```
4. **Check the API using Postman**

## API Endpoints

- **User Registration** (POST)
  ```
  localhost:8000/register
  ```
- **User Login** (POST) - Obtain Access Token
  ```
  localhost:8000/login
  ```
- **Create a To-Do** (POST) - Requires Authorization
- **Delete a To-Do** (DELETE) - Replace `id` with the actual To-Do ID
  ```
  localhost:8000/todos/{id}/
  ```

Make sure to include the access token in the request headers when creating or deleting a To-Do item.


