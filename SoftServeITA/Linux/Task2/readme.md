## 9Task2

1. **/etc/passwd** file contains information for all user accounts on the system. 
```
dev:x:1001:1001:mark,,,:/home/dev:/bin/bash
[--] - [--] [--] [-----] [--------] [--------]
|    |   |    |     |         |        |
|    |   |    |     |         |        +-> 7. Login shell
|    |   |    |     |         +----------> 6. Home directory
|    |   |    |     +--------------------> 5. GECOS
|    |   |    +--------------------------> 4. GID
|    |   +-------------------------------> 3. UID
|    +-----------------------------------> 2. Password
+----------------------------------------> 1. Username
```

GECOS - fuul name of a user + information about room number, work and home phone number, other contact info.
GID - group id
UID - user id

**/etc/group** file contains list of groups on the system as well as users attached to the groups
```
adm:x:4:syslog,dev
[-] - -[---------] 
 |  | |  |
 |  | |  +-> 4. Users in the group
 |  | +----> 3. GID
 |  +------> 2. Password
 +---------> 1. Groupname
```
There are several pseudo-users such as daemon, adm and we can define them by /nologin.

2. UID has range from 0 to 65535. First 1000 register for system and the rest for regular users. 
To set UID we can use **usermod -u <UID> <username>** command

3. To set GID we can use **groupmod -g <GID> <groupname>** command

4. To check the groups user is belonging to we can use **id <username>** command

5. To add user to the system we can use **adduser <username>** or **useradd <username>** commands. We have to specify username. Other parameters can be set up afterwards.

6. To change username we can use **usermod -l <newusername> <oldusername>** command

7. **skel_dir** contains files that are automatically copied over to a new user’s when it is created from **useradd** command. 
It has the following structure:
```
.
├── .bash_logout
├── .bashrc
└── .profile
```
8. To delete user and his email from the system we can use **userdel -r <username>** command

9. To lock user account we can use **usermod -L <username>** or **passwd -l <username>** commands. To unlock it we use **usermod -U <username>** or **passwd -u <username>** command.

10. To disable password for a user we use **passwd -d <username>** command.

11. To display extended information about the directory we use ls -lad */ command.
```
drwxr-xr-x 2 dev dev 4096 лип 11 20:16 Desktop/
[--------] - [-] [-] [--] [----------] [------]
    |      |  |   |   |            |      |
    |      |  |   |   |            |      +-> Dirname
    |      |  |   |   |            +--------> Last modified date and time of the content
    |      |  |   |   +---------------------> Content size in bytes
    |      |  |   +-------------------------> Group owner of the file or directory
    |      |  +-----------------------------> Owner of the file or directory
    |      +--------------------------------> Number of hard links to the content
    +---------------------------------------> Content permissions
```
12. We can set up access right for us (owner), member of a group and other. It can be permissions such as read(r), write(w), execute(x) as well as special permissions directory(d), block device(b), character device(c), symbolick link(l), pipe(p), socket(s), sticky bit(t).

13. The sequence of defining the relationship between the file and user:
*If the UID of the file is the same as the UID of the process, the user is the owner of the file
*If the GID of the file matches the GID of any group the user belongs to, he is a member of the group to
which the file belongs.
*If neither the UID no the GID of a file overlaps with the UID of the process and the list of groups that the
user running it belongs to, that user is an outsider.
 
14. To change owner of a file or directory we can use **chown <newowner> <file or directory>**. To change access mode we can use **chmod u(g,o,a)+r(w,x,t) <filename>** or **chmod 777 <filename>** (wiil provide all access rights for all users). 
![screenshot](./Screenshots/Screenshot%20from%202022-07-13%2015-06-15.png)

15. Octal representation of permissions is numeric representation of a permission. For example 666 will provide read and write access rights to owner, group and other users. 
**umask** command specifies the permission that the user does not want to be gicen out to the newly created file or directory. 

16. **Sticky Bit** is a permission bit that is set on a file or a directory that lets only the owner of the file/directory or the root user to delete or rename the file. No other user is given privileges to delete the file created by some other user.
Directories with sticky bit permission: /tmp, /var/crash, /var/lock

17. To execute a script it have to have **x** permission.
