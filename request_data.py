from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def hello():
    path = request.path
    full_path = request.full_path
    script_root = request.script_root
    base_url = request.base_url
    url = request.url
    url_root = request.url_root

    total=f"""
        <p>{path}</p>
        <p>{full_path}</p>
        <p>{script_root}</p>
        <p>{base_url}</p>
        <p>{url}</p>
        <p>{url_root}</p>
    """
    return total

if __name__=="__main__":
    app.run(debug=True)