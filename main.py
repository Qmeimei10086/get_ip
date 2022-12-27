from flask import Flask, send_file,request

app = Flask(__name__)



@app.route('/get_ip')
def get_ip():
    result = """
    <head>
	    <meta itemprop="name" content="xml卡片标题" />
	    <meta itemprop="description" content="xml卡片描述" />
	    <meta itemprop="image" content="img?id=test.png" />
	    <title>标题</title>
    </head>
    """
    return result

@app.route('/img',methods=['GET'])
def img():
    id = request.args.get("id")
    return send_file(("./static/"+id),mimetype='image/gif')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
