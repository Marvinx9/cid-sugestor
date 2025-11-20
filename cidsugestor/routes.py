from cidsugestor import app
from flask import render_template, redirect, url_for, session
from cidsugestor.forms import FormBase
from cidsugestor.gemini_client import generate_response

@app.route("/", methods=["GET", "POST"])
def base():
    form_base = FormBase()
    response_gemini = None
    message = None
    
    if form_base.validate_on_submit():
        message = form_base.texto.data

        session['response_gemini'] = generate_response(message)
        return redirect(url_for('base'))
    
        print(message)
    response_gemini = session.pop('response_gemini', None)
    
    return render_template("base.html", form_base=form_base, response_gemini=response_gemini)
