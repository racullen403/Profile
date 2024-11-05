"""
Requests.

This module is commonly used for getting and sending information to and from endpoints over the web.

We send a request to the url endpoint, and receive a response object that contains all relevant information provided by that endpoint.

This API allows us to use all the HTTP requests GET, POST, PUT, DELETE, HEAD, OPTIONS through simple methods.


Typically when we send a request, we want to send some data to the URL's query string, this is usually in key:value pairs within the URL, 
ie http://httpbin.org/get?key=val . Requests allows is to provide these as a dictionary using params
ie requests.get(url="https://httpbin.org/get, params = {key1:val1, key2:val2}), would look like ....get?ke1=val1&key2=val2
    - Note that a key with val=None will not be passed in the query string.
    - Additionally k: [val1, val2] will flatten out in the query to k=val1&key=val2

We can see the content of a response through r.text, this is usually very long.

The response will try to autodetect the encoding based on HTTP headers, this is whats accessed when using r.text to decode. We can specify using r.encoding=...

We can access the response body as bytes using r.centent

A lot of the time we will be dealing with JSON data, simply use r.json() to decode.

A common way to check a request was successful is to use r.raise_for_status() (400 and 500 bad requests) or to check the r.status_code.

    Common Status Codes:
        - Information 100 codes 
        - Successful 200 codes 
        - Redirection 300 codes 
        - Client Error 400 codes 
        - Server Error 500 codes


If we wish to get the raw socket response from the server, we must set the parameter stream=True in the get request. Generally we want to save whatever 
is being streamed, into a file

    with open(filename, "wb") as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chuck)

    This is the recommended way when downloading content, and you can adjust the chunk size to fit your needs.
    This method will auto decode the gzip and deflate transfer encodings, if you need the raw bytes, use r.raw.


Headers:
    We can add headers by passing a dict to the headers parameter in the request, ie, requests.get(url, header={...})
    These are key value pairs that make up metadata. This can be used for caching, authentication, session state. They help the API client and server communicate so 
    that we can better optimise and customise API behaviour.

    Some key differences between headers and parameters:
        - Headers carry meta data, parameters carry actual data.
        - Headers are hidden to end users, whereas parameters can be seen in the url.
        - Headers need to be manually encoded client side and decoded server side (Base64 typically) whereas params are auto decoded.



POSTS:
    We typically use post when we want to send some form-encoded data. This is done by passing a dict {...} to the data parameter, which will auto form-encode.

        payload = {"key1": "val1", "key2": "val2"}
        requests.post(url, data=payload)

        note if a key has mulitiple values we represent it as either

            [("key1", "val1"), ("key1", "val2")] list of tuples 

            {"key1": ["val1", "val2"]} dict with list of values

    If we simply want to pass a string instead of a dict, we can do this using data=json.dumps(payload).
        
    
RESPONSE:
    We can see the response headers with r.headers, as a dictionary and access them as r.headers["key"]

    We can retrieve cookies using r.cookies[...] or send them to the server .get(url, cookies=cookie_key="cookie_val").
        Cookies are returned in a RequestsCookieJar which acts as a dict but suitable over multiple paths.

        jar = requests.cookies.RequestsCookieJar()
        jar.set("key1", "val1", domain=url, path=/path1)
        jar.set("key2", "val2", domain=url, path=/path2)

        now we can get the cookies using 

        requests.get(url/path1, cookies=jar) --> {cookies: {key1: val1}}
        equests.get(url/path2, cookies=jar) --> {cookies: {key2: val2}}

        so we have one cookie jar for the url domain but are able to store multiple cookies for different paths.


REDIRECTION:
    By default requests performs location redirection for all verbs except HEAD, we can see this history using r.history.

    We can disable this property using allow_redirections=False or similarly allow it for HEAD.

    We can tell a request to stop waiting on a response after a set time using timeout=3 (3s), failure to do so can result in indefinite wait times.



"""

import requests

# Cheeky temp way to import external module, supposedly the permanent way is to add the module to the directory where python goes to find standard modules
import sys
sys.path.append('c:\\Users\\Ryan\\Programming\\GitHub\\Projects\\Learning\\MyLogger')
print(sys.path)

import mylogger


logger = mylogger.get_logger(__name__)


def test1():

    # We can request data from the endpoint url and recieve the information contained in a response object
    url = "https://api.github.com/events"
    logger.info(f"Sending get request to {url}:")
    r = requests.get(url)

    # Directly check status code
    sts = r.status_code
    try:
        if sts != 200:
            raise KeyError
        logger.info(f"Response OK {r}, from endpoint {r.url}")
    except:
        logger.info(f"Invalid response {r}, http status {r.url}")

    

def test2():
    url = "https://httpbin.org/get"
    url2 = "https://http44bin.org/get"
    payload = {"key1": "val1", "key2": "val2"}
    logger.info(f"Sending get request to {url} with payload {payload}:")
    # General check for no request error

    try:
        r = requests.get(url, params=payload)
        r.raise_for_status()
        logger.info(f"Response OK {r}, from endpoint {r.url}")
    except requests.exceptions.ConnectionError as err:
        logger.info(f"Invalid response, ConnectionError: {err}")
    except:
        logger.info("Unknown Error")

    try:
        r = requests.get(url2, params=payload)
        r.raise_for_status()
        logger.info(f"Response OK {r}, from endpoint {r.url}")
    except requests.exceptions.ConnectionError as err:
        logger.info(f"Invalid response, ConnectionError: {err}")
    except:
        logger.info("Unknown Error")


if __name__ == "__main__":
    test1()
    test2()

