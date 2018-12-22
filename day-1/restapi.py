from flask import Flask,request
import pandas as pd
app = Flask(__name__)
df= pd.read_csv("physician_rx.csv")
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/preview_new")
def preview_new():
  
    # row_count = request.args.get("rows",type=int)
    row_count = request.args.get("rows",default = 5)
    preview_df=df[0:int(row_count)]
   # return preview_df.to_json(orient='records')
    return preview_df.to_html()

@app.route("/search") 
def search():
    col_name = request.args.get("name",type=str,default = "GlycoMax_RX")
    operator_str =request.args.get("operator",type=str,default = "equals") 
    value = request.args.get("value",type=int,default = 1000) 
    if operator_str == "equals":
          my_df = df[df[col_name] == value]
    elif operator_str == "less than":
          my_df = df[df[col_name] < value]
    elif operator_str == "greater than":
          my_df = df[df[col_name] > value]
    return my_df.to_html() 
@app.route("/preview")
def preview():
  
    start= request.args.get("start",type=int,default = 0)
    end = request.args.get("end",type=int,default = 5)
    columns_str =  request.args.get("columns",type=str,default = "0") #0,2,5
   # columns = []
   # for index in columns_str.split(","):
    #    columns.append(int(index))
    columns=list(map(lambda x: int(x), columns_str.split(",")))
    preview_df1=df.iloc[start:end,columns]

   # return preview_df.to_json(orient='records')
    return preview_df1.to_html()

@app.route("/column/<column_name>")
def column_preview(column_name):
    
    #return df[[column_name]].to_html()
    return df[column_name].to_frame().to_html()

# @app.route("/preview/")
# def new_preview():
#     df= pd.read_csv("physician_rx.csv")
    
if __name__ == "__main__":
    app.run()