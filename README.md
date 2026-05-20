# circuitpython_auto_wifi
Simple mechanism for automatic handling of multiple wifi networks in CircuitPython.

If you want to use your circuitpython device in multiple wifi networks while still using `settings.toml`, this small piece of code is for you.

1. Copy `auto_wifi.py` and `templates.py` files to your board.
1. Provide your wifi credentials in `auto_wifi.json`. Order is important, if multiple known networks are found, it will connect to the one appearing on the list the earliest.
   ```json
   [
     {
       "ssid":"some_network",
       "pass":"some_pass"
     },
     {
       "ssid":"another_network",
       "pass":"another_pass"
     },
     {
       "ssid":"more_network",
       "pass":"more_pass"
     }
   ]
   ```
1. Rename your `settings.toml` to `settings.toml.tmpl` and put there placeholders:
   ```
   CIRCUITPY_WIFI_SSID="{{ssid}}"
   CIRCUITPY_WIFI_PASSWORD="{{pass}}"
   ```
1. Run it from your `boot.py` if you want to autoconnect on board reset:
   ```python
   import auto_wifi

   auto_wifi.apply()
   ```
