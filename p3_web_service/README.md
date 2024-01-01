<h1 align="center">Network Services Practices (Web Service) 🌐</h1>

**Apache HTTP Server:**
- **Description:** This project focuses on configuring a web server using Apache HTTP Server, a free and open-source HTTP server.

  - **Features:**
    - Cross-platform support: Unix, FreeBSD, Linux, Microsoft Windows, etc.
    - Supports multiple scripting languages: PHP, Perl, Tcl, Python.
    - J2EE support with Tomcat.
    - Allows dynamic content and easy configuration.

**Server Configuration:**
- **File Structure:**
  - `httpd.conf`: Main configuration file.
  - `conf.modules.d/`: Directory with configuration modules.
  - `.htaccess`: Configuration file in specific folders.

- **Important Directives:**
  - `ServerRoot`: Server installation directory.
  - `Listen`: Listening ports and IP addresses.
  - `Include`: Loading additional modules.
  - `User` and `Group`: Specify the application user and group.
  - `AllowOverride`: Allowed configuration in `.htaccess` files.

**Virtual Server Configuration:**
- **`httpd.conf` Structure:**
  - Text file with configuration directives.
  - Global and container directives (Directory, VirtualHost, Location).

- **Virtual Servers:**
  - Custom configuration for multiple websites on a single machine.
  - IP-based or name-based.

**Practical Instructions:**
1. **Installation and Start of Apache:**
   - `systemctl start/restart/stop/status httpd`
   - `apachectl graceful` (Reload without interrupting pending connections).

2. **Basic Configuration:**
   - Access from a browser to test the Apache test page.
   - Configure domain names, ports, and copy `index.html` from the campus.

3. **Virtual Server Configuration:**
   - Create separate configuration files for each virtual site.
   - Customize values like `ServerAdmin`, `ServerName`, `DocumentRoot`, etc.

4. **SSL (Secure Socket Layer):**
   - Enable the SSL module and configure its loading.
   - Create a self-signed certificate or acquire one.
   - Configure a virtual host for SSL on port 443.

5. **HTTP to HTTPS Redirection:**
   - Ensure all requests to port 80 redirect to port 443.
   - Configure a virtual host on port 80 with a permanent redirection.

6. **User Authentication:**
   - Configure basic authentication to restrict access to certain areas.
   - Create password and group files using `htpasswd`.
   - Set permissions and require authentication in the desired directory.

7. **Restricted Downloads for Registered Users:**
   - Create a downloads directory accessible only to registered users.
   - Configure basic authentication and appropriate permissions.

8. **Client Site Deployment:**
   - Create a virtual host for the client's website.
   - Set DocumentRoot, logs, email aliases, and HTTPS configuration.

9. **Technical Considerations:**
   - Ensure a DNS entry.
   - Secure access through HTTPS.
   - Restrict web access as needed.
   - Transfer files with sftp and customize the home page.

Welcome to the web services practice! 🚀
