import psutil
from flask import Flask 

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory()
    Message = None
    if cpu_percent > 80 or cpu_percent > 80:
        Message = High cpu or memory utilization detected,please scale up""
    return f"cpu utilization : {cpu_percent} and memory utilization : {mem_percent}"

    if __name__ == "__main__":
        app.run(debug=True,host = '0.0.0.0')



