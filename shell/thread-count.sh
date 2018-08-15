#!/usr/bin/bash
# user: zhanglintc

if [[ -z "$1" ]]; then
    name="all"
else
    name="$1"
fi

echo "Counting: $name"
while true; do
    # get count of given name
    cnt=`ps -xH | grep -w "$1" | grep -v -w sh | grep -v -w bash | grep -v -w grep | wc -l`

    # clean current line
    echo -en "                        \r"

    # show count result
    echo -en "Current number: $cnt\r"

    # sleep
    sleep 0.5
done
