# telegram-forward-message-keyword

Simple script to forward telegram new message that contain your keyword.

## How To Run
1. Get your api_id and api_hash in [my.telegram.org](https://my.telegram.org)
2. Use your api_id and api_hash in `get-dialogs.py` and `main.py`.
    ```
    api_id = 123123
    api_hash = 'abcdefhijkl'
    ```
3. Run get-dialogs.py, 
    ```
    python3 get-dialogs.py
    ```
    input your telegram phone number and your login code, new file `dialogs.json` will be created contain chat_id and chat_name.
4. Use chat_id from `dialogs.json` in senders and receiver in `main.py`
5. Run `main.py`
    ```
    python3 main.py
    ```
6. Now every new message from senders that contain keyword will be forwarded to receiver.
