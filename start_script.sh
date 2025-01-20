#!/bin/bash

# Check if an argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 {1|3|10|30|100|300}"
    exit 1
fi

# Check if the argument is in the allowed list
case $1 in
    1|3|10|30|100|300)
        echo "You have entered a valid number: $1"
        CREDS="monetdb"
        NUMBER=$1
        DB=tpch$NUMBER

        # echo "Creating Database..."
        # monetdb create tpc1

        # echo "Release Database for use"
        # monetdb release tpc1

        # echo "Create a schema"
        # mclient -u $CREDS -d tpc1 -i 0-create_tables.sql
        # echo $CREDS

        # echo "Load the data"
        # mclient -u $CREDS -d $DB -i 1_load_data-SF_1.sql
        # echo $CREDS

        # Loop to run a set of commands append results to a file
        for j in {1..22}; do
            for i in {1..6}; do
                echo "Run $i for query $j" >> results$NUMBER.txt

                if [ $j -lt 10 ]; then
                    { time mclient d $DB -i q0$j.sql; } >> results$NUMBER.txt 2>&1
                    # L
                else
                    { time mclient -d $DB -i q$j.sql; } >> results$NUMBER.txt 2>&1
                fi
                echo "Completed run $i for query $j" | tee -a results$NUMBER.txt
            done
        done
        ;;
    *)
        echo "Invalid number. Please enter one of the following: 1, 3, 10, 30, 100, 300"
        exit 1
        ;;

esac