touch ~/.ssh/authorized_keys || echo no authorized keys file || exit
sort -u ~/.ssh/authorized_keys <(grep -v ^# ~/robust_remote_connect/cloud/authorized_keys) > /tmp/.authorized_keys;
mv /tmp/.authorized_keys ~/.ssh/authorized_keys;
echo keys synced
