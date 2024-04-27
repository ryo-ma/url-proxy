# URL Proxy

GPTs Code Interpreter cannot make HTTP requests to external sites.
Therefore, I have developed a proxy server that can be registered in GPTs Actions.

# Usage

Request the URL in the `url` parameter using GET.

```
https://url-proxy-dusky.vercel.app/?url=https://xxxxxxxx/xx.json
```

You can use an `encoding` parameter

```
https://url-proxy-dusky.vercel.app/?url=https://xxxxxxxx/xx.json?encoding=shift-jis
```

# LICENSE

[MIT LICENSE](./LICENSE)
