# Gas Utility Service Customer Portal

A Django-based customer service portal for gas utility companies that streamlines service request management and improves customer support efficiency.

## 🌟 Features

### For Customers
- *Account Management*
  - Secure user authentication
  - Personal profile management
  - Account information viewing
  
- *Service Requests*
  - Online service request submission
  - Multiple request types support
  - File attachment capability
  - Real-time status tracking
  
### For Support Staff
- *Request Management*
  - Comprehensive dashboard
  - Request assignment system
  - Status updates and tracking
  - Customer communication tools

## 🛠 Technology Stack

- *Backend:* Django 5.0.0
- *Frontend:* Bootstrap 5.3
- *Database:* SQLite (default), compatible with PostgreSQL
- *Authentication:* django-allauth
- *Forms:* django-crispy-forms
- *File Handling:* Pillow

## 📋 Prerequisites

- Python 3.8+
- pip (Python package installer)
- Virtual environment (recommended)

## ⚙ Installation

1. *Clone the repository*
   bash
   git clone https://github.com/yourusername/gas-utility-service.git
   cd gas-utility-service
   

2. *Create and activate virtual environment*
   bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Unix or MacOS
   python -m venv venv
   source venv/bin/activate
   

3. *Install required packages*
   bash
   pip install -r requirements.txt
   

4. *Set up environment variables*
   bash
   # Create .env file in project root and add:
   DJANGO_SECRET_KEY=your_secret_key_here
   DEBUG=True
   

5. *Run migrations*
   bash
   python manage.py makemigrations
   python manage.py migrate
   

6. *Create superuser*
   bash
   python manage.py createsuperuser
   

7. *Run development server*
   bash
   python manage.py runserver
   

## 📁 Project Structure

```
gas_utility_service/
│
├── manage.py 
├── requirements.txt
├── .env
├── README.md
│
├── config/                 # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── apps/
│   ├── accounts/          # User management
│   ├── service_requests/  # Service request handling
│   └── customer_support/  # Support staff features
│
│
└── templates/             # HTML templates
    ├── base.html
    ├── accounts/
    ├── service_requests/
    └── customer_support/

```
## 🔑 Key Features Detail

### Service Request Management
- Create new service requests
- Upload supporting documents
- Track request status
- View request history
- Receive status updates

### Customer Support Dashboard
- View all pending requests
- Assign requests to staff
- Update request status
- Communicate with customers
- Generate reports

## 🔒 Security Features

- Secure user authentication
- Password hashing
- CSRF protection
- User permission system
- Secure file upload handling

## 💻 Usage

### For Customers
1. Register/Login to your account
2. Navigate to "New Request"
3. Fill in request details
4. Upload any necessary files
5. Submit and track your request

### For Support Staff
1. Login with staff credentials
2. Access support dashboard
3. View and manage service requests
4. Update request status
5. Communicate with customers

## 🚀 Development

Want to contribute? Great!

1. Fork the repo
2. Create a new branch (git checkout -b feature/amazing-feature)
3. Make changes
4. Commit (git commit -m 'Add amazing feature')
5. Push (git push origin feature/amazing-feature)
6. Open a Pull Request

## 📝 Testing

Run tests using:
bash
python manage.py test
