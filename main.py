from flask import Flask,render_template,request,redirect,url_for
from sqlalchemy import Table,Column,Integer,String,Text,Boolean,Date,text,insert,update,select
from conn_pool import engine,metadata

app=Flask(__name__)

tasks_asgmt=Table(
    'tasks_asgmt',
    metadata,
    Column('assignment_id',Integer,primary_key=True),
    Column('title',String(150),nullable=False),
    Column('subject',String(150),nullable=False),
    Column('descr',Text),
    Column('due_date',Date),
    Column('is_submitted',Boolean),
    Column('submitted_at',Date,onupdate=text('CURRENT_TIMESTAMP'))
)

metadata.create_all(engine)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_asgmt/',methods=['GET','POST'])
def add_asgmt():
    if request.method=='POST':
        title=request.form["title"]
        subject=request.form["subject"]
        descr=request.form["descr"]
        due_date=request.form["due_date"]

        stmt=insert(tasks_asgmt).values(
            title=title,
            subject=subject,
            descr=descr,
            due_date=due_date,
            is_submitted=False
        )
        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()
        return redirect(url_for("view_asgmt"))
    return render_template('add_asgmt.html')

@app.route('/view_asgmt/')
def view_asgmt():
    stmt=select(tasks_asgmt).where(tasks_asgmt.c.is_submitted==False)
    with engine.connect() as conn:
        data=conn.execute(stmt)
        task_list=data.fetchall()
    return render_template('view_asgmt.html',tasks=task_list)

@app.route('/complete_asgmt/',methods=["POST"])
def complete_asgmt():
    assignment_id=request.form["assignment_id"]
    stmt=update(tasks_asgmt).where(tasks_asgmt.c.assignment_id==assignment_id).values(is_submitted=True)
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()
    return redirect(url_for('view_asgmt'))

@app.route('/completed_asgmt/')
def completed_asgmt():
    stmt=select(tasks_asgmt).where(tasks_asgmt.c.is_submitted==True)
    with engine.connect() as conn:
        data=conn.execute(stmt)
        tasks_list=data.fetchall()
    return render_template('complete_asgmt.html',tasks=tasks_list)

if __name__=='__main__':
    app.run(debug=True)