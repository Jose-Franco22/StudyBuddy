# 📚 StudyBuddy — Simple Study Group Finder

## 🧩 Project Description
**StudyBuddy** is a lightweight web app that helps students easily create and join study groups for their classes.  
The app allows users to browse existing groups, add new ones, update details, and remove groups they no longer need — following the full **CRUD (Create, Read, Update, Delete)** model.

This project is developed as part of our **Software Engineering Final Project**, applying **Agile methodology** and the **Software Development Life Cycle (SDLC)**.

---

## 🎯 Objectives
- Practice the full SDLC: requirements, design, implementation, testing, and documentation.  
- Work collaboratively using Agile sprints and GitHub version control.  
- Build a small but complete full-stack web app using modern tools.  
- Emphasize clean code, modularity, and simplicity.

---

## 💡 Core Features
| Feature | Description | CRUD |
|----------|--------------|------|
| **View Groups** | Display all study groups with details (subject, description, members). | Read |
| **Create Group** | Add a new study group with a name, subject, and description. | Create |
| **Edit Group** | Update group information. | Update |
| **Delete Group** | Remove a group from the list. | Delete |
| **Join Group (Optional)** | Users can join or leave a group. | Update |

---

## ⚙️ Tech Stack
| Layer | Technology |
|-------|-------------|
| **Frontend** | React (for web UI) |
| **Backend** | Node.js with Express |
| **Database** | MongoDB (NoSQL) |
| **Version Control** | Git + GitHub |
| **Development Methodology** | Agile (Scrum-based) |

---

## 🧠 Data Model (Example)
```json
{
  "groupName": "Math 101 Study Group",
  "subject": "Mathematics",
  "description": "We meet twice a week to review calculus.",
  "members": ["Jose", "Teammate Name"]
}
