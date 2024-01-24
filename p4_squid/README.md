<h1 align="center">Network Services Practices (Squid Proxy) 🦑</h1>

<img align="left" width="150px" src="https://github.com/AlejandroDavidArzolaSaavedra/NSA/assets/90756437/c6307088-da66-4439-93fd-fd934b9059e4">


Squid acts as an intermediary between the client and server. Provides functionalities like access Control, traffic Logging, traffic Filtering, performance Enhancement, anonymity, web Cache, etc.<br><br><br>

**Gateway:**
- Configured Addresses:
  - Internal Interface Manual: `10.110.R.1 / 24`

**Server:**
- Manual Interface: `10.110.R.x`
- Services:
  - Primary DNS Server
  - Postfix Server
  - Web Server

**Proxy Types:**
- Non-Transparent:
  - Manual access from the application.
  - Configuration required.
  - SSL handled through CONNECT.
- Transparent:
  - Intercepts requests without user configuration.
  - Can be combined with firewalls.

**Reverse Proxy:**
- Receives traffic destined for a set of servers.
- Used for security, encryption, load distribution, and static content caching.

**Squid Functions:**
- GNU web proxy cache.
- Stores content from:
  - HTTP, FTP, SSL proxy, DNS.
  - Content filtering and access control.
- Reduces web time, protects internal hosts, provides statistics, and enhances user privacy.

  
<h2>Explore Squid Proxy in your network services and security practices! 🚀</h2> 
<p align="center">
<img width="400px" src="https://github.com/AlejandroDavidArzolaSaavedra/NSA/assets/90756437/c2919ec9-2089-48eb-be28-f734bcfc4f21">
</p>

