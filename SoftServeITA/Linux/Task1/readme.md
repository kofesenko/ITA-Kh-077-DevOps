[Task1.Par1](./readme.md#task1part1)
[Task1.Par1](./readme.md#task1part2)
### Task1.Part1

* **passwd** command changes **etc/shadow** file after execution
* To list users that are logged in and process they're running we can use **w**. Additionally, we can check for how long system is running, system load averages.
To check all users/daemons registered in the system we can use **cat /etc/passwd** command. 
To check command used by a user we can check **~/.bash_history** file.
* **w user <user>** will show information about specified user. Might be useful to keep more readable output if there are lots of users on system.
**passwd -d <user>** will delete password for a user. Might be useful if a user forgot his password.

![screenshot](./Screenshots/Screenshot%20from%202022-07-11%2021-57-37.png)
![screenshot](./Screenshots/Screenshot%20from%202022-07-11%2021-58-25.png)
![screenshot](./Screenshots/Screenshot%20from%202022-07-11%2022-00-08.png)
![screenshot](./Screenshots/Screenshot%20from%202022-07-11%2022-04-44.png)
![screenshot](./Screenshots/Screenshot%20from%202022-07-11%2022-20-23.png)
![screenshot](./Screenshots/Screenshot%20from%202022-07-11%2022-30-18.png)
![screenshot](./Screenshots/Screenshot%20from%202022-07-11%2022-34-54.png)

### Task1.Part2
1. **tree** command execution results
![screenshot](https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Linux/Task1/Screenshots/Screenshot%20from%202022-07-12%2013-35-40.png)
![screenshot](https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Linux/Task1/Screenshots/Screenshot%20from%202022-07-12%2013-45-53.png)
![screenshot](https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Linux/Task1/Screenshots/Screenshot%20from%202022-07-12%2013-47-01.png)
2. **file** command can be used to check file type
3. To return to the home directory from any part of the system we can execute **cd ~**
4. **ls** command with **-l** switch will show us expanded information of the files and directories: file type, file permissions, file owner, file group, file size, date and time. **ls** command with **-a** switch will show us all files included hidden.
![screenshot](https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Linux/Task1/Screenshots/Screenshot%20from%202022-07-12%2014-05-19.png)
![screenshot](https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Linux/Task1/Screenshots/Screenshot%20from%202022-07-12%2014-05-57.png)
![screenshot](https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Linux/Task1/Screenshots/Screenshot%20from%202022-07-12%2014-06-17.png)
5.
![screenshot](https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Linux/Task1/Screenshots/Screenshot%20from%202022-07-12%2014-28-14.png)
6. Hard link is direct reference to the file or simply it has just another name for original file whereas soft link is a reference by name, thus it points to a file by file name. When we make a change in softlink file, changes are reflected in original file. It is like that because basically we accessing original file via softlinked file. 
When we delete original file we have the following results: 1. file with softlink is inaccessible because it has broken link to original file. 2. file with hardlink can be accessed.
![screenshot](https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Linux/Task1/Screenshots/Screenshot%20from%202022-07-12%2014-58-35.png)
  
7.
![screenshot](https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Linux/Task1/Screenshots/Screenshot%20from%202022-07-12%2015-03-12.png)
  
8.
![screenshot](https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Linux/Task1/Screenshots/Screenshot%20from%202022-07-12%2015-05-09.png)
![screenshot](https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Linux/Task1/Screenshots/Screenshot%20from%202022-07-12%2015-05-09.png)

9.
![screenshot](https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Linux/Task1/Screenshots/Screenshot%20from%202022-07-12%2015-08-51.png)
  
10.
![screenshot](https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Linux/Task1/Screenshots/Screenshot%20from%202022-07-12%2015-14-03.png)
  
11. To list all objects that contain **ss** using grep we can use this command **ls -aRl /etc | grep ss**
![screenshot](https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Linux/Task1/Screenshots/Screenshot%20from%202022-07-12%2015-35-34.png)
![screenshot](https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Linux/Task1/Screenshots/Screenshot%20from%202022-07-12%2015-15-44.png)
  
12. 
![screenshot](https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Linux/Task1/Screenshots/Screenshot%20from%202022-07-12%2015-49-47.png)

13. Type of devices mounted in system helps us to understand what specific type of device is connect to work with it further. There may be: floppy drive, hard drives, mouse, keyboard etc. 

![screenshot](https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Linux/Task1/Screenshots/Screenshot%20from%202022-07-12%2016-03-51.png)
![screenshot](https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Linux/Task1/Screenshots/Screenshot%20from%202022-07-12%2016-04-03.png)

14. To check the type of the file in the system we can use **file** command. There might such file types as: directories, text files, executable files, regular files, media files. 
15. 
![screenshot](https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Linux/Task1/Screenshots/Screenshot%20from%202022-07-12%2016-25-51.png)
