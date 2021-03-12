# Dr. Thitsa's Research Team: ATSPM Web Engine
This website allow users to upload CSV files that contain ATSPM data. 
The website will use machine learning algorithms to make traffic predictions based on that data.

This website is created using Vue for the frontend and Flask for the backend.

The code will not work unless there is a "config.py" file in the main server directory. The file should look like this:

```
import uuid as key


def s3_file_bucket():
    return (S3 File Bucket)


def s3_image_bucket():
    return (S3 Image Bucket)


def s3_access_key_id():
    return (S3 Access Key ID)


def s3_secret_key():
    return (S3 Secret Key)


def s3_file_location():
    return "https://{}.s3.amazonaws.com/".format(s3_file_bucket())


def s3_image_location():
    return "https://{}.s3.amazonaws.com/".format(s3_image_bucket())


def app_secret_key():
    return key.uuid4().hex


def debug():
    return (True or False)


def port():
    return PORT
    
```
This file will be used to insert all of your AWS data, but it is not included in Git so that the security of the AWS data is uncompromised.

This project is a collaboration between [Mercer University](https://www.mercer.edu) and [Georgia Institute of Technology](https://www.gatech.edu).
