
## Setup

1. **Install dependencies**:
    ```sh
    pip install fastapi uvicorn
    ```

2. **Run the application**:
    ```sh
    uvicorn main:app --reload --log-level info
    ```

## Endpoints

- **GET /**: Returns a welcome message.

## Example

To test the application, run the following command and navigate to `http://127.0.0.1:8000` in your browser:

to see doc swagger:  `http://127.0.0.1:8000/docs`

```sh
uvicorn main:app --reload

```

### Postman collection

Postman collection on root folder ./redis.postman_collection.json