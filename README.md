# 📚 StudyBuddy — Study Group Finder (Python Version)

## 🧩 Project Description
**StudyBuddy** is a lightweight web application that helps students create, join, and manage study groups for their classes.  
The app follows the **CRUD** model (Create, Read, Update, Delete) and is built primarily with **Python (Flask)**.  
It allows users to add study groups, view existing ones, edit their details, and delete them when no longer needed.  

This project demonstrates the **Software Development Life Cycle (SDLC)** and applies **Agile** methodology in a small, two-person development team.

---

## 🎯 Objectives
- Apply the full SDLC (requirements, design, implementation, testing, and documentation).  
- Use **Python** for backend development and database management.  
- Build a small but complete full-stack app with Flask and SQLite.  
- Follow Agile methodology with short sprints and version control through GitHub.  
- Emphasize clean, simple, and modular code.

---

## 💡 Core Features
| Feature | Description | CRUD |
|----------|--------------|------|
| **View Groups** | Display all study groups stored in the database. | Read |
| **Create Group** | Add a new study group with name, subject, and description. | Create |
| **Edit Group** | Modify details of an existing study group. | Update |
| **Delete Group** | Remove a study group from the database. | Delete |
| **Join Group (Optional)** | Add yourself as a member of a study group. | Update |

---

## ⚙️ Tech Stack
| Layer | Technology |
|-------|-------------|
| **Frontend** | HTML, CSS, Bootstrap (optional), basic JavaScript |
| **Backend** | Python (Flask) |
| **Database** | SQLite (simple, file-based) |
| **Version Control** | Git + GitHub |
| **Development Methodology** | Agile (Scrum-based teamwork) |

---

## 🧠 Example Data Model
| Column | Type | Description |
|---------|------|-------------|
| `id` | Integer (Primary Key) | Unique group ID |
| `group_name` | Text | Name of the study group |
| `subject` | Text | Subject or course name |
| `description` | Text | Short summary of the group |
| `members` | Text (optional JSON string) | List of group members |

### Example
```json
{
  "group_name": "Physics 101 Study Group",
  "subject": "Physics",
  "description": "Weekly study sessions for Physics 101",
  "members": ["Jose", "Teammate Name"]
}
```

### 🧰 Option 1 — Using Python venv
```bash
# 1️⃣ Create virtual environment
python -m venv venv

# 2️⃣ Activate the environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the Flask app
python app.py

```

### 🧰 Option 2 — Using Conda
```bash
# 1️⃣ Create the environment from YAML file
conda env create -f environment.yml

# 2️⃣ Activate the environment
conda activate studybuddy

# 3️⃣ Run the Flask app
python app.py
```


