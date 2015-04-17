#!/usr/bin/env python
# Simple script to create ebs snapshots for volume list and cleanup of snapshots after n of days

import boto
from boto import ec2
from datetime import datetime
from datetime import timedelta

now = datetime.now()
today = now.date()

#Definitions
num_of_days_to_keep=13
volume_list = { 'portaldata': 'vol-111111','bankdata': 'vol-2222222' }

conn =  boto.ec2.connect_to_region("ap-southeast-2", aws_access_key_id='AAAAAAAAAAAAAAAAAAAAAAAAA', aws_secret_access_key='BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB')

for name,id in volume_list.items():
        print "%s id is %s"% (name,id)
        desc = "%s-%s" % (name,today)
        snap_obj = conn.create_snapshot(id, description=desc)
        if (snap_obj):
                snap_obj.add_tags({'user': 'portalsnapshot'})
        print "%s snapshot id %s"% (name,snap_obj.id)

two_weeks_ago = (today - timedelta(days=num_of_days_to_keep))

for name,id in volume_list.items():

        OldDesc =  "%s-%s" % (name,two_weeks_ago)

        snapshots = conn.get_all_snapshots(filters = {"description": OldDesc})

        for i in snapshots:
                print i.id
                try:
                        print "delete snapshot %s" % i.id
                        conn.delete_snapshot(i.id)
                except Exception, err:
                        print Exception, err
