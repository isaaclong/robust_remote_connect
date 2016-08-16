Boxes that can be difficult to establish incoming ssh connections into because of NATs, Firewalls, etc should run `field/robust_remote_connect.py [cloud_username] [cloud_ip]`. This will use `autossh` to open a `ssh -R` tunnel to a cloud server from the field box. Someone on the cloud server can connect to the box using `cloud/connect_from_cloud.sh [field_username] [field_hostname]`.

Public keys for cloud servers should be added to `cloud/authorized_keys` and public keys for field boxes should be added to `field/authorized_keys`.

Keys in `field/authorized_keys` need to be restricted to only running `cloud/robust_remote_connect_helper.py` for the program to work, see comments `field/authorized_keys` for instructions. This ensures someone with access to the field box after deployment doesn't have full access to the cloud server.

Once keys have been pushed to the repo, running `cloud/add_authorized_keys_from_field.sh` and `field/add_authorized_keys_from_cloud.sh` to add keys from `field/authorized_keys` and `cloud/authorized_keys` respectively to `~/.ssh/authorized_keys` on the cloud servers and field boxes.


Required programs: `autossh, python3`

