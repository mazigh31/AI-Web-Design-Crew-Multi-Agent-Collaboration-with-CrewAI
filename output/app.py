from flask import Flask, render_template, request, redirect, url_for, flash
from forms.contact_form import ContactForm
from forms.booking_form import BookingForm

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# In-Memory storage for bookings
bookings = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Process the contact form and send a message (implement actual logic)
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contact'))
    elif request.method == 'POST':
        flash('Please check the form for errors.', 'danger')
    return render_template('contact.html', form=form)

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    form = BookingForm()
    if form.validate_on_submit():
        booking_data = {
            'name': form.name.data,
            'email': form.email.data,
            'course': form.course.data
        }
        bookings.append(booking_data)  # Store in-memory or optionally save in a database
        flash('Your booking request has been submitted!', 'success')
        return redirect(url_for('booking'))
    elif request.method == 'POST':
        flash('Please check the form for errors.', 'danger')
    return render_template('booking.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)