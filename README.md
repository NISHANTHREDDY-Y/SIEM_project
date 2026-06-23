# SIEM_project

# 🛡️ SIEM Project - Security Information and Event Management System


## 📌 Overview

This project is a lightweight SIEM (Security Information and Event Management) application built using Python and Flask.

The purpose of this project is to collect, analyze, detect, and display security-related events from a Windows system through a web-based dashboard.

The current version focuses on monitoring a **single Windows machine** and collecting real Windows Event Logs.

The project is designed as a base SIEM architecture which can later be expanded to multiple systems and centralized monitoring.



## 🚀 Current Features

### ✅ Windows Event Log Collection

- Collects real logs from Windows Event Viewer
- Reads:
  - Security Logs
  - System Logs
  - Application Logs

- Extracts:
  - Timestamp
  - Event Type
  - Username
  - Source


### ✅ Database Storage

- Uses SQLite database
- Automatically creates required tables
- Stores collected security events


### ✅ Threat Detection Engine

Basic detection framework included for identifying suspicious events.


### ✅ Web Dashboard

Built using Flask.

Dashboard includes:

- Total Events
- Total Alerts
- Users
- Sources
- Logs Viewer
- Alerts Viewer
- Analytics Page



# 🏗️ Project Architecture

