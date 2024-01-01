<h1 align="center">Network Services Practices (Squid Proxy) 🦑</h1>

**Gateway:**
- Configured Addresses:
  - Internal Interface Manual: `10.110.R.1 / 24`

**Server:**
- Manual Interface: `10.110.R.x`
- Services:
  - Primary DNS Server
  - Postfix Server
  - Web Server

**What is Squid?**
- Squid acts as an intermediary between the client and server.
- Provides functionalities like:
  - Access Control
  - Traffic Logging
  - Traffic Filtering
  - Performance Enhancement
  - Anonymity
  - Web Cache, etc.

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

**Installation and Configuration:**
1. Installation: `yum install squid.x86_64`
2. Configuration File: `/etc/squid/squid.conf`
   - Relevant directives and parameters.

**ACL Configuration:**
- `acl localnet src 10.110.$$$.0/24`
- `acl SSL_ports port 443`
- `acl Safe_ports port 80 443 8443`

**Examples of Access Rules:**
- Allow during working hours: `http_access allow horario`
- Restrict specific IP: `http_access deny ip_restringida`
- Deny access to domains: `http_access deny destinos_prohibidos`

**Cache Configuration:**
- Cache directory: `cache_dir ufs /var/spool/squid 500 16 256`
- Maintenance policy configuration.

**Basic Authentication:**
- `auth_param basic program /usr/lib64/squid/basic_ncsa_auth /etc/squid/claves.basic`
- User management: `htpasswd [-c] /etc/squid/claves.basic usuario`

**Example Rule with Authentication:**
- `acl pasa proxy_auth REQUIRED`
- `http_access allow pasa`

**Digest Authentication:**
- Mandatory parameters and user management similar to basic authentication.

**Proxy Configuration with Digest Authentication:**
- Examples of access rules with digest authentication.

**Test Your Configuration!**
- Configure the browser to use the proxy.
- Make web connections and check log files.

**References:**
- [Squid Documentation](http://www.squid-cache.org/Doc/config/auth_param/)

Explore Squid Proxy in your network services and security practices! 🚀
