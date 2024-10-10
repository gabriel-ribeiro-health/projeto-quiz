
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

#https://www.alura.com.br/artigos/como-criar-apis-python-usando-fastapi?utm_term=&utm_campaign=%5BSearch%5D+%5BPerformance%5D+-+Dynamic+Search+Ads+-+Artigos+e+Conte%C3%BAdos&utm_source=adwords&utm_medium=ppc&hsa_acc=7964138385&hsa_cam=11384329873&hsa_grp=164240702375&hsa_ad=703853654617&hsa_src=g&hsa_tgt=dsa-2276348409543&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=CjwKCAjw9p24BhB_EiwA8ID5BnW-RGA9A-LR06ET1OlSp6NVT5aSfcYK4ohBE6wwwpuLRMELCOfyIhoCnNoQAvD_BwE

```sh
uvicorn main:app --reload

## Endpoints

- **GET /**: Returns a welcome message.
```

### Postman collection

Postman collection on root folder ./redis.postman_collection.json