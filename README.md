
# Multi-Room Chat Server

Description:
This project implements a multi-room chat server using Python's socket programming. The server allows multiple clients to connect, choose a chat room (from 1 to 5), exchange messages within the chosen room, and logs the chat messages into room-specific log files. Each client joining a room receives the last 10 messages exchanged in that room upon connection. The code is structured to handle concurrent connections using threads and includes basic error handling for various exceptions.

Features:
- Multi-room chat functionality (5 rooms available).
- Logging of chat messages into room-specific log files.
- New clients receive the last 10 messages upon joining a room.
- Basic error handling for various exceptions.

Instructions:
1. Run the `server.py` file to start the chat server.
2. Connect to the server using the `client.py` file and choose a room number (1-5) to join the chat.


Usage:
- Python 3.x is required to run the server and client scripts.
