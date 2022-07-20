### Task1

1. Script:
    * check IP addresses and symbolic names of all host in the current subnet by provideng **--all** option
    * check open system TCP ports by providing **--target** optin
    ```   
    #!/bin/bash

    all () {
    arp -a 
    }

    target () {
    ss -tln
    }

    if  [ $# -eq 0 ]
    then
            echo "Missing options"
            echo "Use --all to display the IP addresses and symbolic names of all hosts in the current subnet "
            echo "Use --target to display a list of open system TCP ports."
            echo ""

    elif [ $1 = --all ]
    then 
            all

    elif [ $1 = --target ]
    then 
            target

    else
            echo "No valid options"

    fi
    ```
2. Script to analyze log files:
    ```
    #!/bin/bash

    #Check the most frequent IP
    LOG_FILE="$1"

    echo "The most frequent IP"
    #cut -d " " -f 1 $LOG_FILE | sort | uniq -c | sort -n | tail -n 1
    awk '{print $1}' $LOG_FILE | sort | uniq -c | sort -n | tail -1


    echo ""

    #The most requested page
    echo "The most requested page"
    cut -f2 -d\" $LOG_FILE | sort | uniq -c | sort -n | tail -1

    echo ""

    #How many request were there from each IP
    echo "Requests per ip"
    cut -d " " -f 1 $LOG_FILE | sort | uniq -c | sort -rn

    echo ""

    #Non-existent pages
    echo "Clients were reffered to the following non-existent pages: "
    awk '/error404/{print}' $LOG_FILE

    echo""

    #Number of request per time

    echo "There was the highest number of request at: "
    cat $LOG_FILE | cut -d[ -f2 | cut -d] -f1 | awk -F: '{print $2":"$3":$4"}' | uniq -c | sort -n | tail -1

    echo ""

    #Bots that accessed website
    echo " There were the following bots accesing the site: " 
    cut -d " " -f 1,12-17 $LOG_FILE | grep "bot"  | sort | uniq -c  | sort -n
    ```
3. Data backup script
```
#!/bin/bash

if [ -f "backup.log" ]; then
    echo "backup.log file exists"
else
    touch ./backup.log
    echo "backup.log file created"
fi

if [ -z "$1" ]; then
        echo "No destination folder specified!"
        exit 1
else
        dest=$1
fi

if [ -z "$2" ]; then
        echo "No source folder specified!"
        exit 1
else
        source=$2
fi

input=$source
output=$dest/${user}_home_$(date +%Y-%m-%d_%H%M%S).tar.gz


function total_files {
        find $1 -type f | wc -l
}

function total_directories {
        find $1 -type d | wc -l 
}

function total_archived_directories {
        tar -tzf $1 | grep  /$ | wc -l
}

function total_archived_files {
        tar -tzf $1 | grep -v /$ | wc -l 
}

tar -czf $output $input 2> /dev/null
src_files=$( total_files $input )
src_directories=$( total_directories $input )

arch_files=$( total_archived_files $output )
arch_directories=$( total_archived_directories $output )

echo $(date -u) "Files to be included: $src_files" >> backup.log
echo $(date -u) "Directories to be included: $src_directories" >> backup.log
echo $(date -u) "Files archived: $arch_files" >> backup.log
echo $(date -u) "Directories archived: $arch_directories" >> backup.log

if [ $src_files -eq $arch_files ]; then
        echo $(date -u) "Backup of $input completed!" >> backup.log
        echo $(date -u) "Details about the output backup file:" >> backup.log
        ls -l $output
else
        echo $(date -u) "Backup of $input failed!" >> backup.log
fi

echo "Backup completed. Check backup.log for more details"

```