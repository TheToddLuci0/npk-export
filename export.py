import boto3
import sys
import argparse


def main():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()['Buckets']
    # print("Found {} buckets".format(len(buckets)))
    bucket = None
    for b in buckets:
        if b['Name'].startswith('npk-user-data-'):
            bucket = b['Name']
            break
    if bucket == None:
        sys.exit("User data bucket not found")
    # print("Found bucket {}".format(bucket))
    files = s3.list_objects_v2(Bucket = bucket)['Contents']
    potfiles = []
    for f in files:
        if f['Key'].endswith('all_cracked_hashes.txt'):
            potfiles.append(f['Key'])
    # print(potfiles)
    hashes = set()
    for p in potfiles:
        # print("Downloading {}".format(p))
        hashfile = s3.get_object(Bucket=bucket, Key=p)
        for h in hashfile['Body'].readlines():
            hashes.add(h.strip().decode('ASCII'))
    return hashes




if __name__ == '__main__':
    print(*(main()), sep='\n')
