while read line; do    
    grep $line $1 | tail -1
done < $2
