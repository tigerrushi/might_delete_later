from flask import Flask, request
import test_boto

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_files():
    args = request.args
    folder_name = args.get("folder_name")
    print(folder_name)

    return test_boto.get_list(folder_name)
