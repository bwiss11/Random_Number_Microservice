# Random_Number_Microservice

# Random Number Microservice

## Introduction
This microservice has been developed to return a random number within the range of (1, 10000) whenever it receives a request from the client.

The microservice was developed using Python sockets, and utilizes the 'sockets' library in Python, as well as the 'random' library.

The user will need to download the random_number_server.py file and will need to set their client-side file to communicate on the same HOST and PORT numbers that the server file is connected to (feel free to change the server's HOST and PORT numbers). The random_number_client.py file can also be downloaded as a working sample file for making requests and receiving data from random_number_server.py.

## Set Up
Be sure that the HOST and PORT numbers in the random_number_server.py file matches your client-side .py file's HOST and PORT numbers. Having these numbers identical in both files is what allows the client to communicate with the server.

## Requests
After the socket on the client-side is set up correctly (see random_number_client.py for example), the client must make a request to the server using the following format:

![image](https://user-images.githubusercontent.com/79183545/236528968-0105e219-96b5-4841-ad73-06ff22597c6e.png)

The data sent does not need to be exactly of the example above, i.e. the request doesn't need to say "Example request". However, some data must be sent - s.sendall(b"") will not result in any data being requested or received from the server.


## Receiving Data from the Server
After the client submits a request to the server, the server will receive the request and generate a random number within the range (1, 10000). 
The server will then send the random number back to the client. It's important to note that the data is encoded in utf-8 before being sent back to the client. This means the client-side must decode the utf-8 (using the .decode() method) before the number will be usable. See the below picture for an example of how to decode the received data.

![image](https://user-images.githubusercontent.com/79183545/236627654-0c6b2026-27ac-4ba7-9ed7-e094f93db7c9.png)

The **num** variable now holds the randomly-generated number as a string and the user is free to use the number however they like from there.

