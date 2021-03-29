from flask import Flask, request, redirect, render_template


app = Flask(__name__)

@app.route('/') 
def sql_database():
    from functions.sqlquery import sql_query
    results = sql_query(''' SELECT * FROM data_table''')
    msg = 'SELECT * FROM data_table'
    return render_template('sqldatabase.html', results=results, msg=msg)   
    
    
@app.route('/insert',methods = ['POST', 'GET']) 
def sql_datainsert():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        id = request.form['id']
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        amount_due = request.form['amount_due']
        sql_edit_insert(''' INSERT INTO data_table (id,first_name,last_name,amount_due) VALUES (?,?,?,?) ''', (id,first_name,last_name,amount_due) )
    results = sql_query(''' SELECT * FROM data_table''')
    msg = 'INSERT INTO data_table (id,first_name,last_name,amount_due) VALUES ('+id+','+first_name+','+last_name+','+amount_due+')'
    return render_template('sqldatabase.html', results=results, msg=msg) 
    

@app.route('/delete',methods = ['POST', 'GET'])
def sql_datadelete():
    from functions.sqlquery import sql_delete, sql_query
    if request.method == 'GET':
        lname = request.args.get('lname')
        fname = request.args.get('fname')
        sql_delete(''' DELETE FROM data_table where first_name = ? and last_name = ?''', (fname,lname) )
    results = sql_query(''' SELECT * FROM data_table''')
    msg = 'DELETE FROM data_table WHERE first_name = ' + fname + ' and last_name = ' + lname
    return render_template('sqldatabase.html', results=results, msg=msg)
    
    
@app.route('/query_edit',methods = ['POST', 'GET'])
def sql_editlink():
    from functions.sqlquery import sql_query, sql_query2
    if request.method == 'GET':
        elname = request.args.get('elname')
        efname = request.args.get('efname')
        eresults = sql_query2(''' SELECT * FROM data_table where first_name = ? and last_name = ?''', (efname,elname))
    results = sql_query(''' SELECT * FROM data_table''')
    return render_template('sqldatabase.html', eresults=eresults, results=results)
    
    
@app.route('/edit',methods = ['POST', 'GET'])
def sql_dataedit():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        id = request.form['id']
        old_last_name = request.form['old_last_name']
        old_first_name = request.form['old_first_name']
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        amount_due = request.form['amount_due']
        sql_edit_insert(''' UPDATE data_table set id=?,first_name=?,last_name=?,amount_due=? WHERE first_name=? and last_name=? ''', (id,first_name,last_name,amount_due,old_first_name,old_last_name) )
    results = sql_query(''' SELECT * FROM data_table''')
    msg = 'UPDATE data_table set first_name = ' + first_name + ', last_name = ' + last_name + ' WHERE first_name = ' + old_first_name + ' and last_name = ' + old_last_name
    return render_template('sqldatabase.html', results=results, msg=msg)

if __name__ == "__main__":
    app.run(debug=True)

