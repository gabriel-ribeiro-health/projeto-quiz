from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_root():
    return {"message": "Hello World"}


#https://www.alura.com.br/artigos/como-criar-apis-python-usando-fastapi?utm_term=&utm_campaign=%5BSearch%5D+%5BPerformance%5D+-+Dynamic+Search+Ads+-+Artigos+e+Conte%C3%BAdos&utm_source=adwords&utm_medium=ppc&hsa_acc=7964138385&hsa_cam=11384329873&hsa_grp=164240702375&hsa_ad=703853654617&hsa_src=g&hsa_tgt=dsa-2276348409543&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=CjwKCAjw9p24BhB_EiwA8ID5BnW-RGA9A-LR06ET1OlSp6NVT5aSfcYK4ohBE6wwwpuLRMELCOfyIhoCnNoQAvD_BwE