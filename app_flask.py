from flask import Flask, request, render_template
import boto3


app = Flask(__name__, template_folder="template")


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
        print(return_list)
        # return return_list
        # return response["Contents"]
        return return_list

    except:
        return ["NO FOLDER OF THE THIS NAME"]


@app.route("/", methods=["GET"])
def get_files():
    args = request.args
    folder_name = args.get("folder_name")
    print(folder_name)
    return_list = get_list(folder_name)
    return render_template("index.html", return_list=return_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085)
# http://ec2-52-91-201-13.compute-1.amazonaws.com:8085/?folder_name=A
