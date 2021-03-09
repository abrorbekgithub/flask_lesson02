from flask import Flask,request

app=Flask(__name__)
  
@app.route('/api')
def api():
    r=request.args
    print(r)
    a=int(r.get("a",0))
    b=int(r.get("b",0))

    for k,v in r.items():
        print(k,v)

    return { "sum": a + b }

@app.route('/form',methods=['GET','POST'])
def get_form():
    if request.method=='GET':
        print('get')
    if request.method=='POST':
        print('post')
    return 'ok'

@app.route('/')
def hello():
    path = request.path
    full_path = request.full_path
    script_root = request.script_root
    base_url = request.base_url
    url = request.url
    url_root = request.url_root

    total=f"""
        <p> path:{path}</p>
        <p> full path:{full_path}</p>
        <p> script root:{script_root}</p>
        <p> base url:{base_url}</p>
        <p> url:{url}</p>
        <p>url root:{url_root}</p>
    """
    return total

if __name__=="__main__":
    app.run(debug=True)