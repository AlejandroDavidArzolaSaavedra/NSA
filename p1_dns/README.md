<h1 align="center">DNS Server Setup 🌐</h1>

## Table of Contents 📜
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Testing](#testing)
6. [Validation](#validation)

## Introduction 🚀
This document guides you through the process of setting up a primary DNS server and a secondary DNS server for the domain redes.dis.ulpgc.es. The exercises include configuring primary and secondary zones, adjusting zone directives, and testing DNS resolution.

## Prerequisites 🛠️
- Linux server with BIND installed
- Basic understanding of DNS concepts

## Installation 📥
To install BIND on your server, execute the following commands:

```bash
sudo yum install bind
sudo yum install bind-chroot
```

## Configuration ⚙️
1. Configure the primary DNS server with zone directives.
2. Create aliases for secondary DNS servers (ns1.<domain>, ns2.<domain>).
3. Add a new device with IP address 10.110.R.10 and the name "sientoelretraso."
4. Adjust DNS server settings for zone transfers, queries, and forwarding.

## Testing 🧪
1. Flush the DNS cache using `rndc flush`.
2. Test DNS queries from machines within the network.
3. Test DNS queries from external machines (e.g., neptuno).

## Validation ✅
Follow the instructions in the validation document to ensure correct DNS functionality. Perform tests such as querying DNS servers for IP addresses, reverse DNS lookups, and zone transfers.

For more details and additional documentation, refer to [http://www.zytrax.com/books/dns/](http://www.zytrax.com/books/dns/).

**Note:** Replace placeholders such as #### and <domain> with actual values relevant to your network configuration.

Feel free to reach out to the Networking Group at the School of Computer Science and Telecommunications for further assistance: [www.redes.dis.ulpgc.es](www.redes.dis.ulpgc.es). 🌐
