# 🏫 PreSkool — School Management System

Application web Django de gestion scolaire complète  
**Faculté des Sciences et Techniques de Tanger | Prof. Sara AHSAIN | 2025/2026**

---

## 📋 Table des matières
- [Description](#description)
- [Technologies](#technologies)
- [Structure](#structure)
- [Installation](#installation)
- [Identifiants de test](#identifiants-de-test)
- [URLs](#urls)
- [Modèles et relations](#modèles-et-relations)
- [Fonctionnalités](#fonctionnalités)
- [Types d'utilisateurs](#types-dutilisateurs)
- [Démonstration vidéo](#démonstration-vidéo)
- [Auteurs](#auteurs)

---

## 📖 Description

**PreSkool** est une application web complète développée avec Django permettant de gérer un établissement scolaire. Elle couvre :

- Gestion des étudiants et leurs parents
- Gestion des enseignants
- Départements et matières
- Examens et résultats avec système de notes (A+, A, B+…)
- Jours fériés avec calendrier interactif
- Emploi du temps par classe et section
- Bibliothèque de documents par matière
- Gestion des comptes (Fees, Expenses, Salary)
- Événements
- Authentification avec gestion des rôles
- Réinitialisation de mot de passe par email

---

## 🛠️ Technologies

| Technologie     | Version        |
|-----------------|----------------|
| Python          | 3.x            |
| Django          | 6.0.3          |
| Bootstrap       | 4              |
| SQLite          | (développement)|
| FontAwesome     | 5              |
| jQuery          | 3.6.0          |
| DataTables      | —              |
| FullCalendar    | 5.11.3 (CDN)   |
| Pillow          | —              |

---

## 📁 Structure

```
School/
├── School/           # Configuration principale
├── faculty/          # Dashboard & accueil
├── student/          # Étudiants & Parents
├── Teacher/          # Enseignants
├── Departement/      # Départements
├── Subject/          # Matières
├── Exam/             # Examens & Résultats
├── Holidays/         # Jours fériés + calendrier
├── Events/           # Événements
├── TimeTable/        # Emploi du temps par classe
├── Library/          # Bibliothèque de documents
├── Accounts/         # Fees, Expenses, Salary
├── home_auth/        # Authentification & CustomUser
├── Admin/            # Dashboard Admin
├── templates/        # Templates HTML
├── static/           # CSS / JS / Images
├── media/            # Fichiers uploadés
├── data.json         # Données de test
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Cloner le projet
```bash
git clone <url-du-projet>
cd School
```

### 2. Créer et activer l'environnement virtuel
```bash
python -m venv env

# Windows
env\Scripts\activate

# Linux / Mac
source env/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Appliquer les migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Charger les données de test
```bash
python manage.py loaddata data.json
```

### 6. Lancer le serveur
```bash
python manage.py runserver
```

- 🌐 **App** → http://127.0.0.1:8000
- 🔧 **Admin** → http://127.0.0.1:8000/admin

---

## 🔑 Identifiants de test

| Rôle           | Email                | Mot de passe  |
|----------------|----------------------|---------------|
| **Admin**      | admin@gmail.com      | admin123      |
| **Enseignant** | teacher@gmail.com    | teacher123    |
| **Étudiant**   | student@gmail.com    | student123    |

---

## 📚 URLs

| Module | URL |
|--------|-----|
| Accueil | `/` |
| Students | `/student/` |
| Teachers | `/Teacher/teachers/` |
| Departments | `/Departement/` |
| Subjects | `/Subject/` |
| Exams | `/Exam/` |
| Results | `/Exam/Results/` |
| Holidays | `/Holiday/` |
| Events | `/Events/` |
| Time Table | `/TimeTable/` |
| Library | `/Library/` |
| Fees | `/Accounts/fees/` |
| Expenses | `/Accounts/expenses/` |
| Salary | `/Accounts/salary/` |
| Login | `/authentication/login/` |
| Signup | `/authentication/signup/` |
| Admin | `/admin/` |

---

## 🔗 Modèles et relations

```
Parent ──(OneToOne)── Student ──(FK)── Result
                                          │
Teacher ──(M2M)── Department             Exam
                      │                   │
                   Subject ──────────────┘

Holiday   (indépendant — affiché dans calendrier)
Event     (indépendant)
TimeTable (par classe et section)
Document  (Library — lié à Subject)
FeesCollection (lié à Student)
Salary         (lié à Teacher)
Expense        (indépendant)
CustomUser     (AbstractUser + rôles)
```

---

## 🚀 Fonctionnalités

- ✅ CRUD complet pour toutes les entités
- ✅ Authentification complète (login / signup / logout)
- ✅ Réinitialisation mot de passe par email (token sécurisé)
- ✅ Gestion des rôles (Admin / Teacher / Student)
- ✅ Accès différencié par rôle (sidebar dynamique, boutons cachés)
- ✅ Upload images étudiants et enseignants (Pillow)
- ✅ Upload documents bibliothèque (PDF, etc.)
- ✅ Système de notes (A+, A, B+, B, C+, C, D, F)
- ✅ Statuts examens (Scheduled, Completed, Cancelled)
- ✅ Calendrier interactif des jours fériés (FullCalendar)
- ✅ Emploi du temps par classe et section
- ✅ Intégration Visual Timetabling (lien externe)
- ✅ Bibliothèque par matière (Lessons, Exercises, Exams, Other)
- ✅ Gestion financière (Fees, Expenses, Salary)
- ✅ DataTables avec pagination et recherche
- ✅ Messages flash (succès / erreur)
- ✅ Confirmation avant suppression
- ✅ Interface responsive Bootstrap 4
- ✅ Emploi du temps par classe et section (avec Visual Timetabling intégré)
- ✅ Calendrier interactif des jours fériés (FullCalendar 5)

---

## 👥 Types d'utilisateurs

| Rôle | Accès |
|------|-------|
| **Admin** (`is_admin`) | Accès complet — CRUD sur tout |
| **Enseignant** (`is_teacher`) | Voir + modifier matières, examens, résultats, emploi du temps |
| **Étudiant** (`is_student`) | Consultation uniquement — aucune action |

---

## 🎥 Démonstration vidéo

👉 [Voir la démonstration](https://drive.google.com/file/d/1fTzGwjyDGUEuCv87m_KYkd_HesZO0rsn/view?usp=sharing)

---

## 👨‍💻 Auteurs

Projet réalisé par: Chems Eddine AYOUB et Yassine TAHIRI
dans le cadre du module **Développement Web Avancé – Back End Django**  
Faculté des Sciences et Techniques de Tanger | **2025/2026**  
Prof. Sara AHSAIN
