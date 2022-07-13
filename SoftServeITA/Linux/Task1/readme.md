[Task1.Par1](./readme.md#task1part1)
[Task1.Par1](./readme.md#task1part2)
### Task1.Part1

* **passwd** command changes **etc/shadow** file after execution
* To list users that are logged in and process they're running we can use **w**. Additionally, we can check for how long system is running, system load averages.
To check all users/daemons registered in the system we can use **cat /etc/passwd** command. 
To check command used by a user we can check **~/.bash_history** file.
* **w user <user>** will show information about specified user. Might be useful to keep more readable output if there are lots of users on system.
**passwd -d <user>** will delete password for a user. Might be useful if a user forgot his password.

<img src="./Screenshots/Screenshot%20from%202022-07-11%2021-57-37.png width=200 height=400>
![screenshot](./Screenshots/Screenshot%20from%202022-07-11%2021-57-37.png)
![screenshot](./Screenshots/Screenshot%20from%202022-07-11%2021-58-25.png)
![screenshot](./Screenshots/Screenshot%20from%202022-07-11%2022-00-08.png)
![screenshot](./Screenshots/Screenshot%20from%202022-07-11%2022-04-44.png)
![screenshot](./Screenshots/Screenshot%20from%202022-07-11%2022-20-23.png)
![screenshot](./Screenshots/Screenshot%20from%202022-07-11%2022-30-18.png)
![screenshot](./Screenshots/Screenshot%20from%202022-07-11%2022-34-54.png)

### Task1.Part2
1. **tree** command execution results
![screenshot](https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Linux/Task1/Screenshots/Screenshot%20from%202022-07-12%2013-35-40.png =250x250)
* **file** command can be used to check file type
* To return to the home directory from any part of the system we can execute **cd ~**
* **ls** command with **-l** switch will show us expanded information of the files and directories: file type, file permissions, file owner, file group, file size, date and time. **ls** command with **-a** switch will show us all files included hidden.
* Hard link is direct reference to the file or simply it has just another name for original file whereas soft link is a reference by name, thus it points to a file by file name. When we make a change in softlink file, changes are reflected in original file. It is like that because basically we accessing original file via softlinked file. 
When we delete original file we have the following results: 1. file with softlink is inaccessible because it has broken link to original file. 2. file with hardlink can be accessed.
* To list all objects that contain **ss** using grep we can use this command **ls -aRl /etc | grep ss**
* Type of devices mounted in system helps us to understand what specific type of device is connect to work with it further. There may be: floppy drive, hard drives, mouse, keyboard etc. 
* To check the type of the file in the system we can use **file** command. There might such file types as: directories, text files, executable files, regular files, media files. 
