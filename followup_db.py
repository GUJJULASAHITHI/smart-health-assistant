"""
Health Follow-Up and Reminder Database Manager
Uses SQLite for persistent local tracking of health concerns, symptom progression,
and automated clinical safety alerts.
"""

import os
import sqlite3
from datetime import datetime, date

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "health_followup.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Table 1: Primary Health Concern Logs
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS health_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT NOT NULL,
        concern_name TEXT NOT NULL,
        start_date TEXT NOT NULL,
        initial_severity INTEGER NOT NULL,
        notes TEXT,
        created_at TEXT NOT NULL
    );
    """)

    # Table 2: Daily Symptom Progression Check-ins
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS symptom_checkins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        log_id INTEGER NOT NULL,
        checkin_date TEXT NOT NULL,
        status TEXT NOT NULL,
        reported_warning_signs TEXT,
        safety_alert TEXT,
        notes TEXT,
        created_at TEXT NOT NULL,
        FOREIGN KEY (log_id) REFERENCES health_logs (id) ON DELETE CASCADE
    );
    """)

    conn.commit()
    conn.close()

def create_health_log(patient_name: str, concern_name: str, start_date: str, initial_severity: int, notes: str = ""):
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    now_iso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO health_logs (patient_name, concern_name, start_date, initial_severity, notes, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (patient_name.strip(), concern_name.strip(), start_date, initial_severity, notes.strip(), now_iso))

    log_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return log_id

def record_checkin(log_id: int, checkin_date: str, status: str, has_warning_signs: bool, notes: str = ""):
    """
    Records daily progression: 'Improving', 'Unchanged', 'Worsening'.
    Generates automated clinical safety alerts if worsening or persisting.
    """
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()

    # Determine safety alert
    safety_alert = None
    if has_warning_signs:
        safety_alert = "CRITICAL ALERT: Warning signs reported! Please seek urgent medical evaluation or visit the nearest clinic/ER immediately."
    elif status == "Worsening":
        safety_alert = "SAFETY ADVISORY: Symptoms are reported as worsening. Discontinue self-care and schedule an in-person medical consultation."
    elif status == "Unchanged":
        safety_alert = "MONITORING NOTE: Symptoms remain unchanged. If conditions persist beyond 3-4 days from start date, consult a healthcare provider."
    else:
        safety_alert = "POSITIVE PROGRESSION: Symptoms are improving. Continue gentle hydration, nutritious food, and sufficient rest."

    now_iso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    warning_str = "Yes" if has_warning_signs else "No"

    cursor.execute("""
        INSERT INTO symptom_checkins (log_id, checkin_date, status, reported_warning_signs, safety_alert, notes, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (log_id, checkin_date, status, warning_str, safety_alert, notes.strip(), now_iso))

    conn.commit()
    conn.close()
    return safety_alert

def get_all_logs():
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT hl.*, COUNT(sc.id) as checkin_count, 
               MAX(sc.checkin_date) as last_checkin_date,
               (SELECT sc2.status FROM symptom_checkins sc2 WHERE sc2.log_id = hl.id ORDER BY sc2.id DESC LIMIT 1) as latest_status
        FROM health_logs hl
        LEFT JOIN symptom_checkins sc ON hl.id = sc.log_id
        GROUP BY hl.id
        ORDER BY hl.id DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_checkins_for_log(log_id: int):
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM symptom_checkins
        WHERE log_id = ?
        ORDER BY checkin_date ASC, id ASC
    """, (log_id,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]

if __name__ == "__main__":
    init_db()
    test_id = create_health_log("Ramesh Kumar", "Fever", "2026-10-27", 3, "Started with chills after rain")
    record_checkin(test_id, "2026-10-28", "Unchanged", False, "Drinking warm fluids")
    record_checkin(test_id, "2026-10-29", "Improving", False, "Fever down to 99 F")
    logs = get_all_logs()
    print("Database Initialized! Sample logs count:", len(logs))
    print("First log check-ins:", get_checkins_for_log(test_id))
