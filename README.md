# 🏪 Shop & Store Management System

A simple yet robust Django-based web application designed for managing a product catalog and allowing users to request products. This system is ideal for small stores, inventory management, or any scenario where users need to browse and request items.

## 📸 Project Screenshots
<p align="center">
  <img src="https://raw.githubusercontent.com/NoorMustafa4556/Shop-Store-Management-Django-/main/myproject/myapp/static/images/1.jpg" alt="Screenshot 1" width="30%" />
  <img src="https://raw.githubusercontent.com/NoorMustafa4556/Shop-Store-Management-Django-/main/myproject/myapp/static/images/2.jpg" alt="Screenshot 2" width="30%" />
  <img src="https://raw.githubusercontent.com/NoorMustafa4556/Shop-Store-Management-Django-/main/myproject/myapp/static/images/3.jpg" alt="Screenshot 3" width="30%" />
  <img src="https://raw.githubusercontent.com/NoorMustafa4556/Shop-Store-Management-Django-/main/myproject/myapp/static/images/4.jpg" alt="Screenshot 4" width="30%" />
</p>

## ✨ Features

*   **User Authentication:**
    *   Secure user signup and login (by username or email).
    *   Automatic creation of a `Customer` profile upon registration.
*   **Product Catalog:**
    *   Admin can add and manage product `Categories` and `Products`.
    *   Products can have details like name, price, description, and an image.
*   **User-Friendly Browsing:**
    *   A clean homepage to display all products.
    *   Filter products by `Category` using clean, SEO-friendly URLs (slugs).
    *   Search functionality to find products by name or category.
*   **Product Request System:**
    *   Authenticated users can request a product directly from the main page.
    *   A user can only request a specific product once if a previous request is still `Pending` or `Approved`.
    *   Users can view the status of all their requests on a dedicated "My Requests" page.
*   **Admin Management:**
    *   A powerful Django admin panel to manage `Customers`, `Products`, and `Categories`.
    *   Admins can view all `Orders` (requests) and update their status (e.g., from 'Pending' to 'Approved', 'Shipped', etc.).
    *   Custom actions in the admin panel to quickly approve or reject multiple requests.

## 🛠️ Tech Stack

*   **Backend:** Python, Django
*   **Database:** SQLite 3 (default)
*   **Frontend:** HTML, Bootstrap 5

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python (3.8 or higher)
*   pip (Python package installer)
*   Git

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/NoorMustafa4556/Shop-Store-Management-Django.git
    cd Shop-Store-Management-Django
    ```

2.  **Create and activate a virtual environment:**
    *   **Windows:**
        ```bash
        python -m venv env
        .\env\Scripts\activate
        ```
    *   **macOS / Linux:**
        ```bash
        python3 -m venv env
        source env/bin/activate
        ```

3.  **Install the required packages:**
    The `requirements.txt` file contains all the necessary Python packages.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Navigate into the project directory:**
    **Important:** This project's `manage.py` file is inside the `myproject` directory.
    ```bash
    cd myproject
    ```

5.  **Apply database migrations:**
    This will create the necessary database tables.
    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser:**
    This will allow you to access the Django admin panel.
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create an admin username and password.

7.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/`.

    **Note:** While the server is running, if you need to run other `manage.py` commands, you will need to open a *new* terminal and navigate to the `Shop-Store-Management-Django/myproject` directory again.

## ⚙️ How to Use

1.  **Admin Panel:**
    *   Navigate to `http://127.0.0.1:8000/admin/`.
    *   Log in with the superuser credentials.
    *   First, add some **`Categories`**. Then, add some **`Products`**.

2.  **User Side:**
    *   Navigate to `http://127.0.0.1:8000/`.
    *   **Sign up** and then **Log in**.
    *   You can now browse products and **request** them directly.
    *   Check your request status on the **"My Requests"** page.

## 👨‍💻 Author

*   **Name:** Noor Mustafa
*   **GitHub:** [@NoorMustafa4556](https://github.com/NoorMustafa4556)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/NoorMustafa4556/Shop-Store-Management-Django/issues) of this repository.

---
# 👋 Hi, I'm Noor Mustafa

A passionate and results-driven **Flutter Developer** from **Bahawalpur, Pakistan**, specializing in building elegant, scalable, and high-performance cross-platform mobile applications using **Flutter** and **Dart**.

With a strong understanding of **UI/UX principles**, **state management**, and **API integration**, I aim to deliver apps that are not only functional but also user-centric and visually compelling. My development approach emphasizes clean code, reusability, and performance.

---

## 🚀 What I Do

- 🧑‍💻 **Flutter App Development** – I build cross-platform apps for Android, iOS, and the web using Flutter.
- 🔗 **API Integration** – I connect apps to powerful RESTful APIs and third-party services.
- 🎨 **UI/UX Design** – I craft responsive and animated interfaces that elevate the user experience.
- 🔐 **Authentication & Firebase** – I implement secure login systems and integrate Firebase services.
- ⚙️ **State Management** – I use Provider, setState, and Riverpod (in-progress) for scalable app architecture.
- 🧠 **Clean Architecture** – I follow MVVM and MVC patterns for maintainable code.

---


## 🌟 Projects I'm Proud Of

- 🌤️ **[Live Weather Check App](https://github.com/NoorMustafa4556/Live-Weather-Check-App)** – Real-time weather forecast using OpenWeatherMap API  
- 🤖 **[AI Chatbot (Gemini)](https://github.com/NoorMustafa4556/Ai-ChatBot)** – Conversational AI chatbot powered by Google’s Gemini  

- 🍔 **[Recipe App](https://github.com/NoorMustafa4556/Recipe-App)** – Discover recipes with images, categories, and step-by-step instructions  

- 📚 **[Palindrome Checker](https://github.com/NoorMustafa4556/Palindrome-Checker-App)** – A Theory of Automata-based project to identify palindromic strings  

> 🎯 Check out all my repositories on [github.com/NoorMustafa4556](https://github.com/NoorMustafa4556?tab=repositories)

---

## 🛠️ Tech Stack & Tools

| Area                | Tools/Technologies |
|---------------------|--------------------|
| **Languages**       | Dart, JavaScript, Python (basic) |
| **Mobile Framework**| Flutter            |
| **Backend/Cloud**   | Firebase (Auth, Realtime DB, Storage), Django, Flask |
| **Frontend (Web)**  | React.js (basic), HTML, CSS, Bootstrap |
| **State Management**| Provider, setState, Riverpod (learning) |
| **API & Storage**   | REST APIs, HTTP, Shared Preferences, SQLite |
| **Design**          | Material, Cupertino, Lottie Animations, Gradient UI |
| **Version Control** | Git, GitHub        |
| **Tools**           | Android Studio, VS Code, Postman, Figma (basic) |

---

## 🧰 Tech Toolbox

<p align="left">
  <img src="https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white"/>
  <img src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB"/>
  <img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"/>
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
</p>

---

## 📈 Current Focus

- 💡 Enhancing Flutter animations and transitions
- 🤖 Implementing AI-based logic with Google Gemini API
- 📲 Building portfolio-level applications using full-stack Django & Flutter

---

## 📫 Let's Connect!

<p align="left">
  <a href="https://x.com/NoorMustafa4556" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="X / Twitter" height="30" width="40" />
  </a>
  <a href="https://www.linkedin.com/in/noormustafa4556/" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="LinkedIn" height="30" width="40" />
  </a>
  <a href="https://www.facebook.com/NoorMustafa4556" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="Facebook" height="30" width="40" />
  </a>
  <a href="https://instagram.com/noormustafa4556" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="Instagram" height="30" width="40" />
  </a>
  <a href="https://wa.me/923087655076" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/whatsapp.svg" alt="WhatsApp" height="30" width="40" />
  </a>
  <a href="https://www.tiktok.com/@noormustafa4556" target="blank">
    <img src="https://cdn-icons-png.flaticon.com/512/3046/3046122.png" alt="TikTok" height="30" width="30" />
  </a>
</p>

- 📍 **Location:** Bahawalpur, Punjab, Pakistan

---

> _“Learning never stops. Every app I build makes me a better developer — one widget at a time.”_

---


