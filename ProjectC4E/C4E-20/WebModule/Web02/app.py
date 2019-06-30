# fapp
from flask import *
import mlab, datetime
from mongoengine import *
from models.service import Service
from models.customer import Customer
from models.user import User
from models.order import Order
from gmail import GMail, Message

app = Flask(__name__)
app.secret_key = 'a super super secret key'
mlab.connect()

# design pattern (MVC, MVP)
# view populate.py, service.py

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<int:gender>')
def search(gender):
    all_service = Service.objects(gender=gender)
    return render_template(
        'search.html',
        all_service=all_service)

@app.route('/customer')
def index1():
    return render_template('index1.html')

@app.route('/search1/<g>')
def search1(g):
    all_customer = Customer.objects(gender=g)
    return render_template(
        'search1.html',
        all_customer=all_customer)

@app.route('/customer/<g>')
def customer(g):
    all_customer = Customer.objects[:10](gender=g, contacted=False)
    return render_template(
        'search1.html',
        all_customer = all_customer)

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template(
        'admin.html',
        all_service=all_service
        )

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    if service_to_delete is not None:
        service_to_delete.delete()
        return redirect(url_for('admin'))
    else:
        return 'Service not found'

@app.route('/update_service/<service_id>', methods=['GET', 'POST'])
def update_service(service_id):
    service = Service.objects.with_id(service_id)
    if request.method == 'GET':
        return render_template('update_service.html', service=service)
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        gender = form['gender']
        height = form['height']
        address = form['address']

        service.name = name
        service.yob = yob
        service.phone = phone
        service.gender = gender
        service.height = height
        service.address = address
    
        service.save()
        return redirect(url_for('admin'))

@app.route('/new-service', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('new-service.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        gender = form['gender']

        new_service = Service(
            name=name,
            yob=yob,
            phone=phone,
            gender=gender
        )
        new_service.save()
        return redirect(url_for('admin'))

@app.route('/sign_in', methods=['GET','POST'])
def sign_in():
    if request.method == 'GET':
        return render_template('sign_in.html')
    elif request.method == 'POST':
        form = request.form
        fullname = form['fullname']
        email = form['email']
        username = form['username']
        password = form['password']

        new_user = User(
            username=username,
            password=password,
            email=email,
            fullname=fullname
        )

        new_user.save()
        return redirect(url_for('index'))    

@app.route('/detail/<service_id>')
def detail(service_id):
    service = Service.objects.with_id(service_id)
    session['service'] = str(service.id)
    if 'loggedin' in session:
        if session['loggedin'] == True:
            if service is not None:
                return render_template('detail.html', service=service)
            else:
                return 'Service is not found'
        else:
            return 'Yêu cầu đăng nhập'
    else:
        return 'Yêu cầu đăng nhập'

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        form = request.form 
        username = form['username']
        password = form['password']

        found_user = User.objects(
            username=username,
            password=password
        )
        if found_user:
            session['loggedin'] = True
            user = User.objects.get(username=username)
            session['user'] = str(user.id)
            return redirect(url_for('index'))
        else:
            return redirect(url_for('sign_in'))

@app.route('/logout')
def logout():
    session['loggedin'] = False
    session.clear()
    return redirect(url_for('index'))

@app.route('/ordered') 
def ordered():
    user = session['user']
    service = session['service']
    new_order = Order(
        user=user,
        service=service,
        order_time=datetime.datetime.now(),
        is_accepted = False
    )
    new_order.save()
    return 'Đã gửi yêu cầu'

@app.route('/order')
def order():
    orders = Order.objects()
    return render_template('order.html', orders=orders)

@app.route('/accepted/<order_id>')
def accepted(order_id):
    order = Order.objects.with_id(order_id)
    email = order.user.email
    order.update(is_accepted = True)
    
    gmail = GMail('nguyenmson98@gmail.com','abc')
    msg = Message(
    'Phê duyệt yêu cầu',
    to=email,
    text="Yêu cầu của bạn đã được xử lý, chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất. Cảm ơn bạn đã sử dụng dịch vụ của 'Mùa Đông Không Lạnh'")
    gmail.send(msg)

    return redirect(url_for('order'))
    

if __name__ == '__main__':
  app.run(debug=True)
 