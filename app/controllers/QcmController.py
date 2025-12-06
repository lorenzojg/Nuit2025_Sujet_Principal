from flask import render_template, request
from app import app

from flask import session, flash

# Can't url for with qcm
# @app.route('/qcm<num>')
# def qcm(num):
    # return render_template(f"qcm{num}.html", metadata={'pagename': f"qcm{num}"})

@app.route('/qcm1', methods= ['GET', 'POST'])
def qcm1():
    if 'progression' not in session:
        session['progression'] = {}
    if request.method == 'POST':
        session["progression"]['1'] = True
    return render_template('qcm1.html', metadata={'pagename': 'qcm1'})

@app.route('/qcm2')
def qcm2():
    if 'progression' not in session:
        session['progression'] = {}
    session["progression"]['2'] = True
    return render_template('qcm2.html', metadata={'pagename': 'qcm2'})

@app.route('/qcm3')
def qcm3():
    if 'progression' not in session:
        session['progression'] = {}
    session["progression"]['3'] = True
    return render_template('qcm3.html', metadata={'pagename': 'qcm3'})

@app.route('/qcm4')
def qcm4():
    if 'progression' not in session:
        session['progression'] = {}
    session["progression"]['4'] = True
    return render_template('qcm4.html', metadata={'pagename': 'qcm4'})

@app.route('/qcm5')
def qcm5():
    if 'progression' not in session:
        session['progression'] = {}
    session["progression"]['5'] = True
    return render_template('qcm5.html', metadata={'pagename': 'qcm5'})

@app.route('/qcm6')
def qcm6():
    if 'progression' not in session:
        session['progression'] = {}
    session["progression"]['6'] = True
    return render_template('qcm6.html', metadata={'pagename': 'qcm6'})

@app.route('/qcm7')
def qcm7():
    if 'progression' not in session:
        session['progression'] = {}
    session["progression"]['7'] = True
    return render_template('qcm7.html', metadata={'pagename': 'qcm7'})

@app.route('/qcm8')
def qcm8():
    if 'progression' not in session:
        session['progression'] = {}
    session["progression"]['8'] = True
    return render_template('qcm8.html', metadata={'pagename': 'qcm8'})

@app.route('/qcm9')
def qcm9():
    if 'progression' not in session:
        session['progression'] = {}
    session["progression"]['10'] = True
    return render_template('qcm9.html', metadata={'pagename': 'qcm9'})

@app.route('/qcm10')
def qcm10():
    if 'progression' not in session:
        session['progression'] = {}
    session["progression"]['11'] = True
    return render_template('qcm10.html', metadata={'pagename': 'qcm10'})

@app.route('/qcm11')
def qcm11():
    if 'progression' not in session:
        session['progression'] = {}
    session["progression"]['12'] = True
    return render_template('qcm11.html', metadata={'pagename': 'qcm11'})

@app.route('/qcm12')
def qcm12():
    if 'progression' not in session:
        session['progression'] = {}
    session["progression"]['12'] = True
    return render_template('qcm12.html', metadata={'pagename': 'qcm12'})

@app.route('/qcm13')
def qcm13():
    if 'progression' not in session:
        session['progression'] = {}
    session["progression"]['13'] = True
    return render_template('qcm13.html', metadata={'pagename': 'qcm13'})

@app.route('/qcm14')
def qcm14():
    if 'progression' not in session:
        session['progression'] = {}
    session["progression"]['14'] = True
    return render_template('qcm14.html', metadata={'pagename': 'qcm14'})

@app.route('/qcm15')
def qcm15():
    if 'progression' not in session:
        session['progression'] = {}
    session["progression"]['15'] = True
    return render_template('qcm15.html', metadata={'pagename': 'qcm15'})

@app.route('/qcm16')
def qcm16():
    if 'progression' not in session:
        session['progression'] = {}
    session["progression"]['16'] = True
    return render_template('qcm16.html', metadata={'pagename': 'qcm16'})

@app.route('/qcm17')
def qcm17():
    if 'progression' not in session:
        session['progression'] = {}
    session["progression"]['17'] = True
    return render_template('qcm17.html', metadata={'pagename': 'qcm17'})

@app.route('/qcm18')
def qcm18():
    if 'progression' not in session:
        session['progression'] = {}
    session["progression"]['18'] = True
    return render_template('qcm18.html', metadata={'pagename': 'qcm18'})

@app.route('/qcm19')
def qcm19():
    if 'progression' not in session:
        session['progression'] = {}
    session["progression"]['19'] = True
    return render_template('qcm19.html', metadata={'pagename': 'qcm19'})

@app.route('/qcm20')
def qcm20():
    if 'progression' not in session:
        session['progression'] = {}
    session["progression"]['20'] = True
    return render_template('qcm20.html', metadata={'pagename': 'qcm20'})
