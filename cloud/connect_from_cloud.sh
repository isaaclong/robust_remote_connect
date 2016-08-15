if [ "$#" -ne 2 ]; then
echo "Usage: $0 [username] [hostname]"
exit 1
fi

PORT=$(cat /tmp/remote_connect_ports/$2 2> /dev/null )
if [ $PORT ]; then
    echo "Trying to connect to $1@$2 which we expect to be accessible on local port $PORT"
    ssh -p $PORT $1@localhost
else
    echo "Can't connect to $1@$2"
fi
