from flask import Flask, request, jsonify, make_response, render_template
import nltk15_sentimental_analysis as sa
import json

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    error=None
    senti=None
    if request.method=="POST":
        data=request.form['text']
        if data:
            try:
                out=sa.sentiment(data)
                senti = out[0].decode("utf-8") 
            except Exception as e:
                app.logger.error(e)
                error="Internal Server Error"
    return render_template('index.html', senti = senti,error=error)


# @app.route('/sentiment',methods=["POST"])
# def sentiment():
# 	data=request.form['text']
# 	if data:
# 		try:
# 			out=senti.sentiment(data)
# 		except Exception as e:
# 			app.logger(e)
# 			return make_response("UNKOWN RESPONSE",500)
# 		sent = out[0].decode("utf-8") 
# 		return render_template('index.html', senti = sent)
# 	return make_response("No text found",400)	


if __name__=="__main__":
	app.debug=True
	app.run(host="0.0.0.0",port=8000)
