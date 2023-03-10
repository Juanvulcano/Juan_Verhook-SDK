# Juan_Verhook-SDK
SDK sample for "The Lord of the Rings" API

## LOTRSDKTEST

LOTRSDKTEST is a sample (SDK) for Python, which allows Python developers to write software that makes use of services consuming the Lord of The Rings API. 

## Installation

To install the package use pip:

```pip3 install LOTRSDKTEST==1.0```

## Usage

```
from LOTRSDKTEST.client import API_Call
client = API_Call("https://the-one-api.dev/", "/v2/book/", "GET")
response = client.api_request()
all_books = client.serialize_book_names()
```

## Testing
Its possible to check individual tests regarding the expected behavior of the API with: 

 ```python3 -m unittest tests.py```

### Design
Refer to the relevant document for more information about the current project design.