from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def form():
    return render_templete("form.html")


@app.route("/confirm",methods=["POST","GET"])
def confirm():
    if request.method=="POST":
        result=request.form["Name"]   #form.htmlのタグ"Name"の値を取得
        return render_templete("confirm.html",name=result)#nameに値を渡す
