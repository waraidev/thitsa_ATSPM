# In order to use this server properly
# create a config.py file that looks like this:
#
# import uuid as key
#
#
# def s3_file_bucket():
#     return (S3 File Bucket)
#
# def s3_image_bucket():
#     return (S3 Image Bucket)
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


def get_signal_name(filename):
    signal_index = filename.find("signalID_")
    signal = filename[signal_index + 9:signal_index + 9 + 4]
    return "signal" + signal + ".png"


def upload_file_s3(file, bucket_name, filename=None, content_type="image/png", acl="public-read"):
    # Docs: http://boto3.readthedocs.io/en/latest/guide/s3.html
    if filename is None:
        filename = file.filename
        content_type = file.content_type

    try:
        s3.upload_fileobj(
            file,
            bucket_name,
            filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": content_type
            }
        )
    except Exception as e:
        print("File didn't upload: ", e)
        return e

    return "{}{}".format(config.s3_location(), filename)


def delete_file_s3(filename, bucket_name):
    try:
        s3.delete_object(Bucket=bucket_name, Key=filename)
    except Exception as e:
        return e

    return "\'{}\' has been deleted!".format(filename)


def get_all_files_s3(bucket_name):
    try:
        bucket = s3.list_objects_v2(Bucket=bucket_name)
    except Exception as e:
        return e

    return [file['Key'] for file in bucket['Contents']]


def get_filename(filename):
    return "{}{}".format(config.s3_location(), filename)
