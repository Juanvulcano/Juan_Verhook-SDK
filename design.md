# Design
The current version is a minimalistic example of an SDK. It includes a single API call to query for the name of the books. 

## Limitations

1. The SDK is not dealing with potential pagination in case the books listed for LOTR exceeds the 1000 items API limit. I think this is unlikely to be a problem in the next coming years. There is always the chance that Tolkien's legacy is bigger than we know of.  
2. Authentication was off the scope of this project as the endpoint selected has open access. I did include potential code and references to using access token in the original design. 


### Class Diagram with UML

<img width="196" alt="class" src="https://user-images.githubusercontent.com/9177978/209793683-11ad0f54-5e9f-48b4-9e1f-bae66c734ab1.png">


This is an example of what an implementation in javascript could look like as well. 

```
request = new APICall(
    this.baseURL,
    'v2/books/',
    'GET', 
    "A9DS901JE",
);
return request.send();
``` 


