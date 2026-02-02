# velion-dkn-mwcd
📘 Digital Knowledge Network

Implementation of a Component-Based Digital Knowledge Network

📌 Project Overview

This project implements a Component-Based Digital Knowledge Network (DKN) as part of Coursework 2.
The system provides a mobile web platform that enables authenticated users to upload, view, and search organisational knowledge assets. The implementation realises the component-based architecture and interaction models developed in Coursework 1. The solution demonstrates practical application of component-based software engineering principles, RESTful communication, and mobile web development.

🎯 Key Features

Token-based user authentication

Upload and storage of knowledge assets

Searchable knowledge repository

Audit logging for governance and traceability

Mobile-friendly web interface

RESTful backend services

🏗️ Architecture Overview

The system is structured using a component-based architecture consisting of:

Client Layer: Mobile web interface (HTML, CSS, JavaScript)

Application Layer: REST API implemented using Flask

Core Components:

Authentication Component

Knowledge Management Component

Governance and Audit Component

Data Layer: SQLite database

Each component has a clearly defined responsibility, supporting modularity, maintainability, and extensibility.

🛠️ Technology Stack
Layer	Technology
Backend	Python (Flask)
Frontend	HTML5, CSS3, JavaScript
Database	SQLite
Communication	RESTful APIs
Authentication	Token-based
▶️ How to Run the Project
1️⃣ Prerequisites

Python 3.10 or higher

pip (Python package manager)

2️⃣ Install Dependencies
pip install flask flask-cors

3️⃣ Run the Backend
cd backend
python app.py


The backend will start at:

http://127.0.0.1:5000

4️⃣ Access the Application

Open a web browser and navigate to:

http://127.0.0.1:5000

5️⃣ Login Credentials (Demo)

Use the following token for testing:

token123

🧪 Sample Functionalities to Test

Login using access token

Upload new knowledge assets

View all stored knowledge items

Search knowledge by title

Verify successful backend execution via terminal output

📸 Evidence of Implementation

The following evidence is provided as part of the coursework submission:

Login interface

Knowledge upload interface

Search and repository interface

Backend execution console output

These screenshots demonstrate successful end-to-end system execution.

⚠️ Notes and Limitations

Authentication is intentionally lightweight for demonstration purposes

The system is deployed locally and is not intended for production use

Advanced features such as AI-based recommendations are outside the scope of this implementation

🎓 Coursework Context

This project was developed as part of Coursework 2 and focuses on the implementation and deployment of a component-based digital system. The design models, including component and sequence diagrams, were developed in Coursework 1 and are realised in this implementation.
