The requests library tool that provides the ability to make HTTP requests to any API in the world. 
When you want to interact with data via a REST API, this is called a request. A request is made up of the follwoing components:
`Endpoint` - the URL that delineates what data you are interacting with. Similar to how a web page URL is tied to a specific page, an endpoint URL is tied to a specific resource within an API
`Method` - Specifies how youre interacting the the resource located at the provided endpoint. REST APIs can provide methods to enable full Create, Read, Update, and Delete ( #CRUD ) functionality

Here are comon methods most REST APIs provide:
- GET - Retrieve data
- PUT - Replace Data
- POST - Create Data
- DELETE - Delete data

## How to request Data with GET
The GET method is used to Access data for a specific resource from a REST API; Python Requests includes a function to do exactly this. 
#example
``` Python
import requests

response = requests.get("http://api.open-notify.org/astros.json")

print(response)

>>>> Response<200>
```


#### Query Parameters
Queries can be used to filter the data that an API returns, and these are added as query parameters that are appended to the endpoint URL. This is handled through the `params` argument, which accepts a dictionary object; 