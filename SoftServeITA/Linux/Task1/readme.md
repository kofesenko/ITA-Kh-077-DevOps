## Task1.Part1

* **passwd** command changes **etc/shadow** file after execution
* To list users that are logged in and process they're running we can use **w**. Additionally, we can check for how long system is running, system load averages.
To check all users registered in the system we can use **cat /etc/passwd** command. 
To check command used by a user we can check **~/.bash_history** file.
* **w user <user>** will show information about specified user. Might be useful to keep more readable output if there are lots of users on system.
**passwd -d <user>** will delete password for a user. Might be useful if a user forgot his password. 
* 
## Task1.Part2
