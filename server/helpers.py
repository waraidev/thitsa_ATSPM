# In order to use this server properly
# create a config.py file that looks like this:
#
# import uuid as key
#
#
# def s3_bucket():
#     return (S3 Bucket)
#
#
# def s3_access_key_id():
#     return (S3 Access Key ID)
#
#
# def s3_secret_key():
#     return (S3 Secret Key)
#
#
# def s3_location():
#     return "https://%s.s3.amazonaws.com/" % s3_bucket()
#
#
# def app_secret_key():
#     return key.uuid4().hex
#
#
# def debug():
#     return (True of False)
#
#
# def port():
#     return PORT
#
#

import boto3
import config

s3 = boto3.client(
    "s3",
    aws_access_key_id=config.s3_access_key_id(),
    aws_secret_access_key=config.s3_secret_key()
)


def upload_file_s3(file, bucket_name, acl="public-read"):
    # Docs: http://boto3.readthedocs.io/en/latest/guide/s3.html
    try:
        s3.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )
    except Exception as e:
        print("File didn't upload: ", e)
        return e

    return "%s%s" % config.s3_location(), file.filename
