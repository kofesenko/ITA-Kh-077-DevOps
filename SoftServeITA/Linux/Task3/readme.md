###Task3.Part1

1. The process in Linux can have two main states: **foreground** and background.
2. 
<img src="./Screenshots/[to be replaced]" width=100% height=100%>

3. Proc file system is virtual file system creadted when system boots and dissolved when system shut down. It contains information about the processes that are running and it works like control and information center for kernel. It also provides communication medium between kernel and user space. Additionaly it **/proc** includes a directory for each running process.
4. To print information about CPU we can use **cat /proc/cpuinfo** or **lscpu** commands.
5. 

<img src="./Screenshots/[to be replaced]" width=100% height=100%>

6. Kernel processes have a name that is between square brackets. 

7. Processes can have the following statuses:

              * I    Idle kernel thread
              * R    running or runnable (on run queue)
              * S    interruptible sleep (waiting for an event to complete)
              * T    stopped by job control signal
              * t    stopped by debugger during the tracing
              * W    paging (not valid since the 2.6.xx kernel)
              * X    dead (should never be seen)
              * Z    defunct ("zombie") process, terminated but not reaped by its parent
 
<img src="./Screenshots/[to be replaced]" width=100% height=100%>

8. To list processes for specific user we can use **ps -u <username>** command. To have extended view on the processes we can add *ax* swithces to mentioned command.

9. To check and analyze existing running task we can use **top**, **htop** utilities. 

10. **top** command shows a real-time view of running processes in Linux and displays kernel-managed tasks. The command also provides a system information summary that shows resource utilization, including CPU and memory usage.

11. To show information about processes of specific user in real time we can use **top -u <username>** command.

12. There are set of interactice commnads to control the top command:
```
  Z,B,E,e   Global: 'Z' colors; 'B' bold; 'E'/'e' summary/task memory scale
  l,t,m,I   Toggle: 'l' load avg; 't' task/cpu; 'm' memory; 'I' Irix mode
  0,1,2,3,4 Toggle: '0' zeros; '1/2/3' cpu/numa views; '4' cpus two abreast
  f,F,X     Fields: 'f'/'F' add/remove/order/sort; 'X' increase fixed-width

  L,&,<,> . Locate: 'L'/'&' find/again; Move sort column: '<'/'>' left/right
  R,H,J,C . Toggle: 'R' Sort; 'H' Threads; 'J' Num justify; 'C' Coordinates
  c,i,S,j . Toggle: 'c' Cmd name/line; 'i' Idle; 'S' Time; 'j' Str justify
  x,y     . Toggle highlights: 'x' sort field; 'y' running tasks
  z,b     . Toggle: 'z' color/mono; 'b' bold/reverse (only if 'x' or 'y')
  u,U,o,O . Filter by: 'u'/'U' effective/any user; 'o'/'O' other criteria
  n,#,^O  . Set: 'n'/'#' max tasks displayed; Show: Ctrl+'O' other filter(s)
  V,v     . Toggle: 'V' forest view; 'v' hide/show forest view children

  k,r       Manipulate tasks: 'k' kill; 'r' renice
  d or s    Set update interval
  W,Y,!     Write config file 'W'; Inspect other output 'Y'; Combine Cpus '!'
  q         Quit
```
For example, we can use **k** to kill a process or **r** to change a priority or **u** to check specific user's process etc.

13. To sort data inside top window we can use **P** for CPU usage, **M** for memory usage.

14. To set a priority we can use **renice** and **nice**  utilities. Example of usage: **nice -<value> <command>** or **renice -n <value> -p <PID>**. 

15. We can change priority using **top** by pressing **r** and following instructions. 

16. To send signal to a process using **kill** we can use following syntaxis **kill -s <signal> <pid>**. There are commonly used signals such as: SIGKILL, SIGTERM.

17.
 * **nohup** - short for no hang up is a command in Linux systems that keep processes running even after exiting the shell or terminal.
 * **jobs** - dispalys status of jobs in the current shell session.
 * **bg** - resumes suspended jobs in the current environment by running them as background jobs.
 * **fg** - place job in the foreground, and make it the current job using fg command.

###Task3.Part2

1. 
<img src="./Screenshots/[to be replaced]" width=100% height=100%>

2. 
