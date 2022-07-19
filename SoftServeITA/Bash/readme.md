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
