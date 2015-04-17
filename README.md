 Simple python script to backup a list of volumes. The script will also delete snapshots after 2 weeks.

 Both volume ids and retension can be configured

 You will require a IAM user with the following permission

 {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Snapshotpolicy",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateSnapshot",
                "ec2:DescribeInstanceAttribute",
                "ec2:DescribeInstanceStatus",
                "ec2:DescribeInstances",
                "ec2:DescribeSnapshotAttribute",
                "ec2:DescribeSnapshots",
                "ec2:DescribeVolumeAttribute",
                "ec2:DescribeVolumeStatus",
                "ec2:DescribeVolumes",
                "ec2:ReportInstanceStatus",
                "ec2:CreateTags",
                "ec2:ResetSnapshotAttribute",
                "ec2:DescribeAvailabilityZones",
		"ec2:DeleteSnapshot",
                "ec2:DescribeTags"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
} 

Best practice is to use instance role and then remove the parameters in the connection string for ec2. If your instance is not using instance role then you need IAM user.
 

