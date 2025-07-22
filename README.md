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
