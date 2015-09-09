from flask import Flask, render_template, request, redirect
import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.resources import CDN
from bokeh.embed import file_html

app = Flask(__name__)
app.vars={}

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html',ans1='Closing price',ans2='Adjusted closing price',ans3='Volume')
    else:
        # request was a POST
        data=pd.read_csv("wiki.csv",parse_dates=['date'])
        #d=data[data['name'] == 'A']
        #dates=d['date'].tolist()
        sname=pd.read_csv("stock_name.csv")['x'].tolist()
        s=request.form['symbol']
        if s not in sname:
            return render_template('end.html')
        else:
            d=data[data['name'] == s]
            dates=d['date'].tolist()
        #app.vars['symbol'] = request.form['symbol']
        #f = open('%s.txt'%(app.vars['symbol']),'w')
        #f.write('%s\n'%(request.form.getlist('answer')==["Closing price","Adjusted closing price","Volume"]))
        #f.write('%s\n'%(request.form['symbol']=='A'))
        #f.write('%s\n'%(request.form['symbol']))
        #f.write('%s\n'%(app.vars['symbol']))
        #f.close()
        #f = open('%s.txt'%(app_lulu.vars['symbol']),'a')
        #f.write('%s\n\n'%(request.form.getlist['answer'])) #this was the 'name' on layout.html!
            color=["blue","yellow","red"]
        #output_file("a.html")
            p=figure(x_axis_type="datetime")
            nd={}
            nd['Closing']="Closing price"
            nd['Adjusted']="Adjusted closing price"
            nd['Volume']="Volume"
            j=0
            ts=d['Closing price'].tolist()
            for i in request.form.getlist('answer'):
                ts=d[nd[i]].tolist()
                p.line(dates,ts,legend=nd[i],color=color[j])
                j=j+1
            html=file_html(p,CDN,"plot")
            fh=open("templates/plot.html",'w')
            fh.write(html)
            fh.close()
            #f.write("%s\n" % item)
            return render_template('plot.html')
        #return redirect('/main_lulu')

if __name__ == "__main__":
    app.run(debug=True)
#if __name__ == '__main__':
#  app.run(port=33507)
