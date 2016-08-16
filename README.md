Boxes that can be difficult to establish incoming ssh connections into because of NATs, Firewalls, etc should run `field/robust_remote_connect.py [cloud_username] [cloud_ip]`

This will use `autossh` to open a `ssh -R` tunnel to a cloud server. Public keys for cloud servers should be added to `cloud/authorized_keys` and public keys for field boxes should be added to `field/authorized_keys`. Keys in `field/authorized_keys` should be restricted to only running `cloud/robust_remote_connect_helper.py` for the program to work. This ensures someone with access to the field box after deployment doesn't have full access to the cloud server. Run `cloud/add_authorized_keys_from_field.sh` and `field/add_authorized_keys_from_cloud.sh` to add keys from `field/authorized_keys` and `cloud/authorized_keys` respectively to `~/.ssh/authorized_keys`.

Required programs: `autossh, python3`

