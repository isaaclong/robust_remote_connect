touch ~/.ssh/authorized_keys || exit
sort -u ~/.ssh/authorized_keys ~/robust_remote_connect/field/authorized_keys > /tmp/.authorized_keys;
mv /tmp/.authorized_keys ~/.ssh/authorized_keys;
echo keys synced
