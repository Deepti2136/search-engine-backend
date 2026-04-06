# search-engine-backend
# 🔍 Mini Search Engine Project

## 📌 Project Overview

This project is a **Mini Search Engine Web Application** that allows users to search for programming languages and technologies. It displays relevant results with official links, and shows **"Search Not Found"** when no match is found.

---

## 🚀 Features

* 🔎 Search functionality for technologies
* 📄 Displays matching results dynamically
* ❌ Shows "Search Not Found" if no match exists
* 🔗 Provides official website links
* ⚡ Fast and simple UI
* 📱 Responsive design

---

## 🛠️ Technologies Used

### 🌐 Frontend

* HTML
* CSS
* JavaScript

### ⚙️ Backend

* Python (Flask)

### 🗄️ Database

* MySQL

---

## 📂 Project Structure

```id="p6o9zt"
search_engine/
│
├── static/
│   ├── css/
│   ├── js/
│   │   └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
├── database.sql
├── data.json
└── README.md
```

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository

```bash id="vxlw0o"
git clone https://github.com/Deepti2136/search-engine.git
cd search-engine
```

### 2️⃣ Install Dependencies

```bash id="ffmr2l"
pip install flask mysql-connector-python
```

### 3️⃣ Setup Database

```sql id="8z2bdi"
CREATE DATABASE search_engine;
USE search_engine;
```

* Import `database.sql`

---

### 4️⃣ Run the Application

```bash id="r1n0k7"
python app.py
```

---

### 5️⃣ Open in Browser

```id="d89n2q"
http://127.0.0.1:5000/
```

---

## 🗃️ Database Structure

### Table: Technologies

```sql id="5p9x4x"
CREATE TABLE Technologies (
    tech_id INT PRIMARY KEY AUTO_INCREMENT,
    tech_name VARCHAR(100),
    description TEXT,
    official_url VARCHAR(255)
);
```

---

## 🔍 Search Functionality

* User enters a keyword
* Backend (Python Flask) processes request
* MySQL database is searched using `LIKE` query
* Matching results are returned
* If no match → display **"Search Not Found"**

---

## 📌 Example Query

```sql id="rx1r8q"
SELECT * FROM Technologies 
WHERE tech_name LIKE '%python%';
```

---

## 📊 Sample Data

* Python → https://www.python.org
* Java → https://www.java.com
* JavaScript → https://developer.mozilla.org

---

## 📸 Future Enhancements

* 🔍 Advanced search filters
* 📈 Search ranking algorithm
* 🧠 AI-based recommendations
* ⭐ Save favorite searches

---

## 🤝 Contribution

Feel free to fork and contribute to improve this project.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👩‍💻 Author

Developed by **Sakanti Deepti**
