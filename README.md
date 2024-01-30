# Linux Basics

## Introduction
Linux is a kernel, not an operating system. The Linux kernel is combined with the GNU system to form a complete operating system.

## Linux File System
The Linux file system follows a hierarchical structure with the root at its highest level directory.

![Linux Image](FileArchitecture.png)
*Image Source: [Linux Image](https://linkedin.github.io/school-of-sre/level101/linux_basics/images/linux/commands/image17.png)*
- **bin:** The executable program of most commonly used commands resides in the bin directory.
- **dev:** This directory contains files related to devices on the system.
- **etc:** This directory contains all the system configuration files.
- **home:** This directory contains user-related files and directories.
- **lib:** This directory contains all the library files.
- **mnt:** This directory contains files related to mounted devices on the system.
- **proc:** This directory contains files related to the running processes on the system.
- **root:** This directory contains root user-related files and directories.
- **sbin:** This directory contains programs used for system administration.
- **tmp:** This directory is used to store temporary files on the system.
- **usr:** This directory is used to store application programs on the system.

## Commands for Navigating File System
- **ls:** Lists the files in the present directory.
- **pwd:** Shows the present working directory.
- **cd:** Changes the directory.

## Commands for File Manipulation
- **touch:** Used to create empty files (e.g., `touch <file_name>`).
- **mkdir:** Creates a new directory.
- **cp:** Copies files and directories from the source to the destination (e.g., `cp <source> <destination>`).
- **mv:** Moves files or directories from the source to the destination (e.g., `mv <source> <destination>`).

## Commands for File Viewing
- **cat:** Prints the content of a file on the terminal.
- **head:** Prints the first 10 lines on the screen.
- **tail:** Prints the last 10 lines on the screen.
- **more:** Displays the contents of a file or command output, one screen at a time (useful for large files).
- **less:** An improved version of `more` for both forward and backward navigation.

## Commands for Text Processing
- **grep:** Used for searching (e.g., `grep "text_for_searching" <file_name>`).
- **sed:** Used for replacing text in a file (e.g., `sed 's/<text_to_replace>/<replacement_text>/' <file_name> -i').
- **sort:** Used for sorting.

## I/O Redirection
In Linux, everything is treated as a file.
- `>`: Redirects the output of a command to a file (e.g., `ls > out.txt`).
- `|`: Used to pass the output of one command as input to another (e.g., `history | grep ssh`).

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
  After running `useradd` command, the password won't be assigned. ('passwd <username>') gives a password prompt.
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
