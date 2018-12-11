# A NOT SO USEFUL CRYPTO WEBSERVICE 

## Intentions

- Provide 3 API Endpoints : PushAndRecalculate, PushRecalculateAndEncrypt, Decrypt
- Asymmetric Key Encryption , single key on server side for encrypt and decrypt functions
- Calculate Running Average, Running Deviation for given series of inputs
- Swagger API Spec in docs/

### Usage

```bash
pip install -r requirements.txt
python run.py
```

```bash
curl -X POST http://127.0.0.1:8080/api/decrypt -d "<encryptedString>"

curl -X POST http://127.0.0.1:8080/api/pushrecalculateandencrypt -d "1"

curl -X POST http://127.0.0.1:8080/api/pushandrecalculate -d "1"
```


To run tests :  `cd app/tests/;python test_main.py`
*** Using sys path module for test script to import app , please make sure current working directory is within app/tests/ before running the test script. 

To reset statistics : `curl -X GET http://127.0.0.1:8080/api/reset`

API Specification is listed in the docs/

NOTE:
> Please uninstall Crypto, pycrypto python modules if previously installed (MacOS X) and then run pip install requirements

> Windows Machines would need  Microsoft Visual C++ 9.0  to install pycrypto ( https://www.microsoft.com/en-us/download/details.aspx?id=44266 ) 

> References listed in `docs/`

> Default port listed in run.py is 8080 

#### Future Enhancements
- Better logging 
- Custom Error handling for  4xx / 5xx errors
- End to End test cases
- Input Validation 
