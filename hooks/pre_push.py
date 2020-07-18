#!/usr/bin/python3

import sys

[remote_name, remote_loc] = sys.argv[1:]

[local_ref, local_sha1, remote_ref, remote_sha1] = sys.stdin.read().split()

if remote_loc.lower() == "git@github.com:yugabyte/yugabyte-db.git":
    if (remote_ref != "refs/heads/master"):
        print("Cannot push to yugabyte repo")
        sys.exit(1)
