from flask import Flask, render_template,request,session
from DBConnection import Db
import time
import datetime

app = Flask(__name__)
app.secret_key="h1"


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/signup')
def signup():
    return render_template('user/signup.html')

@app.route('/signup_post', methods=['post'])
def signup_post():

    name = request.form['textfield']
    gen = request.form['radiobutton']
    place = request.form['textfield3']
    pin = request.form['textfield4']
    Post = request.form['textfield5']
    dis = request.form['textfield6']
    phone = request.form['textfield8']
    email = request.form['textfield9']
    img = request.files['file']
    fname = time.strftime("%Y%m%d%I%M%S%p")
    img.save("C:\\Users\\HP\\PycharmProjects\\house_price_prediction\\static\\user\\" + fname + ".jpg")
    path = "/static/doctor/" + fname + ".jpg"
    ps = request.form['p1']
    psc = request.form['p2']

    d = Db()
    if ps==psc:
        qry = "insert into login(username,password,type) values('"+email+"','"+ps+"','user')"
        res = d.insert(qry)
        qry1 = "insert into user(log_id,name,gen,place,post,district,phone,email,image) values('"+str(res)+"','"+name+"','"+gen+"','"+place+"','"+Post+"','"+dis+"','"+phone+"','"+email+"','"+path+"')"
        res = d.insert(qry1)
        return login()
    else:
        return '''<script>alert('Invalid');window.location='/signup'</script>'''

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_post', methods=['post'])
def login_post():
    a = request.form['t1']
    b = request.form['t2']
    d = Db()
    qry = "select * from login where username='"+a+"' and password='"+b+"'"
    res = d.selectOne(qry)
    if res!=None:
        session['lid']=res['login_id']
        if res['type']=='user':
            return '''<script>alert('Login Success');window.location='/user_index'</script>'''
        elif res['type']=='admin':
            return '''<script>alert('Login Success');window.location='/admin_index'</script>'''
        else:
            return '''<script>alert('Invalid user');window.location='/login'</script>'''
    else:
        return '''<script>alert('Invalid user');window.location='/login'</script>'''


@app.route('/user_index')
def user_index():
    return render_template('user/user_index.html')

@app.route('/view_prof')
def view_prof():
    d = Db()
    qry = "select * from user where log_id='"+str(session['lid'])+"'"
    res = d.selectOne(qry)
    return render_template('user/profile.html',data=res)

@app.route('/page')
def page():
    return render_template('user/page.html')

@app.route('/page_load', methods=['post'])
def page_load():
    MSubClass = request.form['msc']
    MSZoning = request.form['msz']
    LotFrontage = request.form['ltf']
    lotarea = request.form['lta']
    Street = request.form['st']
    Alley= request.form['aly']
    LotShape = request.form['lts']
    LandContour = request.form['lct']
    Utilities = request.form['ut']
    LotConfig= request.form['ltcf']
    Neighborhood = request.form['nbh']
    Condition1 = request.form['c1']
    Condition2 = request.form['c2']
    BldgType = request.form['bldg']
    HouseStyle = request.form['HouseStyle']
    OverallQual = request.form['OverallQual']
    OverallCond = request.form['OverallCond']
    YearBuilt = request.form['YearBuilt']
    RoofStyle = request.form['s1']
    material = request.form['s2']
    Exterior = request.form['s3']
    exterior_house = request.form['s4']
    OverallQual = request.form['OverallQual']
    Masonry = request.form['s5']
    MasVnrArea = request.form['i1']
    mat_qual = request.form['s6']
    p_cond = request.form['s7']
    t_found = request.form['s8']
    basement_hight = request.form['s9']
    g_cond = request.form['s10']
    walkout = request.form['s11']
    rating = request.form['s12']
    f_sq_ft = request.form['sq_ft']
    rating_2 = request.form['s13']
    BsmtFinSF2 = request.form['i2']
    BsmtUnfSF = request.form['i3']
    total_sq_ft = request.form['i4']
    Heating = request.form['s14']
    Heating_qual = request.form['s15']
    c_Ac = request.form['s16']
    ec = request.form['s17']
    f_floor_sq_ft = request.form['i5']
    s_floor_sq_ft = request.form['i6']
    l_quality = request.form['i8']
    a_grade = request.form['i19']
    basment_fb = request.form['i10']
    basment_hb = request.form['i11']
    basment_hab = request.form['i12']
    bedroom = request.form['i13']
    Kitchen = request.form['i14']
    k_qual = request.form['k18']
    TotRmsAbvGrd = request.form['i15']
    Functional= request.form['s18']
    Fireplaces = request.form['i16']
    Fireplaces_qual = request.form['s19']
    GarageType= request.form['s20']
    GarageYrBlt = request.form['i17']
    GarageFinish= request.form['s21']
    GarageCars= request.form['i18']
    GarageArea = request.form['i19']
    Garage_qual = request.form['s22']
    Garage_condition =request.form['s23']
    Paved_dr = request.form['s24']
    wood_deck =request.form['i20']
    open_porch = request.form['i21']
    enclose = request.form['i22']
    three_season = request.form['i23']
    scren_prch = request.form['i24']
    pool = request.form['i25']
    pool_qual = request.form['s25']
    fence_qual = request.form['s26']
    MiscFeature = request.form['s27']
    value_misfeatr = request.form['i26']
    msold = request.form['msold']
    ysold = request.form['i27']
    type_sale = request.form['s28']
    condition_sale = request.form['s29']
    return page()

@app.route('/admin_index')
def admin_index():
    return render_template('admin/index.html')

@app.route('/view_user')
def view_user():
    d = Db()
    qry = "select * from user"
    res = d.select(qry)
    return render_template('admin/view_user.html', data=res)

@app.route('/view_user_post', methods=['post'])
def view_user_post():
    search = request.form['textfield']
    d = Db()
    qry = "select * from user where name like '%"+search+"%'"
    res = d.select(qry)
    return render_template('admin/view_user.html', data=res)

if __name__ == '__main__':
    app.run(debug=True)
