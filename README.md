# ssgen
Shadowsocks config generator

This is a small graphical utility for generating a simple .json configuration for your shadowsocks server/client.
For options please refer to [shadowsocks documentation](https://github.com/shadowsocks/shadowsocks/wiki). 

How to use

To run either download the self-contained executable from [releases](https://github.com/mfat/ssgen/releases) section or download the python script directly and run with 
```python ssgen.py```


Install shadowsocks-libev or shadowsocks-rust on your server.

```sudo apt install shadowsocks-libev simple-obfs pwgen```

Copy the configuration file you created with the app to /etc/shadowsocks-libev with the name ```config.json```.

Restart shadowsocks service:

```sudo systemctl restart shadowsocks-libev```
Verify everything is working with:

```sudo systemctl status shadowsocks-libev```













