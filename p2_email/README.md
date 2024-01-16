<h1 align="center">Practice: 📧 Email Services and Security in Networks</h1>

<p align="center">
  <img width="400px" src="https://github.com/AlejandroDavidArzolaSaavedra/NSA/assets/90756437/1a93b1ad-7655-40db-b239-377fb1a4df85">
</p>

**Email Gateway Configuration:**

- External OpenVPN interface: 10.110.1.R/24 🌐
- Internal manual interface: 10.110.R.1/24 🏠

**Server:**

- Manually configured IP address 🖥️
- Primary DNS server 🌐

**Linux Station:**

- Secondary DNS server 🌐

**Components of the Email Service:**

- **MTA (Mail Transfer Agent):**
  - Transfers messages from a Mail User Agent (MUA) to a remote mail server (MTA) using SMTP 📤.
  - Remote MTA deposits the message in the recipient's mailbox using a Mail Delivery Agent (MDA) 📬.
  - Clients read email using a MUA with POP or IMAP 📧.

- **Postfix:**
  - Acts as both MTA and MDA 🔄.
  - Manages mail queues (maildrop, incoming, active, deferred) 📮.

**Postfix Commands:**
- `postsuper (-d –p –r -s)` ⚙️
- `postqueue (-f –i –p (mailq))` ⚙️
- `postcat` ⚙️

**Accounts and Aliases:**
- User accounts from databases (local, LDAP, etc.) 👤.
- Aliases define other names for user accounts 📇.

**Main Configuration Files:**
- `master.cf`: Processes with associated parameters ⚙️.
- `main.cf`: Parameters related to Postfix function ⚙️.

**DNS Configuration:**
- Connect DNS domain with Mail Server 🌐.
- Set MX records ⚙️.

**Email Testing Steps:**
1. Configure and start Postfix on the server ⚙️.
2. Create user accounts using `adduser` 👤.
3. Test using `telnet` to send emails locally and to external addresses 🌐.
4. Monitor mail activity using `tail –f /var/log/maillog` 📊.
5. Use the `mail` command for interactive local email testing 📬.

**Alias and List Creation:**
- Define at least one alias for each user account 📇.
- Create the list "mis_vecinos" to forward messages to local and neighboring accounts 📧.

**Dovecot Installation and Configuration:**
- Install Dovecot and configure minimal settings ⚙️.
- Start Dovecot and check the maillog 📊.

**Thunderbird Installation and Configuration:**
- Install and configure Thunderbird on a Windows station 🖥️.
- Send and receive emails using Thunderbird 📤📥.

**SASL Configuration:**
- Enable SASL in Postfix and configure Dovecot for authentication ⚙️.

**TLS Configuration:**
- Configure TLS in Postfix for encrypted communication 🔐.

**Access Control and Restrictions:**
- Configure access control based on client, sender, and recipient ⚙️.
- Use `check_client_access` to allow specific machines ⚙️.
- Implement sender and recipient restrictions ⚙️.

**Practice Validation:**
1. Send an email from a local domain to an external address 🌐.
2. Send an email from an external address to a local user 🌐.
3. Use `telnet` to send an email between two local users from a local network machine 🏠.
4. Use Thunderbird to send an email between two local users from a local network machine 🖥️.
5. Use `telnet` from an external machine to send an email to a local user 🌐.
6. Use Thunderbird from an external machine to send an email to a local user 🌐.
7. Use `telnet` from an external machine (other than Neptuno) to send an email to an external user (should fail) ❌.
8. Use Thunderbird from an external machine to send an email to an external address 🌐.
9. Use `telnet` from Neptuno to send an email to an external user 🌐.
10. Send an email to one of the created mailing lists and verify delivery to all list members 📧👥.
