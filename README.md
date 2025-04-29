# LAN Chat Application (Python)

A simple **LAN (Local Area Network) chat application** built with **Python**. This app allows multiple users to chat with each other in real-time over the same network. It uses **sockets** for communication and **threading** to handle multiple clients simultaneously.

## Features:
- Real-time messaging between multiple clients.
- Simple server-client architecture.
- No external dependencies – uses Python’s built-in libraries (`socket`, `threading`).
- Lightweight and easy to set up.

## How It Works:
- The **server** listens for client connections and broadcasts messages to all connected clients.
- The **clients** can send and receive messages in real-time via the terminal.

## Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/lan-chat-app.git
