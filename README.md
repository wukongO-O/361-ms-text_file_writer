# Json Writer Microservice
## Description 
The Json Writer microservice gets quantity and value data from user to update inventory for a theater. It uses jw-service.txt as communication pipe. It saves the data in json format and writes it in inventory.json file.
## How to request data
Run the ui program (test_json_writer.py) to gather user input and write the request into jw-service.txt 

## How to receive data 
* Run json_writer.py either after the ui program completes or before starts the ui program in a separate process. 
* The json_writer.py reads request from jw-service.txt and responds by generating or updating the inventory.json.

## UML sequence diagram 
<img src="./UML.png"/>