# Agile Tales

Agile Tales is a web application for managing user story maps and agile project management.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/agile-tales.git
   cd agile-tales
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```
   flask db init
   ```

5. Create the initial migration:
   ```
   flask db migrate -m "Initial migration"
   ```

6. Apply the migration to the database:
   ```
   flask db upgrade
   ```

7. (Optional) Add seed data:
   ```
   python seed_data.py
   ```

## Running the Application

To run the application, use the following command:

```
python run.py
```

The application will be available at `http://localhost:5000`.

## Database Migrations

If you make changes to the database models, create a new migration:

```
flask db migrate -m "Description of the changes"
```

Then apply the migration:

```
flask db upgrade
```

## Features

- User authentication (register, login, logout)
- Create and manage story maps
- Create and manage user stories within story maps
- Basic project management functionality

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
