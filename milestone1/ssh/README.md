# SSH

## What is SSH?
SSH (Secure Shell) is a secure protocol used to remotely access and manage servers.  
It encrypts the communication between your machine and the remote machine, ensuring security and privacy.


## SSH Keys (Public & Private)
SSH uses a key pair for authentication:

### **Private Key**
- Stays on your local machine
- Must never be shared

### **Public Key**
- Can be shared or added to servers and services
- Acts like a “lock” that your private key “opens”

Together, they allow passwordless and secure login.


## How SSH Login Works (Simple)
1. You attempt to connect to a server  
2. Server checks if your **public key** is allowed  
3. Your machine proves identity using **private key**  
4. If keys match → login successful

No password required.


## SSH + GitHub
GitHub uses SSH keys to verify your identity when you:
- Push code  
- Pull code  
- Clone private repositories  

Process:
- Your laptop has **private key**  
- GitHub stores **public key**  
- GitHub verifies match during actions like `git push`

This allows secure, passwordless Git operations.