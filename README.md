# 🛡️ SIEM Project - Security Information and Event Management System


## 📌 Overview

This project is a lightweight SIEM (Security Information and Event Management) application developed using Python and Flask.

The purpose of this project is to collect, store, analyze, and display security-related events from a Windows system through a web-based dashboard.

The current version focuses on monitoring a **single Windows machine** and collecting real Windows Event Logs.

The project follows the basic architecture of a real SIEM system and can later be expanded for multiple systems and centralized monitoring.



# 🚀 Current Features


## ✅ Real Windows Event Log Collection

The application collects real logs from Windows Event Viewer.

Currently monitors:

- Security Logs
- System Logs
- Application Logs


Collected information:

- Timestamp
- Event Type
- Username
- Source
- Windows Event ID



## ✅ Database Storage

Uses SQLite database for storing collected events.

Features:

- Automatic database creation
- Log storage
- Alert storage
- Data retrieval



## ✅ Threat Detection Engine

Includes a detection module for identifying suspicious activities.

Current detection framework supports future expansion for:

- Brute force detection
- Suspicious login activity
- User activity monitoring



## ✅ Web Dashboard

Built using Flask.

Dashboard includes:

- Total Events
- Total Alerts
- Users
- Sources
- Log Viewer
- Alert Viewer
- Analytics Page



# 🏗️ System Architecture


```
              Windows Machine

                    |

                    |

          Windows Event Viewer

                    |

                    |

             Collector Module

                    |

                    |

                 Parser

                    |

                    |

             SQLite Database

                    |

                    |

            Detection Engine

                    |

                    |

             Flask Dashboard

```



# 📂 Project Structure


```
SIEM_Project

│

├── app.py

├── collector.py

├── parser.py

├── detector.py

├── database.py

├── requirements.txt

├── README.md

│

├── data

│     └── siem.db

│

├── static

│

│   ├── css

│   │     └── style.css

│   │

│   └── js

│         └── dashboard.js

│

└── templates

    ├── base.html

    ├── dashboard.html

    ├── logs.html

    ├── alerts.html

    └── analytics.html

```



# ⚙️ Requirements


Before running the project, install:


### Software Requirements

- Windows Operating System
- Python 3.10+
- Visual Studio Code (Recommended)


### Python Libraries


```
Flask

pywin32

```


All required packages are available in:

```
requirements.txt
```



# 🔧 Installation Guide



## 1. Clone Repository


```bash
git clone https://github.com/NISHANTHREDDY-Y/SIEM_project.git
```


Move into project directory:


```bash
cd SIEM_project
```



# 2. Create Virtual Environment


Run:


```bash
python -m venv venv
```



Activate virtual environment:


### Windows PowerShell

```powershell
venv\Scripts\activate
```


After activation:


```
(venv)
```


will appear in the terminal.



# 3. Install Dependencies


Run:


```bash
pip install -r requirements.txt
```


If pywin32 is missing:


```bash
pip install pywin32
```



# ▶️ Running the Application



## Important

Windows Event Logs require administrator privileges.

Run:

- VS Code as Administrator

or

- PowerShell as Administrator



Start application:


```bash
python app.py
```



Successful start:


```
Running on http://127.0.0.1:5000
```



Open browser:


```
http://127.0.0.1:5000
```



# 📊 Dashboard Modules



## Dashboard

Displays:

- Total collected events
- Total alerts
- Active users
- Log sources



## Logs Page

Displays collected Windows events.

Example:


```
Timestamp

Event Type

Username

Source

```



## Alerts Page

Displays detected security alerts.



## Analytics Page

Provides visualization of security data.



# 🪟 Windows Event Collection


The collector reads logs from:


```
Windows Event Viewer

        |

        |

 Security

 System

 Application

```



Common Windows Security Events:


```
4624  - Successful Login

4625  - Failed Login

4634  - User Logoff

4672  - Special Privilege Assigned

4720  - User Created

4726  - User Deleted

```



# 🗄️ Database


Database location:


```
data/siem.db
```


The database is automatically created when the application starts.



Database stores:


```
Logs

Alerts

Event Information

```



# 🛠️ Troubleshooting



## Problem:

```
A required privilege is not held by the client
```


### Solution:

Run the application with administrator privileges.



---


## Problem:

No logs appearing


### Check:


1. Run VS Code as Administrator

2. Check Windows Event Viewer

3. Restart application



---


## Problem:

Module not found


Solution:


```bash
pip install -r requirements.txt
```



# 🔮 Future Updates


Planned improvements:


## Advanced Log Processing

- Better Event ID mapping
- Severity classification
- Raw event storage



## Detection Improvements

- Brute force detection
- Suspicious login detection
- Privilege escalation detection



## Dashboard Improvements

- Real-time graphs
- Search
- Filtering
- Sorting
- Pagination



## Alert Management

- Alert status
- Investigation workflow
- SOC-style incident handling



## Reporting

- PDF security reports
- Event summaries



## Authentication

- Admin login
- Analyst roles
- Viewer roles



## Multi-System Monitoring

Future architecture:


```
PC 1
PC 2
PC 3

   |

   |

Central SIEM Server

   |

   |

SOC Dashboard

```



# 👨‍💻 Developer


Nishanth Reddy



# 📜 License


This project is developed for educational and cybersecurity research purposes.
