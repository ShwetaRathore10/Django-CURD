Mealmate - Online Food Ordering System
Mealmate is a Django-based web application that allows users to register as restaurant owners or customers. Restaurant owners can add, edit, and delete restaurants, while customers can browse menus, place orders, and make payments using Razorpay.

Features
Authentication
User registration and login (for both restaurant owners and customers)
Secure authentication using Django's built-in authentication system
Restaurant Management
Add new restaurants
Edit and update restaurant details
Delete restaurants
Menu & Orders
Customers can browse menus
Add items to the cart
Place orders
Payment Integration
Razorpay integrated for secure online payments
Installation & Setup
1. Clone the Repository
git clone https://github.com/your-username/mealmate.git
cd mealmate
2. Set Up a Virtual Environment
python3 -m myenv myenv
source myenv/Scripts/activate 
3. Install Dependencies
pip install Django 
4. Apply Migrations
python manage.py migrate
5. Create a Superuser
python manage.py createsuperuser
6. Run the Development Server
python manage.py runserver
Now, open your browser and go to http://127.0.0.1:8000/

Directory Structure
mealmate/
│── delivery/
│   │── migrations/
│   │── static/
│   │── templates/delivery/
│   │   ├── add_res.html
│   │   ├── base.html
│   │   ├── checkout.html
│   │   ├── cusmenu.html
│   │   ├── customer_home.html
│   │   ├── display_res.html
│   │   ├── failed.html
│   │   ├── index.html
│   │   ├── menu.html
│   │   ├── orders.html
│   │   ├── show_cart.html
│   │   ├── sign_in.html
│   │   ├── sign_up.html
│   │   ├── success.html
│   │   ├── userdata.html
│   │── __init__.py
│   │── admin.py
│   │── apps.py
│   │── forms.py
│   │── models.py
│   │── tests.py
│   │── views.py
│── manage.py
│── requirements.txt
