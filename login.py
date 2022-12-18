from werkzeug.wrappers import Request, Response
from flask import *  
import sqlite3  
  
app = Flask(__name__)  
 
@app.route("/")  
def index():  
    return render_template("login.html");  
 
# @app.route("/add")  
# def add():  
#     return render_template("A_add.html")

# @app.route("/model")
# def model():
#     return render_template("A_modelanswer.html")

# @app.route("/addmodelanswer",methods=["POST","GET"])
# def addmodelanswer():
#     msg="msg"
#     if request.method == "POST":
#         try:
#             first_model = request.form["first_model"]
#             second_model = request.form["second_model"]
#             with sqlite3.connect("answers.db") as con:
#                 cur=con.cursor()
#                 cur.execute("INSERT into Answers (first_model,second_model) values (?,?)",(first_model,second_model))
#                 con.commit()
#                 msg="Answer added successfully"
#         except:
#             con.rollback()
#             msg="We cannot add the answer to the list"
#         finally:
#             return render_template("A_success.html",msg=msg)
#             con.close()
            
 
# @app.route("/savedetails",methods = ["POST","GET"])  
# def saveDetails():  
#     msg = "msg"  
#     if request.method == "POST":  
#         try:  
#             name = request.form["name"]  
#             email = request.form["email"]  
#             address = request.form["address"]  
#             with sqlite3.connect("employee.db") as con:  
#                 cur = con.cursor()  
#                 cur.execute("INSERT into Employees (name, email, address) values (?,?,?)",(name,email,address))  
#                 con.commit()  
#                 msg = "Employee successfully Added"  
#         except:  
#             con.rollback()  
#             msg = "We can not add the employee to the list"  
#         finally:  
#             return render_template("A_success.html",msg = msg)  
#             con.close()  
 
# @app.route("/view")  
# def view():  
#     #t=1
#     con = sqlite3.connect("employee.db")  
#     con.row_factory = sqlite3.Row  
#     cur = con.cursor()  
#     cur.execute("select * from Employees")
#     #cur.execute("select * from Employees where ID = {}".format(t))  
#     rows = cur.fetchall()  
#     return render_template("A_view.html",rows = rows) 

# @app.route("/viewans")  
# def viewans():  
#     #t=1
#     con = sqlite3.connect("answers.db")  
#     con.row_factory = sqlite3.Row  
#     cur = con.cursor()  
#     cur.execute("select * from Answers")
#     rows = cur.fetchall()  
#     return render_template("A_viewans.html",rows = rows) 
 
# @app.route("/deleteans")  
# def deleteans():  
#     return render_template("A_deleteans.html")  
 
# @app.route("/deleteansrecord",methods = ["POST"])  
# def deleteansrecord():  
#     id = request.form["id"]  
#     with sqlite3.connect("answers.db") as con:  
#         try:  
#             cur = con.cursor()  
#             cur.execute("delete from Answers where id = ?",id)  
#             msg = "record successfully deleted"  
#         except:  
#             msg = "can't be deleted"  
#         finally:  
#             return render_template("A_delete_record.html",msg = msg)  
    
# @app.route("/delete")  
# def delete():  
#     return render_template("A_delete.html")  
 
# @app.route("/deleterecord",methods = ["POST"])  
# def deleterecord():  
#     id = request.form["id"]  
#     with sqlite3.connect("employee.db") as con:  
#         try:  
            
#             cur = con.cursor()  
#             cur.execute("delete from Employees where id = ?",id)  
#             msg = "record successfully deleted"  
#         except:  
#             msg = "can't be deleted"  
#         finally:  
#             return render_template("A_delete_record.html",msg = msg)  
  
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 9000, app)