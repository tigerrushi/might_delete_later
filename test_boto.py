import boto3


def get_list(folder_name):
    try:
        # s3 = boto3.resource("s3", aws_access_key_id=ACCESS_ID, aws_secret_access_key=ACCESS_KEY)

        # print(s3)

        client = boto3.client("s3")
        response = client.list_objects_v2(
            Bucket="tiger-mle-pg", Prefix=f"home/rushikesh.naik/{folder_name}/"
        )
        return_list = []
        for key in response["Contents"]:
            return_list.append(key["Key"])

        return return_list
        # return response["Contents"]

    except:
        return "<h1>NO FOLDER OF THE THIS NAME</h1>"
