# A NOT SO USEFUL CRYPTO WEBSERVICE 

## Intentions

- Provide 3 API Endpoints : PushAndRecalculate, PushRecalculateAndEncrypt, Decrypt
- Asymmetric Key Encryption , single key on server side for encrypt and decrypt functions
- Calculate Running Average, Running Deviation for given series of inputs
- Swagger API Spec in docs/

### Usage

```bash
pip install -r requirements.txt
python src/main.py
```

```curl -X POST http://127.0.0.1:8080/api/decrypt -d "<encryptedString>"
```

```curl -X POST http://127.0.0.1:8080/api/pushrecalculateandencrypt -d "1"
```

```curl -X POST http://127.0.0.1:8080/api/pushandrecalculate -d "1"
```

To run tests :  `python app/tests/test_main.py`

To reset statistics : `curl -X GET http://127.0.0.1:8080/api/reset`

API Specification is listed in the docs/

NOTE:
> Please uninstall Crypto, pycrypto python modules if previously installed (MacOS X) and then run pip install requirements
> References listed in `docs/`
> Default port listed in run.py is 8080 