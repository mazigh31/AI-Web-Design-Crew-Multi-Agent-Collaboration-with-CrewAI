import pytest
from app import app as flask_app
from forms.contact_form import ContactForm
from forms.booking_form import BookingForm

@pytest.fixture
def app():
    app = flask_app
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

# Test route accessibility

def test_home_page_accessibility(client):
    response = client.get('/')  
    assert response.status_code == 200

def test_about_page_accessibility(client):
    response = client.get('/about')
    assert response.status_code == 200

def test_contact_page_accessibility(client):
    response = client.get('/contact')
    assert response.status_code == 200

def test_booking_page_accessibility(client):
    response = client.get('/booking')
    assert response.status_code == 200

# Test template rendering

def test_home_template_rendered(client):
    response = client.get('/')  
    assert b'Home' in response.data

def test_about_template_rendered(client):
    response = client.get('/about')  
    assert b'About Us' in response.data

def test_contact_template_rendered(client):
    response = client.get('/contact')  
    assert b'Contact Us' in response.data

def test_booking_template_rendered(client):
    response = client.get('/booking')  
    assert b'Book a Course' in response.data

# Test contact form handling

def test_contact_form_success(client):
    response = client.post('/contact', data={'name': 'Test User', 'email': 'test@example.com', 'message': 'Hello'})
    assert b'Your message has been sent successfully!' in response.data

def test_contact_form_failure(client):
    response = client.post('/contact', data={'name': '', 'email': '', 'message': ''})
    assert b'Please check the form for errors.' in response.data

# Test booking form handling

def test_booking_form_success(client):
    response = client.post('/booking', data={'name': 'Test User', 'email': 'test@example.com', 'course': 'Math 101'})
    assert b'Your booking request has been submitted!' in response.data

def test_booking_form_failure(client):
    response = client.post('/booking', data={'name': '', 'email': '', 'course': ''})
    assert b'Please check the form for errors.' in response.data