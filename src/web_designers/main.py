#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime

from web_designers.crew import WebDesigners

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

requirements = """
A professional tutoring micro-enterprise website owned by a woman.
The site should have the following pages: home, about, contact, and course booking.
The site should allow users to view information about available courses and tutors.
The course booking page should allow users to submit a booking request with their name, email, and selected course.
The contact page should include a form to send a message to the company.
The backend should validate all form submissions and store bookings in memory or a simple database.
The site should have a responsive and professional frontend design using Bootstrap or TailwindCSS.
The frontend should incorporate a welcoming, feminine design style, using colors, fonts, and layout that feel elegant and friendly.
The site should handle errors gracefully and provide feedback to the user.
"""
module_name = "app.py"
class_name = "TutoringApp"



def run():
    """
    Run the research crew.
    """
    inputs = {
        'requirements': requirements,
        'module_name': module_name,
        'class_name': class_name
    }

    # Create and run the crew
    result = WebDesigners().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()



