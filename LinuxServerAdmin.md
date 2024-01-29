# SERVER ADMINISTRATION

Linux-based OS’s are multi-user in nature. SSH makes the life of Linux users easy by enabling multiple connections at the same time.

## USER/GROUP MANAGEMENT 

Users in Linux have a User ID (UID) attached to them. A group is a collection of users, making it easier to share permissions among a group of users. A group has a Group ID (GID).

### COMMANDS

- `id`: Lists UID and GID of the user. (0 for the root user)
- `whoami`: Prints the current user

### FILES ASSOCIATED WITH USERS/GROUPS

- `/etc/passwd`: Stores username, UID, GID, home directory. <`username:x:UID:GID:User description:/home/username:/bin/bash`>
- `/etc/shadow`: Stores the password associated with the username.
- `/etc/group`: Stores information about different groups in the system.
  Format: `groupname:x:GID:user1,user2,user3`

### COMMANDS FOR MANAGING USERS

- `useradd`: Creates a new username (`useradd <username>`).
- `passwd`: Adds or modifies the password of a user.
  After running `useradd` command, the password won't be assigned. (passwd  <username>) gives a password prompt.
- `usermod`: Modifies attributes of a user like shell or home directory (`usermod <username> -s bin/sh`).
- `userdel`: Deletes a user.
- `su <username>`: Changes user from one to another.

### COMMANDS FOR MANAGING GROUPS

Similar to USER commands, but add "group" before the command (`groupadd`, `groupmod`, `groupdel`).

## FILE PERMISSIONS AND COMMANDS

Files or directories are assigned access permissions for owner, group, and other users.
![Linux Image](LinuxFilePermissions.png)
- Read file: 4
- Write: 2
- Execute: 1

### COMMANDS

- `chmod`: For changing permissions (`chmod 777 <file_name>`).
- `chown`: For changing owners of a file or directory (`chown <new_owner> <file_name>`).
- `chgrp`: For changing group ownership of files or directories (`chgrp <new_owner> <file_name>`).
