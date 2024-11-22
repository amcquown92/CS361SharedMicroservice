# Microservice for Processing User Achievments
### Overview
This microservice is implemented using Flask and is designed to process user data, determine achievements based on game attributes, and return the updated user data. The service is accessible via a POST request to the /process endpoint.
### Communication Contract
+ Requesting Data
+ Send a POST request to the /process endpoint with:

Content-Type: application/json
Body: A JSON array containing user data.
### Example Request
```python
import requests

url = "http://localhost:5000/process"
user_data = [
    {
        "user": "Alice",
        "games": [
            {
                "name": "Fidget Spinner",
                "attributes": {
                    "type": "wheel",
                    "color": "colorful",
                    "vibration": True,
                    "sound": False,
                    "preset": True,
                    "functionality": "high"
                }
            }
        ]
    }
]

response = requests.post(url, json=user_data)
print(response.json())
```

### Example Respose:
```json
[
    {
        "user": "Alice",
        "achievements": ["Wheel Whiz", "Threepeat"],
        "games": [
            {
                "name": "Fidget Spinner",
                "attributes": {
                    "type": "wheel",
                    "color": "colorful",
                    "vibration": true,
                    "sound": false,
                    "preset": true,
                    "functionality": "high"
                }
            }
        ]
    }
]
```
### UML Sequence Diagram
Below is the sequence diagram showing how the microservice processes data:

```plaintext

+---------------------+         +-----------------------+         +-------------------------------+
|      Client         |         |    Flask Microservice  |         |   determine_achievements()     |
+---------------------+         +-----------------------+         +-------------------------------+
           |                               |                                      |
           |         1. POST request       |                                      |
           |----------------------------->|                                      |
           |                               |                                      |
           |                               |         2. Process each user        |
           |                               |         ---------------------------->|
           |                               |                                      |
           |                               |         3. Determine achievements    |
           |                               |         (evaluates game attributes)  |
           |                               |<-------------------------------------|
           |                               |                                      |
           |                               |         4. Add achievements to user |
           |                               |         data                        |
           |                               |         ---------------------------->|
           |                               |                                      |
           |         5. Response with      |                                      |
           |            updated data       |                                      |
           |<----------------------------->|                                      |
           |                               |                                      |
+---------------------+         +-----------------------+         +-------------------------------+
|      Client         |         |    Flask Microservice  |         |   determine_achievements()     |
+---------------------+         +-----------------------+         +-------------------------------+

```
Adjusted Sequence Diagram Structure:
1. Client sends a POST request to Flask Microservice.
2. Flask Microservice calls determine_achievements() for each user.
3. determine_achievements() returns the list of achievements to Flask Microservice.
4. Flask Microservice returns the updated user data (with achievements) to the Client.

### How to Run the Microservice
Install dependencies:

```bash
pip install flask
```
Run the server:

```bash
python achievements_get.py
```
The service will be available at http://localhost:5000.

Testing
Use the example Python script in the Requesting Data section to test.
Alternatively, use tools like Postman or curl:
```bash
curl -X POST -H "Content-Type: application/json" -d @input_data.json http://localhost:5000/process
```
