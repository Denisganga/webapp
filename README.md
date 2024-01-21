# Online Agrovet

This Django project combines user authentication features with an online agrovet platform. Users can register, log in, and explore the features of the agrovet application.
Although its an incomplete project i will be back to it as soon as possible.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Future Development](#future-development)
- [License](#license)

## Features

- User Registration
- User Login
- Homepage Access after Successful Login

## Requirements

Make sure you have the following dependencies installed inside the virtual enviroment `myworld`:

- Python 3.x
- Django
- 

## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:Denisganga/webapp.git
   ```
2. Navigate to the project directory:

```bash

cd webapp
```

3. Install dependencies:

```bash

pip install -r requirements.txt
```
4. Apply database migrations:

```bash

python manage.py migrate
```
### Usage

1.  Run the development server:

   ```bash

python manage.py runserver
```
2. Open your web browser and go to http://127.0.0.1:8000/ to access the agrovet application.

3. Register a new user and log in to explore the user authentication and agrovet features.

### Contributing

Contribution to this project is welcomed. If you would like to contribute to the project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

    ```bash

git checkout -b feature-or-bugfix-branch
```

3. Make your changes and commit them:

 ```bash

git commit -m "Your commit message here"
```

4. Push the changes to your fork:

```bash

    git push origin feature-or-bugfix-branch
```

5. Create a pull request on GitHub.

### Future Development

I plan to return and continue working on this project to enhance its features and functionality. Feel free to check back for updates.
License

### License

This project is licensed under the [MIT_license](MIT_license).
