# SocialConnect - Social Media Platform 🚀

**SocialConnect** is a full-stack social media web application built using the **Django** framework. This project demonstrates modern web development practices with user authentication, real-time interactions, and a responsive design.

## 🌟 Features

### 🔐 Authentication & User Management
- **User Registration & Login** - Secure account creation and authentication
- **User Profiles** - Personalized profiles with bio, location, and profile pictures
- **Profile Editing** - Update personal information and profile pictures

### 📱 Social Features
- **Post Creation** - Share text content and images with the community
- **Like System** - Engage with posts through likes/unlikes
- **Comment System** - Discuss and interact with posts through comments
- **News Feed** - View posts from all users in chronological order
- **User Interactions** - View other users' profiles and posts

### 🎨 User Experience
- **Responsive Design** - Works seamlessly on desktop and mobile devices
- **Real-time Updates** - Instant feedback for likes and comments
- **Intuitive Navigation** - Easy-to-use interface for all features

---

## 🛠️ Technical Stack

### Backend
- **Framework**: Django 4.2.7 (Python)
- **Database**: SQLite (Development)
- **Authentication**: Django's built-in authentication system
- **File Handling**: Image uploads for posts and profile pictures

### Frontend
- **Templating**: Django Template Language (DTL)
- **Styling**: Custom CSS with responsive design
- **JavaScript**: Enhanced user interactions

### Architecture
- **MVC Pattern** - Model-View-Controller architecture
- **App Modularity** - Separate apps for social features and user management
- **Session Management** - Secure user sessions

---

## 📁 Project Structure
socialconnect/
├── socialconnect/ # Project configuration
│ ├── settings.py # Django settings
│ ├── urls.py # Main URL routing
│ └── wsgi.py
├── social/ # Social features app
│ ├── models.py # Post, Comment, Like models
│ ├── views.py # Social feature logic
│ ├── urls.py # Social app URLs
│ ├── templates/social/ # Social templates
│ │ ├── feed.html # Main news feed
│ │ ├── create_post.html # Post creation form
│ │ └── post_detail.html # Individual post view
│ └── admin.py # Admin panel configuration
├── users/ # User management app
│ ├── models.py # Profile model
│ ├── views.py # Authentication & profile logic
│ ├── urls.py # User app URLs
│ └── templates/users/ # User templates
│ ├── register.html # User registration
│ ├── login.html # User login
│ ├── profile.html # User profile
│ └── edit_profile.html # Profile editing
├── templates/ # Base templates
│ └── base.html # Main template with navigation
├── static/ # Static files
│ ├── css/
│ └── js/
├── media/ # User-uploaded files
│ ├── profile_pics/ # Profile pictures
│ └── posts/ # Post images
├── manage.py # Django management script
└── requirements.txt # Python dependencies


---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone [your-repo-url]
   cd socialconnect
Create Virtual Environment

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies

bash
pip install -r requirements.txt
Apply Database Migrations

bash
python manage.py makemigrations
python manage.py migrate
Create Superuser (Optional)

bash
python manage.py createsuperuser
Run Development Server

bash
python manage.py runserver
Access the Application
Main App: http://127.0.0.1:8000
Admin Panel: http://127.0.0.1:8000/admin

📊 Database Models

Social App Models
Post: User-generated content with text and optional images
Comment: User comments on posts with relationships
Like: Track user likes on posts with unique constraints

Users App Models

Profile: Extended user information (bio, location, profile picture)
Automatic Profile Creation: Profiles created automatically for new users

🎯 API Endpoints

Authentication

GET/POST /users/register/ - User registration
GET/POST /users/login/ - User login
POST /users/logout/ - User logout

User Profiles

GET /users/profile/<username>/ - View user profile
GET/POST /users/profile/edit/ - Edit user profile

Social Features

GET / - Main news feed
GET/POST /post/create/ - Create new post
GET /post/<post_id>/ - View post details
POST /post/<post_id>/comment/ - Add comment to post
POST /post/<post_id>/like/ - Like/unlike post

🔧 Key Features Implementation

User Authentication
Secure password hashing
Session-based authentication
Login-required decorators for protected views
File Uploads
Profile picture upload with validation
Post image upload with proper file handling
Media file serving in development

Database Relationships

User-Post (One-to-Many)
Post-Comment (One-to-Many)
Post-Like (Many-to-Many with through model)
User-Profile (One-to-One)

🌈 User Journey

Registration → Create new account
Login → Access personalized features
Profile Setup → Add bio, location, profile picture
Content Creation → Create posts with text and images
Social Interaction → Like and comment on posts
Community Engagement → View other users' profiles and content

🛡️ Security Features

CSRF Protection - All forms include CSRF tokens
Authentication Required - Protected views require login
File Upload Validation - Secure handling of user uploads
SQL Injection Prevention - Django's ORM provides protection
XSS Protection - Template auto-escaping

📱 Usage Guide

For End Users:

Register a new account or Login to existing account
Complete your profile with personal information
Create posts to share content with the community
Interact with posts by liking and commenting
Explore other profiles to discover new content

For Developers

The code follows Django best practices
Modular app structure for easy maintenance
Comprehensive template organization
Clear separation of concerns

🔮 Future Enhancements

Follow/Unfollow system
Real-time notifications
Direct messaging
Post search and filtering
Image compression and optimization
Email verification
Password reset functionality
Advanced user settings

👨‍💻 Developer

Shiza Aamir
📧 [Email](shizaaamir3@gmail.com)
💼 [LinkedIn](www.linkedin.com/in/shiza-aamir-4805a1267)

