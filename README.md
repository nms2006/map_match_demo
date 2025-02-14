# Map Matching Demo Dash App

This repository contains a demo Dash application for map matching, showcasing how GPS traces can be matched to a road network.

## Demo Link
You can access the live demo here: [Map Matching Demo](https://map-matching-demo.onrender.com/)

## Installation
To run the application locally, follow these steps:

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install dependencies using Poetry:
   ```sh
   poetry install
   ```

3. Run the application:
   ```sh
   poetry run python app.py
   ```

## Updating Dependencies
If you install new packages using Poetry, ensure that the requirements file is updated before committing:

```sh
poetry export --without-hashes --format=requirements.txt > requirements.txt
```

This ensures that the deployment environment has the correct dependencies.

## License
This project is licensed under the MIT License.

---

For any questions or issues, feel free to open an issue in the repository.
