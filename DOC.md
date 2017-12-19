# Routes
___

## 1. Cennets -
#### 1. Get all cennets
* Method - GET
* url - http://127.0.0.1:5000/cennets
* Output Json value - 
    ```
            {
        "cennets": [
            {
                "cennet_type": "WALL",
                "discovered": true,
                "id": 1,
                "ip_address": "192.168.1.3",
                "name": "abc",
                "room_id": 1,
                "udid": "HALO"
            }
        ]
    }
    ```

#### 2. Get only one cennet by id
* Method - GET
* url - http://127.0.0.1:5000/cennets/1
* Output Json value - 
    ```
        {
        "cennet_type": "SIDE",
        "dimmers": [
            {
                "id": 1,
                "intensity": 98,
                "number": 1,
                "power": true
            },
            {
                "id": 2,
                "intensity": 0,
                "number": 2,
                "power": false
            }
        ],
        "discovered": true,
        "id": 1,
        "ip_address": "192.168.1.4",
        "name": "def",
        "relays": [
            {
                "id": 1,
                "number": 1,
                "power": true
            },
            {
                "id": 2,
                "number": 2,
                "power": true
            }
        ],
        "room_id": 1,
        "udid": "ADA"
    }
    ```
   
#### 3. Add a cennet
* Method - POST
* url - http://127.0.0.1:5000/cennets
* Input Json value - 
    ```
   {
	"udid": "ADA",
	"name": "def",
	"cennet_type": "SIDE",
	"relays" : [{"power":false, "number":1},{"power":false, "number":2}],
	"dimmers": [{"power":false, "intensity":0, "number":1},{"power":false, "intensity":0, "number":2}],
	"ip_address": "192.168.1.4"
    }
    ```
    
#### 4.  Changing the value of room_id in cennet
* Method - PUT
* url - http://127.0.0.1:5000/cennets/1
* Input Json value - 
    ```
    {
    "room_id": 2
    }
    ```
    
#### 5.  Delete a cennet
* Method - DELETE
* url - http://127.0.0.1:5000/cennets/1
* Output Json value - 
    ```
    msg: Whether operation was successfull or not 
    ```
___

## 2. Rooms - 
#### 1. Get all rooms
* Method - GET
* url - http://127.0.0.1:5000/rooms
* Output Json value 
    ```
          {
        "rooms": [
            {
                "id": 1,
                "name": "Dinning room"
            }
        ]
    }
    ```
    
#### 2. Get a single room
* Method - GET
* url - http://127.0.0.1:5000/rooms/1
* Output Json value - 
    ```
        {
    "buttons": [
        {
            "button_type": "dimmer",
            "dimmer_id": 1,
            "id": 1,
            "intensity": 98,
            "ip_address": "192.168.1.4",
            "name": "Light",
            "power": true,
            "room_id": 1
        },
        {
            "button_type": "dimmer",
            "dimmer_id": 2,
            "id": 2,
            "intensity": 0,
            "ip_address": "192.168.1.4",
            "name": "Heater",
            "power": false,
            "room_id": 1
        },
        {
            "button_type": "relay",
            "id": 3,
            "ip_address": "192.168.1.4",
            "name": "Fan",
            "power": true,
            "relay_id": 1,
            "room_id": 1
        },
        {
            "button_type": "relay",
            "id": 4,
            "ip_address": "192.168.1.4",
            "name": "Tubelight",
            "power": true,
            "relay_id": 2,
            "room_id": 1
        }
    ],
    "room_id": 1,
    "room_name": "Living Room"
    }
    ```

#### 3. Adding a room
* Method - POST
* url - http://127.0.0.1:5000/rooms
* Input Json value - 
    ```
    {
	"name": "Dinning room"
    }
    ```
#### 4. Changing the room name
* Method - PUT
* url - http://127.0.0.1:5000/rooms/1
* Input Json value - 
    ```
    {
    	"name": "Living Room"
    }
    ```
     
#### 5. Delete a room
* Method - DELETE
* url - http://127.0.0.1:5000/rooms/2
* Output Json value - 
    ```
    msg: operation succeded or not
    ```
___
## 3. Buttons

#### 1. Get all buttons
* Method - GET
* url - http://127.0.0.1:5000/buttons
* Output Json value - 
    ```
        {
        "buttons": [
            {
                "button_type": "dimmer",
                "dimmer_id": 1,
                "id": 1,
                "intensity": 98,
                "ip_address": "192.168.1.4",
                "name": "Light",
                "power": true,
                "room_id": 1
            },
            {
                "button_type": "dimmer",
                "dimmer_id": 2,
                "id": 2,
                "intensity": 0,
                "ip_address": "192.168.1.4",
                "name": "Heater",
                "power": false,
                "room_id": 1
            },
            {
                "button_type": "relay",
                "id": 3,
                "ip_address": "192.168.1.4",
                "name": "Fan",
                "power": true,
                "relay_id": 1,
                "room_id": 1
            },
            {
                "button_type": "relay",
                "id": 4,
                "ip_address": "192.168.1.4",
                "name": "Tubelight",
                "power": true,
                "relay_id": 2,
                "room_id": 1
            }
        ]
    }
    ```

#### 2. Get a single button
* Method - GET
* url - http://127.0.0.1:5000/buttons/1
* Output Json value - 
    ```
   {
    "button_type": "dimmer",
    "dimmer_id": 1,
    "id": 1,
    "intensity": 0,
    "ip_address": "192.168.1.4",
    "name": "Light",
    "power": false,
    "room_id": 1
    }
    ```

#### 3. Add a button
* Method - POST
* url - http://127.0.0.1:5000/buttons
* Input Json value - 
    ```
    {
	"name": "Tubelight",
	"button_type":"relay",
	"room_id": 1,
	"power": false,
	"relay_id": 2,
	"ip_address": "192.168.1.4"
    }
    ```
    
#### 4. Change the value of a button
* Method - PUT
* url - http://127.0.0.1:5000/buttons/1
* Input Json value - 
    ```
    {
	"power": false,
	"intensity": 0,
	"dimmer_id": 2
    }
    ```
#### 5. Delete a button
* Method - DELETE
* url - http://127.0.0.1:5000/buttons/1
* Output Json value - 
    ```
    msg: operation succedded or not
    ```
    

    
    
    
    
    
    
    
    
    



