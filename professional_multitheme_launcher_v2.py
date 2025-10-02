#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Suppress warnings
import warnings
warnings.filterwarnings('ignore', category=UserWarning)
warnings.filterwarnings('ignore', category=DeprecationWarning)

"""
PROFESSIONAL MULTI-THEME NODE AUTOMATION LAUNCHER - FINAL VERSION

✅ FIXED ALL USER FEEDBACK:
- Missing Launch/Stop buttons restored
- Compact dashboard metric cards  
- Space analyzer shows actual data
- Clear process explanations
- Debug logs with legends
- Network Health renamed to Network Connection
- Fixed exit dialog functionality
- Immediate theme changes (no restart)
- Removed redundant text/headings

PRODUCTION READY - FINAL VERSION

📋 TABLE OF CONTENTS (Function Index):
═══════════════════════════════════════════════════════════════════════════════

🔧 CORE SYSTEM FUNCTIONS:
├── Line 100-150:   Global Configuration & Settings
├── Line 200-250:   Theme Management System
├── Line 300-350:   System Monitoring Classes
├── Line 400-500:   Process Management
├── Line 600-700:   Network Connection Monitoring

🎨 GUI CREATION FUNCTIONS:
├── Line 800-900:   Main Application Class Init
├── Line 1000-1100: Automation Scripts Tab
├── Line 1200-1300: Dashboard Tab Creation
├── Line 1400-1500: Space Analyzer Tab
├── Line 1600-1700: Processes Tab
├── Line 1800-1900: System Tab
├── Line 2000-2100: Debug Logs Tab
├── Line 2200-2300: Network Connection Tab
├── Line 2400-2500: Settings Tab

🔄 UPDATE & REFRESH FUNCTIONS:
├── Line 2600-2700: Dashboard Updates
├── Line 2800-2900: Space Analyzer Updates
├── Line 3000-3100: Process Display Updates
├── Line 3200-3300: System Info Updates
├── Line 3400-3500: Debug Logs Updates
├── Line 3600-3700: Network Status Updates

⚙️ UTILITY & HELPER FUNCTIONS:
├── Line 3800-3900: File Operations
├── Line 4000-4100: System Utilities
├── Line 4200-4300: Theme Helpers
├── Line 4400-4500: Configuration Management
├── Line 4600-4700: Node/Server Management
├── Line 4800-4900: Debug Log Analysis
├── Line 4900-5000: Main Execution

📝 NOTE: Line numbers are approximate. Use Ctrl+G to jump to specific lines.
      This index is updated with major code changes.

═══════════════════════════════════════════════════════════════════════════════
"""

import os
import sys
import json
import time
import subprocess
# Matplotlib availability will be determined by import attempt
MATPLOTLIB_AVAILABLE = False  # Default to False, will be set to True if import succeeds
# Minimal startup - removed verbose output
import platform
import threading
import getpass
import shutil
import glob
import hashlib
import base64
import signal
from datetime import datetime, timedelta
from pathlib import Path
import re
import socket

# GUI imports
try:
    import tkinter as tk
    from tkinter import ttk, messagebox, filedialog, scrolledtext
    from tkinter import font as tkfont
except ImportError as e:
    print(f"GUI import error: {e}")
    sys.exit(1)

# Enhanced GUI imports for advanced visualizations
try:
    import matplotlib
    matplotlib.use('TkAgg')  # Use TkAgg backend for tkinter integration
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
    from matplotlib.figure import Figure
    import matplotlib.animation as animation
    from matplotlib.patches import Wedge
    import numpy as np
    MATPLOTLIB_AVAILABLE = True
    # Silently enabled
except ImportError as e:
    MATPLOTLIB_AVAILABLE = False

# Database for historical data
try:
    import sqlite3
    DATABASE_AVAILABLE = True
    # Silently enabled
except ImportError as e:
    DATABASE_AVAILABLE = False
    print(f"⚠️ SQLite not available: {e}")

# Advanced data analysis
try:
    import collections
    from collections import deque
    COLLECTIONS_AVAILABLE = True
except ImportError:
    COLLECTIONS_AVAILABLE = False

# Optional enterprise imports (graceful degradation)
ENTERPRISE_FEATURES = {
    'cryptography': False,
    'pillow': False,
    'requests': False,
    'yaml': False
}

try:
    from cryptography.fernet import Fernet
    ENTERPRISE_FEATURES['cryptography'] = True
except ImportError:
    pass

try:
    from PIL import Image, ImageTk
    ENTERPRISE_FEATURES['pillow'] = True
except ImportError:
    pass

try:
    import requests
    ENTERPRISE_FEATURES['requests'] = True
except ImportError:
    pass

try:
    import yaml
    ENTERPRISE_FEATURES['yaml'] = True
except ImportError:
    pass

# Direct emoji usage - no compatibility layer needed for Docker deployment

# Minimal startup output
print("🚀 Starting Node Automation Launcher...")
###############################################################################
# DIRECTORY SETUP (FIXED: NO MULTIPLE DIRECTORIES)
###############################################################################

def setup_working_directory():
    """Setup working directory and logs folder"""
    target_dir = "/users/paruljot/patchfinder/GUI_Scripts_V2"
    logs_dir = os.path.join(target_dir, "logs")
    
    # Create logs directory if it doesn't exist
    try:
        os.makedirs(logs_dir, exist_ok=True)
    except Exception as e:
        print(f"Warning: Could not create logs directory: {e}")
    
    if not os.path.exists("master_config.json"):
        if os.path.exists(target_dir):
            try:
                os.chdir(target_dir)
            except Exception as e:
                print(f"Failed to change directory: {e}")
        else:
            print(f"Target directory not found: {target_dir}")

# Global paths
BASE_DIR = "/users/paruljot/patchfinder/GUI_Scripts_V2"
LOGS_DIR = os.path.join(BASE_DIR, "logs")

def ensure_required_directories():
    """Create required directories if they don't exist"""
    required_dirs = ["logs", "health_reports"]

    for dir_name in required_dirs:
        try:
            if not os.path.exists(dir_name):
                os.makedirs(dir_name, exist_ok=True)
        except Exception as e:
                print(f"Warning: Could not create directory {dir_name}: {e}")

ensure_required_directories()

###############################################################################
# ENHANCED DATABASE SYSTEM FOR HISTORICAL DATA
###############################################################################

class HistoricalDataManager:
    """Manages historical system data for trend analysis and performance tracking"""
    
    def __init__(self):
        self.db_path = os.path.join(LOGS_DIR, "system_history.db")
        self.init_database()
        
    def init_database(self):
        """Initialize SQLite database for historical data"""
        if not DATABASE_AVAILABLE:
            return
            
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # System metrics table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS system_metrics (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        cpu_percent REAL,
                        memory_percent REAL,
                        disk_usage REAL,
                        user_disk_usage REAL,
                        processes INTEGER,
                        load_average REAL,
                        uptime INTEGER
                    )
                ''')
                
                # Network health table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS network_health (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        node_name TEXT,
                        node_type TEXT,
                        ip_address TEXT,
                        status TEXT,
                        response_time REAL,
                        success_rate REAL
                    )
                ''')
                
                # Application events table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS app_events (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        event_type TEXT,
                        event_category TEXT,
                        description TEXT,
                        severity TEXT
                    )
                ''')
                
                conn.commit()
                log_message("Historical database initialized successfully", "SYSTEM")
                
        except Exception as e:
            log_message(f"Database initialization error: {e}", "ERROR")
    
    def record_system_metrics(self, system_data):
        """Record current system metrics to database"""
        if not DATABASE_AVAILABLE:
            return
            
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO system_metrics 
                    (cpu_percent, memory_percent, disk_usage, user_disk_usage, 
                     processes, load_average, uptime)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    system_data.get('cpu_percent', 0),
                    system_data.get('memory_percent', 0),
                    system_data.get('disk_usage', 0),
                    system_data.get('user_disk_usage', 0),
                    system_data.get('processes', 0),
                    system_data.get('load_average', 0),
                    system_data.get('uptime', 0)
                ))
                conn.commit()
        except Exception as e:
            log_message(f"Error recording system metrics: {e}", "ERROR")
    
    def record_network_event(self, node_name, node_type, ip_address, status, response_time):
        """Record network health event"""
        if not DATABASE_AVAILABLE:
            return
            
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO network_health 
                    (node_name, node_type, ip_address, status, response_time)
                    VALUES (?, ?, ?, ?, ?)
                ''', (node_name, node_type, ip_address, status, response_time))
                conn.commit()
        except Exception as e:
            log_message(f"Error recording network event: {e}", "ERROR")
    
    def record_app_event(self, event_type, category, description, severity="INFO"):
        """Record application event"""
        if not DATABASE_AVAILABLE:
            return
            
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO app_events 
                    (event_type, event_category, description, severity)
                    VALUES (?, ?, ?, ?)
                ''', (event_type, category, description, severity))
                conn.commit()
        except Exception as e:
            log_message(f"Error recording app event: {e}", "ERROR")
    
    def get_system_history(self, hours=24):
        """Get system metrics history for specified hours"""
        if not DATABASE_AVAILABLE:
            return []
            
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT timestamp, cpu_percent, memory_percent, disk_usage, 
                           processes, load_average
                    FROM system_metrics 
                    WHERE timestamp > datetime('now', '-{} hours')
                    ORDER BY timestamp
                '''.format(hours))
                return cursor.fetchall()
        except Exception as e:
            log_message(f"Error getting system history: {e}", "ERROR")
            return []
    
    def get_network_statistics(self, hours=24):
        """Get network health statistics"""
        if not DATABASE_AVAILABLE:
            return {}
            
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT node_name, node_type, 
                           AVG(response_time) as avg_response,
                           COUNT(*) as total_checks,
                           SUM(CASE WHEN status = 'Healthy' THEN 1 ELSE 0 END) as healthy_count
                    FROM network_health 
                    WHERE timestamp > datetime('now', '-{} hours')
                    GROUP BY node_name, node_type
                '''.format(hours))
                
                results = {}
                for row in cursor.fetchall():
                    node_name, node_type, avg_response, total_checks, healthy_count = row
                    success_rate = (healthy_count / total_checks * 100) if total_checks > 0 else 0
                    results[node_name] = {
                        'type': node_type,
                        'avg_response': avg_response or 0,
                        'success_rate': success_rate,
                        'total_checks': total_checks
                    }
                return results
        except Exception as e:
            log_message(f"Error getting network statistics: {e}", "ERROR")
            return {}

# Historical data manager will be initialized after log_message is defined

###############################################################################
# ENHANCED SECURITY + ERROR HANDLING
###############################################################################

def mask_sensitive_data(text):
    """Only mask passwords, NOT IPs"""
    if isinstance(text, str):
        text = re.sub(r'(passwd\s*[=:]\s*)[^\s\n]+', r'\1***', text, flags=re.IGNORECASE) 
        text = re.sub(r'(pwd\s*[=:]\s*)[^\s\n]+', r'\1***', text, flags=re.IGNORECASE)
    return text

def get_current_username():
    """Get current username from config or system"""
    try:
        # First try to get from master_config.json if it exists
        config_path = os.path.join(BASE_DIR, "master_config.json")
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = json.load(f)
                
                # Look for username in remote_server array (correct structure)
                remote_servers = config.get('remote_server', [])
                if remote_servers and len(remote_servers) > 0:
                    remote_server = remote_servers[0]  # Get first server
                    if 'own_login' in remote_server:
                        return remote_server['own_login']
                
                # Also check nodes for username
                nodes = config.get('nodes', [])
                for node in nodes:
                    if 'username' in node:
                        return node['username']
        
        # Fallback to system username
        return os.getenv('USER') or os.getenv('USERNAME') or 'paruljot'
    except:
        return 'paruljot'  # Default to paruljot instead of 'user'

###############################################################################
# THEME SYSTEM (ENHANCED COLORS)
###############################################################################
THEMES = {
    'Professional': {
        'bg': '#f8fafc', 'card_bg': '#ffffff', 'text_bg': '#ffffff',
        'header_bg': '#1e40af', 'primary_text': '#1f2937', 'secondary_text': '#4b5563',
        'success': '#059669', 'error': '#dc2626', 'warning': '#d97706',
        'info': '#0891b2', 'highlight': '#7c3aed', 'border': '#e5e7eb',
        'display_text': '#374151', 'display_bg': '#f9fafb',
        'metric_good': '#10b981', 'metric_warning': '#f59e0b', 'metric_critical': '#ef4444',
        'network_healthy': '#059669', 'network_unhealthy': '#dc2626'
    },
    'Dark': {
        'bg': '#0f172a', 'card_bg': '#1e293b', 'text_bg': '#1a1a1a',
        'header_bg': '#1e40af', 'primary_text': '#f1f5f9', 'secondary_text': '#94a3b8',
        'success': '#10b981', 'error': '#ef4444', 'warning': '#f59e0b',
        'info': '#06b6d4', 'highlight': '#a855f7', 'border': '#334155',
        'display_text': '#e2e8f0', 'display_bg': '#1e293b',
        'metric_good': '#34d399', 'metric_warning': '#fbbf24', 'metric_critical': '#f87171',
        'network_healthy': '#10b981', 'network_unhealthy': '#ef4444'
    },
    'Light': {
        'bg': '#ffffff', 'card_bg': '#f9fafb', 'text_bg': '#f3f4f6',
        'header_bg': '#3b82f6', 'primary_text': '#111827', 'secondary_text': '#374151',
        'success': '#059669', 'error': '#dc2626', 'warning': '#d97706',
        'info': '#0284c7', 'highlight': '#7c3aed', 'border': '#d1d5db',
        'display_text': '#1f2937', 'display_bg': '#f3f4f6',
        'metric_good': '#059669', 'metric_warning': '#d97706', 'metric_critical': '#dc2626',
        'network_healthy': '#065f46', 'network_unhealthy': '#991b1b'
    },
    'Matrix': {
        'bg': '#000000', 'card_bg': '#001100', 'text_bg': '#001100',
        'header_bg': '#003300', 'primary_text': '#00ff00', 'secondary_text': '#008800',
        'success': '#00ff00', 'error': '#ff0000', 'warning': '#ffff00',
        'info': '#00ffff', 'highlight': '#ff00ff', 'border': '#004400',
        'display_text': '#00ff00', 'display_bg': '#001100',
        'metric_good': '#00ff00', 'metric_warning': '#ffff00', 'metric_critical': '#ff0000',
        'network_healthy': '#00ff00', 'network_unhealthy': '#ff0000'
    },
    'Ocean': {
        'bg': '#f0f9ff', 'card_bg': '#e0f2fe', 'text_bg': '#e0f2fe',
        'header_bg': '#0369a1', 'primary_text': '#0c4a6e', 'secondary_text': '#075985',
        'success': '#059669', 'error': '#dc2626', 'warning': '#d97706',
        'info': '#0284c7', 'highlight': '#7c2d12', 'border': '#bae6fd',
        'display_text': '#0c4a6e', 'display_bg': '#f0f9ff',
        'metric_good': '#059669', 'metric_warning': '#d97706', 'metric_critical': '#dc2626',
        'network_healthy': '#059669', 'network_unhealthy': '#dc2626'
    },
    'Sunset': {
        'bg': '#fef7ed', 'card_bg': '#fed7aa', 'text_bg': '#fed7aa',
        'header_bg': '#ea580c', 'primary_text': '#9a3412', 'secondary_text': '#c2410c',
        'success': '#059669', 'error': '#dc2626', 'warning': '#d97706',
        'info': '#0891b2', 'highlight': '#7c3aed', 'border': '#fdba74',
        'display_text': '#9a3412', 'display_bg': '#fef7ed',
        'metric_good': '#059669', 'metric_warning': '#d97706', 'metric_critical': '#dc2626',
        'network_healthy': '#059669', 'network_unhealthy': '#dc2626'
    }
}

###############################################################################
# SETTINGS (FIXED NETWORK HANGING)
###############################################################################

app_settings = {
    'theme': 'Professional', 'refresh_interval': 5, 'debug_mode': True,
    'auto_save_logs': True, 'show_notifications': True, 
    'node_timeout': 2,  # FIXED: 2 seconds (NO HANGING)
    'log_retention_days': 30, 'encrypt_configs': False, 'config_password': '',
    'max_log_size_mb': 10, 'auto_cleanup_on_start': True, 'show_ip_addresses': True,
    'health_check_interval': 60, 'backup_configs': True, 
    'max_concurrent_checks': 3,  # FIXED: Concurrent limit
    'show_help_text': True  # NEW: Show help tooltips
}

def load_settings():
    global app_settings
    try:
        settings_file = os.path.join("logs", "launcher_settings.json")
        if os.path.exists(settings_file):
            with open(settings_file, 'r') as f:
                loaded = json.load(f)
                app_settings.update(loaded)
    except:
        pass

def save_settings():
    try:
        settings_file = os.path.join("logs", "launcher_settings.json")
        with open(settings_file, 'w') as f:
            json.dump(app_settings, f, indent=2)
    except:
        pass

load_settings()

###############################################################################
# LOGGING
###############################################################################

def log_message(message, log_type="INFO"):
    """Production-ready logging"""
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    masked_message = mask_sensitive_data(message)
    log_entry = f"{timestamp} [{log_type}] {masked_message}"

    try:
        ensure_required_directories()
        log_file = os.path.join(LOGS_DIR, "professional_launcher.log")
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry + "\n")

        if app_settings.get('debug_mode', True):
                debug_file = os.path.join(LOGS_DIR, f"debug_{datetime.now().strftime('%Y%m%d')}.log")
                with open(debug_file, 'a', encoding='utf-8') as f:
                    f.write(log_entry + "\n")

    except Exception as e:
        if log_type in ['CRITICAL', 'ERROR']:
                print(f"[{log_type}] {masked_message}")

def cleanup_old_logs(retention_days):
    """Clean up old log files"""
    cutoff_date = datetime.now() - timedelta(days=retention_days)
    cleaned_count = 0

    for log_file in glob.glob(os.path.join(LOGS_DIR, "*.log")):
        try:
                file_time = datetime.fromtimestamp(os.path.getmtime(log_file))
                if file_time < cutoff_date:
                    os.remove(log_file)
                    cleaned_count += 1
        except:
            continue

    return cleaned_count

# Initialize historical data manager after log_message is defined
historical_data = HistoricalDataManager()

###############################################################################
# AUTOMATION SCRIPTS CONFIGURATION
###############################################################################

AUTOMATION_SCRIPTS = {
    'version_check': {
        'name': 'Version Monitor', 'description': 'Check software versions on network nodes',
        'file': 'List_Telnet_and_SSH_Node_version_GUI_CrossPlatform.py', 'icon': '📊',
        'color': '#059669', 'benefit': 'Track outdated software'
    },
    'backup': {
        'name': 'Backup Manager', 'description': 'Create and manage node configuration backups',
        'file': 'Telnet_and_SSH_Node_Backup_GUI_CrossPlatform.py', 'icon': '🛡️',
        'color': '#2563eb', 'benefit': 'Protect against data loss'
    },
    'upgrade': {
        'name': 'Update Manager', 'description': 'Upgrade or rollback node software safely',
        'file': 'Node_upgrade_Downgrade_ENTERPRISE.py', 'icon': '🔄',
        'color': '#dc2626', 'benefit': 'Keep systems updated'
    },
    'patch': {
        'name': 'Patch Creator', 'description': 'Create and deploy custom software patches',
        'file': 'Patch_creation_compilation_ENTERPRISE.py', 'icon': '⚡',
        'color': '#8b5cf6', 'benefit': 'Fix issues quickly'
    }
}

###############################################################################
# SYSTEM MONITORING (ENHANCED)
###############################################################################

class SystemMonitor:
    """Enhanced system monitoring with detailed explanations"""

    def __init__(self):
        self.running = True
        self.current_user = get_current_username()
        self.user_dir = f"/users/{self.current_user}"
        self.data = {
            'cpu_percent': 0, 'memory_percent': 0, 'disk_usage': 0,
            'user_disk_usage': 0, 'user_disk_size': 0, 'processes': 0,
            'uptime': 0, 'load_average': 0, 'suggestions': [],
            'largest_files': [], 'explanations': {}, 'last_update': datetime.now(),
            'disk_io': {'read': 0, 'write': 0},
            'network_io': {'sent': 0, 'recv': 0},
            'process_usage': []
        }
        self.thread = threading.Thread(target=self._monitor_loop, daemon=True)

    def start(self):
        self.thread.start()
        log_message("System monitoring started", "SYSTEM")

    def stop(self):
        self.running = False

    def _monitor_loop(self):
        while self.running:
            try:
                self.data['cpu_percent'] = self._get_cpu_usage()
                self.data['memory_percent'] = self._get_memory_usage()
                self.data['disk_usage'] = self._get_disk_usage()
                self.data['user_disk_usage'], self.data['user_disk_size'] = self._get_user_disk_usage()
                self.data['processes'] = self._get_process_count()
                self.data['uptime'] = self._get_uptime()
                self.data['load_average'] = self._get_load_average()
                self.data['suggestions'] = self._generate_improvements()
                self.data['largest_files'] = self._get_largest_files()
                self.data['explanations'] = self._generate_explanations()
                self.data['last_update'] = datetime.now()
            except Exception as e:
                log_message(f"System monitoring error: {e}", "ERROR")
            time.sleep(app_settings['refresh_interval'])

    def _generate_explanations(self):
        """Generate comprehensive explanations"""
        explanations = {}

        cpu = self.data['cpu_percent']
        if cpu < 30:
            explanations['cpu'] = {'status': 'excellent', 'meaning': 'CPU running smoothly', 'color': 'metric_good'}
        elif cpu < 60:
            explanations['cpu'] = {'status': 'good', 'meaning': 'CPU usage moderate', 'color': 'metric_good'}
        elif cpu < 80:
            explanations['cpu'] = {'status': 'warning', 'meaning': 'CPU usage high', 'color': 'metric_warning'}
        else:
            explanations['cpu'] = {'status': 'critical', 'meaning': 'CPU usage very high', 'color': 'metric_critical'}

        memory = self.data['memory_percent']
        if memory < 50:
            explanations['memory'] = {'status': 'excellent', 'meaning': 'Memory usage low', 'color': 'metric_good'}
        elif memory < 75:
            explanations['memory'] = {'status': 'good', 'meaning': 'Memory usage moderate', 'color': 'metric_good'}
        elif memory < 90:
            explanations['memory'] = {'status': 'warning', 'meaning': 'Memory usage high', 'color': 'metric_warning'}
        else:
            explanations['memory'] = {'status': 'critical', 'meaning': 'Memory usage very high',
                                      'color': 'metric_critical'}

        return explanations

    def _get_user_disk_usage(self):
        """Get user directory disk usage using du command for speed"""
        try:
            if os.path.exists(self.user_dir):
                # Use du command for faster calculation
                import subprocess
                log_message(f"[SPACE] Calculating disk usage for {self.user_dir} using 'du -sb'", "SPACE")
                result = subprocess.run(['du', '-sb', self.user_dir], 
                                      capture_output=True, text=True, timeout=10)
                if result.returncode == 0:
                    total_size = int(result.stdout.split()[0])
                    log_message(f"[SPACE] Total size calculated: {total_size} bytes ({total_size/(1024**3):.2f} GB)", "SPACE")
                    
                    if total_size > 0:
                        statvfs = os.statvfs(self.user_dir)
                        available_space = statvfs.f_frsize * statvfs.f_bavail
                        usage_percent = (total_size / (total_size + available_space)) * 100 if available_space > 0 else 0
                        log_message(f"[SPACE] Usage percentage: {usage_percent:.2f}%", "SPACE")
                        return min(usage_percent, 100), total_size
                else:
                    log_message(f"[SPACE] du command failed with return code {result.returncode}", "ERROR")
            else:
                log_message(f"[SPACE] Directory {self.user_dir} does not exist", "ERROR")
            return 0, 0
        except Exception as e:
            log_message(f"[SPACE] Error in du command: {e}, falling back to slow method", "WARNING")
            # Fallback to slow method
            try:
                if os.path.exists(self.user_dir):
                    total_size = 0
                    for dirpath, dirnames, filenames in os.walk(self.user_dir):
                        for filename in filenames:
                            try:
                                filepath = os.path.join(dirpath, filename)
                                total_size += os.path.getsize(filepath)
                            except:
                                continue
                    log_message(f"[SPACE] Fallback method calculated: {total_size} bytes", "SPACE")
                    if total_size > 0:
                        statvfs = os.statvfs(self.user_dir)
                        available_space = statvfs.f_frsize * statvfs.f_bavail
                        usage_percent = (total_size / (total_size + available_space)) * 100 if available_space > 0 else 0
                        return min(usage_percent, 100), total_size
                return 0, 0
            except Exception as e2:
                log_message(f"[SPACE] Fallback method also failed: {e2}", "ERROR")
                return 0, 0

    def _get_largest_files(self):
        """Find largest files in user directory"""
        largest_files = []
        try:
            if os.path.exists(self.user_dir):
                file_sizes = []
                for dirpath, dirnames, filenames in os.walk(self.user_dir):
                    for filename in filenames:
                        try:
                            filepath = os.path.join(dirpath, filename)
                            size = os.path.getsize(filepath)
                            if size > 1024 * 1024:  # Files > 1MB
                                file_sizes.append((filepath, size))
                        except:
                            continue

                file_sizes.sort(key=lambda x: x[1], reverse=True)
                for filepath, size in file_sizes[:15]:
                    relative_path = os.path.relpath(filepath, self.user_dir)
                    size_mb = size / (1024 * 1024)
                    largest_files.append({
                        'path': relative_path, 'size_mb': size_mb, 'full_path': filepath
                    })
        except:
            pass
        return largest_files

    def _get_cpu_usage(self):
        try:
            if platform.system().lower() == 'linux':
                with open('/proc/stat', 'r') as f:
                    line = f.readline()
                    cpu_times = [int(x) for x in line.split()[1:]]
                    idle_time = cpu_times[3]
                    total_time = sum(cpu_times)

                    if hasattr(self, '_prev_total'):
                        total_diff = total_time - self._prev_total
                        idle_diff = idle_time - self._prev_idle
                        cpu_usage = 100.0 * (total_diff - idle_diff) / total_diff if total_diff > 0 else 0
                    else:
                        cpu_usage = 0

                    self._prev_total = total_time
                    self._prev_idle = idle_time
                    return min(max(cpu_usage, 0), 100)
        except:
            pass
        return 25.0

    def _get_memory_usage(self):
        try:
            if platform.system().lower() == 'linux':
                with open('/proc/meminfo', 'r') as f:
                    lines = f.readlines()
                    mem_info = {}
                    for line in lines:
                        if ':' in line:
                            key, value = line.split(':', 1)
                            mem_info[key.strip()] = int(value.strip().split()[0]) * 1024

                    total_mem = mem_info.get('MemTotal', 0)
                    available_mem = mem_info.get('MemAvailable', mem_info.get('MemFree', 0))
                    used_mem = total_mem - available_mem

                    if total_mem > 0:
                        return (used_mem / total_mem) * 100
        except:
            pass
        return 45.0

    def _get_disk_usage(self):
        try:
            if platform.system().lower() == 'linux':
                statvfs = os.statvfs('/')
                total_size = statvfs.f_frsize * statvfs.f_blocks
                free_size = statvfs.f_frsize * statvfs.f_available
                used_size = total_size - free_size

                if total_size > 0:
                    return (used_size / total_size) * 100
        except:
            pass
        return 35.0

    def _get_process_count(self):
        try:
            if platform.system().lower() == 'linux':
                proc_dirs = [d for d in os.listdir('/proc') if d.isdigit()]
                return len(proc_dirs)
        except:
            pass
        return 120

    def _get_uptime(self):
        try:
            if platform.system().lower() == 'linux':
                with open('/proc/uptime', 'r') as f:
                    return float(f.read().split()[0])
        except:
            pass
        return 86400.0

    def _get_load_average(self):
        try:
            if platform.system().lower() == 'linux':
                with open('/proc/loadavg', 'r') as f:
                    return float(f.read().split()[0])
        except:
            pass
        return 0.5

    def _generate_improvements(self):
        suggestions = []

        if self.data['cpu_percent'] > 80:
            suggestions.append({
                'issue': 'High CPU Usage', 'action': 'Close unused applications',
                'priority': 'HIGH', 'color': '#dc2626'
            })

        if self.data['memory_percent'] > 85:
            suggestions.append({
                'issue': 'High Memory Usage', 'action': 'Restart applications, clear cache',
                'priority': 'HIGH', 'color': '#dc2626'
            })

        if self.data['user_disk_usage'] > 80:
            suggestions.append({
                'issue': 'High User Directory Usage',
                'action': f'Clean files in /users/{self.current_user}/',
                'priority': 'MEDIUM', 'color': '#f59e0b'
            })

        if not suggestions:
            suggestions.append({
                'issue': 'System Healthy', 'action': 'All metrics within optimal ranges',
                'priority': 'GOOD', 'color': '#059669'
            })

        return suggestions

    def get_data(self):
        return self.data.copy()

    def delete_large_file(self, filepath):
        """Delete large files"""
        try:
            if os.path.exists(filepath):
                os.remove(filepath)
                log_message(f"Deleted large file: {filepath}", "CLEANUP")
                return True
        except Exception as e:
            log_message(f"Error deleting file {filepath}: {e}", "ERROR")
            return False

# SystemMonitor ready

###############################################################################
# ENHANCED UI COMPONENTS - Dramatic Visual Improvements
###############################################################################

class EnhancedUIComponents:
    """Provides dramatic visual enhancements for the GUI"""
    
    @staticmethod
    def create_animated_progress_bar(parent, width=300, height=25, theme_colors=None):
        """Create an animated progress bar with gradient effect"""
        if theme_colors is None:
            theme_colors = {'success': '#4CAF50', 'info': '#2196F3'}
        
        canvas = tk.Canvas(parent, width=width, height=height, 
                          bg=theme_colors.get('display_bg', '#1e1e1e'),
                          highlightthickness=0)
        canvas.pack(pady=5)
        
        # Store progress value
        canvas.progress = 0
        canvas.max_value = 100
        
        def update_progress(value):
            """Update progress bar value with animation"""
            canvas.progress = min(value, canvas.max_value)
            canvas.delete('all')
            
            # Calculate fill width
            fill_width = (canvas.progress / canvas.max_value) * width
            
            # Draw background
            canvas.create_rectangle(0, 0, width, height, 
                                   fill=theme_colors.get('display_bg', '#2e2e2e'),
                                   outline=theme_colors.get('border', '#555'))
            
            # Draw progress with gradient effect (simulated with multiple rectangles)
            if fill_width > 0:
                segments = 20
                segment_width = fill_width / segments
                for i in range(segments):
                    x1 = i * segment_width
                    x2 = (i + 1) * segment_width
                    # Color gradient from blue to green
                    color_intensity = int(255 * (i / segments))
                    color = f'#{color_intensity:02x}{200:02x}{100:02x}'
                    canvas.create_rectangle(x1, 2, x2, height-2, 
                                           fill=color, outline='')
            
            # Draw percentage text
            percent_text = f"{int(canvas.progress)}%"
            canvas.create_text(width/2, height/2, text=percent_text,
                             fill='white', font=('Arial', 10, 'bold'))
        
        canvas.update_progress = update_progress
        return canvas
    
    @staticmethod
    def create_tooltip(widget, text, theme_colors=None):
        """Create hover tooltip for widgets"""
        if theme_colors is None:
            theme_colors = {'card_bg': '#2e2e2e', 'primary_text': '#ffffff'}
        
        tooltip = None
        
        def show_tooltip(event):
            nonlocal tooltip
            if tooltip:
                return
            
            x, y, _, _ = widget.bbox("insert")
            x += widget.winfo_rootx() + 25
            y += widget.winfo_rooty() + 25
            
            tooltip = tk.Toplevel(widget)
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{x}+{y}")
            
            label = tk.Label(tooltip, text=text, 
                           bg=theme_colors.get('card_bg', '#2e2e2e'),
                           fg=theme_colors.get('primary_text', '#ffffff'),
                           relief='solid', borderwidth=1,
                           font=('Arial', 9), padx=10, pady=5)
            label.pack()
        
        def hide_tooltip(event):
            nonlocal tooltip
            if tooltip:
                tooltip.destroy()
                tooltip = None
        
        widget.bind('<Enter>', show_tooltip)
        widget.bind('<Leave>', hide_tooltip)
    
    @staticmethod
    def create_enhanced_button(parent, text, command, bg_color, theme_colors, 
                               width=None, icon=None):
        """Create button with hover effects and modern styling"""
        
        # Create frame for button with shadow effect
        button_frame = tk.Frame(parent, bg=theme_colors.get('bg', '#1e1e1e'))
        
        # Main button
        button = tk.Button(button_frame, text=text, command=command,
                          bg=bg_color, fg='white', 
                          font=('Arial', 10, 'bold'),
                          relief='flat', padx=20, pady=10, 
                          cursor='hand2', borderwidth=0)
        button.pack(padx=2, pady=2)
        
        # Hover effects
        def on_enter(e):
            # Lighten color on hover
            button.config(relief='raised', borderwidth=2)
        
        def on_leave(e):
            button.config(relief='flat', borderwidth=0)
        
        button.bind('<Enter>', on_enter)
        button.bind('<Leave>', on_leave)
        
        return button_frame
    
    @staticmethod
    def create_notification_toast(parent, message, duration=3000, 
                                  notification_type='info', theme_colors=None):
        """Create temporary notification toast"""
        if theme_colors is None:
            theme_colors = {
                'success': '#4CAF50',
                'error': '#F44336',
                'warning': '#FF9800',
                'info': '#2196F3'
            }
        
        # Create toast window
        toast = tk.Toplevel(parent)
        toast.wm_overrideredirect(True)
        
        # Position at top-right of parent
        parent.update_idletasks()
        x = parent.winfo_rootx() + parent.winfo_width() - 320
        y = parent.winfo_rooty() + 80
        toast.wm_geometry(f"+{x}+{y}")
        
        # Color based on type
        bg_color = theme_colors.get(notification_type, theme_colors.get('info'))
        
        # Toast content
        frame = tk.Frame(toast, bg=bg_color, relief='raised', borderwidth=2)
        frame.pack(fill='both', expand=True)
        
        # Icon based on type
        icons = {
            'success': '✅',
            'error': '❌',
            'warning': '⚠️',
            'info': 'ℹ️'
        }
        icon = icons.get(notification_type, 'ℹ️')
        
        label = tk.Label(frame, text=f"{icon} {message}",
                        bg=bg_color, fg='white',
                        font=('Arial', 10, 'bold'),
                        padx=20, pady=15)
        label.pack()
        
        # Auto-destroy after duration
        toast.after(duration, toast.destroy)
        
        # Fade-in animation (simplified)
        toast.attributes('-alpha', 0.0)
        for i in range(1, 11):
            toast.attributes('-alpha', i/10)
            toast.update()
            time.sleep(0.03)
        
        return toast
    
    @staticmethod
    def create_gauge_widget(parent, label, max_value=100, theme_colors=None):
        """Create circular gauge widget for metrics"""
        if not MATPLOTLIB_AVAILABLE:
            # Fallback to text display
            frame = tk.Frame(parent, bg=theme_colors.get('card_bg', '#2e2e2e'))
            tk.Label(frame, text=label, font=('Arial', 10, 'bold'),
                    bg=theme_colors.get('card_bg'), 
                    fg=theme_colors.get('primary_text')).pack()
            value_label = tk.Label(frame, text="0%", font=('Arial', 20, 'bold'),
                                  bg=theme_colors.get('card_bg'),
                                  fg=theme_colors.get('success'))
            value_label.pack()
            frame.value_label = value_label
            return frame
        
        # Create matplotlib gauge
        fig = Figure(figsize=(2.5, 2.5), dpi=80)
        ax = fig.add_subplot(111, projection='polar')
        
        # Initial gauge setup
        theta = [0, 0]
        r = [0, 1]
        ax.plot(theta, r, linewidth=10, color='#4CAF50')
        ax.set_ylim(0, 1)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.spines['polar'].set_visible(False)
        
        canvas = FigureCanvasTkAgg(fig, parent)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
        def update_gauge(value):
            """Update gauge value"""
            ax.clear()
            percentage = min(value / max_value, 1.0)
            theta = [0, percentage * 3.14159]
            r = [0.8, 0.8]
            
            # Color based on value
            if percentage < 0.6:
                color = '#4CAF50'  # Green
            elif percentage < 0.8:
                color = '#FF9800'  # Orange
            else:
                color = '#F44336'  # Red
            
            ax.plot(theta, r, linewidth=15, color=color)
            ax.set_ylim(0, 1)
            ax.set_xticks([])
            ax.set_yticks([])
            ax.spines['polar'].set_visible(False)
            ax.text(0, 0, f'{int(value)}%', ha='center', va='center',
                   fontsize=16, fontweight='bold')
            canvas.draw()
        
        canvas.update_gauge = update_gauge
        return canvas

###############################################################################
# ENHANCED VISUALIZATION SYSTEM
###############################################################################

class AdvancedVisualizationManager:
    """Manages advanced charts and graphs using matplotlib"""
    
    def __init__(self, theme_colors):
        self.theme_colors = theme_colors
        self.figures = {}
        self.canvases = {}
        
        if MATPLOTLIB_AVAILABLE:
            plt.style.use('default')
            self.setup_matplotlib_theme()
    
    def setup_matplotlib_theme(self):
        """Configure matplotlib to match application theme"""
        if not MATPLOTLIB_AVAILABLE:
            return
            
        plt.rcParams['figure.facecolor'] = self.theme_colors.get('card_bg', '#ffffff')
        plt.rcParams['axes.facecolor'] = self.theme_colors.get('display_bg', '#f8f9fa')
        plt.rcParams['text.color'] = self.theme_colors.get('primary_text', '#000000')
    
    def create_disk_usage_pie_chart(self, parent_frame, system_data, launcher_ref=None):
        """Create interactive pie chart for disk usage"""
        if not MATPLOTLIB_AVAILABLE:
            return self.create_fallback_disk_chart(parent_frame, system_data)
        
        try:
            fig = Figure(figsize=(6, 4), dpi=100)
            ax = fig.add_subplot(111)
            
            # Prepare data
            total_disk = system_data.get('disk_usage', 0)
            user_disk = system_data.get('user_disk_usage', 0)
            system_disk = max(0, total_disk - user_disk)
            free_disk = max(0, 100 - total_disk)
            
            sizes = [user_disk, system_disk, free_disk]
            labels = ['User Files', 'System Files', 'Free Space']
            colors = ['#ff6b6b', '#4ecdc4', '#45b7d1']
            
            wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', 
                  startangle=90, shadow=True)
            ax.set_title('Disk Usage Breakdown', fontsize=12, fontweight='bold')
            
            canvas = FigureCanvasTkAgg(fig, parent_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True, padx=10, pady=10)
            
            # Add click event handler if launcher reference provided
            if launcher_ref:
                def on_click(event):
                    if event.inaxes == ax:
                        for i, wedge in enumerate(wedges):
                            if wedge.contains_point([event.x, event.y]):
                                launcher_ref.show_disk_details(labels[i], sizes[i], system_data)
                                break
                
                canvas.mpl_connect('button_press_event', on_click)

            
            return canvas
            
        except Exception as e:
            log_message(f"Error creating pie chart: {e}", "ERROR")
            return None
    
    def create_fallback_disk_chart(self, parent_frame, system_data):
        """Fallback text-based disk chart when matplotlib unavailable"""
        chart_text = tk.Text(parent_frame, height=8, bg=self.theme_colors['display_bg'])
        
        total_disk = system_data.get('disk_usage', 0)
        user_disk = system_data.get('user_disk_usage', 0)
        free_disk = 100 - total_disk
        
        system_disk = total_disk - user_disk
        
        # Create color-coded visual bar
        user_blocks = int(user_disk / 5)
        system_blocks = int(system_disk / 5)
        free_blocks = int(free_disk / 5)
        
        chart_content = f"""📊 DISK USAGE BREAKDOWN
        
💾 Total Usage: {total_disk:.1f}%
👤 User Files: {user_disk:.1f}%
🖥️ System: {system_disk:.1f}%
🟢 Free Space: {free_disk:.1f}%

Visual Breakdown:
👤 User:   {'█' * user_blocks}{'░' * (20 - user_blocks)} {user_disk:.1f}%
🖥️ System: {'█' * system_blocks}{'░' * (20 - system_blocks)} {system_disk:.1f}%
🟢 Free:   {'█' * free_blocks}{'░' * (20 - free_blocks)} {free_disk:.1f}%

Combined: {'█' * int(total_disk/5)}{'░' * int(free_disk/5)}
"""
        chart_text.insert('1.0', chart_content)
        chart_text.config(state='disabled')
        chart_text.pack(fill='both', expand=True, padx=10, pady=10)
        return chart_text
    
    def create_performance_graph(self, parent_frame, width=8, height=4):
        """Create live performance monitoring graph"""
        if not MATPLOTLIB_AVAILABLE:
            return self.create_fallback_performance_display(parent_frame)
        
        try:
            # Create figure with subplots
            fig = Figure(figsize=(width, height), dpi=100, 
                        facecolor=self.theme_colors.get('card_bg', '#ffffff'))
            
            # CPU subplot
            ax1 = fig.add_subplot(211)
            ax1.set_title('CPU Usage (%)', color=self.theme_colors.get('primary_text', '#000000'),
                         fontsize=10, fontweight='bold')
            ax1.set_ylim(0, 100)
            ax1.set_yticks([0, 25, 50, 75, 100])  # Show intermediate values
            ax1.grid(True, alpha=0.3)
            ax1.set_facecolor(self.theme_colors.get('display_bg', '#f8f9fa'))
            
            # Memory subplot
            ax2 = fig.add_subplot(212)
            ax2.set_title('Memory Usage (%)', color=self.theme_colors.get('primary_text', '#000000'),
                         fontsize=10, fontweight='bold')
            ax2.set_ylim(0, 100)
            ax2.set_yticks([0, 25, 50, 75, 100])  # Show intermediate values
            ax2.grid(True, alpha=0.3)
            ax2.set_facecolor(self.theme_colors.get('display_bg', '#f8f9fa'))
            ax2.set_xlabel('Time (seconds)', color=self.theme_colors.get('primary_text', '#000000'))
            
            # Initialize data arrays
            if COLLECTIONS_AVAILABLE:
                self.cpu_data = deque(maxlen=50)
                self.memory_data = deque(maxlen=50)
                self.time_data = deque(maxlen=50)
            else:
                self.cpu_data = []
                self.memory_data = []
                self.time_data = []
            
            # Create initial empty plots
            self.cpu_line, = ax1.plot([], [], 'b-', linewidth=2, label='CPU')
            self.memory_line, = ax2.plot([], [], 'r-', linewidth=2, label='Memory')
            
            # Add hover annotations
            self.cpu_annot = ax1.annotate("", xy=(0,0), xytext=(10,10), textcoords="offset points",
                                         bbox=dict(boxstyle="round", fc="yellow", alpha=0.9),
                                         arrowprops=dict(arrowstyle="->"))
            self.cpu_annot.set_visible(False)
            
            self.mem_annot = ax2.annotate("", xy=(0,0), xytext=(10,10), textcoords="offset points",
                                         bbox=dict(boxstyle="round", fc="yellow", alpha=0.9),
                                         arrowprops=dict(arrowstyle="->"))
            self.mem_annot.set_visible(False)
            
            # Adjust layout
            fig.tight_layout(pad=2.0)
            
            # Create canvas
            canvas = FigureCanvasTkAgg(fig, parent_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True, padx=10, pady=10)
            
            # Add hover event handler
            def on_hover(event):
                if event.inaxes == ax1 and len(self.cpu_data) > 0:
                    # CPU graph hover
                    cont, ind = self.cpu_line.contains(event)
                    if cont:
                        idx = ind["ind"][0]
                        if idx < len(self.cpu_data):
                            x = (self.time_data[idx] - self.time_data[0]).total_seconds()
                            y = self.cpu_data[idx]
                            self.cpu_annot.xy = (x, y)
                            self.cpu_annot.set_text(f"CPU: {y:.1f}%\nTime: {x:.0f}s")
                            self.cpu_annot.set_visible(True)
                            canvas.draw_idle()
                    else:
                        if self.cpu_annot.get_visible():
                            self.cpu_annot.set_visible(False)
                            canvas.draw_idle()
                elif event.inaxes == ax2 and len(self.memory_data) > 0:
                    # Memory graph hover
                    cont, ind = self.memory_line.contains(event)
                    if cont:
                        idx = ind["ind"][0]
                        if idx < len(self.memory_data):
                            x = (self.time_data[idx] - self.time_data[0]).total_seconds()
                            y = self.memory_data[idx]
                            self.mem_annot.xy = (x, y)
                            self.mem_annot.set_text(f"Memory: {y:.1f}%\nTime: {x:.0f}s")
                            self.mem_annot.set_visible(True)
                            canvas.draw_idle()
                    else:
                        if self.mem_annot.get_visible():
                            self.mem_annot.set_visible(False)
                            canvas.draw_idle()
            
            canvas.mpl_connect("motion_notify_event", on_hover)
            
            # Store references
            graph_id = f"performance_{id(parent_frame)}"
            self.figures[graph_id] = fig
            self.canvases[graph_id] = canvas
            
            # Start periodic updates
            parent_frame.after(2000, self.update_performance_data)
            
            return canvas
            
        except Exception as e:
            log_message(f"Error creating performance graph: {e}", "ERROR")
            return self.create_fallback_performance_display(parent_frame)
    
    def update_performance_data(self):
        """Update performance graph with new data"""
        try:
            # Get current system data
            if not hasattr(self, 'system_monitor_ref') or not self.system_monitor_ref:
                # Skip update if no system monitor provided
                return
            system_data = self.system_monitor_ref.get_data()
            current_time = datetime.now()
            
            # Add new data points
            if COLLECTIONS_AVAILABLE:
                self.cpu_data.append(system_data.get('cpu_percent', 0))
                self.memory_data.append(system_data.get('memory_percent', 0))
                self.time_data.append(current_time)
            else:
                # Fallback for systems without collections
                if len(self.cpu_data) >= 50:
                    self.cpu_data.pop(0)
                    self.memory_data.pop(0)
                    self.time_data.pop(0)
                self.cpu_data.append(system_data.get('cpu_percent', 0))
                self.memory_data.append(system_data.get('memory_percent', 0))
                self.time_data.append(current_time)
            
            # Update plot data
            if len(self.time_data) > 1:
                # Convert time to relative seconds for x-axis
                time_seconds = [(t - self.time_data[0]).total_seconds() for t in self.time_data]
                
                self.cpu_line.set_data(time_seconds, list(self.cpu_data))
                self.memory_line.set_data(time_seconds, list(self.memory_data))
                
                # Update axis limits
                if time_seconds:
                    for ax in [self.cpu_line.axes, self.memory_line.axes]:
                        ax.set_xlim(min(time_seconds), max(time_seconds))
                        ax.relim()
                        ax.autoscale_view(scalex=True, scaley=False)
                
                # Redraw canvas
                for canvas in self.canvases.values():
                    canvas.draw()
            
            # Schedule next update
            if hasattr(self, 'cpu_line'):  # Check if graph still exists
                self.cpu_line.axes.figure.canvas.get_tk_widget().after(2000, self.update_performance_data)
                
        except Exception as e:
            log_message(f"Error updating performance graph: {e}", "ERROR")
    
    def create_fallback_performance_display(self, parent_frame):
        """Fallback performance display when matplotlib unavailable"""
        perf_text = tk.Text(parent_frame, height=10, bg=self.theme_colors['display_bg'])
        perf_text.insert('1.0', "📈 PERFORMANCE MONITORING\n\nMatplotlib not available - using text display\n\nReal-time graphs require matplotlib installation.")
        perf_text.config(state='disabled')
        perf_text.pack(fill='both', expand=True, padx=10, pady=10)
        return perf_text
    
    def create_network_health_pie_chart(self, parent_frame, connection_data):
        """Create pie chart showing network connection health status"""
        if not MATPLOTLIB_AVAILABLE:
            return self.create_fallback_network_chart(parent_frame, connection_data)
        
        try:
            fig = Figure(figsize=(4, 3), dpi=80)  # Reduced size
            ax = fig.add_subplot(111)
            
            # Prepare data
            healthy = connection_data.get('healthy_nodes', 0)
            unhealthy = connection_data.get('unhealthy_nodes', 0)
            total = healthy + unhealthy
            
            if total == 0:
                # No nodes configured
                ax.text(0.5, 0.5, 'No Nodes Configured\n\nAdd nodes in Settings', 
                       ha='center', va='center', fontsize=12, transform=ax.transAxes)
                ax.axis('off')
            else:
                sizes = [healthy, unhealthy]
                labels = [f'Healthy ({healthy})', f'Unhealthy ({unhealthy})']
                colors = ['#4CAF50', '#F44336']
                explode = (0.1, 0) if healthy > 0 else (0, 0.1)
                
                ax.pie(sizes, explode=explode, labels=labels, colors=colors, 
                      autopct='%1.1f%%', startangle=90, shadow=True)
                ax.set_title('Connection Health Status', fontsize=11, fontweight='bold', pad=10)
            
            canvas = FigureCanvasTkAgg(fig, parent_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True, padx=5, pady=5)
            
            return canvas
            
        except Exception as e:
            log_message(f"Error creating network pie chart: {e}", "ERROR")
            return None
    
    def update_network_health_chart(self, canvas, connection_data):
        """Update existing network health pie chart with new data"""
        if not canvas or not MATPLOTLIB_AVAILABLE:
            return
        
        try:
            # Get the figure from canvas
            fig = canvas.figure
            ax = fig.axes[0]
            ax.clear()
            
            # Prepare data
            healthy = connection_data.get('healthy_nodes', 0)
            unhealthy = connection_data.get('unhealthy_nodes', 0)
            total = healthy + unhealthy
            
            if total == 0:
                ax.text(0.5, 0.5, 'No Nodes Configured\n\nAdd nodes in Settings', 
                       ha='center', va='center', fontsize=12, transform=ax.transAxes)
                ax.axis('off')
            else:
                sizes = [healthy, unhealthy]
                labels = [f'Healthy ({healthy})', f'Unhealthy ({unhealthy})']
                colors = ['#4CAF50', '#F44336']
                explode = (0.1, 0) if healthy > 0 else (0, 0.1)
                
                ax.pie(sizes, explode=explode, labels=labels, colors=colors, 
                      autopct='%1.1f%%', startangle=90, shadow=True)
                ax.set_title('Connection Health Status', fontsize=11, fontweight='bold', pad=10)
            
            canvas.draw()
            
        except Exception as e:
            log_message(f"Error updating network pie chart: {e}", "ERROR")
    
    def create_process_resource_bar_chart(self, parent_frame, process_data):
        """Create horizontal bar chart showing top processes by resource usage"""
        if not MATPLOTLIB_AVAILABLE:
            return self.create_fallback_process_chart(parent_frame, process_data)
        
        try:
            fig = Figure(figsize=(6, 4), dpi=90)
            ax = fig.add_subplot(111)
            
            # Get top 5 processes by CPU usage
            processes = process_data.get('top_processes', [])
            if not processes:
                ax.text(0.5, 0.5, '⚙️ No Process Data\n\nData will appear when available', 
                       ha='center', va='center', fontsize=12, transform=ax.transAxes)
                ax.axis('off')
            else:
                # Limit to top 5
                processes = processes[:5]
                names = [p.get('name', 'Unknown')[:15] for p in processes]
                cpu_values = [p.get('cpu', 0) for p in processes]
                mem_values = [p.get('memory', 0) for p in processes]
                
                y_pos = range(len(names))
                
                # Create horizontal bars
                ax.barh([i - 0.2 for i in y_pos], cpu_values, 0.4, label='CPU %', color='#FF6B6B')
                ax.barh([i + 0.2 for i in y_pos], mem_values, 0.4, label='Memory %', color='#4ECDC4')
                
                ax.set_yticks(y_pos)
                ax.set_yticklabels(names)
                ax.set_xlabel('Usage (%)', fontsize=9)
                ax.set_title('⚙️ Top Processes Resource Usage', fontsize=11, fontweight='bold')
                ax.legend(loc='lower right', fontsize=8)
                ax.grid(axis='x', alpha=0.3)
                
                # Tight layout
                fig.tight_layout()
            
            canvas = FigureCanvasTkAgg(fig, parent_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True, padx=5, pady=5)
            
            return canvas
            
        except Exception as e:
            log_message(f"Error creating process bar chart: {e}", "ERROR")
            return None
    
    def update_process_resource_chart(self, canvas, process_data):
        """Update existing process resource bar chart with new data"""
        if not canvas or not MATPLOTLIB_AVAILABLE:
            return
        
        try:
            # Get the figure from canvas
            fig = canvas.figure
            ax = fig.axes[0]
            ax.clear()
            
            # Get top 5 processes
            processes = process_data.get('top_processes', [])
            if not processes:
                ax.text(0.5, 0.5, '⚙️ No Process Data\n\nData will appear when available', 
                       ha='center', va='center', fontsize=12, transform=ax.transAxes)
                ax.axis('off')
            else:
                # Limit to top 5
                processes = processes[:5]
                names = [p.get('name', 'Unknown')[:15] for p in processes]
                cpu_values = [p.get('cpu', 0) for p in processes]
                mem_values = [p.get('memory', 0) for p in processes]
                
                y_pos = range(len(names))
                
                # Create horizontal bars
                ax.barh([i - 0.2 for i in y_pos], cpu_values, 0.4, label='CPU %', color='#FF6B6B')
                ax.barh([i + 0.2 for i in y_pos], mem_values, 0.4, label='Memory %', color='#4ECDC4')
                
                ax.set_yticks(y_pos)
                ax.set_yticklabels(names)
                ax.set_xlabel('Usage (%)', fontsize=9)
                ax.set_title('⚙️ Top Processes Resource Usage', fontsize=11, fontweight='bold')
                ax.legend(loc='lower right', fontsize=8)
                ax.grid(axis='x', alpha=0.3)
                
                # Tight layout
                fig.tight_layout()
            
            canvas.draw()
            
        except Exception as e:
            log_message(f"Error updating process bar chart: {e}", "ERROR")
    
    def create_fallback_network_chart(self, parent_frame, connection_data):
        """Fallback network status display"""
        chart_text = tk.Text(parent_frame, height=8, bg=self.theme_colors['display_bg'], 
                            fg=self.theme_colors['display_text'], font=('Arial', 9))
        
        healthy = connection_data.get('healthy_nodes', 0)
        unhealthy = connection_data.get('unhealthy_nodes', 0)
        total = healthy + unhealthy
        
        if total == 0:
            content = "📡 NETWORK CONNECTION STATUS\n\n"
            content += "No nodes configured yet.\n"
            content += "Add nodes in Settings → Add/Modify Nodes"
        else:
            health_percent = (healthy / total * 100) if total > 0 else 0
            content = f"""📡 NETWORK CONNECTION STATUS

✅ Healthy Nodes: {healthy} ({health_percent:.1f}%)
❌ Unhealthy Nodes: {unhealthy} ({100-health_percent:.1f}%)
📊 Total Nodes: {total}

Visual Status:
{'█' * healthy}{'░' * unhealthy}
"""
        
        chart_text.insert('1.0', content)
        chart_text.config(state='disabled')
        chart_text.pack(fill='both', expand=True, padx=5, pady=5)
        return chart_text
    
    def create_fallback_process_chart(self, parent_frame, process_data):
        """Fallback process display"""
        chart_text = tk.Text(parent_frame, height=8, bg=self.theme_colors['display_bg'],
                            fg=self.theme_colors['display_text'], font=('Courier', 9))
        
        processes = process_data.get('top_processes', [])
        if not processes:
            content = "⚙️ TOP PROCESSES\n\nNo process data available yet."
        else:
            content = "⚙️ TOP PROCESSES (CPU/MEM %)\n\n"
            for i, p in enumerate(processes[:5], 1):
                name = p.get('name', 'Unknown')[:20].ljust(20)
                cpu = p.get('cpu', 0)
                mem = p.get('memory', 0)
                content += f"{i}. {name} CPU:{cpu:5.1f}% MEM:{mem:5.1f}%\n"
        
        chart_text.insert('1.0', content)
        chart_text.config(state='disabled')
        chart_text.pack(fill='both', expand=True, padx=5, pady=5)
        return chart_text

###############################################################################
# NETWORK HEALTH MONITOR (RENAMED TO NETWORK CONNECTION)
###############################################################################

class NetworkConnectionMonitor:
    """FIXED: NO HANGING network connection monitoring"""

    def __init__(self):
        self.health_data = {}
        self.running = True
        self.check_in_progress = False
        self.thread = threading.Thread(target=self._monitor_loop, daemon=True)

    def start(self):
        self.thread.start()
        log_message("Network connection monitoring started (NO HANGING)", "NETWORK")
        threading.Thread(target=self._safe_immediate_check, daemon=True).start()

    def stop(self):
        self.running = False

    def _safe_immediate_check(self):
        """Non-blocking immediate check"""
        try:
            time.sleep(3)
            self._check_connections_safely()
        except Exception as e:
            log_message(f"Safe immediate check error: {e}", "ERROR")

    def _monitor_loop(self):
        while self.running:
            try:
                if not self.check_in_progress:
                    self._check_connections_safely()
            except Exception as e:
                log_message(f"Network monitoring error: {e}", "ERROR")
            time.sleep(app_settings.get('health_check_interval', 60))

    def _check_connections_safely(self):
        """Safe connection check with timeout limits"""
        if self.check_in_progress:
            return

        self.check_in_progress = True

        try:
                config_path = os.path.join(BASE_DIR, "master_config.json")
                if not os.path.exists(config_path):
                    return

                with open(config_path, 'r') as f:
                    config = json.load(f)

                nodes = config.get('nodes', [])
                if not nodes:
                    return

                max_concurrent = app_settings.get('max_concurrent_checks', 3)
                timeout = app_settings.get('node_timeout', 2)

                # Process nodes in batches
                for i in range(0, len(nodes), max_concurrent):
                    batch = nodes[i:i + max_concurrent]
                    threads = []

                    for node in batch:
                        thread = threading.Thread(
                            target=self._check_single_node,
                            args=(node, timeout),
                            daemon=True
                        )
                        threads.append(thread)
                        thread.start()

                    for thread in threads:
                        thread.join(timeout=timeout + 1)

                    time.sleep(0.1)

        except Exception as e:
            log_message(f"Safe connection check error: {e}", "ERROR")
        finally:
            self.check_in_progress = False

    def _check_single_node(self, node, timeout):
        """Check single node connection"""
        node_name = node.get('name', 'Unknown')
        ip = node.get('ip', '')
        node_type = node.get('type', 'unknown').lower()

        try:
            is_healthy, response_time = self._check_connectivity(ip, node_type, timeout)

            self.health_data[node_name] = {
                'ip': ip, 'type': node_type, 
                'status': 'Healthy' if is_healthy else 'Unhealthy',
                'response_time': response_time, 
                'last_check': datetime.now(),
                'recommendation': self._get_recommendation(is_healthy, response_time, node_type)
            }

        except Exception as e:
            self.health_data[node_name] = {
                'ip': ip, 'type': node_type, 'status': 'Error',
                'response_time': 0, 'last_check': datetime.now(),
                'recommendation': f"Connection failed: {str(e)[:50]}"
            }

    def _check_connectivity(self, host, node_type, timeout):
        """Safe connectivity check"""
        start_time = time.time()

        try:
            if node_type == 'ssh':
                test_ports = [22]
            elif node_type == 'telnet':
                test_ports = [23]
            else:
                test_ports = [22, 23]

            for port in test_ports:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(timeout)
                    result = sock.connect_ex((host, port))
                    sock.close()

                    if result == 0:
                        response_time = max(int((time.time() - start_time) * 1000), 1)
                        return True, response_time
                except:
                    continue

                response_time = int((time.time() - start_time) * 1000)
            return False, response_time

        except Exception as e:
                response_time = int((time.time() - start_time) * 1000)
                return False, response_time

    def _get_recommendation(self, is_healthy, response_time, node_type):
        """Generate connection recommendations"""
        if not is_healthy:
            if node_type == 'ssh':
                return "SSH connection failed - verify SSH service running"
            elif node_type == 'telnet':
                return "Telnet connection failed - verify telnet service running"
            else:
                return "Connection failed - verify node is online"
        elif response_time > 3000:
            return "Very slow response (>3s) - check network performance"
        elif response_time > 1000:
            return "Slow response (>1s) - monitor network performance"
        else:
            return "Good connection - healthy network connectivity"

    def get_health_data(self):
        return self.health_data.copy()

    def force_check(self):
        """Force immediate connection check"""
        if not self.check_in_progress:
            threading.Thread(target=self._check_connections_safely, daemon=True).start()
            return True
        return False

###############################################################################
# PROCESS MANAGER
###############################################################################

class ProcessManager:
    """Process management with PID tracking"""

    def __init__(self):
        self.processes = {}
        self.process_lock = threading.Lock()

    def launch_script(self, script_key, script_info):
        try:
                script_file = script_info['file']
                script_name = script_info['name']
                script_path = os.path.join(BASE_DIR, script_file)

                if not os.path.exists(script_path):
                    return False, f"Script file not found: {script_file}"

                if platform.system().lower() == "windows":
                    process = subprocess.Popen([sys.executable, script_path], cwd=BASE_DIR,
                                            creationflags=subprocess.CREATE_NEW_CONSOLE)
                else:
                    process = subprocess.Popen([sys.executable, script_path], cwd=BASE_DIR)

                with self.process_lock:
                    self.processes[script_key] = {
                        'process': process, 'name': script_name, 'file': script_file,
                        'started': datetime.now(), 'pid': process.pid, 'status': 'Running'
                    }

                log_message(f"Launched {script_name} (PID: {process.pid})", "LAUNCH")
                return True, f"Launched {script_name} (PID: {process.pid})"

        except Exception as e:
                error_msg = f"Failed to launch {script_info['name']}: {e}"
                log_message(error_msg, "ERROR")
                return False, error_msg

    def kill_process(self, script_key):
        """Kill specific process"""
        with self.process_lock:
            if script_key not in self.processes:
                return False, "Process not found"

            try:
                process_info = self.processes[script_key]
                process = process_info['process']
                pid = process_info['pid']
                name = process_info['name']

                if process.poll() is None:
                    process.terminate()
                    time.sleep(1)

                    if process.poll() is None:
                        process.kill()

                        if platform.system().lower() != 'windows':
                            try:
                                os.kill(pid, signal.SIGKILL)
                            except ProcessLookupError:
                                pass

                log_message(f"Killed {name} (PID: {pid})", "STOP")
                del self.processes[script_key]
                return True, f"Killed {name} (PID: {pid})"

            except Exception as e:
                error_msg = f"Error killing process: {e}"
                log_message(error_msg, "ERROR")
                return False, error_msg

    def kill_process_by_pid(self, pid):
        """Kill process by PID"""
        try:
                pid = int(pid)
                log_message(f"[PROCESSES] Attempting to kill process PID: {pid}", "PROCESSES")

                if platform.system().lower() == 'windows':
                    result = subprocess.run(['taskkill', '/F', '/PID', str(pid)], 
                                        capture_output=True, text=True)
                    if result.returncode == 0:
                        log_message(f"[PROCESSES] Successfully killed Windows process PID: {pid}", "PROCESSES")
                        return True, f"Force killed process PID: {pid}"
                    else:
                        log_message(f"[PROCESSES] Failed to kill PID {pid}: {result.stderr}", "ERROR")
                        return False, f"Failed to kill PID {pid}: {result.stderr}"
                else:
                    os.kill(pid, signal.SIGKILL)
                    log_message(f"[PROCESSES] Successfully killed Unix process PID: {pid}", "PROCESSES")
                    return True, f"Force killed process PID: {pid}"

        except ProcessLookupError:
            log_message(f"[PROCESSES] Process PID {pid} not found", "WARNING")
            return False, f"Process PID {pid} not found"
        except PermissionError:
            log_message(f"[PROCESSES] Permission denied to kill PID {pid}", "ERROR")
            return False, f"Permission denied to kill PID {pid}"
        except ValueError:
            log_message(f"[PROCESSES] Invalid PID number: {pid}", "ERROR")
            return False, f"Invalid PID number: {pid}"
        except Exception as e:
                error_msg = f"Failed to kill PID {pid}: {e}"
                log_message(error_msg, "ERROR")
                return False, error_msg

    def get_processes(self):
        """Get current process status"""
        with self.process_lock:
            for script_key, proc_info in list(self.processes.items()):
                if proc_info['process'].poll() is not None:
                    proc_info['status'] = 'Finished'

            return self.processes.copy()

    def kill_all(self):
        """Kill all tracked processes"""
        count = 0
        with self.process_lock:
            for script_key in list(self.processes.keys()):
                success, _ = self.kill_process(script_key)
                if success:
                    count += 1
        return count

###############################################################################
# MAIN GUI CLASS - FIXED ALL ISSUES
###############################################################################

class NodeAutomationLauncher:
    """FINAL GUI - Fixed all user feedback issues"""

    def __init__(self, root):
        self.root = root
        
        # Clear debug log files on startup for fresh session
        try:
            # Clear main log
            main_log = "logs/professional_launcher.log"
            if os.path.exists(main_log):
                with open(main_log, 'w') as f:
                    f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [SYSTEM] Node Automation Launcher started - New session\n")
            
            # Clear today's debug log
            debug_log = f"logs/debug_{datetime.now().strftime('%Y%m%d')}.log"
            if os.path.exists(debug_log):
                with open(debug_log, 'w') as f:
                    f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [SYSTEM] Node Automation Launcher started - New session\n")
        except Exception as e:
            print(f"Warning: Could not clear debug logs: {e}")
        
        # FIXED: Even smaller window size to prevent bottom cutoff
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Use much smaller size to ensure everything fits properly
        window_width = min(1100, int(screen_width * 0.8))
        window_height = min(750, int(screen_height * 0.75))
        
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.minsize(1000, 700)
        
        # Center window on screen
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Initialize theme
        self.current_theme = app_settings.get('theme', 'Professional')
        self.theme_colors = THEMES[self.current_theme]

        # Window setup - REMOVED maximize_window() call
        self.apply_theme_immediately()  # FIXED: Immediate theme application

        # Initialize managers
        self.process_manager = ProcessManager()
        self.system_monitor = SystemMonitor()
        self.network_monitor = NetworkConnectionMonitor()
        self.visualization_manager = AdvancedVisualizationManager(self.theme_colors)
        self.ui_components = EnhancedUIComponents()  # NEW: Enhanced UI components

        self.system_monitor.start()
        self.network_monitor.start()

        # Initialize search and filter states
        self.search_results_active = False
        self.space_filter_active = False
        self.filtered_files = []
        
        # Store active toasts for management
        self.active_toasts = []

        # Create GUI
        self.create_gui()
        self.start_updates()
        
        # Calculate space analyzer data on startup (after GUI is created)
        self.root.after(2000, self.initial_space_calculation)

        # Setup exit handler
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        log_message("Node Automation Launcher initialized", "SYSTEM")
    
    def initial_space_calculation(self):
        """Calculate space analyzer data on startup"""
        try:
            # This will trigger the calculation in background
            if hasattr(self, 'directory_stats'):
                self.update_space_analyzer()
        except Exception as e:
            log_message(f"Error in initial space calculation: {e}", "ERROR")

    def show_toast(self, message, notification_type='info', duration=3000):
        """Show toast notification with enhanced UI"""
        try:
            toast = self.ui_components.create_notification_toast(
                self.root, message, duration, notification_type, self.theme_colors)
            self.active_toasts.append(toast)
            
            # Clean up old toasts
            def cleanup():
                if toast in self.active_toasts:
                    self.active_toasts.remove(toast)
            
            toast.after(duration + 500, cleanup)
        except Exception as e:
            log_message(f"Error showing toast: {e}", "ERROR")

    def apply_theme_immediately(self):
        """Apply theme immediately without restart"""
        try:
                system = platform.system().lower()
                if system == 'windows':
                    self.root.state('zoomed')
                elif system == 'linux':
                    try:
                        self.root.attributes('-zoomed', True)
                    except:
                        self.root.geometry("1400x900")
                else:
                    self.root.geometry("1400x900")
        except:
            self.root.geometry("1400x900")

    def apply_theme_immediately(self):
        """FIXED: Apply theme immediately without restart"""
        self.root.configure(bg=self.theme_colors['bg'])

        # Update all existing widgets immediately
        def update_widget_theme(widget):
            try:
                widget_class = widget.winfo_class()
                if widget_class in ['Frame', 'Toplevel']:
                    if 'bg' in widget.configure():
                        widget.configure(bg=self.theme_colors['bg'])
                elif widget_class == 'Label':
                    if 'bg' in widget.configure() and 'fg' in widget.configure():
                        widget.configure(bg=self.theme_colors['bg'], fg=self.theme_colors['primary_text'])
                elif widget_class == 'Text':
                    if 'bg' in widget.configure() and 'fg' in widget.configure():
                        widget.configure(bg=self.theme_colors['display_bg'], fg=self.theme_colors['display_text'])

                # Recursively update children
                for child in widget.winfo_children():
                    update_widget_theme(child)
            except:
                pass

        # Apply to all widgets
        update_widget_theme(self.root)

    def create_themed_text_widget(self, parent, height=10):
        """Enhanced text widget with proper colors"""
        if self.current_theme == 'Matrix':
                text_widget = tk.Text(parent, height=height, font=('Courier', 10, 'bold'),
                                bg=self.theme_colors['display_bg'], fg=self.theme_colors['display_text'],
                                insertbackground=self.theme_colors['display_text'], wrap='word', state='disabled')
        else:
                text_widget = tk.Text(parent, height=height, font=('Consolas', 10),
                                bg=self.theme_colors['display_bg'], fg=self.theme_colors['display_text'],
                                insertbackground=self.theme_colors['display_text'], wrap='word', state='disabled')

        # Configure color tags
        text_widget.tag_configure('success', foreground=self.theme_colors['success'], font=('Consolas', 10, 'bold'))
        text_widget.tag_configure('error', foreground=self.theme_colors['error'], font=('Consolas', 10, 'bold'))
        text_widget.tag_configure('warning', foreground=self.theme_colors['warning'], font=('Consolas', 10, 'bold'))
        text_widget.tag_configure('info', foreground=self.theme_colors['info'], font=('Consolas', 10))
        text_widget.tag_configure('highlight', foreground=self.theme_colors['highlight'], font=('Consolas', 10, 'bold'))
        text_widget.tag_configure('secondary', foreground=self.theme_colors['secondary_text'])
        text_widget.tag_configure('primary', foreground=self.theme_colors['primary_text'])

        return text_widget

    def insert_themed_text(self, text_widget, text, tag='primary'):
        """Insert text with theme support"""
        try:
            text_widget.config(state='normal')
            text_widget.insert(tk.END, text + "\n", tag)
            text_widget.see(tk.END)
            text_widget.config(state='disabled')
        except:
            pass

    def create_gui(self):
        """Create main GUI with all fixes"""

        # FIXED: Simplified header without redundant text
        header_frame = tk.Frame(self.root, bg=self.theme_colors['header_bg'], height=60)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)

        title_frame = tk.Frame(header_frame, bg=self.theme_colors['header_bg'])
        title_frame.pack(expand=True, fill='both')

        tk.Label(title_frame, text="🚀 NODE AUTOMATION LAUNCHER",
               font=('Arial', 18, 'bold'), bg=self.theme_colors['header_bg'], fg='white').pack(side='left', expand=True, padx=20)

        # Theme controls
        controls_frame = tk.Frame(title_frame, bg=self.theme_colors['header_bg'])
        controls_frame.pack(side='right', padx=20)

        tk.Label(controls_frame, text="Theme:", font=('Arial', 10, 'bold'),
               bg=self.theme_colors['header_bg'], fg='white').pack(side='left', padx=5)

        self.theme_var = tk.StringVar(value=self.current_theme)
        theme_combo = ttk.Combobox(controls_frame, textvariable=self.theme_var,
                                 values=list(THEMES.keys()), state="readonly", width=12)
        theme_combo.pack(side='left', padx=5)
        theme_combo.bind('<<ComboboxSelected>>', self.on_theme_change)

        # Main notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # Create all tabs with fixes
        self.create_automation_scripts_tab()      # FIXED: Missing buttons
        self.create_dashboard_tab()               # FIXED: Compact metric cards
        self.create_space_analyzer_tab()          # FIXED: Show actual data
        self.create_processes_tab()               # FIXED: Better layout, PID explanations
        self.create_system_tab()                  # Enhanced system info
        self.create_debug_logs_tab()              # FIXED: Legends for three boxes
        self.create_network_connection_tab()      # FIXED: Renamed from Network Health
        self.create_settings_tab()                # Settings management

        # Status bar
        self.create_status_bar()

    def create_automation_scripts_tab(self):
        """FIXED: Automation scripts with visible Launch/Stop buttons"""
        scripts_frame = tk.Frame(self.root, bg=self.theme_colors['bg'])
        self.notebook.add(scripts_frame, text="🚀 AUTOMATION SCRIPTS")

        # Header with controls
        header_frame = tk.Frame(scripts_frame, bg=self.theme_colors['card_bg'], relief='raised', bd=2)
        header_frame.pack(fill='x', padx=10, pady=10)

        tk.Label(header_frame, text="🎯 AUTOMATION SCRIPTS",  # FIXED: Unicode compatible
               font=('Arial', 16, 'bold'), bg=self.theme_colors['card_bg'],
               fg=self.theme_colors['primary_text']).pack(side='left', padx=20, pady=15)

        # Controls
        controls_frame = tk.Frame(header_frame, bg=self.theme_colors['card_bg'])
        controls_frame.pack(side='right', padx=20, pady=15)

        tk.Button(controls_frame, text="🔄 Refresh All", command=self.refresh_all_scripts,
                bg=self.theme_colors['info'], fg='white', font=('Arial', 10, 'bold'),
                relief='flat', padx=15, pady=8, cursor='hand2').pack(side='left', padx=5)

        tk.Button(controls_frame, text="⏹️ Stop All", command=self.stop_all_scripts,
                bg=self.theme_colors['error'], fg='white', font=('Arial', 10, 'bold'),
                relief='flat', padx=15, pady=8, cursor='hand2').pack(side='left', padx=5)

        # Scripts grid
        scripts_container = tk.Frame(scripts_frame, bg=self.theme_colors['bg'])
        scripts_container.pack(expand=True, fill='both', padx=20, pady=20)

        # Configure grid weights
        for i in range(2):
            scripts_container.grid_rowconfigure(i, weight=1)
            scripts_container.grid_columnconfigure(i, weight=1)

        # FIXED: Create script cards with VISIBLE Launch/Stop buttons
        script_keys = list(AUTOMATION_SCRIPTS.keys())
        positions = [(0,0), (0,1), (1,0), (1,1)]

        self.script_status_labels = {}
        self.script_buttons = {}

        for idx, (script_key, pos) in enumerate(zip(script_keys, positions)):
            if script_key in AUTOMATION_SCRIPTS:
                script = AUTOMATION_SCRIPTS[script_key]
                self.create_script_card(scripts_container, script_key, script, pos[0], pos[1])

    def create_script_card(self, parent, script_key, script, row, col):
        """FIXED: Script card with VISIBLE Launch/Stop buttons"""
        card_frame = tk.Frame(parent, bg=self.theme_colors['card_bg'], relief='raised', bd=3)
        card_frame.grid(row=row, column=col, padx=15, pady=15, sticky='nsew', ipadx=10, ipady=10)

        # Header
        header = tk.Frame(card_frame, bg=self.theme_colors['card_bg'])
        header.pack(fill='x', padx=20, pady=(20, 10))

        # Icon and title
        icon_label = tk.Label(header, text=script['icon'], font=('Arial', 28),
                            bg=self.theme_colors['card_bg'])
        icon_label.pack(side='left')

        title_frame = tk.Frame(header, bg=self.theme_colors['card_bg'])
        title_frame.pack(side='left', fill='x', expand=True, padx=(15, 0))

        tk.Label(title_frame, text=script['name'], font=('Arial', 14, 'bold'),
                bg=self.theme_colors['card_bg'], fg=script['color']).pack(anchor='w')

        # Status
        status_frame = tk.Frame(header, bg=self.theme_colors['card_bg'])
        status_frame.pack(side='right')

        self.script_status_labels[script_key] = tk.Label(status_frame, text="⚪ Ready", 
                                                        font=('Arial', 10), bg=self.theme_colors['card_bg'], 
                                                        fg=self.theme_colors['secondary_text'])
        self.script_status_labels[script_key].pack()

        # Compact description - only one line to save space
        desc_frame = tk.Frame(card_frame, bg=self.theme_colors['card_bg'])
        desc_frame.pack(fill='x', padx=20, pady=5)

        tk.Label(desc_frame, text=script['description'], font=('Arial', 9), wraplength=280,
                bg=self.theme_colors['card_bg'], fg=self.theme_colors['secondary_text'], 
                justify='left').pack(anchor='w')

        # FIXED: Action buttons - PROPERLY VISIBLE
        button_frame = tk.Frame(card_frame, bg=self.theme_colors['card_bg'])
        button_frame.pack(fill='x', padx=20, pady=20)

        launch_btn = tk.Button(button_frame, text="🚀 LAUNCH", 
                             command=lambda: self.launch_script(script_key),
                             bg=script['color'], fg='white', font=('Arial', 11, 'bold'), 
                             relief='flat', padx=25, pady=12, cursor='hand2', width=10)
        launch_btn.pack(side='left', padx=(0, 15))

        stop_btn = tk.Button(button_frame, text="⏹ STOP", 
                           command=lambda: self.stop_script(script_key),
                           bg=self.theme_colors['error'], fg='white', font=('Arial', 11, 'bold'), 
                           relief='flat', padx=25, pady=12, cursor='hand2', width=10)
        stop_btn.pack(side='left')

        # Store button references
        self.script_buttons[script_key] = {'launch': launch_btn, 'stop': stop_btn}

    def create_dashboard_tab(self):
        """FIXED: Dashboard with COMPACT metric cards"""
        dashboard_frame = tk.Frame(self.root, bg=self.theme_colors['bg'])
        self.notebook.add(dashboard_frame, text="📊 DASHBOARD")

        # Header
        header_frame = tk.Frame(dashboard_frame, bg=self.theme_colors['bg'])
        header_frame.pack(fill='x', padx=20, pady=15)

        tk.Label(header_frame, text="📊 SYSTEM DASHBOARD", font=('Arial', 16, 'bold'),  # FIXED: Removed redundant text
               bg=self.theme_colors['bg'], fg=self.theme_colors['primary_text']).pack(side='left')

        # Controls
        controls_frame = tk.Frame(header_frame, bg=self.theme_colors['bg'])
        controls_frame.pack(side='right')

        tk.Button(controls_frame, text="🔄 Refresh", command=self.refresh_dashboard,
                bg=self.theme_colors['info'], fg='white', font=('Arial', 10, 'bold'),
                relief='flat', padx=15, pady=8, cursor='hand2').pack()

        # Main dashboard with resizable panes
        main_paned = tk.PanedWindow(dashboard_frame, orient=tk.VERTICAL,
                                    sashwidth=6, sashrelief=tk.RAISED,
                                    bg=self.theme_colors['bg'])
        main_paned.pack(fill='both', expand=True, padx=20, pady=10)

        # Top pane - System overview (REDUCED)
        overview_frame = tk.LabelFrame(main_paned, text="🖥️ Real-Time System Overview", 
                                     font=('Arial', 12, 'bold'), bg=self.theme_colors['card_bg'],
                                     fg=self.theme_colors['primary_text'])
        main_paned.add(overview_frame, minsize=100)

        # FIXED: Compact metrics grid
        metrics_frame = tk.Frame(overview_frame, bg=self.theme_colors['card_bg'])
        metrics_frame.pack(fill='x', padx=20, pady=10)

        for i in range(4):
            metrics_frame.grid_columnconfigure(i, weight=1)

        # FIXED: Create COMPACT metric cards
        self.cpu_card = self.create_compact_metric_card(metrics_frame, "💻", "CPU Usage", "0%", 
                                                       self.theme_colors['info'], 0, 0)
        self.memory_card = self.create_compact_metric_card(metrics_frame, "🧠", "Memory", "0%", 
                                                          self.theme_colors['warning'], 0, 1)

        user = get_current_username()
        self.user_disk_card = self.create_compact_metric_card(metrics_frame, "💾", f"User {user}", "0%", 
                                                             self.theme_colors['success'], 0, 2)
        self.processes_card = self.create_compact_metric_card(metrics_frame, "⚙️", "Processes", "0", 
                                                             self.theme_colors['highlight'], 0, 3)

        # Bottom pane - Activity tabs (INCREASED)
        activity_container = tk.Frame(main_paned, bg=self.theme_colors['bg'])
        main_paned.add(activity_container, minsize=300)

        activity_notebook = ttk.Notebook(activity_container)
        activity_notebook.pack(fill='both', expand=True)

        # Recent Activity tab
        activity_frame = tk.Frame(activity_notebook, bg=self.theme_colors['card_bg'])
        activity_notebook.add(activity_frame, text="📝 Recent Activity")

        # FIXED: Add explanation for Recent Activity
        tk.Label(activity_frame, text="📝 Shows recent launcher actions, script launches, and system events",
               font=('Arial', 10), bg=self.theme_colors['card_bg'], fg=self.theme_colors['secondary_text']).pack(pady=5)

        self.activity_text = self.create_themed_text_widget(activity_frame, height=10)
        self.activity_text.pack(fill='both', expand=True, padx=10, pady=5)

        # ENHANCED: System Insights with Actions instead of just events
        insights_frame = tk.Frame(activity_notebook, bg=self.theme_colors['card_bg'])
        activity_notebook.add(insights_frame, text="💡 System Insights")

        # Help text for System Insights - CLEARER EXPLANATIONS
        if app_settings.get('show_help_text', True):
                help_frame = tk.Frame(insights_frame, bg=self.theme_colors['card_bg'])
                help_frame.pack(fill='x', padx=10, pady=5)
            
                help_text = ("💡 Quick Cleanup: Deletes /tmp files, old logs, package cache (shows count deleted) | "
                        "🔧 Fix Issues: Fixes file permissions, broken symlinks (shows issues fixed) | "
                        "📊 Health Check: Checks CPU, memory, disk, processes (100/100 = perfect health)")
            
                tk.Label(help_frame, text=help_text, font=('Arial', 8), 
                    bg=self.theme_colors['card_bg'], fg=self.theme_colors['secondary_text'],
                    wraplength=850).pack()

        # Quick action buttons
        insights_actions = tk.Frame(insights_frame, bg=self.theme_colors['card_bg'])
        insights_actions.pack(fill='x', padx=10, pady=5)
        
        tk.Button(insights_actions, text="🧹 Quick Cleanup", command=self.quick_system_cleanup,
                 bg=self.theme_colors['warning'], fg='white', font=('Arial', 9),
                 relief='raised', bd=1, width=12).pack(side='left', padx=2)
        
        tk.Button(insights_actions, text="🔧 Fix Issues", command=self.auto_fix_issues,
                 bg=self.theme_colors['error'], fg='white', font=('Arial', 9),
                 relief='raised', bd=1, width=12).pack(side='left', padx=2)
        
        tk.Button(insights_actions, text="📊 Health Check", command=self.system_health_check,
                 bg=self.theme_colors['info'], fg='white', font=('Arial', 9),
                 relief='raised', bd=1, width=12).pack(side='left', padx=2)

        self.events_text = self.create_themed_text_widget(insights_frame, height=8)
        self.events_text.pack(fill='both', expand=True, padx=10, pady=5)

        self.events_text.pack(fill='both', expand=True, padx=10, pady=5)

        # Performance History tab with EXPLANATION
        performance_frame = tk.Frame(activity_notebook, bg=self.theme_colors['card_bg'])
        activity_notebook.add(performance_frame, text="📊 Performance History")

        # ENHANCED: Live Performance Graph with matplotlib
        if MATPLOTLIB_AVAILABLE:
            tk.Label(performance_frame, text="📊 Live Performance Monitoring: Real-time CPU/Memory graphs with trend analysis",
                   font=('Arial', 10), bg=self.theme_colors['card_bg'], fg=self.theme_colors['secondary_text']).pack(pady=5)
            
            # Create live performance graph - REDUCED SIZE
            self.performance_graph = self.visualization_manager.create_performance_graph(performance_frame, width=8, height=3.5)
            # Store system_monitor reference for updates
            self.visualization_manager.system_monitor_ref = self.system_monitor
        else:
            # Fallback to text widget
            tk.Label(performance_frame, text="📊 Historical performance data: CPU/Memory trends over time with timestamps",
                   font=('Arial', 10), bg=self.theme_colors['card_bg'], fg=self.theme_colors['secondary_text']).pack(pady=5)
            
            self.performance_text = self.create_themed_text_widget(performance_frame, height=10)
            self.performance_text.pack(fill='both', expand=True, padx=10, pady=5)

    def create_compact_metric_card(self, parent, icon, title, value, color, row, col):
        """FIXED: Create COMPACT metric cards (smaller size)"""
        card = tk.Frame(parent, bg=self.theme_colors['display_bg'], relief='raised', bd=2)
        card.grid(row=row, column=col, padx=8, pady=8, sticky='ew', ipadx=15, ipady=10)  # FIXED: Reduced padding

        # Icon - smaller
        tk.Label(card, text=icon, font=('Arial', 20), bg=self.theme_colors['display_bg']).pack(pady=(8, 3))  # FIXED: Smaller font

        # Title - smaller font
        tk.Label(card, text=title, font=('Arial', 9, 'bold'),  # FIXED: Smaller font
                bg=self.theme_colors['display_bg'], fg=self.theme_colors['primary_text']).pack()

        # Value - smaller font
        value_label = tk.Label(card, text=value, font=('Arial', 16, 'bold'),  # FIXED: Smaller font
                             bg=self.theme_colors['display_bg'], fg=color)
        value_label.pack(pady=(3, 8))  # FIXED: Reduced padding

        # Status indicator - smaller
        status_label = tk.Label(card, text="●", font=('Arial', 10),  # FIXED: Smaller font
                              bg=self.theme_colors['display_bg'], fg=color)
        status_label.pack()

        card.value_label = value_label
        card.status_label = status_label
        card.color = color

        return card

    def create_space_analyzer_tab(self):
        """FIXED: Space analyzer with ACTUAL DATA display"""
        space_frame = tk.Frame(self.root, bg=self.theme_colors['bg'])
        self.notebook.add(space_frame, text="💾 SPACE ANALYZER")

        # Header
        header_frame = tk.Frame(space_frame, bg=self.theme_colors['bg'])
        header_frame.pack(fill='x', padx=20, pady=15)

        tk.Label(header_frame, text="💾 DISK SPACE ANALYZER", font=('Arial', 16, 'bold'),  # FIXED: Removed redundant text
               bg=self.theme_colors['bg'], fg=self.theme_colors['primary_text']).pack(side='left')

        # Controls
        controls_frame = tk.Frame(header_frame, bg=self.theme_colors['bg'])
        controls_frame.pack(side='right')

        tk.Button(controls_frame, text="📊 Export Report", command=self.export_space_report,
                bg=self.theme_colors['info'], fg='white', font=('Arial', 10, 'bold'),
                relief='flat', padx=15, pady=8, cursor='hand2').pack(side='left', padx=5)

        tk.Button(controls_frame, text="🧹 Clean Temp Files", command=self.clean_temp_files,
                bg=self.theme_colors['warning'], fg='white', font=('Arial', 10, 'bold'),
                relief='flat', padx=15, pady=8, cursor='hand2').pack(side='left', padx=5)

        # Compact Filters - All in one line
        filters_frame = tk.LabelFrame(space_frame, text="🔍 FILTERS & ACTIONS:",
                                    font=('Arial', 11, 'bold'), bg=self.theme_colors['card_bg'],
                                    fg=self.theme_colors['primary_text'])
        filters_frame.pack(fill='x', padx=20, pady=(10, 5))

        # Single line with size filter + file types + actions
        filter_line = tk.Frame(filters_frame, bg=self.theme_colors['card_bg'])
        filter_line.pack(fill='x', padx=10, pady=8)

        # Size filter (left side)
        tk.Label(filter_line, text="Size >", font=('Arial', 9, 'bold'),
                bg=self.theme_colors['card_bg'], fg=self.theme_colors['info']).pack(side='left')

        self.size_threshold_var = tk.StringVar(value="1")
        size_spinbox = tk.Spinbox(filter_line, from_=1, to=1000, textvariable=self.size_threshold_var,
                                width=4, font=('Arial', 9))
        size_spinbox.pack(side='left', padx=(2, 5))

        tk.Label(filter_line, text="MB", font=('Arial', 9, 'bold'),
                bg=self.theme_colors['card_bg'], fg=self.theme_colors['warning']).pack(side='left', padx=(0, 15))

        # File type checkboxes (middle)
        tk.Label(filter_line, text="Types:", font=('Arial', 9, 'bold'),
                bg=self.theme_colors['card_bg'], fg=self.theme_colors['info']).pack(side='left', padx=(0, 5))

        # Checkbox variables - more file types
        self.filter_vars = {
            'PDF': tk.BooleanVar(),
            'DOC': tk.BooleanVar(),
            'XLS': tk.BooleanVar(), 
            'PPT': tk.BooleanVar(),
            'TXT': tk.BooleanVar(),
            'LOG': tk.BooleanVar(),
            'JSON': tk.BooleanVar(),
            'IMG': tk.BooleanVar(),
            'VIDEO': tk.BooleanVar(),
            'ARCHIVE': tk.BooleanVar()
        }

        # Colors for each file type
        type_colors = {
            'PDF': self.theme_colors['error'],      # Red
            'DOC': self.theme_colors['info'],       # Blue
            'XLS': self.theme_colors['success'],    # Green
            'PPT': self.theme_colors['warning'],    # Orange
            'TXT': '#8E24AA',                       # Purple
            'LOG': '#5D4037',                       # Brown
            'JSON': '#00ACC1',                      # Cyan
            'IMG': '#E91E63',                       # Pink
            'VIDEO': '#FF5722',                     # Deep Orange
            'ARCHIVE': '#795548'                    # Brown
        }

        # All checkboxes in one line (compact)
        for file_type, var in self.filter_vars.items():
            cb = tk.Checkbutton(filter_line, text=file_type, variable=var,
                              font=('Arial', 7), bg=self.theme_colors['card_bg'],
                              fg=type_colors[file_type], selectcolor=self.theme_colors['display_bg'])
            cb.pack(side='left', padx=2)

        # Separator
        tk.Label(filter_line, text="|", font=('Arial', 10, 'bold'),
                bg=self.theme_colors['card_bg'], fg=self.theme_colors['secondary_text']).pack(side='left', padx=5)

        # Action buttons (better positioned)
        tk.Button(filter_line, text="Apply", command=self.apply_enhanced_space_filters,
                 bg=self.theme_colors['info'], fg='white', font=('Arial', 8, 'bold'),
                 relief='raised', bd=1, padx=8, pady=2).pack(side='left', padx=3)

        tk.Button(filter_line, text="Select All", command=self.select_all_space_filters,
                 bg=self.theme_colors['success'], fg='white', font=('Arial', 7),
                 relief='raised', bd=1, padx=4, pady=2).pack(side='left', padx=1)

        tk.Button(filter_line, text="Clear All", command=self.clear_all_space_filters,
                 bg=self.theme_colors['error'], fg='white', font=('Arial', 7),
                 relief='raised', bd=1, padx=4, pady=2).pack(side='left', padx=1)

        tk.Button(filter_line, text="Reset", command=self.reset_space_filters,
                 bg=self.theme_colors['warning'], fg='white', font=('Arial', 7),
                 relief='raised', bd=1, padx=4, pady=2).pack(side='left', padx=1)

        # File analysis
        analysis_container = tk.Frame(space_frame, bg=self.theme_colors['bg'])
        analysis_container.pack(fill='both', expand=True, padx=20, pady=10)

        # Left side - File list
        files_frame = tk.LabelFrame(analysis_container, text="📄 LARGEST FILES (>1MB)",
                                  font=('Arial', 12, 'bold'), bg=self.theme_colors['card_bg'],
                                  fg=self.theme_colors['primary_text'])
        files_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))

        # File checkboxes system (FIXED: Replace listbox with checkboxes)
        list_container = tk.Frame(files_frame, bg=self.theme_colors['card_bg'])
        list_container.pack(fill='both', expand=True, padx=10, pady=10)

        # Scrollable frame for checkboxes
        canvas = tk.Canvas(list_container, bg=self.theme_colors['display_bg'])
        v_scrollbar = tk.Scrollbar(list_container, orient='vertical', command=canvas.yview)
        self.files_scroll_frame = tk.Frame(canvas, bg=self.theme_colors['display_bg'])

        self.files_scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.files_scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=v_scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        v_scrollbar.pack(side="right", fill="y")

        # Initialize checkbox tracking
        self.file_checkboxes = {}
        self.file_vars = {}
        self.selected_files = set()

        # File action buttons
        file_actions = tk.Frame(files_frame, bg=self.theme_colors['card_bg'])
        file_actions.pack(fill='x', padx=10, pady=10)

        tk.Button(file_actions, text="🗑️ Delete Selected", command=self.delete_selected_file,
                bg=self.theme_colors['error'], fg='white', font=('Arial', 10, 'bold'),
                relief='flat', padx=15, pady=8, cursor='hand2').pack(side='left', padx=5)


        tk.Button(file_actions, text="📂 Open Location", command=self.open_file_location,
                bg=self.theme_colors['info'], fg='white', font=('Arial', 10, 'bold'),
                relief='flat', padx=15, pady=8, cursor='hand2').pack(side='left', padx=5)

        # Right side - Directory statistics
        analysis_frame = tk.LabelFrame(analysis_container, text="📊 Directory Statistics",
                                     font=('Arial', 12, 'bold'), bg=self.theme_colors['card_bg'],
                                     fg=self.theme_colors['primary_text'])
        analysis_frame.pack(side='right', fill='y', padx=(10, 0))
        analysis_frame.configure(width=350)
        analysis_frame.pack_propagate(False)

        self.directory_stats = self.create_themed_text_widget(analysis_frame, height=10)
        self.directory_stats.pack(fill='both', expand=True, padx=10, pady=10)

    
    def select_all_space_filters(self):
        """Select all file type filters"""
        for var in self.filter_vars.values():
            var.set(True)
        self.insert_themed_text(self.directory_stats, "✅ All file type filters selected", 'success')

    def clear_all_space_filters(self):
        """Clear all file type filters - uncheck all checkboxes"""
        for var in self.filter_vars.values():
            var.set(False)
        self.insert_themed_text(self.directory_stats, "✅ All file type filters cleared (unchecked)", 'success')

    def reset_space_filters(self):
        """Reset all filters to default"""
        self.size_threshold_var.set("1")
        self.clear_all_filters()
        self.space_filter_active = False
        self.filtered_files = []
        self.update_space_analyzer()
        self.insert_themed_text(self.directory_stats, "🔄 All filters reset to default", 'info')

    def apply_enhanced_space_filters(self):
        """Apply enhanced filters with multiple file types"""
        try:
            size_threshold = int(self.size_threshold_var.get())
            selected_types = [ftype for ftype, var in self.filter_vars.items() if var.get()]
            
            if not selected_types:
                self.insert_themed_text(self.directory_stats, 
                                      "⚠️ No file types selected - showing all files", 'warning')
                selected_types = list(self.filter_vars.keys())
            
            self.insert_themed_text(self.directory_stats, 
                                  f"🔍 Applying filters: >{size_threshold}MB, Types: {', '.join(selected_types)}", 'info')
            
            # Get current file data
            system_data = self.system_monitor.get_data()
            all_files = system_data.get('largest_files', [])
            
            # Apply filters
            filtered_files = []
            for file_info in all_files:
                size_mb = file_info.get('size_mb', 0)
                file_path = file_info.get('path', '').lower()
                
                # Size filter
                if size_mb < size_threshold:
                    continue
                
                # Type filter
                file_matches = False
                for file_type in selected_types:
                    if file_type == "PDF" and file_path.endswith('.pdf'):
                        file_matches = True
                    elif file_type == "DOC" and any(file_path.endswith(ext) for ext in ['.doc', '.docx']):
                        file_matches = True
                    elif file_type == "XLS" and any(file_path.endswith(ext) for ext in ['.xls', '.xlsx']):
                        file_matches = True
                    elif file_type == "PPT" and any(file_path.endswith(ext) for ext in ['.ppt', '.pptx']):
                        file_matches = True
                    elif file_type == "TXT" and any(file_path.endswith(ext) for ext in ['.txt', '.md', '.readme']):
                        file_matches = True
                    elif file_type == "LOG" and any(file_path.endswith(ext) for ext in ['.log', '.out', '.err']):
                        file_matches = True
                    elif file_type == "JSON" and any(file_path.endswith(ext) for ext in ['.json', '.xml', '.yaml', '.yml']):
                        file_matches = True
                    elif file_type == "IMG" and any(file_path.endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg']):
                        file_matches = True
                    elif file_type == "VIDEO" and any(file_path.endswith(ext) for ext in ['.mp4', '.avi', '.mov', '.mkv', '.webm']):
                        file_matches = True
                    elif file_type == "ARCHIVE" and any(file_path.endswith(ext) for ext in ['.zip', '.rar', '.7z', '.tar', '.gz']):
                        file_matches = True
                
                if file_matches:
                    filtered_files.append(file_info)
            
            # Store filtered results
            self.space_filter_active = True
            self.filtered_files = filtered_files
            
            # Clear and populate with checkboxes (FIXED: Use checkbox system)
            for widget in self.files_scroll_frame.winfo_children():
                widget.destroy()
            self.file_checkboxes.clear()
            self.file_vars.clear()
            self.selected_files.clear()
            
            for i, file_info in enumerate(filtered_files):
                size_mb = file_info['size_mb']
                path = file_info['path']
                filename = os.path.basename(path)
                
                if size_mb > 100:
                    size_str = "size_mb:.0f MB"
                elif size_mb > 10:
                    size_str = "size_mb:.1f MB"
                else:
                    size_str = "size_mb:.2f MB"

                # Create checkbox for each filtered file
                var = tk.BooleanVar()
                self.file_vars[path] = var
                
                checkbox_frame = tk.Frame(self.files_scroll_frame, bg=self.theme_colors['display_bg'])
                checkbox_frame.pack(fill='x', padx=5, pady=2)
                
                checkbox = tk.Checkbutton(checkbox_frame, variable=var, 
                                        bg=self.theme_colors['display_bg'], 
                                        fg=self.theme_colors['display_text'],
                                        selectcolor=self.theme_colors['card_bg'])
                checkbox.pack(side='left')
                
                file_label = tk.Label(checkbox_frame, text=f"{size_str:>8} | {filename}",
                                    font=('Courier', 9), bg=self.theme_colors['display_bg'],
                                    fg=self.theme_colors['display_text'], anchor='w')
                file_label.pack(side='left', fill='x', expand=True)
                
                self.file_checkboxes[path] = checkbox
            
            self.insert_themed_text(self.directory_stats, 
                                  f"✅ Enhanced filter applied: {len(filtered_files)} files match criteria", 'success')
            
        except Exception as e:
            messagebox.showerror("Filter Error", f"Failed to apply enhanced filters: {e}")

    
    def select_all_results(self):
        """Select all files in results"""
        for item in self.files_tree.get_children():
            self.files_tree.set(item, '#0', '☑️')
            self.selected_files.add(item)
        self.update_results_count()

    def clear_result_selection(self):
        """Clear all file selections"""
        for item in self.files_tree.get_children():
            self.files_tree.set(item, '#0', '☐')
        self.selected_files.clear()
        self.update_results_count()

    def on_file_click(self, event):
        """Handle file selection clicks"""
        item = self.files_tree.identify('item', event.x, event.y)
        if item:
            if item in self.selected_files:
                self.files_tree.set(item, '#0', '☐')
                self.selected_files.discard(item)
            else:
                self.files_tree.set(item, '#0', '☑️')
                self.selected_files.add(item)
            self.update_results_count()

    def update_results_count(self):
        """Update the results count display"""
        total = len(self.files_tree.get_children())
        selected = len(self.selected_files)
        self.results_count_label.config(text="selected/{total} files selected")

    def delete_selected_files(self):
        """Delete selected files"""
        if not self.selected_files:
            messagebox.showwarning("No Selection", "Please select files to delete")
            return
        
        count = len(self.selected_files)
        if messagebox.askyesno("Confirm Delete", f"Delete {count} selected files?"):
            deleted = 0
            for item in list(self.selected_files):
                try:
                    file_path = self.files_tree.item(item)['values'][1]
                    os.remove(file_path)
                    self.files_tree.delete(item)
                    deleted += 1
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")
            
            self.selected_files.clear()
            messagebox.showinfo("Delete Complete", f"Deleted {deleted} files")
            self.update_results_count()

    def open_selected_location(self):
        """Open location of first selected file"""
        if not self.selected_files:
            messagebox.showwarning("No Selection", "Please select a file")
            return
        
        first_item = next(iter(self.selected_files))
        file_path = self.files_tree.item(first_item)['values'][1]
        try:
            import subprocess
            subprocess.run(['xdg-open', os.path.dirname(file_path)])
        except:
            messagebox.showerror("Error", "Could not open file location")

    
    def on_file_select(self, event):
        """Handle file selection in listbox"""
        try:
            selection = self.files_listbox.curselection()
            self.update_results_count()
        except:
            pass

    def toggle_file_selection(self, event):
        """Toggle file selection with double-click"""
        try:
            index = self.files_listbox.nearest(event.y)
            if index in self.selected_files:
                self.selected_files.discard(index)
                # Update display to show unselected
                current_text = self.files_listbox.get(index)
                if current_text.startswith('☑️'):
                    new_text = '☐' + current_text[1:]
                    self.files_listbox.delete(index)
                    self.files_listbox.insert(index, new_text)
            else:
                self.selected_files.add(index)
                # Update display to show selected
                current_text = self.files_listbox.get(index)
                if current_text.startswith('☐'):
                    new_text = '☑️' + current_text[1:]
                    self.files_listbox.delete(index)
                    self.files_listbox.insert(index, new_text)
            self.update_results_count()
        except Exception as e:
            print(f"Selection error: {e}")

    def select_all_results(self):
        """Select all files in results"""
        try:
            total_items = self.files_listbox.size()
            self.selected_files = set(range(total_items))
            
            # Update display
            for i in range(total_items):
                current_text = self.files_listbox.get(i)
                if current_text.startswith('☐'):
                    new_text = '☑️' + current_text[1:]
                    self.files_listbox.delete(i)
                    self.files_listbox.insert(i, new_text)
            
            self.update_results_count()
        except Exception as e:
            print(f"Select all error: {e}")

    def clear_result_selection(self):
        """Clear all file selections"""
        try:
            total_items = self.files_listbox.size()
            self.selected_files.clear()
            
            # Update display
            for i in range(total_items):
                current_text = self.files_listbox.get(i)
                if current_text.startswith('☑️'):
                    new_text = '☐' + current_text[1:]
                    self.files_listbox.delete(i)
                    self.files_listbox.insert(i, new_text)
            
            self.update_results_count()
        except Exception as e:
            print(f"Clear selection error: {e}")

    def update_results_count(self):
        """Update the results count display"""
        try:
            total = self.files_listbox.size()
            selected = len(self.selected_files)
            self.results_count_label.config(text=f"{selected}/{total} files selected")
        except:
            pass

    def delete_selected_files(self):
        """Delete selected files"""
        if not self.selected_files:
            messagebox.showwarning("No Selection", "Please double-click files to select them for deletion")
            return
        
        count = len(self.selected_files)
        if messagebox.askyesno("Confirm Delete", f"Delete {count} selected files?\n\nThis action cannot be undone!"):
            deleted = 0
            # Sort indices in reverse order to avoid index shifting
            for index in sorted(self.selected_files, reverse=True):
                try:
                    file_text = self.files_listbox.get(index)
                    # Extract file path from the display text
                    parts = file_text.split(' - ', 1)
                    if len(parts) > 1:
                        file_path = parts[1]
                        if os.path.exists(file_path):
                            os.remove(file_path)
                            self.files_listbox.delete(index)
                            deleted += 1
                except Exception as e:
                    print(f"Failed to delete file at index {index}: {e}")
            
            self.selected_files.clear()
            messagebox.showinfo("Delete Complete", f"Successfully deleted {deleted} files")
            self.update_results_count()

    def open_selected_location(self):
        """Open location of first selected file"""
        if not self.selected_files:
            messagebox.showwarning("No Selection", "Please double-click a file to select it")
            return
        
        first_index = min(self.selected_files)
        try:
            file_text = self.files_listbox.get(first_index)
            parts = file_text.split(' - ', 1)
            if len(parts) > 1:
                file_path = parts[1]
                directory = os.path.dirname(file_path)
                subprocess.run(['xdg-open', directory])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file location: {e}")

    def create_processes_tab(self):
        """FIXED: Processes tab with better layout and PID explanations"""
        processes_frame = tk.Frame(self.root, bg=self.theme_colors['bg'])
        self.notebook.add(processes_frame, text="⚙️ PROCESSES")

        # Header
        header_frame = tk.Frame(processes_frame, bg=self.theme_colors['bg'])
        header_frame.pack(fill='x', padx=20, pady=15)

        # Title with safety features inline
        title_frame = tk.Frame(header_frame, bg=self.theme_colors['bg'])
        title_frame.pack(side='left')
        
        tk.Label(title_frame, text="⚙️ PROCESS MANAGER", font=('Arial', 16, 'bold'),
               bg=self.theme_colors['bg'], fg=self.theme_colors['primary_text']).pack(anchor='w')
        tk.Label(title_frame, text="🛡️ Graceful termination • Status monitoring • Complete logging",
               font=('Arial', 9, 'italic'), bg=self.theme_colors['bg'], 
               fg=self.theme_colors['secondary_text']).pack(anchor='w')

        # Controls with Manual PID Control - UNIFORM BUTTONS
        controls_frame = tk.Frame(header_frame, bg=self.theme_colors['bg'])
        controls_frame.pack(side='right')

        # Manual PID entry in header
        tk.Label(controls_frame, text="PID:", font=('Arial', 10, 'bold'),
               bg=self.theme_colors['bg'], fg=self.theme_colors['primary_text']).pack(side='left', padx=(0,5))
        
        self.pid_entry = tk.Entry(controls_frame, width=10, font=('Consolas', 10))
        self.pid_entry.pack(side='left', padx=5)
        
        tk.Button(controls_frame, text="💀 Kill PID", command=self.manual_kill_pid,
                bg=self.theme_colors['error'], fg='white', font=('Arial', 10, 'bold'),
                relief='flat', padx=15, pady=8, cursor='hand2').pack(side='left', padx=5)

        tk.Button(controls_frame, text="🔄 Refresh", command=self.refresh_processes,
                bg=self.theme_colors['info'], fg='white', font=('Arial', 10, 'bold'),
                relief='flat', padx=15, pady=8, cursor='hand2').pack(side='left', padx=5)

        tk.Button(controls_frame, text="💀 Kill All", command=self.kill_all_processes,
                bg=self.theme_colors['error'], fg='white', font=('Arial', 10, 'bold'),
                relief='flat', padx=15, pady=8, cursor='hand2').pack(side='left', padx=5)

        # Main process display with resizable PanedWindow
        main_paned = tk.PanedWindow(processes_frame, orient=tk.HORIZONTAL,
                                    sashwidth=8, sashrelief=tk.RAISED,
                                    bg=self.theme_colors['bg'])
        main_paned.pack(fill='both', expand=True, padx=20, pady=10)

        # Left side - Process list
        process_frame = tk.LabelFrame(main_paned, text="🏃 Active Automation Processes",
                                    font=('Arial', 12, 'bold'), bg=self.theme_colors['card_bg'],
                                    fg=self.theme_colors['primary_text'])
        main_paned.add(process_frame, minsize=400)

        self.processes_text = self.create_themed_text_widget(process_frame, height=12)
        self.processes_text.pack(fill='both', expand=True, padx=10, pady=10)

        # FIXED: Right side - Scrollable controls container
        controls_outer = tk.Frame(main_paned, bg=self.theme_colors['bg'])
        main_paned.add(controls_outer, minsize=350)
        
        # Add canvas for scrolling
        canvas = tk.Canvas(controls_outer, bg=self.theme_colors['bg'], highlightthickness=0)
        scrollbar = tk.Scrollbar(controls_outer, orient="vertical", command=canvas.yview)
        controls_container = tk.Frame(canvas, bg=self.theme_colors['bg'])
        
        controls_container.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=controls_container, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Process resource bar chart at top
        chart_frame = tk.LabelFrame(controls_container, text="📊 Resource Usage",
                                   font=('Arial', 11, 'bold'), bg=self.theme_colors['card_bg'],
                                   fg=self.theme_colors['primary_text'])
        chart_frame.pack(fill='x', pady=(0, 10), padx=5)
        chart_frame.configure(height=220)  # Reduced height
        
        # Create process resource chart
        process_data = {'top_processes': []}
        self.process_resource_chart = self.visualization_manager.create_process_resource_bar_chart(
            chart_frame, process_data)

    def create_system_tab(self):
        """System monitoring tab with detailed explanations"""
        system_frame = tk.Frame(self.root, bg=self.theme_colors['bg'])
        self.notebook.add(system_frame, text="🖥️ SYSTEM")

        # Header
        header_frame = tk.Frame(system_frame, bg=self.theme_colors['bg'])
        header_frame.pack(fill='x', padx=20, pady=15)

        user = get_current_username()
        tk.Label(header_frame, text=f"🖥️ SYSTEM MONITOR - User: {user}",
                 font=('Arial', 16, 'bold'), bg=self.theme_colors['bg'],
                 fg=self.theme_colors['primary_text']).pack(side='left')

        # Controls
        controls_frame = tk.Frame(header_frame, bg=self.theme_colors['bg'])
        controls_frame.pack(side='right')

        tk.Button(controls_frame, text="🔄 Refresh", command=self.refresh_system_info,
                  bg=self.theme_colors['info'], fg='white', font=('Arial', 10, 'bold'),
                  relief='flat', padx=15, pady=8, cursor='hand2').pack(side='left', padx=5)

        # Main system display with resizable PanedWindow
        main_paned = tk.PanedWindow(system_frame, orient=tk.HORIZONTAL,
                                    sashwidth=8, sashrelief=tk.RAISED,
                                    bg=self.theme_colors['bg'])
        main_paned.pack(fill='both', expand=True, padx=20, pady=10)

        # Left side - System metrics with recommendations inside
        metrics_container = tk.Frame(main_paned, bg=self.theme_colors['bg'])
        main_paned.add(metrics_container, minsize=400)
        
        metrics_frame = tk.LabelFrame(metrics_container, text="📊 Real-Time Metrics with Analysis",
                                      font=('Arial', 12, 'bold'), bg=self.theme_colors['card_bg'],
                                      fg=self.theme_colors['primary_text'])
        metrics_frame.pack(fill='both', expand=True, pady=(0,5))

        self.system_display = self.create_themed_text_widget(metrics_frame, height=12)
        self.system_display.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Performance recommendations moved inside left panel
        recommendations_frame = tk.LabelFrame(metrics_container, text="🎯 Performance Recommendations",
                                              font=('Arial', 11, 'bold'), bg=self.theme_colors['card_bg'],
                                              fg=self.theme_colors['primary_text'])
        recommendations_frame.pack(fill='both', expand=True)

        self.recommendations_text = self.create_themed_text_widget(recommendations_frame, height=6)
        self.recommendations_text.pack(fill='both', expand=True, padx=10, pady=10)

        # Right side - Charts only
        recommendations_container = tk.Frame(main_paned, bg=self.theme_colors['bg'])
        main_paned.add(recommendations_container, minsize=350)

        # Pie chart for disk usage
        chart_frame = tk.LabelFrame(recommendations_container, text="📊 Disk Usage Breakdown",
                                  font=('Arial', 11, 'bold'), bg=self.theme_colors['card_bg'],
                                  fg=self.theme_colors['primary_text'])
        chart_frame.pack(fill='both', expand=True, pady=(5, 10))
        
        # Create enhanced pie chart using visualization manager
        system_data = self.system_monitor.get_data()
        self.disk_chart = self.visualization_manager.create_disk_usage_pie_chart(chart_frame, system_data, launcher_ref=self)

    
    def create_settings_help_display(self, parent_frame):
        """Create comprehensive help text display for settings"""
        try:
            # Creating settings help display
            
            # Create scrollable text widget
            help_text_frame = tk.Frame(parent_frame, bg=self.theme_colors['card_bg'])
            help_text_frame.pack(fill='both', expand=True, padx=5, pady=5)
            
            # Scrollbar
            help_scrollbar = tk.Scrollbar(help_text_frame)
            help_scrollbar.pack(side='right', fill='y')
            
            # Text widget with comprehensive help
            self.settings_help_text = tk.Text(help_text_frame, bg=self.theme_colors['display_bg'],
                                           fg=self.theme_colors['display_text'], font=('Courier', 8),
                                           yscrollcommand=help_scrollbar.set, wrap='word',
                                           height=15, state='normal')
            self.settings_help_text.pack(side='left', fill='both', expand=True)
            help_scrollbar.config(command=self.settings_help_text.yview)
            
            # Configure text tags for colors
            self.settings_help_text.tag_configure('header', foreground=self.theme_colors['primary_text'], 
                                                font=('Arial', 10, 'bold'))
            self.settings_help_text.tag_configure('section', foreground=self.theme_colors['info'], 
                                                font=('Arial', 9, 'bold'))
            self.settings_help_text.tag_configure('important', foreground=self.theme_colors['error'], 
                                                font=('Arial', 8, 'bold'))
            self.settings_help_text.tag_configure('success', foreground=self.theme_colors['success'])
            self.settings_help_text.tag_configure('warning', foreground=self.theme_colors['warning'])
            
            # Insert concise help content
            help_content = """⚙️ SETTINGS QUICK GUIDE

📁 DEPENDENT FILES & PATHS:
- Base Directory: /users/paruljot/patchfinder/GUI_Scripts_V2/
- Configuration: master_config.json (main config file)
- Logs Directory: logs/ (all log files stored here)
- Main Log: logs/professional_launcher.log
- Debug Logs: logs/debug_YYYYMMDD.log (daily debug files)
- Backups: config_backup_*.json (timestamped backups)
- User Path: 'paruljot' (from remote server own_login - may change)

🔧 SYSTEM PERFORMANCE:
- GUI Refresh: 5 seconds (recommended)
- Node Timeout: 2 seconds (local), 5+ (remote)

📊 LOGGING & DEBUG:
- Debug Mode: ON for troubleshooting, OFF for performance
- Log Retention: 7-30 days
- Auto Cleanup: ON (recommended)

🖥️ WINDOW & INTERFACE:
- Always on Top: Keep launcher visible
- Show Notifications: Enable for alerts

🌐 NETWORK & MONITORING:
- Health Check: 60 seconds interval
- Max Concurrent: 3 connections

🎨 THEMES:
- 🌅 Sunset - 🌙 Dark - ☀️ Light - 🔮 Matrix

🔧 NODE & SERVER CONFIG:
- Add/Modify Nodes: Manage connection settings
- Servers: Configure remote server access
- Backup: Create/restore configuration files

❓ HELP TEXT:
- Toggle this help panel visibility
- Shows/hides detailed explanations

🔍 QUICK FIXES:
- Slow interface → Increase refresh interval
- Connection issues → Check timeout settings
- Missing logs → Enable debug mode
- High CPU → Increase refresh, disable debug"""

            # Insert content with formatting
            lines = help_content.split('\n')
            for line in lines:
                if line.startswith("📚") or line.startswith("🔧") or line.startswith("📊") or line.startswith("🖥️") or line.startswith("✏️") or line.startswith("⚙️") or line.startswith("🔍") or line.startswith("💡") or line.startswith("🚀") or line.startswith("📞"):
                    self.settings_help_text.insert(tk.END, line + '\n', 'header')
                elif line.endswith(':') and not line.startswith("' '"):
                    self.settings_help_text.insert(tk.END, line + '\n', 'section')
                elif '✅' in line or '[ERR]' in line:
                    if '✅' in line:
                        self.settings_help_text.insert(tk.END, line + '\n', 'success')
                    else:
                        self.settings_help_text.insert(tk.END, line + '\n', 'warning')
                elif line.startswith("'- Recommended:'") or line.startswith("'- Impact:'"):
                    self.settings_help_text.insert(tk.END, line + '\n', 'important')
                else:
                    self.settings_help_text.insert(tk.END, line + '\n')
            
            # Make text read-only
            self.settings_help_text.config(state='disabled')
            # Settings help display created successfully
            
        except Exception as e:
            pass  # Silent error handling
            error_label = tk.Label(parent_frame, text=f"Settings Help Error: {e}\nPlease check console for details.",
                                 bg=self.theme_colors['card_bg'], fg=self.theme_colors['error'],
                                 font=('Arial', 10), wraplength=400, justify='left')
            error_label.pack(expand=True, padx=10, pady=20)

    def create_debug_logs_tab(self):
        """FIXED: Debug logs with COLOR-CODED display and LEGENDS for three boxes"""
        logs_frame = tk.Frame(self.root, bg=self.theme_colors['bg'])
        self.notebook.add(logs_frame, text="🐛 DEBUG LOGS")

        # Header
        header_frame = tk.Frame(logs_frame, bg=self.theme_colors['bg'])
        header_frame.pack(fill='x', padx=20, pady=15)

        tk.Label(header_frame, text="🔧 DEBUG & ACTIVITY LOGS", font=('Arial', 16, 'bold'),
                 bg=self.theme_colors['bg'], fg=self.theme_colors['primary_text']).pack(side='left')

        # Controls
        controls_frame = tk.Frame(header_frame, bg=self.theme_colors['bg'])
        controls_frame.pack(side='right')

        tk.Button(controls_frame, text="🔄 Refresh Logs", command=self.refresh_debug_logs,
                  bg=self.theme_colors['info'], fg='white', font=('Arial', 10, 'bold'),
                  relief='flat', padx=15, pady=8, cursor='hand2').pack(side='left', padx=5)

        tk.Button(controls_frame, text="🗑️ Clear Display", command=self.clear_debug_display,
                  bg=self.theme_colors['warning'], fg='white', font=('Arial', 10, 'bold'),
                  relief='flat', padx=15, pady=8, cursor='hand2').pack(side='left', padx=5)
        
        tk.Button(controls_frame, text="🧹 Delete Old Files", command=self.clean_old_logs,
                  bg=self.theme_colors['error'], fg='white', font=('Arial', 10, 'bold'),
                  relief='flat', padx=15, pady=8, cursor='hand2').pack(side='left', padx=5)

        # MOVED: Filter options to top pane below title
        filter_frame = tk.Frame(logs_frame, bg=self.theme_colors['bg'])
        filter_frame.pack(fill='x', padx=20, pady=(0, 10))

        # Filter label
        tk.Label(filter_frame, text="🔍 Quick Filters:", font=('Arial', 11, 'bold'),
                bg=self.theme_colors['bg'], fg=self.theme_colors['primary_text']).pack(side='left')

        # Filter checkboxes - ALL TABS
        self.log_filter_vars = {}
        filter_types = ['ERROR', 'WARNING', 'INFO', 'SYSTEM', 'NETWORK', 'DASHBOARD', 'PROCESSES', 'SPACE', 'DEBUG']
        
        for log_type in filter_types:
            var = tk.BooleanVar(value=True)
            self.log_filter_vars[log_type] = var
            cb = tk.Checkbutton(filter_frame, text=log_type, variable=var,
                              font=('Arial', 8), bg=self.theme_colors['bg'],
                              fg=self.theme_colors['primary_text'], command=self.apply_log_filter)
            cb.pack(side='left', padx=3)

        # Apply filter button
        tk.Button(filter_frame, text="Apply Filter", command=self.apply_log_filter,
                 bg=self.theme_colors['info'], fg='white', font=('Arial', 9, 'bold'),
                 relief='raised', bd=1, padx=10, pady=2).pack(side='left', padx=10)

        # Select All button - check all checkboxes
        tk.Button(filter_frame, text="Select All", command=self.select_all_debug_filters,
                 bg=self.theme_colors['success'], fg='white', font=('Arial', 9, 'bold'),
                 relief='raised', bd=1, padx=10, pady=2).pack(side='left', padx=5)

        # Clear All button - uncheck all checkboxes
        tk.Button(filter_frame, text="Clear All", command=self.clear_all_filters,
                 bg=self.theme_colors['error'], fg='white', font=('Arial', 9, 'bold'),
                 relief='raised', bd=1, padx=10, pady=2).pack(side='left', padx=5)

        # FIXED: Main container with resizable PanedWindow
        main_paned = tk.PanedWindow(logs_frame, orient=tk.HORIZONTAL,
                                    sashwidth=8, sashrelief=tk.RAISED,
                                    bg=self.theme_colors['bg'])
        main_paned.pack(fill='both', expand=True, padx=20, pady=10)

        # FIXED: Left side - Debug information with LEGEND
        debug_frame = tk.LabelFrame(main_paned, text="🔍 Debug Diagnostic Information - Real-time system logs",
                                    font=('Arial', 12, 'bold'), bg=self.theme_colors['card_bg'],
                                    fg=self.theme_colors['primary_text'])
        main_paned.add(debug_frame, minsize=450)

        # LEGEND for debug logs
        debug_legend = tk.Frame(debug_frame, bg=self.theme_colors['card_bg'])
        debug_legend.pack(fill='x', padx=10, pady=5)

        tk.Label(debug_legend, text="🎨 Color Legend: ", font=('Arial', 9, 'bold'),
                 bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).pack(side='left')
        tk.Label(debug_legend, text="ERROR", font=('Arial', 9, 'bold'),
                 bg=self.theme_colors['card_bg'], fg=self.theme_colors['error']).pack(side='left', padx=5)
        tk.Label(debug_legend, text="WARNING", font=('Arial', 9, 'bold'),
                 bg=self.theme_colors['card_bg'], fg=self.theme_colors['warning']).pack(side='left', padx=5)
        tk.Label(debug_legend, text="SUCCESS", font=('Arial', 9, 'bold'),
                 bg=self.theme_colors['card_bg'], fg=self.theme_colors['success']).pack(side='left', padx=5)
        tk.Label(debug_legend, text="INFO", font=('Arial', 9, 'bold'),
                 bg=self.theme_colors['card_bg'], fg=self.theme_colors['info']).pack(side='left', padx=5)

        self.debug_display = self.create_themed_text_widget(debug_frame, height=15)
        self.debug_display.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Add color tags for different log categories
        self.debug_display.tag_configure('DASHBOARD', foreground='#00CED1', font=('Consolas', 9, 'bold'))  # Dark Turquoise
        self.debug_display.tag_configure('PROCESSES', foreground='#FF69B4', font=('Consolas', 9, 'bold'))  # Hot Pink
        self.debug_display.tag_configure('SPACE', foreground='#FFD700', font=('Consolas', 9, 'bold'))  # Gold
        self.debug_display.tag_configure('DEBUG', foreground='#9370DB', font=('Consolas', 9, 'bold'))  # Medium Purple

        # FIXED: Right side container for TWO boxes with LEGENDS
        right_container = tk.Frame(main_paned, bg=self.theme_colors['bg'])
        main_paned.add(right_container, minsize=300)

        # FIXED: Log files overview with LEGEND
        log_files_frame = tk.LabelFrame(right_container, text="📄 Log Files Management - Available log files",
                                        font=('Arial', 11, 'bold'), bg=self.theme_colors['card_bg'],
                                        fg=self.theme_colors['primary_text'])
        log_files_frame.pack(fill='x', pady=(0, 10))

        # LEGEND for log files
        files_legend = tk.Frame(log_files_frame, bg=self.theme_colors['card_bg'])
        files_legend.pack(fill='x', padx=10, pady=5)

        tk.Label(files_legend, text="📋 Shows: Daily logs, main logs, debug logs", font=('Arial', 9),
                 bg=self.theme_colors['card_bg'], fg=self.theme_colors['secondary_text']).pack()

        # Log files listbox with horizontal and vertical scrollbars
        log_list_container = tk.Frame(log_files_frame, bg=self.theme_colors['card_bg'])
        log_list_container.pack(fill='both', expand=True, padx=10, pady=5)

        # Vertical scrollbar
        log_v_scrollbar = tk.Scrollbar(log_list_container, orient='vertical')
        log_v_scrollbar.pack(side='right', fill='y')

        # Horizontal scrollbar
        log_h_scrollbar = tk.Scrollbar(log_list_container, orient='horizontal')
        log_h_scrollbar.pack(side='bottom', fill='x')

        self.log_files_listbox = tk.Listbox(log_list_container, bg=self.theme_colors['display_bg'],
                                            fg=self.theme_colors['display_text'], font=('Courier', 9),
                                            yscrollcommand=log_v_scrollbar.set,
                                            xscrollcommand=log_h_scrollbar.set, height=6)
        self.log_files_listbox.pack(side='left', fill='both', expand=True)
        log_v_scrollbar.config(command=self.log_files_listbox.yview)
        log_h_scrollbar.config(command=self.log_files_listbox.xview)
        
        # Add delete button for selected log file
        delete_log_frame = tk.Frame(log_files_frame, bg=self.theme_colors['card_bg'])
        delete_log_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Button(delete_log_frame, text="🗑️ Delete Selected Log", command=self.delete_selected_log_file,
                 bg=self.theme_colors['error'], fg='white', font=('Arial', 9, 'bold'),
                 relief='flat', padx=10, pady=5).pack(side='left', padx=5)
        
        tk.Label(delete_log_frame, text="Click log file above, then delete",
                font=('Arial', 8, 'italic'), bg=self.theme_colors['card_bg'],
                fg=self.theme_colors['secondary_text']).pack(side='left', padx=5)

        # SIMPLIFIED: Just Filter Controls
        analysis_frame = tk.LabelFrame(right_container, text="🔍 Advanced Filters",
                                       font=('Arial', 11, 'bold'), bg=self.theme_colors['card_bg'],
                                       fg=self.theme_colors['primary_text'])
        analysis_frame.pack(fill='both', expand=True)

        # Quick actions
        actions_frame = tk.Frame(analysis_frame, bg=self.theme_colors['card_bg'])
        actions_frame.pack(fill='x', padx=10, pady=5)

        tk.Label(actions_frame, text="⚡ Quick Actions:", font=('Arial', 10, 'bold'),
                bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).pack(anchor='w')

        # Action buttons in grid
        btn_frame = tk.Frame(actions_frame, bg=self.theme_colors['card_bg'])
        btn_frame.pack(fill='x', pady=5)

        tk.Button(btn_frame, text="📤 Export", command=self.export_debug_logs,
                 bg=self.theme_colors['success'], fg='white', font=('Arial', 8, 'bold'),
                 relief='raised', bd=1, width=12).grid(row=0, column=0, padx=2, pady=2)

        tk.Button(btn_frame, text="📋 Copy", command=self.copy_debug_logs_to_clipboard,
                 bg=self.theme_colors['info'], fg='white', font=('Arial', 8, 'bold'),
                 relief='raised', bd=1, width=12).grid(row=0, column=1, padx=2, pady=2)

        tk.Button(btn_frame, text="📊 Analyze", command=self.analyze_debug_logs,
                 bg=self.theme_colors['warning'], fg='white', font=('Arial', 8, 'bold'),
                 relief='raised', bd=1, width=12).grid(row=1, column=0, padx=2, pady=2, columnspan=2)

        # Advanced filter options
        filter_frame = tk.Frame(analysis_frame, bg=self.theme_colors['card_bg'])
        filter_frame.pack(fill='both', expand=True, padx=10, pady=5)

        tk.Label(filter_frame, text="🔧 Advanced Filtering:", font=('Arial', 10, 'bold'),
                bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).pack(anchor='w')

        # Time-based filters
        time_frame = tk.Frame(filter_frame, bg=self.theme_colors['card_bg'])
        time_frame.pack(fill='x', pady=5)

        tk.Label(time_frame, text="⏰ Time Range:", font=('Arial', 9),
                bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).pack(anchor='w')

        time_options = ["Last Hour", "Last 4 Hours", "Today", "All Time"]
        self.time_filter_var = tk.StringVar(value="All Time")
        time_combo = tk.OptionMenu(time_frame, self.time_filter_var, *time_options)
        time_combo.config(bg=self.theme_colors['card_bg'], font=('Arial', 8))
        time_combo.pack(anchor='w', pady=2)

        # Keyword filter
        keyword_frame = tk.Frame(filter_frame, bg=self.theme_colors['card_bg'])
        keyword_frame.pack(fill='x', pady=5)

        tk.Label(keyword_frame, text="🔍 Keyword Filter:", font=('Arial', 9),
                bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).pack(anchor='w')

        self.keyword_filter_var = tk.StringVar()
        keyword_entry = tk.Entry(keyword_frame, textvariable=self.keyword_filter_var, 
                                font=('Arial', 9), width=20)
        keyword_entry.pack(side='left', pady=2, padx=(0, 5))
        
        # Apply keyword filter button
        tk.Button(keyword_frame, text="🔍 Apply", 
                 command=self.apply_advanced_filter,
                 bg=self.theme_colors['highlight'], fg='white', font=('Arial', 8, 'bold'),
                 relief='raised', bd=1, padx=8, pady=3).pack(side='left', padx=2)
        
        # Reset keyword filter button
        tk.Button(keyword_frame, text="↺ Reset", 
                 command=self.reset_keyword_filter,
                 bg=self.theme_colors['warning'], fg='white', font=('Arial', 8, 'bold'),
                 relief='raised', bd=1, padx=8, pady=3).pack(side='left')

        # Search functionality
        search_frame = tk.Frame(analysis_frame, bg=self.theme_colors['card_bg'])
        search_frame.pack(fill='x', padx=10, pady=5)

        tk.Label(search_frame, text="🔍 Search Logs:", font=('Arial', 10, 'bold'),
                bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).pack(anchor='w')

        search_input_frame = tk.Frame(search_frame, bg=self.theme_colors['card_bg'])
        search_input_frame.pack(fill='x', pady=2)

        self.log_search_var = tk.StringVar()
        search_entry = tk.Entry(search_input_frame, textvariable=self.log_search_var, 
                               width=15, font=('Arial', 9))
        search_entry.pack(side='left', padx=(0, 5))

        tk.Button(search_input_frame, text="Go", command=self.search_logs,
                 bg=self.theme_colors['info'], fg='white', font=('Arial', 8, 'bold'),
                 relief='raised', bd=1, width=4).pack(side='left')

        # Search results
        self.search_status_label = tk.Label(search_frame, text="", font=('Arial', 8),
                                          bg=self.theme_colors['card_bg'], fg=self.theme_colors['success'])
        self.search_status_label.pack(anchor='w', pady=2)


    def create_help_text_display(self, parent_frame):
        """Create help text display for settings"""
        help_frame = tk.LabelFrame(parent_frame, text="❓ Settings Help & Explanations",
                                 font=('Arial', 11, 'bold'), bg=self.theme_colors['card_bg'],
                                 fg=self.theme_colors['primary_text'])
        help_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        help_text = tk.Text(help_frame, height=12, bg=self.theme_colors['display_bg'],
                           fg=self.theme_colors['display_text'], font=('Arial', 9),
                           wrap='word', state='disabled')
        help_text.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Configure text tags for colored help text
        help_text.tag_configure('setting', foreground=self.theme_colors['highlight'], font=('Arial', 9, 'bold'))
        help_text.tag_configure('description', foreground=self.theme_colors['primary_text'])
        help_text.tag_configure('warning', foreground=self.theme_colors['warning'], font=('Arial', 9, 'bold'))
        help_text.tag_configure('success', foreground=self.theme_colors['success'])
        
        # Add help content
        help_content = """🎨 THEME SETTINGS:
- Professional: Clean business interface with blue accents
- Dark: Modern dark theme for reduced eye strain
- Light: Bright theme for well-lit environments  
- Matrix: Green terminal-style theme for developers
- Sunset: Warm orange theme for evening use

⏰ REFRESH INTERVAL:
- Controls how often the dashboard updates (1-60 seconds)
- Lower values = more responsive but higher CPU usage
- Recommended: 5 seconds for balance

🌐 NODE TIMEOUT:
- Maximum time to wait for network connections (1-10 seconds)
- CRITICAL: Prevents hanging on slow networks
- Lower values = faster response, may miss slow nodes
- Recommended: 2 seconds (NO HANGING GUARANTEE)

🐛 DEBUG MODE:
- Enables detailed logging for troubleshooting
- Creates daily debug log files
- Increases disk usage but helps with problem diagnosis

📁 LOG RETENTION:
- How many days to keep old log files (1-365 days)
- Automatic cleanup prevents disk space issues
- Recommended: 30 days

🔐 ENCRYPT CONFIGS:
- Password-protect configuration files
- Uses AES-256 encryption for security
- Required for sensitive network credentials

📊 MAX LOG SIZE:
- Maximum size for individual log files (1-100 MB)
- Prevents runaway log files from filling disk
- Files are rotated when limit reached

🔍 MAX CONCURRENT CHECKS:
- How many network nodes to check simultaneously (1-10)
- Higher values = faster scanning but more resource usage
- Recommended: 3 for stability

⚠️ IMPORTANT WARNINGS:
- Node Timeout below 2 seconds may cause instability
- Debug Mode increases disk usage significantly
- Refresh Interval below 3 seconds may impact performance
- Always backup configurations before encryption"""
        
        # Insert help content with formatting
        help_text.config(state='normal')
        lines = help_content.split('\n')
        for line in lines:
            if line.startswith("✏️") or line.startswith("'⏰'") or line.startswith("'🌐'") or line.startswith("'🐛'") or line.startswith("'📁'") or line.startswith("'🔐'") or line.startswith("📊") or line.startswith("🔍"):
                help_text.insert(tk.END, line + '\n', 'setting')
            elif line.startswith("'⚠️'"):
                help_text.insert(tk.END, line + '\n', 'warning')
            elif 'Recommended:' in line:
                help_text.insert(tk.END, line + '\n', 'success')
            else:
                help_text.insert(tk.END, line + '\n', 'description')
        help_text.config(state='disabled')
        
        return help_text

    def create_text_fallback_chart(self, parent_frame, system_data):
        """Create text-based fallback when matplotlib unavailable"""
        total_disk = system_data.get('disk_usage', 0)
        user_disk = system_data.get('user_disk_usage', 0)
        free_space = 100 - total_disk
        system_space = max(0, total_disk - user_disk)
        
        fallback_text = f"""📊 DISK USAGE BREAKDOWN
        
💾 Total Disk Usage: {total_disk:.1f}%
👤 User Files: {user_disk:.1f}%
🖥️ System Files: {system_space:.1f}%
✅ Free Space: {free_space:.1f}%

📈 Usage Bar:
{"█}" * int(user_disk/2)}{"▓}" * int(system_space/2)}{"░}" * int(free_space/2)}

Legend: █ User  ▓ System  ░ Free

💡 Install matplotlib for visual pie chart:
   pip install matplotlib"""
        
        fallback_label = tk.Label(parent_frame, text=fallback_text,
                                bg=self.theme_colors['card_bg'], 
                                fg=self.theme_colors['primary_text'],
                                font=('Courier', 9), justify='left')
        fallback_label.pack(expand=True, pady=10, padx=10)
        return fallback_label

    
    def get_user_from_config(self):
        """Get username from JSON config file"""
        try:
            config_file = "master_config.json"
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    config = json.load(f)
                    remote_servers = config.get('remote_server', [])
                    if remote_servers:
                        return remote_servers[0].get('own_login', 'paruljot')
            return 'paruljot'  # Default fallback
        except:
            return 'paruljot'  # Fallback if config read fails

    def create_disk_usage_pie_chart(self, parent_frame):
        """Create enhanced disk usage breakdown with GB values and clickable details"""
        try:
            import shutil
            
            # Get disk usage in bytes
            total, used, free = shutil.disk_usage("/")
            total_gb = total / (1024**3)
            used_gb = used / (1024**3)
            free_gb = free / (1024**3)
            
            # Calculate percentages
            used_percent = (used / total) * 100
            free_percent = (free / total) * 100
            
            # Get user from config and estimate user vs system
            config_user = self.get_user_from_config()
            user_path = f"/users/{config_user}"
            # Fallback to current user if config path doesn't exist
            if not os.path.exists(user_path):
                user_path = f"/home/{getpass.getuser()}"
            try:
                user_total, user_used, user_free = shutil.disk_usage(user_path)
                user_gb = user_used / (1024**3)
                user_percent = (user_used / total) * 100
            except:
                user_gb = 0
                user_percent = 0
            
            system_gb = used_gb - user_gb
            system_percent = used_percent - user_percent
            
            # Create enhanced chart frame
            chart_frame = tk.Frame(parent_frame, bg=self.theme_colors['card_bg'])
            chart_frame.pack(fill='both', expand=True, padx=10, pady=10)
            
            # Title with directory info
            title_label = tk.Label(chart_frame, text="💾 DISK USAGE BREAKDOWN", 
                                 font=('Arial', 12, 'bold'),
                                 bg=self.theme_colors['card_bg'], 
                                 fg=self.theme_colors['primary_text'])
            title_label.pack(pady=(0, 5))
            
            # Directory info with enterprise path
            dir_info = tk.Label(chart_frame, text=f"📁 Analyzing: Root (/) | Enterprise User: {user_path}", 
                              font=('Arial', 9), bg=self.theme_colors['card_bg'], 
                              fg=self.theme_colors['secondary_text'])
            dir_info.pack(pady=(0, 10))
            
            # Clickable usage bars with GB values
            bar_frame = tk.Frame(chart_frame, bg=self.theme_colors['card_bg'])
            bar_frame.pack(fill='x', pady=5)
            
            # User files bar (clickable)
            user_frame = tk.Frame(bar_frame, bg=self.theme_colors['card_bg'])
            user_frame.pack(fill='x', pady=2)
            
            user_label = tk.Label(user_frame, text=f"[RED] User Files: {user_gb:.1f}GB ({user_percent:.1f}%)", 
                                font=('Arial', 10, 'bold'), bg=self.theme_colors['card_bg'], 
                                fg=self.theme_colors['error'], cursor='hand2')
            user_label.pack(anchor='w')
            user_label.bind("<Button-1>", lambda e: self.show_user_usage_details())
            
            user_bar = tk.Label(user_frame, text="█" * max(1, int(user_percent/2)) + "░" * (50 - max(1, int(user_percent/2))), 
                              fg=self.theme_colors['error'], bg=self.theme_colors['card_bg'], 
                              font=('Courier', 8), cursor='hand2')
            user_bar.pack(anchor='w', padx=10)
            user_bar.bind("<Button-1>", lambda e: self.show_user_usage_details())
            
            # System files bar (clickable)
            system_frame = tk.Frame(bar_frame, bg=self.theme_colors['card_bg'])
            system_frame.pack(fill='x', pady=2)
            
            system_label = tk.Label(system_frame, text=f"[YELLOW] System Files: {system_gb:.1f}GB ({system_percent:.1f}%)", 
                                  font=('Arial', 10, 'bold'), bg=self.theme_colors['card_bg'], 
                                  fg=self.theme_colors['warning'], cursor='hand2')
            system_label.pack(anchor='w')
            system_label.bind("<Button-1>", lambda e: self.show_system_usage_details())
            
            system_bar = tk.Label(system_frame, text="█" * max(1, int(system_percent/2)) + "░" * (50 - max(1, int(system_percent/2))), 
                                fg=self.theme_colors['warning'], bg=self.theme_colors['card_bg'], 
                                font=('Courier', 8), cursor='hand2')
            system_bar.pack(anchor='w', padx=10)
            system_bar.bind("<Button-1>", lambda e: self.show_system_usage_details())
            
            # Free space bar
            free_frame = tk.Frame(bar_frame, bg=self.theme_colors['card_bg'])
            free_frame.pack(fill='x', pady=2)
            
            free_label = tk.Label(free_frame, text=f"[GREEN] Free Space: {free_gb:.1f}GB ({free_percent:.1f}%)", 
                                font=('Arial', 10, 'bold'), bg=self.theme_colors['card_bg'], 
                                fg=self.theme_colors['success'])
            free_label.pack(anchor='w')
            
            free_bar = tk.Label(free_frame, text="█" * max(1, int(free_percent/2)) + "░" * (50 - max(1, int(free_percent/2))), 
                              fg=self.theme_colors['success'], bg=self.theme_colors['card_bg'], font=('Courier', 8))
            free_bar.pack(anchor='w', padx=10)
            
            # Enhanced statistics
            stats_text = f"""📊 DETAILED SUMMARY:
            
💾 Total Capacity: {total_gb:.1f} GB
📊 Used Space: {used_gb:.1f} GB ({used_percent:.1f}%)
🆓 Available: {free_gb:.1f} GB ({free_percent:.1f}%)

🔍 User Analysis:
{'  - User directory (' + user_path + ')' if user_percent > 0 else '  - User: 0% (No files in home directory)'}
{'  - Contains: Documents, Downloads, Desktop files' if user_percent > 0 else '  - Possible reasons: New user, files in other locations'}

🎯 Space Status: {'[GREEN] Healthy' if free_percent > 20 else '[YELLOW] Warning' if free_percent > 10 else '[RED] Critical'}
[!] Click on colored bars above to see detailed breakdown!"""
            
            stats_label = tk.Label(chart_frame, text=stats_text, 
                                 font=('Courier', 8), justify='left',
                                 bg=self.theme_colors['card_bg'], 
                                 fg=self.theme_colors['primary_text'])
            stats_label.pack(pady=10)
            
            return chart_frame
            
        except Exception as e:
            error_label = tk.Label(parent_frame, 
                                 text=f"📊 Chart Error: {e}\n\nFallback: Basic disk info unavailable",
                                 bg=self.theme_colors['card_bg'], fg=self.theme_colors['error'],
                                 font=('Arial', 10), justify='left')
            error_label.pack(expand=True, pady=20)
            return error_label

    def show_user_usage_details(self):
        """Show detailed breakdown of user space usage"""
        try:
            user_path = f"/home/{getpass.getuser()}"
            config_user = self.get_user_from_config()
            enterprise_path = f"/users/{config_user}"
            current_path = f"/home/{getpass.getuser()}"
            
            details = f"""🔴 USER SPACE BREAKDOWN:

📁 Enterprise Directory: {enterprise_path}
📁 Current Directory: {current_path}
👤 Config User: {config_user}

📊 Common User Directories:
- Documents/     - Text files, PDFs
- Downloads/     - Downloaded files  
- Desktop/       - Desktop files
- Pictures/      - Images, photos
- Videos/        - Video files
- Music/         - Audio files
- .cache/        - Application cache
- .config/       - Configuration files

[!] To reduce user space:
1. Clean Downloads folder
2. Remove old documents
3. Clear browser cache
4. Delete duplicate files
5. Move large files to external storage

🔍 Use Space Analyzer tab for detailed file analysis!"""
            
            messagebox.showinfo("User Space Details", details)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to analyze user space: {e}")

    def show_system_usage_details(self):
        """Show detailed breakdown of system space usage"""
        try:
            details = f"""🟡 SYSTEM SPACE BREAKDOWN:

📁 Major System Directories:
- /usr/          - Installed programs & libraries
- /var/          - Variable data (logs, cache)
- /opt/          - Optional software packages
- /lib/          - System libraries
- /boot/         - Boot files & kernel
- /tmp/          - Temporary files
- /root/         - Root user directory

📊 Typical System Usage:
- Base OS:       ~2-4 GB
- Applications:  ~1-10 GB  
- System logs:   ~100 MB - 1 GB
- Package cache: ~500 MB - 2 GB

⚠️ System space is managed automatically
🔧 Only modify if you're an advanced user
[!] Use 'sudo apt autoremove' to clean packages"""
            
            messagebox.showinfo("System Space Details", details)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to analyze system space: {e}")

    def clear_space_filters(self):
        """Clear space analyzer filters and show all files"""
        try:
            self.space_filter_active = False
            self.filtered_files = []
            
            # Reset filter controls
            self.size_threshold_var.set("10")
            self.file_type_filter_var.set("All")
            
            # Refresh display with all files
            self.update_space_analyzer()
            
            self.insert_themed_text(self.directory_stats, "🔄 Filters cleared - showing all files", 'info')
            
        except Exception as e:
            messagebox.showerror("Clear Error", f"Failed to clear filters: {e}")

            # Connect debug display to logging system
        log_message.gui_callback = self.update_debug_display
        log_message("Debug logs tab initialized with GUI connection", "INFO")

    def create_network_connection_tab(self):
        """FIXED: Network Connection tab (renamed from Network Health)"""
        connection_frame = tk.Frame(self.root, bg=self.theme_colors['bg'])
        self.notebook.add(connection_frame, text="🌐 NETWORK CONNECTION")  # FIXED: Renamed

        # Header
        header_frame = tk.Frame(connection_frame, bg=self.theme_colors['bg'])
        header_frame.pack(fill='x', padx=20, pady=15)

        tk.Label(header_frame, text="🌐 NETWORK NODE CONNECTION MONITOR (NO HANGING)",
                 font=('Arial', 16, 'bold'), bg=self.theme_colors['bg'],
                 fg=self.theme_colors['primary_text']).pack(side='left')

        # Controls
        controls_frame = tk.Frame(header_frame, bg=self.theme_colors['bg'])
        controls_frame.pack(side='right')

        tk.Button(controls_frame, text="🔄 Force Check Now", command=self.manual_connection_check,
                  bg=self.theme_colors['info'], fg='white', font=('Arial', 10, 'bold'),
                  relief='flat', padx=15, pady=8, cursor='hand2').pack()


        # Main content with resizable PanedWindow
        main_paned = tk.PanedWindow(connection_frame, orient=tk.HORIZONTAL, 
                                    sashwidth=8, sashrelief=tk.RAISED,
                                    bg=self.theme_colors['bg'])
        main_paned.pack(fill='both', expand=True, padx=20, pady=10)

        # Left side - Connection status
        left_frame = tk.LabelFrame(main_paned, text="[HEALTH] Node Connection Status (SSH + Telnet)",
                                   font=('Arial', 12, 'bold'), bg=self.theme_colors['card_bg'],
                                   fg=self.theme_colors['primary_text'])
        main_paned.add(left_frame, minsize=400)

        self.connection_display = self.create_themed_text_widget(left_frame, height=20)
        self.connection_display.pack(fill='both', expand=True, padx=10, pady=10)

        # Right side - Statistics with vertical resizable panes
        right_frame = tk.Frame(main_paned, bg=self.theme_colors['bg'])
        main_paned.add(right_frame, minsize=300)
        
        # Vertical PanedWindow for chart (top) and stats (bottom)
        stats_paned = tk.PanedWindow(right_frame, orient=tk.VERTICAL,
                                     sashwidth=6, sashrelief=tk.RAISED,
                                     bg=self.theme_colors['bg'])
        stats_paned.pack(fill='both', expand=True)
        
        # Top: Chart
        chart_frame = tk.LabelFrame(stats_paned, text="📊 Connection Health Status",
                                    font=('Arial', 11, 'bold'), bg=self.theme_colors['card_bg'],
                                    fg=self.theme_colors['primary_text'])
        stats_paned.add(chart_frame, minsize=200)
        
        # Create network health pie chart
        connection_data = {'healthy_nodes': 0, 'unhealthy_nodes': 0}
        self.network_health_chart = self.visualization_manager.create_network_health_pie_chart(
            chart_frame, connection_data)

        # Bottom: Statistics text
        stats_text_frame = tk.LabelFrame(stats_paned, text="📈 Connection Statistics",
                                         font=('Arial', 11, 'bold'), bg=self.theme_colors['card_bg'],
                                         fg=self.theme_colors['primary_text'])
        stats_paned.add(stats_text_frame, minsize=150)
        
        self.connection_stats = self.create_themed_text_widget(stats_text_frame, height=8)
        self.connection_stats.pack(fill='both', expand=True, padx=10, pady=10)


    def create_settings_tab(self):
        """Settings tab with all functional settings"""
        settings_frame = tk.Frame(self.root, bg=self.theme_colors['bg'])
        self.notebook.add(settings_frame, text="⚙️ SETTINGS")

        # Header
        header_frame = tk.Frame(settings_frame, bg=self.theme_colors['bg'])
        header_frame.pack(fill='x', padx=20, pady=15)

        tk.Label(header_frame, text="⚙️ SETTINGS & CONFIGURATION", font=('Arial', 16, 'bold'),
                 bg=self.theme_colors['bg'], fg=self.theme_colors['primary_text']).pack(side='left')

        # Controls
        controls_frame = tk.Frame(header_frame, bg=self.theme_colors['bg'])
        controls_frame.pack(side='right')

        tk.Button(controls_frame, text="💾 Save Settings", command=self.apply_settings,
                  bg=self.theme_colors['success'], fg='white', font=('Arial', 9, 'bold'),
                  relief='flat', padx=10, pady=6, cursor='hand2').pack(side='left', padx=3)

        tk.Button(controls_frame, text="🔄 Reset Defaults", command=self.reset_settings,
                  bg=self.theme_colors['warning'], fg='white', font=('Arial', 9, 'bold'),
                  relief='flat', padx=10, pady=6, cursor='hand2').pack(side='left', padx=3)

        # MOVED: Node & Server Configuration buttons to top right
        tk.Button(controls_frame, text="🔧 Add/Modify Nodes", command=self.manage_nodes_config,
                 bg=self.theme_colors['success'], fg='white', font=('Arial', 9, 'bold'),
                 relief='flat', padx=10, pady=6, cursor='hand2').pack(side='right', padx=3)

        tk.Button(controls_frame, text="🌐 Servers", command=self.manage_servers_config,
                 bg=self.theme_colors['info'], fg='white', font=('Arial', 9, 'bold'),
                 relief='flat', padx=10, pady=6, cursor='hand2').pack(side='right', padx=3)

        tk.Button(controls_frame, text="💾 Backup", command=self.backup_json_config,
                 bg=self.theme_colors['warning'], fg='white', font=('Arial', 9, 'bold'),
                 relief='flat', padx=10, pady=6, cursor='hand2').pack(side='right', padx=3)

        # FIXED: Create left and right panes for better layout
        main_container = tk.Frame(settings_frame, bg=self.theme_colors['bg'])
        main_container.pack(fill='both', expand=True, padx=20, pady=10)

        # Left pane with scrollable content
        left_frame = tk.Frame(main_container, bg=self.theme_colors['bg'])
        left_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))

        left_canvas = tk.Canvas(left_frame, bg=self.theme_colors['bg'])
        left_scrollbar = tk.Scrollbar(left_frame, orient="vertical", command=left_canvas.yview)
        left_scrollable = tk.Frame(left_canvas, bg=self.theme_colors['bg'])

        left_scrollable.bind(
            "<Configure>",
            lambda e: left_canvas.configure(scrollregion=left_canvas.bbox("all"))
        )

        left_canvas.create_window((0, 0), window=left_scrollable, anchor="nw")
        left_canvas.configure(yscrollcommand=left_scrollbar.set)

        left_canvas.pack(side="left", fill="both", expand=True)
        left_scrollbar.pack(side="right", fill="y")

        # Right pane for help and additional content
        right_frame = tk.Frame(main_container, bg=self.theme_colors['bg'])
        right_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))

        # Settings content goes to left pane
        settings_content = left_scrollable

        # Performance settings
        perf_frame = tk.LabelFrame(settings_content, text="PERFORMANCE_ICON System Performance Settings",
                                   font=('Arial', 12, 'bold'), bg=self.theme_colors['card_bg'],
                                   fg=self.theme_colors['primary_text'])
        perf_frame.pack(fill='x', pady=10)

        perf_grid = tk.Frame(perf_frame, bg=self.theme_colors['card_bg'])
        perf_grid.pack(fill='x', padx=20, pady=20)

        perf_grid.grid_columnconfigure(1, weight=1)

        # Refresh interval
        tk.Label(perf_grid, text="GUI Refresh Interval (seconds):", font=('Arial', 11),
                 bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=0, column=0,
                                                                                             sticky='w', padx=5,
                                                                                             pady=10)

        self.refresh_interval_var = tk.StringVar(value=str(app_settings['refresh_interval']))
        tk.Spinbox(perf_grid, from_=1, to=30, textvariable=self.refresh_interval_var, width=10).grid(row=0, column=1,
                                                                                                     sticky='w', padx=5,
                                                                                                     pady=10)

        # Node timeout
        tk.Label(perf_grid, text="Node Connection Timeout (seconds):", font=('Arial', 11),
                 bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=1, column=0,
                                                                                             sticky='w', padx=5,
                                                                                             pady=10)

        self.timeout_var = tk.StringVar(value=str(app_settings['node_timeout']))
        tk.Spinbox(perf_grid, from_=1, to=10, textvariable=self.timeout_var, width=10).grid(row=1, column=1, sticky='w',
                                                                                            padx=5, pady=10)
        
        # ENHANCED: Add more useful settings
        
        # Logging Settings
        logging_frame = tk.LabelFrame(settings_content, text="📝 Logging & Debug Settings",
                                     font=('Arial', 12, 'bold'), bg=self.theme_colors['card_bg'],
                                     fg=self.theme_colors['primary_text'])
        logging_frame.pack(fill='x', pady=10)
        
        logging_grid = tk.Frame(logging_frame, bg=self.theme_colors['card_bg'])
        logging_grid.pack(fill='x', padx=20, pady=20)
        logging_grid.grid_columnconfigure(1, weight=1)
        
        # Debug mode
        tk.Label(logging_grid, text="Enable Debug Mode:", font=('Arial', 11),
                bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=0, column=0,
                                                                                           sticky='w', padx=5, pady=5)
        
        self.debug_mode_var = tk.BooleanVar(value=app_settings.get('debug_mode', True))
        tk.Checkbutton(logging_grid, variable=self.debug_mode_var,
                      bg=self.theme_colors['card_bg']).grid(row=0, column=1, sticky='w', padx=5, pady=5)
        
        # Log retention
        tk.Label(logging_grid, text="Log Retention (days):", font=('Arial', 11),
                bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=1, column=0,
                                                                                           sticky='w', padx=5, pady=5)
        
        self.log_retention_var = tk.StringVar(value=str(app_settings.get('log_retention_days', 30)))
        tk.Spinbox(logging_grid, from_=1, to=365, textvariable=self.log_retention_var, width=10).grid(row=1, column=1,
                                                                                                      sticky='w', padx=5, pady=5)
        
        # Auto cleanup
        tk.Label(logging_grid, text="Auto cleanup on startup:", font=('Arial', 11),
                bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=2, column=0,
                                                                                           sticky='w', padx=5, pady=5)
        
        self.auto_cleanup_var = tk.BooleanVar(value=app_settings.get('auto_cleanup_on_start', True))
        tk.Checkbutton(logging_grid, variable=self.auto_cleanup_var,
                      bg=self.theme_colors['card_bg']).grid(row=2, column=1, sticky='w', padx=5, pady=5)
        
        # Window Management Settings
        window_frame = tk.LabelFrame(settings_content, text="🪟 Window & Interface Settings",
                                    font=('Arial', 12, 'bold'), bg=self.theme_colors['card_bg'],
                                    fg=self.theme_colors['primary_text'])
        window_frame.pack(fill='x', pady=10)
        
        window_grid = tk.Frame(window_frame, bg=self.theme_colors['card_bg'])
        window_grid.pack(fill='x', padx=20, pady=20)
        window_grid.grid_columnconfigure(1, weight=1)
        
        # Always on top
        tk.Label(window_grid, text="Always on top:", font=('Arial', 11),
                bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=0, column=0,
                                                                                           sticky='w', padx=5, pady=5)
        
        self.always_on_top_var = tk.BooleanVar(value=app_settings.get('always_on_top', False))
        always_on_top_check = tk.Checkbutton(window_grid, variable=self.always_on_top_var,
                                            command=self.toggle_always_on_top,
                                            bg=self.theme_colors['card_bg'])
        always_on_top_check.grid(row=0, column=1, sticky='w', padx=5, pady=5)
        
        # Show notifications
        tk.Label(window_grid, text="Show notifications:", font=('Arial', 11),
                bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=1, column=0,
                                                                                           sticky='w', padx=5, pady=5)
        
        self.notifications_var = tk.BooleanVar(value=app_settings.get('show_notifications', True))
        tk.Checkbutton(window_grid, variable=self.notifications_var,
                      bg=self.theme_colors['card_bg']).grid(row=1, column=1, sticky='w', padx=5, pady=5)
        
        # Network Settings
        network_frame = tk.LabelFrame(settings_content, text="🌐 Network & Monitoring Settings",
                                     font=('Arial', 12, 'bold'), bg=self.theme_colors['card_bg'],
                                     fg=self.theme_colors['primary_text'])
        network_frame.pack(fill='x', pady=10)
        
        network_grid = tk.Frame(network_frame, bg=self.theme_colors['card_bg'])
        network_grid.pack(fill='x', padx=20, pady=20)
        network_grid.grid_columnconfigure(1, weight=1)
        
        # Health check interval
        tk.Label(network_grid, text="Health Check Interval (seconds):", font=('Arial', 11),
                bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=0, column=0,
                                                                                           sticky='w', padx=5, pady=5)
        
        self.health_interval_var = tk.StringVar(value=str(app_settings.get('health_check_interval', 60)))
        tk.Spinbox(network_grid, from_=30, to=300, textvariable=self.health_interval_var, width=10).grid(row=0, column=1,
                                                                                                         sticky='w', padx=5, pady=5)
        
        # Max concurrent checks
        tk.Label(network_grid, text="Max Concurrent Checks:", font=('Arial', 11),
                bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=1, column=0,
                                                                                           sticky='w', padx=5, pady=5)
        
        self.max_concurrent_var = tk.StringVar(value=str(app_settings.get('max_concurrent_checks', 3)))
        tk.Spinbox(network_grid, from_=1, to=10, textvariable=self.max_concurrent_var, width=10).grid(row=1, column=1,
                                                                                                      sticky='w', padx=5, pady=5)
        
        # REMOVED: Node & Server Configuration section (moved to top right)

        # Help Text Settings
        help_frame = tk.LabelFrame(settings_content, text="❓ Help & Interface Settings",
                                  font=('Arial', 12, 'bold'), bg=self.theme_colors['card_bg'],
                                  fg=self.theme_colors['primary_text'])
        help_frame.pack(fill='x', pady=10)
        
        help_grid = tk.Frame(help_frame, bg=self.theme_colors['card_bg'])
        help_grid.pack(fill='x', padx=20, pady=20)
        help_grid.grid_columnconfigure(1, weight=1)
        
        # Show help text option
        tk.Label(help_grid, text="Show Help Text:", font=('Arial', 11),
                bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=0, column=0,
                                                                                           sticky='w', padx=5, pady=5)
        
        self.show_help_var = tk.BooleanVar(value=app_settings.get('show_help_text', True))
        help_checkbox = tk.Checkbutton(help_grid, variable=self.show_help_var,
                                     bg=self.theme_colors['card_bg'], 
                                     command=self.toggle_help_text)
        help_checkbox.grid(row=0, column=1, sticky='w', padx=5, pady=5)

        # REMOVED: Duplicate Node & Server Configuration section (keeping the one in JSON section)
        
        # MOVED: Help Text to Right Pane with larger size
        help_text_frame = tk.LabelFrame(right_frame, text="📚 Settings Help & Explanations",
                                      font=('Arial', 12, 'bold'), bg=self.theme_colors['card_bg'],
                                      fg=self.theme_colors['primary_text'])
        help_text_frame.pack(fill='both', expand=True, padx=0, pady=0)
        
        # Create help text display with larger size
        self.help_text_frame_ref = help_text_frame  # Store reference for toggling
        self.create_settings_help_display(help_text_frame)

    def toggle_help_text(self):
        """Toggle help text panel visibility"""
        try:
            if hasattr(self, 'help_text_frame_ref') and self.help_text_frame_ref:
                if self.show_help_var.get():
                    # Show help text
                    self.help_text_frame_ref.pack(fill='both', expand=True, padx=0, pady=0)
                else:
                    # Hide help text
                    self.help_text_frame_ref.pack_forget()
        except Exception as e:
            print(f"Error toggling help text: {e}")

    def get_all_debug_content(self):
        """Get comprehensive debug content from GUI and files"""
        try:
            content_parts = []
            
            # 1. Get GUI display content
            if hasattr(self, 'debug_display'):
                gui_content = self.debug_display.get(1.0, tk.END).strip()
                if gui_content:
                    content_parts.append("=== GUI DEBUG DISPLAY ===")
                    content_parts.append(gui_content)
                    content_parts.append("")
            
            # 2. Get today's log file content
            today_log = f"debug_logs_{datetime.now().strftime('%Y%m%d')}.log"
            if os.path.exists(today_log):
                with open(today_log, 'r', encoding='utf-8') as f:
                    file_content = f.read().strip()
                    if file_content:
                        content_parts.append("=== TODAY'S LOG FILE ===")
                        content_parts.append(file_content)
                        content_parts.append("")
            
            # 3. Get recent log files (last 3 days)
            for i in range(1, 4):
                date = (datetime.now() - timedelta(days=i)).strftime('%Y%m%d')
                log_file = f"debug_logs_{date}.log"
                if os.path.exists(log_file):
                    with open(log_file, 'r', encoding='utf-8') as f:
                        file_content = f.read().strip()
                        if file_content:
                            content_parts.append(f"=== LOG FILE {date} ===")
                            content_parts.append(file_content)
                            content_parts.append("")
            
            # 4. Add system information
            content_parts.append("=== SYSTEM INFORMATION ===")
            content_parts.append(f"Current Time: {datetime.now()}")
            content_parts.append(f"Working Directory: {os.getcwd()}")
            content_parts.append(f"Python Path: {sys.executable}")
            content_parts.append(f"Available Memory: {self.get_memory_info()}")
            content_parts.append("")
            
            if content_parts:
                return "\n".join(content_parts)
            else:
                return "No debug content available yet.\n\nTip: Use the application features to generate debug logs."
                
        except Exception as e:
            return f"Error retrieving debug content: {e}"
    
    def get_memory_info(self):
        """Get basic memory information"""
        try:
            import psutil
            memory = psutil.virtual_memory()
            return "memory.available // (1024**3) GB available"
        except:
            return "Memory info unavailable"

    
    def update_debug_display(self, log_entry, level):
        """Update debug display with new log entry"""
        try:
            if hasattr(self, 'debug_display'):
                self.debug_display.config(state='normal')
                
                # Color coding based on level
                if level == "ERROR" or level == "CRITICAL":
                    self.debug_display.insert(tk.END, log_entry + "\n", 'error')
                elif level == "WARNING":
                    self.debug_display.insert(tk.END, log_entry + "\n", 'warning')
                elif level == "ACTION":
                    self.debug_display.insert(tk.END, log_entry + "\n", 'success')
                else:
                    self.debug_display.insert(tk.END, log_entry + "\n", 'info')
                
                # Auto-scroll to bottom
                self.debug_display.see(tk.END)
                self.debug_display.config(state='disabled')
        except:
            pass

    def create_status_bar(self):
        """Status bar with system information"""
        status_frame = tk.Frame(self.root, bg=self.theme_colors['card_bg'], relief='raised', bd=1)
        status_frame.pack(fill='x', side='bottom')

        user = get_current_username()
        current_dir = os.getcwd()

        # Left side status
        self.status_text = tk.Label(status_frame,
                                    text=f"[USER] User: {user} | 📁 Directory: {current_dir} | ⏰ {datetime.now().strftime('%H:%M:%S')}",
                                    bg=self.theme_colors['card_bg'], fg=self.theme_colors['secondary_text'],
                                    font=('Arial', 9))
        self.status_text.pack(side='left', padx=15, pady=5)

        # Right side status
        self.connection_status = tk.Label(status_frame, text="🔄 Initializing monitoring...",
                                          bg=self.theme_colors['card_bg'], fg=self.theme_colors['info'],
                                          font=('Arial', 9))
        self.connection_status.pack(side='right', padx=15, pady=5)

    # ========================================================================
    # ALL EVENT HANDLERS AND ACTION METHODS
    # ========================================================================

    def on_theme_change(self, event=None):
        """FIXED: Theme change with restart option for full application"""
        new_theme = self.theme_var.get()
        if new_theme in THEMES:
            self.current_theme = new_theme
            self.theme_colors = THEMES[new_theme]
            app_settings['theme'] = new_theme
            save_settings()

            # Apply theme immediately (partial)
            self.apply_theme_immediately()

            # Show restart option for full theme application
            restart_response = messagebox.askyesno(
                "Theme Applied", 
                f"Theme changed to {new_theme}!\n"
                "Some theme elements may not be fully applied.\n"
                "Would you like to restart the application for complete theme application?",
                icon='question'
            )
            
            if restart_response:
                # Restart the application
                self.on_closing()
                os.execv(sys.executable, ['python'] + sys.argv)

            log_message(f"Theme changed to {new_theme}", "THEME")

    def apply_theme_immediately(self):
        """Apply theme changes immediately to ALL GUI elements"""
        try:
            # Update root window
            self.root.configure(bg=self.theme_colors['bg'])

            # Update all frames recursively
            self._update_widget_theme(self.root)

            # Update notebook style
            style = ttk.Style()
            style.theme_use('clam')
            style.configure('TNotebook', background=self.theme_colors['bg'])
            style.configure('TNotebook.Tab', background=self.theme_colors['card_bg'],
                            foreground=self.theme_colors['primary_text'])
            style.configure('TCombobox', fieldbackground=self.theme_colors['display_bg'])

        except Exception as e:
            log_message(f"Error applying theme immediately: {e}", "ERROR")
    
    def _update_widget_theme(self, widget):
        """Recursively update theme for all widgets"""
        try:
            widget_class = widget.winfo_class()
            
            if widget_class == 'Frame':
                widget.configure(bg=self.theme_colors['bg'])
            elif widget_class == 'LabelFrame':
                widget.configure(bg=self.theme_colors['card_bg'], 
                               fg=self.theme_colors['primary_text'])
            elif widget_class == 'Label':
                widget.configure(bg=self.theme_colors.get('card_bg', self.theme_colors['bg']), 
                               fg=self.theme_colors['primary_text'])
            elif widget_class == 'Text':
                widget.configure(bg=self.theme_colors['display_bg'], 
                               fg=self.theme_colors['display_text'],
                               insertbackground=self.theme_colors['primary_text'])
            elif widget_class == 'Button':
                # Don't change button colors as they have specific theme colors
                pass
            elif widget_class == 'Listbox':
                widget.configure(bg=self.theme_colors['display_bg'], 
                               fg=self.theme_colors['display_text'])
            
            # Recursively update children
            for child in widget.winfo_children():
                self._update_widget_theme(child)
                
        except Exception as e:
            # Silently continue if widget doesn't support certain configurations
            pass

    def launch_script(self, script_key):
        """FIXED: Launch automation script"""
        try:
            if script_key not in AUTOMATION_SCRIPTS:
                messagebox.showerror("Error", f"Script {script_key} not found")
                return

            script_info = AUTOMATION_SCRIPTS[script_key]
            success, message = self.process_manager.launch_script(script_key, script_info)

            if success:
                # Update status label
                if script_key in self.script_status_labels:
                    self.script_status_labels[script_key].config(text="🟢 Running", fg=self.theme_colors['success'])

                # Show toast notification instead of messagebox
                self.show_toast(f"✅ {script_info['name']} started successfully!", 'success')
                self.insert_themed_text(self.activity_text, f"✅ {message}", 'success')
            else:
                self.show_toast(f"❌ Failed to start {script_info['name']}", 'error')
                self.insert_themed_text(self.activity_text, f"[ERR] {message}", 'error')

        except Exception as e:
                error_msg = f"Failed to launch script {script_key}: {e}"
                messagebox.showerror("Error", error_msg)
                log_message(error_msg, "ERROR")

    def stop_script(self, script_key):
        """FIXED: Stop automation script"""
        try:
            if script_key not in AUTOMATION_SCRIPTS:
                messagebox.showerror("Error", f"Script {script_key} not found")
                return

            script_name = AUTOMATION_SCRIPTS[script_key]['name']

            if messagebox.askyesno("Confirm Stop", f"Stop {script_name}?\n\nThis will terminate the running process."):
                success, message = self.process_manager.kill_process(script_key)

                if success:
                    # Update status label
                    if script_key in self.script_status_labels:
                        self.script_status_labels[script_key].config(text="⚪ Ready",
                                                                     fg=self.theme_colors['secondary_text'])

                    # Show toast notification
                    self.show_toast(f"⏹️ {script_name} stopped successfully", 'warning')
                    self.insert_themed_text(self.activity_text, f"⏹ {message}", 'warning')
                else:
                    self.show_toast(f"❌ Failed to stop {script_name}", 'error')
                    self.insert_themed_text(self.activity_text, f"[ERR] {message}", 'error')

        except Exception as e:
                error_msg = f"Failed to stop script {script_key}: {e}"
                messagebox.showerror("Error", error_msg)
                log_message(error_msg, "ERROR")

    def refresh_all_scripts(self):
        """Refresh all script statuses"""
        try:
            processes = self.process_manager.get_processes()

            for script_key in AUTOMATION_SCRIPTS.keys():
                if script_key in self.script_status_labels:
                    if script_key in processes and processes[script_key]['status'] == 'Running':
                        self.script_status_labels[script_key].config(text="🟢 Running", fg=self.theme_colors['success'])
                    else:
                        self.script_status_labels[script_key].config(text="⚪ Ready",
                                                                     fg=self.theme_colors['secondary_text'])

            self.insert_themed_text(self.activity_text, "🔄 Script statuses refreshed", 'info')

        except Exception as e:
            log_message(f"Error refreshing scripts: {e}", "ERROR")

    def stop_all_scripts(self):
        """Stop all running scripts"""
        try:
            processes = self.process_manager.get_processes()
            running_count = len([p for p in processes.values() if p['status'] == 'Running'])

            if running_count == 0:
                messagebox.showinfo("Info", "No scripts are currently running")
                return

            if messagebox.askyesno("Confirm Stop All", f"Stop all {running_count} running scripts?"):
                count = self.process_manager.kill_all()

                # Update all status labels
                for script_key in AUTOMATION_SCRIPTS.keys():
                    if script_key in self.script_status_labels:
                        self.script_status_labels[script_key].config(text="⚪ Ready",
                                                                     fg=self.theme_colors['secondary_text'])

                messagebox.showinfo("Success", f"Successfully stopped {count} scripts")
                self.insert_themed_text(self.activity_text, f"⏹ Stopped {count} scripts", 'warning')

        except Exception as e:
                error_msg = f"Error stopping all scripts: {e}"
                messagebox.showerror("Error", error_msg)
                log_message(error_msg, "ERROR")

    def refresh_dashboard(self):
        """Refresh dashboard metrics and record historical data"""
        try:
            self.update_dashboard_metrics()
            
            # Record current system metrics to historical database
            system_data = self.system_monitor.get_data()
            historical_data.record_system_metrics(system_data)
            
            self.insert_themed_text(self.activity_text, "📊 Dashboard refreshed - Data recorded to history", 'info')
        except Exception as e:
            log_message(f"Error refreshing dashboard: {e}", "ERROR")

    def export_space_report(self):
        """Export disk space analysis to text file"""
        try:
            # Get current file list from filtered_files
            if not hasattr(self, 'filtered_files') or not self.filtered_files:
                messagebox.showinfo("No Data", "No files to export. Please scan for large files first.")
                return
            
            file_count = len(self.filtered_files)
            
            # Create report
            report_lines = []
            report_lines.append("=" * 80)
            report_lines.append("DISK SPACE ANALYSIS REPORT")
            report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            report_lines.append("=" * 80)
            report_lines.append("")
            
            # Add file list
            report_lines.append(f"LARGE FILES FOUND: {file_count}")
            report_lines.append("-" * 80)
            for file_info in self.filtered_files:
                size_mb = file_info['size_mb']
                path = file_info['path']
                report_lines.append(f"{size_mb:6.1f} MB - {path}")
            
            report_lines.append("")
            report_lines.append("=" * 80)
            report_lines.append("END OF REPORT")
            
            # Save to file
            filename = f"disk_space_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, 'w') as f:
                f.write('\n'.join(report_lines))
            
            messagebox.showinfo("Export Complete", f"Report saved to:\n{filename}")
            log_message(f"Disk space report exported to {filename}", "INFO")
            
        except Exception as e:
            messagebox.showerror("Export Error", f"Failed to export report: {e}")

    def perform_deep_analysis(self):
        """Actually perform the deep analysis"""
        results = {
            'total_files': 0,
            'total_size': 0,
            'largest_files': [],
            'file_type_breakdown': {},
            'duplicate_files': [],
            'recommendations': []
        }
        
        # Analyze user directory
        user_path = f"/users/{self.get_user_from_config()}"
        if not os.path.exists(user_path):
            user_path = f"/home/{getpass.getuser()}"
        
        for root, dirs, files in os.walk(user_path):
            for file in files:
                try:
                    file_path = os.path.join(root, file)
                    if os.path.exists(file_path):
                        size = os.path.getsize(file_path)
                        results['total_files'] += 1
                        results['total_size'] += size
                        
                        # Track large files
                        if size > 10 * 1024 * 1024:  # > 10MB
                            results['largest_files'].append({
                                'path': file_path,
                                'size_mb': size / (1024 * 1024)
                            })
                        
                        # File type breakdown
                        ext = os.path.splitext(file)[1].lower()
                        if ext:
                            results['file_type_breakdown'][ext] = results['file_type_breakdown'].get(ext, 0) + size
                            
                except (OSError, PermissionError):
                    continue
        
        # Sort largest files
        results['largest_files'].sort(key=lambda x: x['size_mb'], reverse=True)
        results['largest_files'] = results['largest_files'][:20]  # Top 20
        
        # Generate recommendations
        total_gb = results['total_size'] / (1024**3)
        if total_gb > 50:
            results['recommendations'].append("Consider moving large files to external storage")
        if len(results['largest_files']) > 10:
            results['recommendations'].append("Review and delete unnecessary large files")
        
        return results

    def show_disk_details(self, category, percentage, system_data):
        """Show detailed breakdown when pie chart slice is clicked"""
        try:
            details_window = tk.Toplevel(self.root)
            details_window.title(f"Disk Details - {category}")
            details_window.geometry("600x400")
            details_window.configure(bg=self.theme_colors['bg'])
            
            # Center window
            details_window.update_idletasks()
            x = (details_window.winfo_screenwidth() // 2) - (600 // 2)
            y = (details_window.winfo_screenheight() // 2) - (400 // 2)
            details_window.geometry(f"600x400+{x}+{y}")
            
            # Header
            header = tk.Label(details_window, text=f"📊 {category} Details",
                            font=('Arial', 14, 'bold'),
                            bg=self.theme_colors['bg'],
                            fg=self.theme_colors['primary_text'])
            header.pack(pady=10)
            
            # Content frame
            content_frame = tk.Frame(details_window, bg=self.theme_colors['card_bg'])
            content_frame.pack(fill='both', expand=True, padx=20, pady=10)
            
            # Details text
            text_widget = tk.Text(content_frame, bg=self.theme_colors['display_bg'],
                                fg=self.theme_colors['display_text'],
                                font=('Courier', 10), wrap='word')
            text_widget.pack(fill='both', expand=True, padx=10, pady=10)
            
            # Get disk info
            import shutil
            total, used, free = shutil.disk_usage("/")
            total_gb = total / (1024**3)
            category_gb = (percentage / 100) * total_gb
            
            details = f"""Category: {category}
Percentage: {percentage:.1f}%
Size: {category_gb:.2f} GB

"""
            
            if category == "User Files":
                user_path = f"/users/{self.get_user_from_config()}"
                details += f"Location: {user_path}\n\n"
                
                # Get largest files with full paths
                largest_files = system_data.get('largest_files', [])[:10]
                if largest_files:
                    details += "Largest files in your directory:\n"
                    details += "=" * 60 + "\n\n"
                    for i, file_info in enumerate(largest_files, 1):
                        size_mb = file_info.get('size_mb', 0)
                        path = file_info.get('path', 'Unknown')
                        # Show relative path from user directory
                        if path.startswith(user_path):
                            rel_path = path[len(user_path)+1:]
                        else:
                            rel_path = path
                        details += f"{i}. {rel_path}\n"
                        details += f"   Size: {size_mb:.1f} MB\n\n"
                else:
                    details += "No large files found (files > 10 MB)\n"
                    details += "\nTip: Run 'Deep Analysis' in Space Analyzer\n"
                    details += "to find all large files in your directory."
                    
            elif category == "System Files":
                # Get actual directory sizes using du -h (human readable)
                import subprocess
                log_message(f"[SYSTEM] User clicked System Files disk details", "SYSTEM")
                
                # Get user directory from config or use default
                user_dir = '/users/paruljot'
                if hasattr(self, 'config') and 'remote_server' in self.config:
                    user_dir = self.config['remote_server'].get('user_directory', '/users/paruljot')
                
                details = f"""Category: {category}
Percentage: {percentage:.1f}%
Size: {category_gb:.2f} GB

🔍 Analyzing directory: {user_dir}
{"=" * 60}

"""
                # Show initial message
                text_widget.config(state='normal')
                text_widget.delete('1.0', tk.END)
                text_widget.insert('1.0', details)
                text_widget.config(state='disabled')
                text_widget.update()
                
                # Now calculate sizes for subdirectories
                details = f"""Category: {category}
Percentage: {percentage:.1f}%
Size: {category_gb:.2f} GB

📁 Directory Breakdown for {user_dir}:
{"=" * 60}

"""
                # Get subdirectories in user_dir
                try:
                    import os
                    subdirs = []
                    for item in os.listdir(user_dir):
                        item_path = os.path.join(user_dir, item)
                        if os.path.isdir(item_path):
                            subdirs.append(item_path)
                    
                    # Calculate size for each subdirectory
                    dir_sizes = []
                    for dir_path in subdirs:
                        try:
                            result = subprocess.run(['du', '-sh', dir_path], 
                                                  capture_output=True, text=True, timeout=10)
                            if result.returncode == 0 and result.stdout.strip():
                                parts = result.stdout.strip().split()
                                if len(parts) >= 1:
                                    size = parts[0]
                                    dir_name = os.path.basename(dir_path)
                                    dir_sizes.append((dir_name, size))
                                    log_message(f"[SYSTEM] {dir_name}: {size}", "SYSTEM")
                        except Exception as e:
                            log_message(f"[SYSTEM] Error calculating {dir_path}: {e}", "ERROR")
                    
                    # Sort by size (convert to bytes for sorting)
                    def size_to_bytes(size_str):
                        """Convert du -h output to bytes for sorting"""
                        size_str = size_str.strip()
                        if size_str.endswith('K'):
                            return float(size_str[:-1]) * 1024
                        elif size_str.endswith('M'):
                            return float(size_str[:-1]) * 1024 * 1024
                        elif size_str.endswith('G'):
                            return float(size_str[:-1]) * 1024 * 1024 * 1024
                        else:
                            return float(size_str)
                    
                    dir_sizes.sort(key=lambda x: size_to_bytes(x[1]), reverse=True)
                    
                    # Display sorted results
                    for dir_name, size in dir_sizes:
                        details += f"{dir_name.ljust(30)} : {size:>10}\n"
                    
                    if not dir_sizes:
                        details += "No subdirectories found\n"
                        
                except Exception as e:
                    details += f"Error listing directories: {e}\n"
                    log_message(f"[SYSTEM] Error: {e}", "ERROR")
                
                details += "\n💡 Cleanup Recommendations:\n"
                details += "- Package cache: sudo apt-get clean\n"
                details += "- Old logs: sudo journalctl --vacuum-time=7d\n"
                details += "- Temp files: sudo rm -rf /tmp/*\n"
                
            elif category == "Free Space":
                details += f"Available space: {category_gb:.2f} GB\n\n"
                if percentage < 20:
                    details += "⚠️ WARNING: Low disk space!\n"
                    details += "Recommendations:\n"
                    details += "- Delete unnecessary files\n"
                    details += "- Clear package cache\n"
                    details += "- Remove old log files\n"
                elif percentage < 40:
                    details += "ℹ️ Disk space is getting low.\n"
                    details += "Consider cleanup soon.\n"
                else:
                    details += "✅ Sufficient free space available.\n"
            
            # Update text widget with final content
            text_widget.config(state='normal')
            text_widget.delete('1.0', tk.END)
            text_widget.insert('1.0', details)
            text_widget.config(state='disabled')
            
            # Action buttons
            button_frame = tk.Frame(details_window, bg=self.theme_colors['bg'])
            button_frame.pack(pady=10)
            
            def copy_to_clipboard():
                self.root.clipboard_clear()
                self.root.clipboard_append(details)
                messagebox.showinfo("Copied", "Details copied to clipboard!")
            
            def export_to_file():
                filename = f"disk_details_{category.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                with open(filename, 'w') as f:
                    f.write(details)
                messagebox.showinfo("Exported", f"Details exported to:\n{filename}")
            
            tk.Button(button_frame, text="📋 Copy", command=copy_to_clipboard,
                     bg=self.theme_colors['info'], fg='white',
                     font=('Arial', 10, 'bold'), padx=15, pady=8).pack(side='left', padx=5)
            
            tk.Button(button_frame, text="💾 Export", command=export_to_file,
                     bg=self.theme_colors['success'], fg='white',
                     font=('Arial', 10, 'bold'), padx=15, pady=8).pack(side='left', padx=5)
            
            tk.Button(button_frame, text="Close", command=details_window.destroy,
                     bg=self.theme_colors['secondary_text'], fg='white',
                     font=('Arial', 10, 'bold'), padx=20, pady=8).pack(side='left', padx=5)
            
        except Exception as e:
            log_message(f"Error showing disk details: {e}", "ERROR")
            messagebox.showerror("Error", f"Failed to show details: {e}")
    
    def show_analysis_results(self, results):
        """Display deep analysis results"""
        total_gb = results['total_size'] / (1024**3)
        
        report = f"""🔍 DEEP ANALYSIS RESULTS
        
📊 OVERVIEW:
- Total Files: {results['total_files']:,}
- Total Size: {total_gb:.2f} GB
- Large Files (>10MB): {len(results['largest_files'])}

📁 TOP LARGE FILES:
"""
        
        for i, file_info in enumerate(results['largest_files'][:10], 1):
            filename = os.path.basename(file_info['path'])
            report += f"{i:2d}. {file_info['size_mb']:6.1f} MB - {filename}\n"
        
        if results['recommendations']:
            report += "\n💡 RECOMMENDATIONS:\n"
            for i, rec in enumerate(results['recommendations'], 1):
                report += f"{i}. {rec}\n"
        
        # Show in a new window
        result_window = tk.Toplevel(self.root)
        result_window.title("Deep Analysis Results")
        result_window.geometry("600x500")
        result_window.configure(bg=self.theme_colors['bg'])
        
        text_widget = tk.Text(result_window, bg=self.theme_colors['display_bg'],
                            fg=self.theme_colors['display_text'], font=('Courier', 10),
                            wrap='word')
        text_widget.pack(fill='both', expand=True, padx=10, pady=10)
        text_widget.insert('1.0', report)
        text_widget.config(state='disabled')
    def apply_space_filters(self):
        """Apply size and type filters to space analyzer - FIXED: Persistent filters"""
        try:
            size_threshold = int(self.size_threshold_var.get())
            file_type = self.file_type_filter_var.get()
            
            self.insert_themed_text(self.directory_stats, 
                                  f"🔍 Applying filters: >{size_threshold}MB, Type: {file_type}", 'info')
            
            # Get current file data
            system_data = self.system_monitor.get_data()
            all_files = system_data.get('largest_files', [])
            
            # Apply filters
            filtered_files = []
            for file_info in all_files:
                size_mb = file_info.get('size_mb', 0)
                file_path = file_info.get('path', '').lower()
                
                # Size filter
                if size_mb < size_threshold:
                    continue
                
                # Type filter
                if file_type != "All":
                    if file_type == "PDF" and not file_path.endswith('.pdf'):
                        continue
                    elif file_type == "PPT" and not (file_path.endswith('.ppt') or file_path.endswith('.pptx')):
                        continue
                    elif file_type == "DOC" and not (file_path.endswith('.doc') or file_path.endswith('.docx')):
                        continue
                    elif file_type == "XLS" and not (file_path.endswith('.xls') or file_path.endswith('.xlsx')):
                        continue
                    elif file_type == "IMG" and not any(file_path.endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']):
                        continue
                    elif file_type == "VIDEO" and not any(file_path.endswith(ext) for ext in ['.mp4', '.avi', '.mov', '.mkv']):
                        continue
                    elif file_type == "ARCHIVE" and not any(file_path.endswith(ext) for ext in ['.zip', '.rar', '.7z', '.tar']):
                        continue
                
                filtered_files.append(file_info)
            
            # Store filtered results to prevent auto-refresh from clearing
            self.space_filter_active = True
            self.filtered_files = filtered_files
            
            # Update display with filtered results
            self.files_listbox.delete(0, tk.END)
            for file_info in filtered_files:
                size_mb = file_info['size_mb']
                path = file_info['path']
                display_text = f"{size_mb:6.1f} MB - {path}"
                self.files_listbox.insert(tk.END, display_text)
            
            self.insert_themed_text(self.directory_stats, 
                                  f"✅ Filter applied: {len(filtered_files)} files match criteria", 'success')
            
        except Exception as e:
            messagebox.showerror("Filter Error", f"Failed to apply filters: {e}")
    
    def search_logs(self):
        """Search through log files for specific terms - FIXED: Results persist"""
        try:
            search_term = self.log_search_var.get().strip()
            if not search_term:
                messagebox.showwarning("Search", "Please enter a search term")
                return
            
            # Store search results to prevent them from being overwritten
            # Search results will be shown in main debug display
            
            # Search through log files
            log_file = os.path.join("logs", "professional_launcher.log")
            matches_found = 0
            search_results = []
            
            if os.path.exists(log_file):
                with open(log_file, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    
                    for i, line in enumerate(lines):
                        if search_term.lower() in line.lower():
                            matches_found += 1
                            search_results.append(f"Line {i+1}: {line.strip()}")
                            if matches_found >= 10:  # Limit results
                                break
                
                # Display results in main debug display
                if matches_found == 0:
                    result_text = f"No matches found for '{search_term}'"
                    self.search_status_label.config(text=result_text, fg=self.theme_colors['warning'])
                else:
                    # Show results in main debug display
                    self.debug_display.config(state='normal')
                    self.debug_display.delete(1.0, tk.END)
                    
                    # Add header
                    header = f"🔍 Search Results for '{search_term}' ({matches_found} matches):\n" + "="*50
                    self.insert_themed_text(self.debug_display, header, 'highlight')
                    
                    # Add results
                    for result in search_results:
                        self.insert_themed_text(self.debug_display, result, 'info')
                    
                    # Add footer
                    footer = f"\n✅ Search completed - {matches_found} matches found"
                    self.insert_themed_text(self.debug_display, footer, 'success')
                    
                    self.debug_display.config(state='disabled')
                    self.search_status_label.config(text=f"Found {matches_found} matches", fg=self.theme_colors['success'])
                
                self.search_results_active = True  # Flag to prevent auto-refresh from clearing
                
        except Exception as e:
                messagebox.showerror("Search Error", f"Failed to search logs: {e}")
    
    def clear_search_results(self):
        """Clear search results and restore normal log analysis"""
        try:
                self.search_results_active = False
                self.last_search_results = ""
                self.log_search_var.set("")  # Clear search field
                
                # Restore normal debug display
                self.refresh_debug_logs()
                self.search_status_label.config(text="Search results cleared", fg=self.theme_colors['info'])
                
        except Exception as e:
                messagebox.showerror("Error", f"Failed to clear search results: {e}")
    
    def quick_system_cleanup(self):
        """FIXED: Perform actual quick system cleanup with DETAILED LIST"""
        try:
            self.insert_themed_text(self.events_text, "🧹 Starting quick system cleanup...", 'info')
            
            cleaned_items = []
            
            # Clean application temp files and logs
            logs_dir = "logs"
            if os.path.exists(logs_dir):
                for file in os.listdir(logs_dir):
                    if file.endswith('.tmp') or (file.startswith('debug_') and file.endswith('.log')):
                        try:
                            file_path = os.path.join(logs_dir, file)
                            # Only remove files older than 1 day
                            if os.path.getmtime(file_path) < time.time() - 86400:
                                os.remove(file_path)
                                cleaned_items.append(f"Old log: {file}")
                        except:
                            pass
            
            # Clean Python cache files
            for root, dirs, files in os.walk('.'):
                if '__pycache__' in dirs:
                    try:
                        import shutil
                        cache_path = os.path.join(root, '__pycache__')
                        shutil.rmtree(cache_path)
                        cleaned_items.append(f"Cache: {cache_path}")
                    except:
                        pass
                for file in files:
                    if file.endswith('.pyc'):
                        try:
                            pyc_path = os.path.join(root, file)
                            os.remove(pyc_path)
                            cleaned_items.append(f"Compiled: {file}")
                        except:
                            pass
            
            # Show detailed list
            self.insert_themed_text(self.events_text, 
                                  f"✅ Cleanup completed: {len(cleaned_items)} items removed", 'success')
            if cleaned_items:
                for item in cleaned_items[:10]:  # Show first 10
                    self.insert_themed_text(self.events_text, f"  - {item}", 'info')
                if len(cleaned_items) > 10:
                    self.insert_themed_text(self.events_text, 
                                          f"  ... and {len(cleaned_items)-10} more items", 'info')
            
            # Update system metrics after cleanup
            self.refresh_dashboard()
            
        except Exception as e:
            self.insert_themed_text(self.events_text, f"[ERR] Cleanup failed: {e}", 'error')
    
    def auto_fix_issues(self):
        """FIXED: Automatically fix common system issues with DETAILED reporting"""
        try:
            self.insert_themed_text(self.events_text, "🔧 Scanning for common issues...", 'info')
            
            fixes_applied = 0
            fix_details = []
            
            # 1. Check and fix logs directory
            logs_dir = "logs"
            if not os.path.exists(logs_dir):
                try:
                    os.makedirs(logs_dir, 0o755)
                    fixes_applied += 1
                    fix_details.append("Created missing logs directory")
                    self.insert_themed_text(self.events_text, "✅ Created logs directory", 'success')
                except Exception as e:
                    self.insert_themed_text(self.events_text, f"[ERR] Failed to create logs dir: {e}", 'error')
            
            # 2. Check for corrupted config files
            config_file = "master_config.json"
            if os.path.exists(config_file):
                try:
                    with open(config_file, 'r') as f:
                        json.load(f)  # Test if valid JSON
                except json.JSONDecodeError:
                    try:
                        # Backup corrupted file and create new one
                        backup_name = "config_file.backup_{int(time.time())}"
                        os.rename(config_file, backup_name)
                        
                        # Create minimal valid config
                        default_config = {"remote_server": [], "nodes": []}
                        with open(config_file, 'w') as f:
                            json.dump(default_config, f, indent=2)
                        
                        fixes_applied += 1
                        fix_details.append(f"Fixed corrupted config file (backup: {backup_name})")
                        self.insert_themed_text(self.events_text, "✅ Fixed corrupted config file", 'success')
                    except Exception as e:
                        self.insert_themed_text(self.events_text, f"[ERR] Config fix failed: {e}", 'error')
            
            # 3. Check for stuck processes
            try:
                import psutil
                current_pid = os.getpid()
                python_processes = []
                for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                    if proc.info['name'] == 'python3' and proc.info['pid'] != current_pid:
                        cmdline = ' '.join(proc.info['cmdline'] or [])
                        if 'professional_multitheme_launcher' in cmdline:
                            python_processes.append(proc.info['pid'])
                
                if python_processes:
                    self.insert_themed_text(self.events_text, 
                                          f"⚠️ Found {len(python_processes)} other launcher processes", 'warning')
                    fix_details.append(f"Detected {len(python_processes)} duplicate processes")
            except ImportError:
                pass  # psutil not available
            
            # 4. Summary
            if fixes_applied > 0:
                self.insert_themed_text(self.events_text, 
                                      f"✅ Auto-fix completed: {fixes_applied} issues resolved", 'success')
                for detail in fix_details:
                    self.insert_themed_text(self.events_text, f"  - {detail}", 'info')
            else:
                self.insert_themed_text(self.events_text, "✅ No issues found - system healthy", 'success')
            
            # Update system metrics
            self.refresh_dashboard()
            
        except Exception as e:
            self.insert_themed_text(self.events_text, f"[ERR] Auto-fix failed: {e}", 'error')
            
            # Check and restart system monitoring if needed
            if hasattr(self, 'system_monitor'):
                if not self.system_monitor.running:
                    self.system_monitor.start()
                    fixes_applied += 1
                    fix_details.append("Restarted system monitoring service (was stopped)")
                    self.insert_themed_text(self.events_text, "✅ Restarted system monitoring", 'success')
            
            # Check for orphaned log files and clean them
            try:
                import glob
                orphaned_logs = glob.glob("*.log")
                temp_files = glob.glob("*.tmp") + glob.glob("*.temp")
                all_cleanup = orphaned_logs + temp_files
                
                if all_cleanup:
                    cleaned_count = 0
                    for cleanup_file in all_cleanup:
                        try:
                            file_size = os.path.getsize(cleanup_file)
                            os.remove(cleanup_file)
                            cleaned_count += 1
                            fixes_applied += 1
                            fix_details.append(f"Removed orphaned file: {cleanup_file} ({file_size} bytes)")
                        except:
                            pass
                    
                    if cleaned_count > 0:
                        self.insert_themed_text(self.events_text, f"✅ Cleaned {cleaned_count} orphaned files", 'success')
            except:
                pass
            
            # Check network monitor health
            if hasattr(self, 'network_monitor'):
                if not self.network_monitor.running:
                    try:
                        self.network_monitor.start()
                        fixes_applied += 1
                        fix_details.append("Restarted network connection monitoring (was stopped)")
                        self.insert_themed_text(self.events_text, "✅ Restarted network monitoring", 'success')
                    except:
                        pass
            
            # Report results with DETAILED breakdown
            if fixes_applied == 0:
                self.insert_themed_text(self.events_text, "✅ No issues found - system healthy", 'success')
                fix_details.append("System scan completed - no issues detected")
            else:
                self.insert_themed_text(self.events_text, 
                                      f"🔧 Applied {fixes_applied} fixes:", 'success')
                for i, detail in enumerate(fix_details, 1):
                    self.insert_themed_text(self.events_text, f"  {i}. {detail}", 'info')
                
                # Add summary
                self.insert_themed_text(self.events_text, 
                                      f"📊 Fix Summary: {fixes_applied} issues resolved successfully", 'highlight')
            
        except Exception as e:
            self.insert_themed_text(self.events_text, f"[ERR] Auto-fix failed: {e}", 'error')

    def system_health_check(self):
        """Perform comprehensive system health check"""
        try:
                self.insert_themed_text(self.events_text, "📊 Running system health check...", 'info')
                
                system_data = self.system_monitor.get_data()
                health_score = 100
                issues = []
                
                # Check CPU usage
                cpu_percent = system_data.get('cpu_percent', 0)
                if cpu_percent > 80:
                    health_score -= 20
                    issues.append(f"High CPU usage: {cpu_percent:.1f}%")
                
                # Check memory usage
                memory_percent = system_data.get('memory_percent', 0)
                if memory_percent > 85:
                    health_score -= 25
                    issues.append(f"High memory usage: {memory_percent:.1f}%")
                
                # Check disk space
                disk_percent = system_data.get('user_disk_usage', 0)
                if disk_percent > 90:
                    health_score -= 30
                    issues.append(f"Low disk space: {disk_percent:.1f}% used")
                
                # Check log file sizes
                log_file = os.path.join("logs", "professional_launcher.log")
                if os.path.exists(log_file):
                    log_size_mb = os.path.getsize(log_file) / (1024 * 1024)
                    if log_size_mb > 50:
                        health_score -= 10
                        issues.append(f"Large log file: {log_size_mb:.1f}MB")
                
                # Display results
                if health_score >= 90:
                    status = "EXCELLENT"
                    color = 'success'
                elif health_score >= 70:
                    status = "GOOD"
                    color = 'info'
                elif health_score >= 50:
                    status = "FAIR"
                    color = 'warning'
                else:
                    status = "POOR"
                    color = 'error'
                
                self.insert_themed_text(self.events_text, 
                                      f"📊 Health Score: {health_score}/100 - {status}", color)
                
                if issues:
                    self.insert_themed_text(self.events_text, "\n⚠️ Issues found:", 'warning')
                    for issue in issues:
                        self.insert_themed_text(self.events_text, f"  - {issue}", 'warning')
                else:
                    self.insert_themed_text(self.events_text, "✅ No issues detected", 'success')
                
        except Exception as e:
                self.insert_themed_text(self.events_text, f"[ERR] Health check failed: {e}", 'error')
    
    def toggle_always_on_top(self):
        """Toggle always on top window setting"""
        try:
                is_on_top = self.always_on_top_var.get()
                self.root.attributes('-topmost', is_on_top)
                status = "enabled" if is_on_top else "disabled"
                log_message(f"Always on top {status}", "SETTINGS")
        except Exception as e:
                log_message(f"Error toggling always on top: {e}", "ERROR")

    def clean_temp_files(self):
        """Clean temporary files"""
        try:
                if messagebox.askyesno("Confirm Cleanup",
                                       "Clean temporary files?\n\nThis will remove .tmp, .temp files older than 7 days."):
                    cleaned_count = 0

                    user_dir = f"/users/{get_current_username()}"
                    if os.path.exists(user_dir):
                        cutoff_date = datetime.now() - timedelta(days=7)

                        for root, dirs, files in os.walk(user_dir):
                            for file in files:
                                if file.endswith(('.tmp', '.temp')):
                                    try:
                                        filepath = os.path.join(root, file)
                                        file_time = datetime.fromtimestamp(os.path.getmtime(filepath))
                                        if file_time < cutoff_date:
                                            os.remove(filepath)
                                            cleaned_count += 1
                                    except:
                                        continue

                    messagebox.showinfo("Cleanup Complete", f"Cleaned {cleaned_count} temporary files")
                    self.insert_themed_text(self.directory_stats, f"🧹 Cleaned {cleaned_count} files", 'success')

        except Exception as e:
                log_message(f"Error cleaning temp files: {e}", "ERROR")
                messagebox.showerror("Error", f"Cleanup failed: {e}")

    def delete_selected_file(self):
        """Delete selected large file"""
        try:
                selection = self.files_listbox.curselection()
                if not selection:
                    messagebox.showwarning("Warning", "Please select a file to delete")
                    return

                system_data = self.system_monitor.get_data()
                largest_files = system_data.get('largest_files', [])

                if selection[0] < len(largest_files):
                    file_info = largest_files[selection[0]]
                    filepath = file_info['full_path']

                    if messagebox.askyesno("Confirm Delete",
                                           f"Delete file?\n\n{file_info['path']}\nSize: {file_info['size_mb']:.1f} MB\n\nThis action cannot be undone."):
                        success = self.system_monitor.delete_large_file(filepath)

                        if success:
                            messagebox.showinfo("Success", "File deleted successfully")
                            self.deep_space_analysis()
                            self.insert_themed_text(self.directory_stats, f"🗑️ Deleted: {file_info['path']}", 'success')
                        else:
                            messagebox.showerror("Error", "Failed to delete file")

        except Exception as e:
                log_message(f"Error deleting file: {e}", "ERROR")
                messagebox.showerror("Error", f"Delete failed: {e}")

    def open_file_location(self):
        """Open selected file location - FIXED: Works with checkbox system"""
        try:
                # Get selected files from checkbox system
                if not hasattr(self, 'file_vars') or not self.file_vars:
                    messagebox.showwarning("Warning", "No files available")
                    return
                
                selected_paths = [path for path, var in self.file_vars.items() if var.get()]
                
                if not selected_paths:
                    messagebox.showwarning("Warning", "Please select at least one file by checking its checkbox")
                    return
                
                # Open location of first selected file
                filepath = selected_paths[0]
                
                if not os.path.exists(filepath):
                    messagebox.showerror("Error", "File no longer exists")
                    return
                
                directory = os.path.dirname(filepath)
                
                if not os.path.exists(directory):
                    messagebox.showerror("Error", f"Directory not found: {directory}")
                    return

                if platform.system().lower() == 'windows':
                    os.startfile(directory)
                elif platform.system().lower() == 'darwin':
                    subprocess.run(['open', directory])
                else:
                    # Use file manager for Linux
                    try:
                        subprocess.run(['xdg-open', directory], check=False)
                    except:
                        subprocess.run(['nautilus', directory], check=False)
                
                messagebox.showinfo("Success", f"Opened location:\n{directory}")

        except Exception as e:
                log_message(f"Error opening file location: {e}", "ERROR")
                messagebox.showerror("Error", f"Failed to open location: {str(e)}")

    def refresh_processes(self):
        """Refresh process list"""
        try:
                self.update_processes_display()
                self.insert_themed_text(self.processes_text, "🔄 Process list refreshed", 'info')
        except Exception as e:
                log_message(f"Error refreshing processes: {e}", "ERROR")

    def kill_all_processes(self):
        """Kill all tracked processes"""
        try:
                processes = self.process_manager.get_processes()
                running_count = len([p for p in processes.values() if p['status'] == 'Running'])

                if running_count == 0:
                    messagebox.showinfo("Info", "No processes to kill")
                    return

                if messagebox.askyesno("Confirm Kill All", f"Kill all {running_count} tracked processes?"):
                    count = self.process_manager.kill_all()
                    messagebox.showinfo("Success", f"Killed {count} processes")
                    self.update_processes_display()

        except Exception as e:
                log_message(f"Error killing all processes: {e}", "ERROR")
                messagebox.showerror("Error", f"Failed to kill processes: {e}")

    def manual_kill_pid(self):
        """Manual PID kill with safety checks"""
        try:
                pid_text = self.pid_entry.get().strip()
                if not pid_text:
                    messagebox.showwarning("Warning", "Please enter a Process ID")
                    return

                try:
                    pid = int(pid_text)
                except ValueError:
                    messagebox.showerror("Error", "Invalid Process ID. Must be a number.")
                    return

                if messagebox.askyesno("Confirm Force Kill", f"Force kill process PID {pid}?\n\n⚠️ This is irreversible."):
                    success, message = self.process_manager.kill_process_by_pid(pid)

                    if success:
                        messagebox.showinfo("Success", message)
                        self.pid_entry.delete(0, tk.END)
                        self.update_processes_display()
                        self.insert_themed_text(self.processes_text, f"💀 Manual kill: {message}", 'warning')
                    else:
                        messagebox.showerror("Error", message)
                        self.insert_themed_text(self.processes_text, f"[ERR] Kill failed: {message}", 'error')

        except Exception as e:
                log_message(f"Error in manual PID kill: {e}", "ERROR")
                messagebox.showerror("Error", f"Manual kill failed: {e}")

    def refresh_system_info(self):
        """Refresh system information"""
        try:
                self.update_system_display()
                self.insert_themed_text(self.system_display, "🔄 System information refreshed", 'info')
        except Exception as e:
                log_message(f"Error refreshing system info: {e}", "ERROR")

    def show_performance_tips(self):
        """Show performance optimization tips"""
        tips = """🎯 SYSTEM PERFORMANCE OPTIMIZATION TIPS:

🚀 CPU Optimization:
- Close unnecessary applications and browser tabs
- Check for high CPU processes in Process Manager
- Consider upgrading if consistently above 80%

🧠 Memory Management:
- Restart applications periodically to clear memory leaks
- Close unused browser tabs and applications
- Clear system cache and temporary files

💾 Disk Space Management:
- Use the Space Analyzer to identify large files
- Clean temporary files regularly
- Move old files to external storage

⚙️ General Performance:
- Keep system updated with latest patches
- Run disk cleanup and defragmentation
- Monitor background processes for resource usage"""

        # Create performance tips window
        tips_window = tk.Toplevel(self.root)
        tips_window.title("Performance Tips")
        tips_window.geometry("800x600")
        tips_window.configure(bg=self.theme_colors['bg'])

        tips_text = self.create_themed_text_widget(tips_window, height=25)
        tips_text.pack(fill='both', expand=True, padx=20, pady=20)

        self.insert_themed_text(tips_text, tips, 'info')

    def refresh_debug_logs(self):
        """Refresh debug logs display - reload from file"""
        try:
                # Reset the cleared flag when manually refreshing
                if hasattr(self, 'logs_cleared'):
                    self.logs_cleared = False
                
                # Reset filter flags to show all logs
                if hasattr(self, 'filters_active'):
                    self.filters_active = False
                if hasattr(self, 'search_results_active'):
                    self.search_results_active = False
                
                # Call update_debug_logs which reads from file
                self.update_debug_logs()
                
                log_message("🔄 Debug logs refreshed", "INFO")
        except Exception as e:
                log_message(f"Error refreshing debug logs: {e}", "ERROR")

    def clear_debug_display(self):
        """Clear the debug display window only"""
        try:
            if messagebox.askyesno("Clear Display", "Clear the debug log display?\n(Log files will NOT be deleted)"):
                # Set flag to prevent auto-refresh from overwriting
                self.logs_cleared = True
                self.debug_display.config(state='normal')
                self.debug_display.delete(1.0, tk.END)
                self.debug_display.config(state='disabled')
                self.insert_themed_text(self.debug_display, "✅ Display cleared - logs still saved to files\n💡 Click 'Refresh Logs' to reload", 'success')
        except Exception as e:
            log_message(f"Error clearing display: {e}", "ERROR")
    
    def delete_selected_log_file(self):
        """Delete the selected log file"""
        try:
            selection = self.log_files_listbox.curselection()
            if not selection:
                messagebox.showwarning("No Selection", "Please select a log file to delete")
                return
            
            log_file_path = self.log_files_listbox.get(selection[0])
            
            if messagebox.askyesno("Delete Log File", f"Permanently delete this log file?\n\n{os.path.basename(log_file_path)}\n\nThis cannot be undone!"):
                if os.path.exists(log_file_path):
                    os.remove(log_file_path)
                    messagebox.showinfo("Deleted", f"Log file deleted:\n{os.path.basename(log_file_path)}")
                    self.update_debug_logs()
                else:
                    messagebox.showerror("Error", "Log file not found")
        except Exception as e:
            log_message(f"Error deleting log file: {e}", "ERROR")
            messagebox.showerror("Error", f"Failed to delete log file: {e}")
    
    def clean_old_logs(self):
        """Delete old log files from disk"""
        try:
                retention_days = app_settings['log_retention_days']

                if messagebox.askyesno("Delete Log Files", f"Permanently DELETE log files older than {retention_days} days?\n\nThis cannot be undone!"):
                    cleaned_count = cleanup_old_logs(retention_days)
                    messagebox.showinfo("Deletion Complete", f"Deleted {cleaned_count} old log files from disk")
                    self.update_debug_logs()

        except Exception as e:
                log_message(f"Error deleting old logs: {e}", "ERROR")
                messagebox.showerror("Error", f"Log deletion failed: {e}")

    def manual_connection_check(self):
        """FIXED: Manual network connection check"""
        try:
                if self.network_monitor.force_check():
                    self.insert_themed_text(self.connection_display, "🔄 Manual connection check initiated...", 'info')
                    messagebox.showinfo("Connection Check", "Manual check started.\nResults will appear shortly.")
                else:
                    messagebox.showwarning("Warning", "Connection check already in progress.")

        except Exception as e:
                log_message(f"Error in manual connection check: {e}", "ERROR")
                messagebox.showerror("Error", f"Connection check failed: {e}")

    def apply_settings(self):
        """Apply all settings"""
        try:
                # Performance settings
                app_settings['refresh_interval'] = int(self.refresh_interval_var.get())
                app_settings['node_timeout'] = int(self.timeout_var.get())
                
                # Logging settings
                app_settings['debug_mode'] = self.debug_mode_var.get()
                app_settings['log_retention_days'] = int(self.log_retention_var.get())
                app_settings['auto_cleanup_on_start'] = self.auto_cleanup_var.get()
                
                # Window settings
                app_settings['always_on_top'] = self.always_on_top_var.get()
                app_settings['show_notifications'] = self.notifications_var.get()
                
                # Network settings
                app_settings['health_check_interval'] = int(self.health_interval_var.get())
                app_settings['max_concurrent_checks'] = int(self.max_concurrent_var.get())
                
                # Help settings
                app_settings['show_help_text'] = self.show_help_var.get()

                save_settings()

                messagebox.showinfo("Settings Saved", 
                                  "All settings applied successfully!\n"
                                  "Some changes may require restart to take full effect.")
                log_message("Enhanced settings applied and saved", "SETTINGS")

        except Exception as e:
                log_message(f"Error applying settings: {e}", "ERROR")
                messagebox.showerror("Error", f"Failed to apply settings: {e}")

    def reset_settings(self):
        """Reset settings to defaults"""
        try:
                if messagebox.askyesno("Confirm Reset", "Reset all settings to defaults?"):
                    global app_settings
                    app_settings = {
                        'theme': 'Professional', 'refresh_interval': 5, 'debug_mode': True,
                        'auto_save_logs': True, 'show_notifications': True,
                        'node_timeout': 2, 'log_retention_days': 30, 'encrypt_configs': False,
                        'config_password': '', 'max_log_size_mb': 10, 'auto_cleanup_on_start': True,
                        'show_ip_addresses': True, 'health_check_interval': 60, 'backup_configs': True,
                        'max_concurrent_checks': 3
                    }

                    self.refresh_interval_var.set(str(app_settings['refresh_interval']))
                    self.timeout_var.set(str(app_settings['node_timeout']))

                    save_settings()

                    messagebox.showinfo("Reset Complete", "All settings reset to defaults.")

        except Exception as e:
                log_message(f"Error resetting settings: {e}", "ERROR")
                messagebox.showerror("Error", f"Failed to reset settings: {e}")

    # ========================================================================
    # PERIODIC UPDATE METHODS
    # ========================================================================

    def start_updates(self):
        """Start periodic GUI updates"""
        self.update_dashboard_metrics()
        self.update_processes_display()
        self.update_system_display()
        self.update_connection_display()
        self.update_space_analyzer()
        self.update_debug_logs()

        # Schedule next update
        self.root.after(app_settings['refresh_interval'] * 1000, self.start_updates)

    def update_dashboard_metrics(self):
        """FIXED: Update dashboard with COMPACT metric cards"""
        try:
                system_data = self.system_monitor.get_data()
                
                # Log dashboard update
                log_message(f"[DASHBOARD] Updating metrics - CPU: {system_data['cpu_percent']:.1f}%, Memory: {system_data['memory_percent']:.1f}%", "DASHBOARD")

                # Update CPU card
                cpu_percent = system_data['cpu_percent']
                self.cpu_card.value_label.config(text=f"{cpu_percent:.1f}%")
                if cpu_percent > 80:
                    color = self.theme_colors['metric_critical']
                    log_message(f"[DASHBOARD] CPU usage critical: {cpu_percent:.1f}%", "WARNING")
                elif cpu_percent > 60:
                    color = self.theme_colors['metric_warning']
                else:
                    color = self.theme_colors['metric_good']
                self.cpu_card.value_label.config(fg=color)
                self.cpu_card.status_label.config(fg=color)

                # Update Memory card
                memory_percent = system_data['memory_percent']
                self.memory_card.value_label.config(text=f"{memory_percent:.1f}%")
                if memory_percent > 85:
                    color = self.theme_colors['metric_critical']
                    log_message(f"[DASHBOARD] Memory usage critical: {memory_percent:.1f}%", "WARNING")
                elif memory_percent > 70:
                    color = self.theme_colors['metric_warning']
                else:
                    color = self.theme_colors['metric_good']
                self.memory_card.value_label.config(fg=color)
                self.memory_card.status_label.config(fg=color)

                # Update User Disk card
                user_disk_percent = system_data['user_disk_usage']
                self.user_disk_card.value_label.config(text=f"{user_disk_percent:.1f}%")
                if user_disk_percent > 80:
                    color = self.theme_colors['metric_critical']
                elif user_disk_percent > 60:
                    color = self.theme_colors['metric_warning']
                else:
                    color = self.theme_colors['metric_good']
                self.user_disk_card.value_label.config(fg=color)
                self.user_disk_card.status_label.config(fg=color)

                # Update Processes card
                process_count = system_data['processes']
                self.processes_card.value_label.config(text=str(process_count))

                # Update performance history with explanations
                if hasattr(self, 'performance_text'):
                    current_time = datetime.now().strftime("%H:%M:%S")
                    perf_entry = f"{current_time} - CPU: {cpu_percent:.1f}% | Memory: {memory_percent:.1f}% | Load: {system_data['load_average']:.2f}"
                    self.insert_themed_text(self.performance_text, perf_entry, 'info')

                # Update system events with detailed explanations
                if cpu_percent > 80:
                    self.insert_themed_text(self.events_text,
                                            f"{current_time} - ⚠️ HIGH CPU ALERT: {cpu_percent:.1f}% - System overloaded, close applications",
                                            'error')
                elif memory_percent > 85:
                    self.insert_themed_text(self.events_text,
                                            f"{current_time} - 🔴 HIGH MEMORY ALERT: {memory_percent:.1f}% - RAM nearly full, restart apps",
                                            'error')

                
                if user_disk_percent > 80:
                    self.insert_themed_text(self.events_text,
                                            f"{current_time} - 💾 DISK SPACE WARNING: User directory {user_disk_percent:.1f}% full",
                                            'warning')

        except Exception as e:
                log_message(f"Error updating dashboard metrics: {e}", "ERROR")

    def update_disk_chart(self, system_data):
        """MISSING: Update interactive disk usage chart"""
        try:
            if hasattr(self, 'disk_chart_text'):
                user = get_current_username()
                user_disk_size = system_data.get('user_disk_size', 0)
                user_disk_usage = system_data.get('user_disk_usage', 0)
                
                # Clear previous content
                self.disk_chart_text.config(state='normal')
                self.disk_chart_text.delete(1.0, tk.END)
                
                if user_disk_size > 0:
                    used_gb = user_disk_size / (1024 ** 3)
                    used_percent = user_disk_usage
                    free_percent = 100 - used_percent
                    
                    # Create visual bar chart
                    bar_length = 40
                    used_blocks = int((used_percent / 100) * bar_length)
                    free_blocks = bar_length - used_blocks
                    
                    chart_text = f"""💾 DISK SPACE USAGE - /users/{user}/

🔴 USED: {used_gb:.1f} GB ({used_percent:.1f}%) {'█' * used_blocks}
🟢 FREE: ({free_percent:.1f}%) {'░' * free_blocks}

📊 Visual Chart:
[{'█' * used_blocks}{'░' * free_blocks}] {used_percent:.1f}% Used

📈 Statistics:
- Total Directory Size: {used_gb:.2f} GB
- Usage Percentage: {used_percent:.1f}%
- Status: {"⚠️ High Usage" if used_percent > 80 else "✅ Normal" if used_percent < 60 else "⚡ Moderate"}

💡 Recommendations:
{"- Consider cleanup - usage over 80%" if used_percent > 80 else "- Monitor growth - approaching limit" if used_percent > 60 else "- Disk usage is healthy"}"""
                else:
                    chart_text = f"""💾 DISK SPACE USAGE - /users/{user}/

📊 Calculating disk usage...
🔄 Please wait while system analyzes directory size
⏰ This may take a moment for large directories"""

                self.insert_themed_text(self.disk_chart_text, chart_text, 'info')
                self.disk_chart_text.config(state='disabled')
        except Exception as e:
            log_message(f"Error updating disk chart: {e}", "ERROR")

    def update_processes_display(self):
        """Update processes display with PID explanations"""
        try:
        # Clear display
            self.processes_text.config(state='normal')
            self.processes_text.delete(1.0, tk.END)
            self.processes_text.config(state='disabled')

            processes = self.process_manager.get_processes()

            if not processes:
                self.insert_themed_text(self.processes_text, "No automation processes currently tracked", 'secondary')
            else:
                self.insert_themed_text(self.processes_text, "🏃 TRACKED AUTOMATION PROCESSES:", 'highlight')
                self.insert_themed_text(self.processes_text, "=" * 50, 'primary')

                for script_key, proc_info in processes.items():
                    name = proc_info['name']
                    pid = proc_info['pid']
                    status = proc_info['status']
                    started = proc_info['started'].strftime("%H:%M:%S")

                    if status == 'Running':
                        tag = 'success'
                        status_icon = "🟢"
                    else:
                        tag = 'secondary'
                        status_icon = "⚪"

                    process_line = f"{status_icon} {name} (PID: {pid}) - {status} - Started: {started}"
                    self.insert_themed_text(self.processes_text, process_line, tag)

            # Update process resource chart
            if hasattr(self, 'process_resource_chart') and self.process_resource_chart:
                try:
                    import psutil
                    top_processes = []
                    for proc in psutil.process_iter(['name', 'cpu_percent', 'memory_percent']):
                        try:
                            info = proc.info
                            if info['cpu_percent'] is not None and info['cpu_percent'] > 0:
                                top_processes.append({
                                    'name': info['name'],
                                    'cpu': info['cpu_percent'],
                                    'memory': info['memory_percent'] or 0
                                })
                        except (psutil.NoSuchProcess, psutil.AccessDenied):
                            pass
                    
                    # Sort by CPU and get top 5
                    top_processes.sort(key=lambda x: x['cpu'], reverse=True)
                    top_processes = top_processes[:5]
                    
                    if top_processes:
                        chart_data = {'top_processes': top_processes}
                        self.visualization_manager.update_process_resource_chart(
                            self.process_resource_chart, chart_data)
                except Exception as chart_err:
                    log_message(f"Error updating process chart: {chart_err}", "DEBUG")
            
        except Exception as e:
            log_message(f"Error updating processes display: {e}", "ERROR")

    def update_system_display(self):
        """Update system monitoring display"""
        try:
                # Clear display
                self.system_display.config(state='normal')
                self.system_display.delete(1.0, tk.END)
                self.system_display.config(state='disabled')

                system_data = self.system_monitor.get_data()
                explanations = system_data.get('explanations', {})

                self.insert_themed_text(self.system_display, "🖥️ SYSTEM ANALYSIS:", 'highlight')
                self.insert_themed_text(self.system_display, "=" * 50, 'primary')

                # CPU Analysis
                cpu_percent = system_data['cpu_percent']
                cpu_exp = explanations.get('cpu', {})
                cpu_line = f"💻 CPU Usage: {cpu_percent:.1f}% - {cpu_exp.get('status', 'unknown').upper()}"
                self.insert_themed_text(self.system_display, cpu_line, cpu_exp.get('color', 'primary'))
                self.insert_themed_text(self.system_display, f"   {cpu_exp.get('meaning', 'No explanation available')}",
                                        'secondary')
                self.insert_themed_text(self.system_display, "", 'primary')

                # Memory Analysis
                memory_percent = system_data['memory_percent']
                memory_exp = explanations.get('memory', {})
                memory_line = f"[MEM] Memory Usage: {memory_percent:.1f}% - {memory_exp.get('status', 'unknown').upper()}"
                self.insert_themed_text(self.system_display, memory_line, memory_exp.get('color', 'primary'))
                self.insert_themed_text(self.system_display, f"   {memory_exp.get('meaning', 'No explanation available')}",
                                        'secondary')
                self.insert_themed_text(self.system_display, "", 'primary')

                # Additional metrics
                user = get_current_username()
                additional_metrics = f"""💾 Disk Usage: {system_data['disk_usage']:.1f}%
👤 User {user} Directory: {system_data['user_disk_usage']:.1f}%
⚙️ Total Processes: {system_data['processes']}
⏰ System Uptime: {system_data['uptime'] / 3600:.1f} hours"""

                self.insert_themed_text(self.system_display, additional_metrics, 'info')

                # Update recommendations
                self.recommendations_text.config(state='normal')
                self.recommendations_text.delete(1.0, tk.END)
                self.recommendations_text.config(state='disabled')

                suggestions = system_data.get('suggestions', [])
                self.insert_themed_text(self.recommendations_text, "🎯 PERFORMANCE RECOMMENDATIONS:", 'highlight')

                for suggestion in suggestions:
                    priority = suggestion.get('priority', 'MEDIUM')
                    issue = suggestion.get('issue', 'Unknown')
                    action = suggestion.get('action', 'No action specified')

                    if priority == 'HIGH':
                        tag = 'error'
                    elif priority == 'MEDIUM':
                        tag = 'warning'
                    elif priority == 'GOOD':
                        tag = 'success'
                    else:
                        tag = 'info'

                    self.insert_themed_text(self.recommendations_text, f"- {issue}", tag)
                    self.insert_themed_text(self.recommendations_text, f"  Action: {action}", 'secondary')

                # System information removed - no longer displayed

        except Exception as e:
                log_message(f"Error updating system display: {e}", "ERROR")

    def update_connection_display(self):
        """FIXED: Update network connection display"""
        try:
                # Clear displays
                self.connection_display.config(state='normal')
                self.connection_display.delete(1.0, tk.END)
                self.connection_display.config(state='disabled')

                self.connection_stats.config(state='normal')
                self.connection_stats.delete(1.0, tk.END)
                self.connection_stats.config(state='disabled')

                health_data = self.network_monitor.get_health_data()

                if not health_data:
                    self.insert_themed_text(self.connection_display, "🔄 Connection monitoring initializing...", 'info')
                else:
                    self.insert_themed_text(self.connection_display, "[HEALTH] NODE CONNECTION STATUS:", 'highlight')
                    self.insert_themed_text(self.connection_display, "=" * 50, 'primary')

                    healthy_nodes = 0
                    unhealthy_nodes = 0
                    total_response_time = 0

                    for node_name, node_info in health_data.items():
                        status = node_info['status']
                        ip = node_info['ip']
                        node_type = node_info['type'].upper()
                        response_time = node_info['response_time']
                        last_check = node_info['last_check'].strftime('%H:%M:%S')
                        recommendation = node_info['recommendation']

                        if status == 'Healthy':
                            status_icon = "✅"
                            tag = 'success'
                            healthy_nodes += 1
                            total_response_time += response_time
                        else:
                            status_icon = "❌"
                            tag = 'error'
                            unhealthy_nodes += 1

                        if app_settings.get('show_ip_addresses', True):
                            node_line = f"{status_icon} {node_name} ({node_type}) - {ip}"
                        else:
                            node_line = f"{status_icon} {node_name} ({node_type})"

                        self.insert_themed_text(self.connection_display, node_line, tag)

                        if status == 'Healthy':
                            detail_line = f"    Status: {status} - Response: {response_time}ms - Checked: {last_check}"
                        else:
                            detail_line = f"    Status: {status} - Last Check: {last_check}"

                        self.insert_themed_text(self.connection_display, detail_line, 'secondary')
                        self.insert_themed_text(self.connection_display, f"    {recommendation}", 'info')

                    # Statistics panel
                    total_nodes = healthy_nodes + unhealthy_nodes
                    avg_response = total_response_time / max(healthy_nodes, 1)

                    stats = "📊 CONNECTION STATISTICS:\n\n" + \
                           "🎯 Overall Health Summary:\n" + \
                           f"- Total Nodes: {total_nodes}\n" + \
                           f"- Healthy: {healthy_nodes} ({100 * healthy_nodes / max(total_nodes, 1):.1f}%)\n" + \
                           f"- Unhealthy: {unhealthy_nodes} ({100 * unhealthy_nodes / max(total_nodes, 1):.1f}%)\n\n" + \
                           "⚡ Performance Metrics:\n" + \
                           f"- Average Response Time: {avg_response:.0f}ms\n" + \
                           f"- Connection Timeout: {app_settings['node_timeout']}s\n" + \
                           f"- Max Concurrent: {app_settings['max_concurrent_checks']}\n\n" + \
                           "🔍 Network Analysis:\n" + \
                           f"- SSH Nodes: {sum(1 for n in health_data.values() if n['type'] == 'ssh')}\n" + \
                           f"- Telnet Nodes: {sum(1 for n in health_data.values() if n['type'] == 'telnet')}\n" + \
                           f"- Error Nodes: {sum(1 for n in health_data.values() if n['status'] == 'Error')}\n\n" + \
                           "🛡️ System Protection:\n" + \
                           "✅ NO HANGING: Timeout protection active\n" + \
                           "✅ Concurrent limits prevent overload\n" + \
                           "✅ Background monitoring active\n" + \
                           "✅ Comprehensive error handling"

                    self.insert_themed_text(self.connection_stats, stats, 'info')
                    
                    # Update network health chart
                    if hasattr(self, 'network_health_chart') and self.network_health_chart:
                        chart_data = {
                            'healthy_nodes': healthy_nodes,
                            'unhealthy_nodes': unhealthy_nodes
                        }
                        self.visualization_manager.update_network_health_chart(
                            self.network_health_chart, chart_data)

        except Exception as e:
                log_message(f"Error updating connection display: {e}", "ERROR")

    def update_space_analyzer(self):
        """FIXED: Update space analyzer with ACTUAL DATA - Respects filters"""
        try:
            # Don't update if filters are active OR user has selected checkboxes
            if hasattr(self, 'space_filter_active') and self.space_filter_active:
                return  # Keep filtered results
            
            # Check if any checkboxes are selected - don't reset if user is working
            if hasattr(self, 'file_vars') and any(var.get() for var in self.file_vars.values()):
                return  # Don't reset user selections
                
            system_data = self.system_monitor.get_data()
            largest_files = system_data.get('largest_files', [])

            # Clear existing checkboxes (FIXED: Use checkbox system)
            for widget in self.files_scroll_frame.winfo_children():
                widget.destroy()
            self.file_checkboxes.clear()
            self.file_vars.clear()

            if largest_files:
                for i, file_info in enumerate(largest_files):
                    size_mb = file_info['size_mb']
                    path = file_info['path']

                    if size_mb > 100:
                        size_str = f"{size_mb:.0f} MB"
                    elif size_mb > 10:
                        size_str = f"{size_mb:.1f} MB"
                    else:
                        size_str = f"{size_mb:.2f} MB"

                    if len(path) > 50:
                        display_path = "..." + path[-47:]
                    else:
                        display_path = path

                    # Create checkbox for each file
                    var = tk.BooleanVar()
                    self.file_vars[path] = var
                    
                    checkbox_frame = tk.Frame(self.files_scroll_frame, bg=self.theme_colors['display_bg'])
                    checkbox_frame.pack(fill='x', padx=5, pady=2)
                    
                    checkbox = tk.Checkbutton(checkbox_frame, variable=var, 
                                            bg=self.theme_colors['display_bg'], 
                                            fg=self.theme_colors['display_text'],
                                            selectcolor=self.theme_colors['card_bg'])
                    checkbox.pack(side='left')
                    
                    file_label = tk.Label(checkbox_frame, text=f"{size_str:>8} | {display_path}",
                                        font=('Courier', 9), bg=self.theme_colors['display_bg'],
                                        fg=self.theme_colors['display_text'], anchor='w')
                    file_label.pack(side='left', fill='x', expand=True)
                    
                    self.file_checkboxes[path] = checkbox

            else:
                # Show message when no large files found
                msg_label = tk.Label(self.files_scroll_frame, 
                                   text="No files larger than 1MB found\nDirectory is clean - excellent!",
                                   font=('Arial', 11), bg=self.theme_colors['display_bg'],
                                   fg=self.theme_colors['success'], justify='center')
                msg_label.pack(expand=True, pady=20)

            # FIXED: Update directory statistics with ACTUAL data
            self.directory_stats.config(state='normal')
            self.directory_stats.delete(1.0, tk.END)
            self.directory_stats.config(state='disabled')

            user = get_current_username()
            user_disk_size = system_data.get('user_disk_size', 0)
            user_disk_usage = system_data.get('user_disk_usage', 0)

            # FIXED: Show actual space data even if no large files
            if user_disk_size > 0:
                total_size_gb = user_disk_size / (1024 ** 3)
                total_size_mb = user_disk_size / (1024 ** 2)

                # Calculate largest file size safely
                largest_file_size = largest_files[0]['size_mb'] if largest_files else 0
                total_large_files_size = sum(f['size_mb'] for f in largest_files) if largest_files else 0
                
                stats = "📊 DIRECTORY STATISTICS:\n\n" + \
                       f"👤 User: {user}\n" + \
                       f"📁 Directory: /users/{user}/\n" + \
                       f"💾 Total Size: {total_size_gb:.2f} GB ({total_size_mb:.0f} MB)\n" + \
                       f"📈 Usage: {user_disk_usage:.1f}%\n\n" + \
                       "📄 Large Files Analysis:\n" + \
                       f"- Files > 1MB: {len(largest_files)}\n" + \
                       f"- Largest File: {largest_file_size:.1f} MB\n" + \
                       f"- Total in Large Files: {total_large_files_size:.1f} MB\n\n" + \
                       "💡 SPACE EXPLANATION:\n" + \
                       f"Even with no large files (>1MB), your directory\n" + \
                       f"uses {total_size_mb:.0f} MB from many small files.\n" + \
                       "This is normal - system files, configs, and\n" + \
                       "documents under 1MB each add up to total space.\n\n" + \
                       "🧹 Cleanup Recommendations:"
            else:
                stats = "📊 DIRECTORY STATISTICS:\n\n" + \
                       f"👤 User: {user}\n" + \
                       f"📁 Directory: /users/{user}/\n" + \
                       "💾 Total Size: Calculating...\n" + \
                       f"📈 Usage: {user_disk_usage:.1f}%\n\n" + \
                       "📄 Large Files Analysis:\n" + \
                       f"- Files > 1MB: {len(largest_files)}\n" + \
                       "- Directory appears to be very clean!\n\n" + \
                       "🧹 Cleanup Recommendations:"

            self.insert_themed_text(self.directory_stats, stats, 'info')

            # Add cleanup recommendations
            if largest_files:
                if any(f['size_mb'] > 100 for f in largest_files):
                    self.insert_themed_text(self.directory_stats, "- Consider reviewing files over 100MB", 'warning')
                if len(largest_files) > 10:
                    self.insert_themed_text(self.directory_stats, "- Many large files detected - cleanup recommended",
                                            'warning')
                self.insert_themed_text(self.directory_stats, "- Use 'Delete Selected' to remove unwanted files",
                                        'info')
            else:
                self.insert_themed_text(self.directory_stats, "- No large files found - directory is clean", 'success')
                self.insert_themed_text(self.directory_stats, "- Space usage from many small files is normal", 'info')

        except Exception as e:
            log_message(f"Error updating space analyzer: {e}", "ERROR")

    def update_debug_logs(self):
        """FIXED: Update debug logs with COLOR-CODED display"""
        try:
            # FIXED: Don't update if filters are active
            if hasattr(self, 'filters_active') and self.filters_active:
                return
                
            # FIXED: Don't update if search results are active
            if hasattr(self, 'search_results_active') and self.search_results_active:
                return
            
            # FIXED: Don't update if logs were manually cleared
            if hasattr(self, 'logs_cleared') and self.logs_cleared:
                return
                
            # Clear display
            self.debug_display.config(state='normal')
            self.debug_display.delete(1.0, tk.END)
            self.debug_display.config(state='disabled')

            # Show recent log entries with COLOR CODING
            log_file = os.path.join("logs", "professional_launcher.log")
            if os.path.exists(log_file):
                try:
                    with open(log_file, 'r', encoding='utf-8') as f:
                        lines = f.readlines()

                    # Show last 200 lines instead of 30
                    recent_lines = lines[-200:] if len(lines) > 200 else lines

                    self.insert_themed_text(self.debug_display, "🔍 RECENT DEBUG LOG ENTRIES (COLOR-CODED):",
                                            'highlight')
                    self.insert_themed_text(self.debug_display, "=" * 60, 'primary')

                    for line in recent_lines:
                        line = line.strip()
                        # FIXED: COLOR-CODED log entries with tab-specific colors
                        if '[ERROR]' in line or '❌' in line:
                            tag = 'error'
                        elif '[WARNING]' in line:
                            tag = 'warning'
                        elif '✅' in line or '[LAUNCH]' in line:
                            tag = 'success'
                        elif '[DASHBOARD]' in line:
                            tag = 'DASHBOARD'
                        elif '[PROCESSES]' in line:
                            tag = 'PROCESSES'
                        elif '[SPACE]' in line:
                            tag = 'SPACE'
                        elif '[DEBUG]' in line:
                            tag = 'DEBUG'
                        elif '[SYSTEM]' in line:
                            tag = 'highlight'
                        elif '[NETWORK]' in line:
                            tag = 'info'
                        elif '[INFO]' in line or 'ℹ️' in line:
                            tag = 'info'
                        else:
                            tag = 'primary'

                        self.insert_themed_text(self.debug_display, line, tag)

                except Exception as e:
                    self.insert_themed_text(self.debug_display, f"Error reading log file: {e}", 'error')
            else:
                self.insert_themed_text(self.debug_display, "No log file found - will be created on first activity",
                                        'secondary')

            # Update log files list
            self.log_files_listbox.delete(0, tk.END)

            if os.path.exists(LOGS_DIR):
                log_files = [f for f in os.listdir(LOGS_DIR) if f.endswith('.log')]
                log_files.sort(reverse=True)

                for log_file in log_files:
                    # Show absolute path for clarity
                    full_path = os.path.join(LOGS_DIR, log_file)
                    self.log_files_listbox.insert(tk.END, full_path)

            # FIXED: Don't update log analysis if search results are active
            if not hasattr(self, 'search_results_active') or not self.search_results_active:
                # Log analysis
                # Skip analysis - debug display shows logs directly
                pass  # Analysis removed
            else:
                # Keep existing search results - do not update
                pass

        except Exception as e:
            log_message(f"Error updating debug logs: {e}", "ERROR")

###############################################################################
# MAIN EXECUTION
###############################################################################

    def copy_debug_logs_to_clipboard(self):
        """Copy debug logs to clipboard - FIXED"""
        try:
            if hasattr(self, 'debug_display'):
                # Get all text content
                content = self.debug_display.get('1.0', 'end-1c')
                
                if not content or content.strip() == "":
                    messagebox.showwarning("Warning", "No debug logs available to copy")
                    return
                
                # Add header with system info
                header = f"""=== NODE AUTOMATION LAUNCHER DEBUG LOGS ===
Exported: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Theme: {self.current_theme}
System: {platform.system()} {platform.release()}
Python: {sys.version.split()[0]}
{'='*60}

🔍 RECENT DEBUG LOG ENTRIES (COLOR-CODED):
{'='*60}

"""
                full_content = header + content
                
                # Copy to clipboard - use multiple methods for reliability
                try:
                    # Method 1: Tkinter clipboard
                    self.root.clipboard_clear()
                    self.root.clipboard_append(full_content)
                    self.root.update()
                    
                    # Method 2: Try xclip if available (Linux)
                    try:
                        import subprocess
                        subprocess.run(['xclip', '-selection', 'clipboard'], 
                                     input=full_content.encode(), 
                                     timeout=2, check=False)
                    except:
                        pass
                    
                except Exception as clipboard_error:
                    log_message(f"Clipboard error: {clipboard_error}", "WARNING")
                
                # Show success message
                messagebox.showinfo("Copied", 
                                  f"✅ Debug logs copied to clipboard!\n\n"
                                  f"Lines: {len(content.splitlines())}\n"
                                  f"Characters: {len(full_content)}")
                
                log_message("[DEBUG] Debug logs copied to clipboard", "DEBUG")
            else:
                messagebox.showwarning("Warning", "No debug logs available to copy")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy debug logs: {e}")

    def clear_debug_logs(self):
        """Clear debug logs - NEW FEATURE"""
        try:
            if hasattr(self, 'debug_display'):
                response = messagebox.askyesno("Confirm Clear", 
                                             "Are you sure you want to clear all debug logs?\n"
                                             "This action cannot be undone.")
                if response:
                    # Set flag to prevent auto-refresh from reloading logs
                    self.logs_cleared = True
                    
                    self.debug_display.config(state='normal')
                    self.debug_display.delete(1.0, tk.END)
                    
                    # Add cleared message
                    clear_msg = f"🗑️ Debug logs cleared at {datetime.now().strftime('%H:%M:%S')}\n\n"
                    clear_msg += "📝 Note: New log entries will appear as they are generated.\n"
                    clear_msg += "🔄 Click 'Refresh Logs' to reload all historical logs."
                    self.insert_themed_text(self.debug_display, clear_msg, 'warning')
                    
                    self.debug_display.config(state='disabled')
                    
                    messagebox.showinfo("Success", "Debug logs display cleared!\n\nNew logs will appear as generated.")
                    
                    # Log the action
                    if hasattr(self, 'activity_text'):
                        self.insert_themed_text(self.activity_text, 
                                              "🗑️ Debug logs display cleared", 'warning')
        except Exception as e:
            messagebox.showerror("Error", f"Failed to clear debug logs: {e}")

    def export_debug_logs(self):
        """Export debug logs to file - NEW FEATURE"""
        try:
            if hasattr(self, 'debug_display'):
                from tkinter import filedialog
                
                filename = filedialog.asksaveasfilename(
                    defaultextension=".txt",
                    filetypes=[("Text files", "*.txt"), ("Log files", "*.log"), ("All files", "*.*")],
                    title="Export Debug Logs",
                    initialdir=LOGS_DIR
                )
                
                if filename:
                    content = self.debug_display.get(1.0, tk.END)
                    header = f"""NODE AUTOMATION LAUNCHER DEBUG LOGS
Exported: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Theme: {self.current_theme}
System: {platform.system()} {platform.release()}
{'='*60}

"""
                    
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(header + content)
                    
                    messagebox.showinfo("Success", f"Debug logs exported to:\n{filename}")
                    
                    # Log the action
                    if hasattr(self, 'activity_text'):
                        self.insert_themed_text(self.activity_text, 
                                              f"[EXP] Debug logs exported to {os.path.basename(filename)}", 'success')
            else:
                messagebox.showwarning("Warning", "No debug logs available to export")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export debug logs: {e}")

    def toggle_always_on_top(self):
        """Toggle always on top window attribute"""
        try:
            self.root.attributes('-topmost', self.always_on_top_var.get())
        except Exception as e:
                print(f"⚠️ Could not toggle always on top: {e}")
    
    def save_window_position(self):
        """Save current window position"""
        try:
            if self.remember_position_var.get():
                geometry = self.root.geometry()
                app_settings['window_geometry'] = geometry
                with open('app_settings.json', 'w') as f:
                    json.dump(app_settings, f, indent=2)
        except Exception as e:
                print(f"⚠️ Could not save window position: {e}")
    
    def restore_window_position(self):
        """Restore saved window position"""
        try:
            if self.remember_position_var.get() and 'window_geometry' in app_settings:
                self.root.geometry(app_settings['window_geometry'])
        except Exception as e:
                print(f"⚠️ Could not restore window position: {e}")


    def on_closing(self):
        """Handle application closing with save dialog"""
        try:
            # Ask user about saving debug logs
            from tkinter import messagebox, filedialog
            import datetime
            
            response = messagebox.askyesnocancel(
                "Save Debug Logs?",
                "Do you want to save debug logs before closing?\n\n"
                "- Yes: Save logs to file\n"
                "- No: Close without saving\n"
                "- Cancel: Don't close"
            )
            
            if response is None:  # Cancel
                return
            elif response:  # Yes - Save logs
                try:
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
                    default_filename = f"debug_logs_{timestamp}.log"
                    
                    filename = filedialog.asksaveasfilename(
                        title="Save Debug Logs",
                        defaultextension=".log",
                        filetypes=[("Log files", "*.log"), ("Text files", "*.txt"), ("All files", "*.*")],
                        initialdir=LOGS_DIR,
                        initialfile=default_filename
                    )
                    
                    if filename:
                        # Get debug logs content
                        if hasattr(self, 'debug_display'):
                            log_content = self.debug_display.get(1.0, tk.END)
                            with open(filename, 'w') as f:
                                f.write(f"Debug Logs Export - {datetime.datetime.now()}\n")
                                f.write("="*50 + "\n")
                                f.write(log_content)
                            messagebox.showinfo("Saved", f"Debug logs saved to:\n{filename}")
                        else:
                            messagebox.showwarning("No Logs", "No debug logs to save")
                except Exception as e:
                    messagebox.showerror("Save Error", f"Failed to save logs: {e}")
            
            # Proceed with shutdown
            if hasattr(self, 'system_monitor'):
                self.system_monitor.stop()
            if hasattr(self, 'network_monitor'):
                self.network_monitor.stop()
            if hasattr(self, 'process_manager'):
                self.process_manager.kill_all()
            
            log_message("Node Automation Launcher shutdown", "SYSTEM")
            self.root.quit()
            self.root.destroy()
            
        except Exception as e:
            print(f"Error during shutdown: {e}")
            self.root.quit()
            self.root.destroy()

    def manage_nodes_config(self):
        """FIXED: Complete Node Management - Add/Edit/Delete with all JSON fields"""
        try:
            # Create node management window
            node_window = tk.Toplevel(self.root)
            node_window.title("Node Management")
            node_window.geometry("900x650")
            node_window.configure(bg=self.theme_colors['bg'])
            node_window.transient(self.root)
            node_window.grab_set()

            # Enhanced Header with gradient effect
            header_frame = tk.Frame(node_window, bg=self.theme_colors['info'], relief='raised', bd=2)
            header_frame.pack(fill='x', padx=0, pady=0)
            
            header_inner = tk.Frame(header_frame, bg=self.theme_colors['info'])
            header_inner.pack(fill='x', padx=20, pady=15)

            tk.Label(header_inner, text="🔧 NODE MANAGEMENT CENTER", font=('Arial', 16, 'bold'),
                    bg=self.theme_colors['info'], fg='white').pack()
            tk.Label(header_inner, text="Configure and manage network node connections", 
                    font=('Arial', 10), bg=self.theme_colors['info'], fg='white').pack()

            # Main container
            main_container = tk.Frame(node_window, bg=self.theme_colors['bg'])
            main_container.pack(fill='both', expand=True, padx=20, pady=10)

            # Left side - Existing nodes list with enhanced styling
            left_frame = tk.LabelFrame(main_container, text="📋 Existing Nodes",
                                     font=('Arial', 12, 'bold'), bg=self.theme_colors['card_bg'],
                                     fg=self.theme_colors['info'], relief='groove', bd=2)
            left_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))

            # Load existing nodes
            config_file = "master_config.json"
            nodes = []
            if os.path.exists(config_file):
                try:
                    with open(config_file, 'r') as f:
                        config = json.load(f)
                        nodes = config.get("nodes", [])
                except:
                    nodes = []

            # Nodes listbox with wider width and colored background
            listbox_frame = tk.Frame(left_frame, bg=self.theme_colors['card_bg'])
            listbox_frame.pack(fill='both', expand=True, padx=10, pady=10)
            
            scrollbar = tk.Scrollbar(listbox_frame)
            scrollbar.pack(side='right', fill='y')
            
            nodes_listbox = tk.Listbox(listbox_frame, bg=self.theme_colors['display_bg'],
                                     fg=self.theme_colors['display_text'], 
                                     font=('Courier', 9),  # Monospace for better alignment
                                     selectbackground=self.theme_colors['info'],
                                     selectforeground='white',
                                     yscrollcommand=scrollbar.set)
            nodes_listbox.pack(side='left', fill='both', expand=True)
            scrollbar.config(command=nodes_listbox.yview)

            # Populate nodes list with better formatting
            for i, node in enumerate(nodes):
                name = node.get('name', 'Unknown')[:20].ljust(20)  # Fixed width
                node_type = node.get('type', 'N/A').upper()[:6].ljust(6)
                ip = node.get('ip', 'N/A')
                node_info = f"{name} | {node_type} | {ip}"
                nodes_listbox.insert(tk.END, node_info)

            # Right side - Add/Edit form with enhanced styling
            right_frame = tk.LabelFrame(main_container, text="➕ Add/Edit Node",
                                      font=('Arial', 12, 'bold'), bg=self.theme_colors['card_bg'],
                                      fg=self.theme_colors['success'], relief='groove', bd=2)
            right_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))

            # Form fields matching JSON structure exactly
            form_frame = tk.Frame(right_frame, bg=self.theme_colors['card_bg'])
            form_frame.pack(fill='both', expand=True, padx=20, pady=15)

            # Name
            tk.Label(form_frame, text="Name:", font=('Arial', 11, 'bold'),
                    bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=0, column=0, sticky='w', pady=5)
            name_var = tk.StringVar()
            tk.Entry(form_frame, textvariable=name_var, font=('Arial', 10), width=25).grid(row=0, column=1, padx=10, pady=5)

            # Type
            tk.Label(form_frame, text="Type:", font=('Arial', 11, 'bold'),
                    bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=1, column=0, sticky='w', pady=5)
            type_var = tk.StringVar(value="telnet")
            type_frame = tk.Frame(form_frame, bg=self.theme_colors['card_bg'])
            type_frame.grid(row=1, column=1, sticky='w', padx=10, pady=5)
            tk.Radiobutton(type_frame, text="Telnet", variable=type_var, value="telnet",
                          bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).pack(side='left')
            tk.Radiobutton(type_frame, text="SSH", variable=type_var, value="ssh",
                          bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).pack(side='left', padx=10)

            # IP Address
            tk.Label(form_frame, text="IP Address:", font=('Arial', 11, 'bold'),
                    bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=2, column=0, sticky='w', pady=5)
            ip_var = tk.StringVar()
            tk.Entry(form_frame, textvariable=ip_var, font=('Arial', 10), width=25).grid(row=2, column=1, padx=10, pady=5)

            # Login
            tk.Label(form_frame, text="Login:", font=('Arial', 11, 'bold'),
                    bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=3, column=0, sticky='w', pady=5)
            login_var = tk.StringVar(value="mtcl")
            tk.Entry(form_frame, textvariable=login_var, font=('Arial', 10), width=25).grid(row=3, column=1, padx=10, pady=5)

            # Password
            tk.Label(form_frame, text="Password:", font=('Arial', 11, 'bold'),
                    bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=4, column=0, sticky='w', pady=5)
            password_var = tk.StringVar(value="mtcl")
            tk.Entry(form_frame, textvariable=password_var, font=('Arial', 10), width=25, show='*').grid(row=4, column=1, padx=10, pady=5)

            # Confirm Password
            tk.Label(form_frame, text="Confirm Password:", font=('Arial', 11, 'bold'),
                    bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=5, column=0, sticky='w', pady=5)
            password_confirm_var = tk.StringVar(value="mtcl")
            tk.Entry(form_frame, textvariable=password_confirm_var, font=('Arial', 10), width=25, show='*').grid(row=5, column=1, padx=10, pady=5)

            # SWINST Password
            tk.Label(form_frame, text="SWINST Password:", font=('Arial', 11, 'bold'),
                    bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=6, column=0, sticky='w', pady=5)
            swinst_password_var = tk.StringVar(value="SoftInst")
            tk.Entry(form_frame, textvariable=swinst_password_var, font=('Arial', 10), width=25, show='*').grid(row=6, column=1, padx=10, pady=5)

            # Confirm SWINST Password
            tk.Label(form_frame, text="Confirm SWINST Password:", font=('Arial', 11, 'bold'),
                    bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=7, column=0, sticky='w', pady=5)
            swinst_confirm_var = tk.StringVar(value="SoftInst")
            tk.Entry(form_frame, textvariable=swinst_confirm_var, font=('Arial', 10), width=25, show='*').grid(row=7, column=1, padx=10, pady=5)

            # Root Password
            tk.Label(form_frame, text="Root Password:", font=('Arial', 11, 'bold'),
                    bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=8, column=0, sticky='w', pady=5)
            root_password_var = tk.StringVar(value="letacla")
            tk.Entry(form_frame, textvariable=root_password_var, font=('Arial', 10), width=25, show='*').grid(row=8, column=1, padx=10, pady=5)

            # Confirm Root Password
            tk.Label(form_frame, text="Confirm Root Password:", font=('Arial', 11, 'bold'),
                    bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=9, column=0, sticky='w', pady=5)
            root_confirm_var = tk.StringVar(value="letacla")
            tk.Entry(form_frame, textvariable=root_confirm_var, font=('Arial', 10), width=25, show='*').grid(row=9, column=1, padx=10, pady=5)

            # Current editing index
            current_edit_index = None

            def load_node_for_edit():
                nonlocal current_edit_index
                selection = nodes_listbox.curselection()
                if selection:
                    current_edit_index = selection[0]
                    node = nodes[current_edit_index]
                    
                    name_var.set(node.get('name', ''))
                    type_var.set(node.get('type', 'telnet'))
                    ip_var.set(node.get('ip', ''))
                    login_var.set(node.get('login', 'mtcl'))
                    password_var.set(node.get('password', 'mtcl'))
                    password_confirm_var.set(node.get('password', 'mtcl'))
                    swinst_password_var.set(node.get('swinst_password', 'SoftInst'))
                    swinst_confirm_var.set(node.get('swinst_password', 'SoftInst'))
                    root_password_var.set(node.get('root_password', 'letacla'))
                    root_confirm_var.set(node.get('root_password', 'letacla'))

            def clear_form():
                nonlocal current_edit_index
                current_edit_index = None
                name_var.set('')
                type_var.set('telnet')
                ip_var.set('')
                login_var.set('mtcl')
                password_var.set('mtcl')
                password_confirm_var.set('mtcl')
                swinst_password_var.set('SoftInst')
                swinst_confirm_var.set('SoftInst')
                root_password_var.set('letacla')
                root_confirm_var.set('letacla')

            def save_node():
                try:
                    name = name_var.get().strip()
                    node_type = type_var.get().strip()
                    ip = ip_var.get().strip()
                    login = login_var.get().strip()
                    password = password_var.get().strip()
                    password_confirm = password_confirm_var.get().strip()
                    swinst_password = swinst_password_var.get().strip()
                    swinst_confirm = swinst_confirm_var.get().strip()
                    root_password = root_password_var.get().strip()
                    root_confirm = root_confirm_var.get().strip()

                    if not all([name, ip, login]):
                        messagebox.showwarning("Missing Fields", "Please fill in Name, IP Address, and Login")
                        return

                    # Validate password confirmations
                    if password != password_confirm:
                        messagebox.showerror("Error", "Password and Confirm Password do not match!")
                        return
                    if swinst_password != swinst_confirm:
                        messagebox.showerror("Error", "SWINST Password and Confirm SWINST do not match!")
                        return
                    if root_password != root_confirm:
                        messagebox.showerror("Error", "Root Password and Confirm Root do not match!")
                        return

                    # Load config
                    if os.path.exists(config_file):
                        with open(config_file, 'r') as f:
                            config = json.load(f)
                    else:
                        config = {"nodes": [], "remote_server": []}

                    # Create node matching JSON structure
                    new_node = {
                        "name": name,
                        "type": node_type,
                        "ip": ip,
                        "login": login,
                        "password": password,
                        "swinst_password": swinst_password,
                        "root_password": root_password
                    }

                    if "nodes" not in config:
                        config["nodes"] = []

                    if current_edit_index is not None:
                        # Edit existing node
                        config["nodes"][current_edit_index] = new_node
                        action = "updated"
                    else:
                        # Add new node - insert in correct position based on type
                        nodes = config["nodes"]
                        if node_type == "telnet":
                            # Find position after last telnet node but before first ssh node
                            insert_pos = 0
                            for i, existing_node in enumerate(nodes):
                                if existing_node.get("type") == "telnet":
                                    insert_pos = i + 1
                                elif existing_node.get("type") == "ssh":
                                    # Stop at first SSH node - insert before it
                                    break
                            nodes.insert(insert_pos, new_node)
                        else:  # ssh
                            # SSH nodes go at the end
                            nodes.append(new_node)
                        action = "added"

                    # Save config
                    with open(config_file, 'w') as f:
                        json.dump(config, f, indent=2)

                    messagebox.showinfo("Success", f"Node '{name}' {action} successfully!")
                    node_window.destroy()

                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save node: {e}")

            def delete_node():
                selection = nodes_listbox.curselection()
                if not selection:
                    messagebox.showwarning("No Selection", "Please select a node to delete")
                    return

                node_index = selection[0]
                node_name = nodes[node_index].get('name', 'Unknown')
                
                if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete node '{node_name}'?"):
                    try:
                        # Load config
                        with open(config_file, 'r') as f:
                            config = json.load(f)
                        
                        # Remove node
                        config["nodes"].pop(node_index)
                        
                        # Save config
                        with open(config_file, 'w') as f:
                            json.dump(config, f, indent=2)
                        
                        messagebox.showinfo("Success", f"Node '{node_name}' deleted successfully!")
                        node_window.destroy()
                        
                    except Exception as e:
                        messagebox.showerror("Error", f"Failed to delete node: {e}")

            # Bind double-click to load for editing
            nodes_listbox.bind('<Double-Button-1>', lambda e: load_node_for_edit())

            # Enhanced Buttons with icons
            btn_frame = tk.Frame(right_frame, bg=self.theme_colors['card_bg'])
            btn_frame.pack(fill='x', padx=20, pady=15)

            tk.Button(btn_frame, text="➕ Add New", command=clear_form,
                     bg=self.theme_colors['info'], fg='white', font=('Arial', 10, 'bold'),
                     relief='raised', bd=2, padx=20, pady=8, cursor='hand2').pack(side='left', padx=5)

            tk.Button(btn_frame, text="📝 Load Selected", command=load_node_for_edit,
                     bg=self.theme_colors['warning'], fg='white', font=('Arial', 10, 'bold'),
                     relief='raised', bd=2, padx=20, pady=8, cursor='hand2').pack(side='left', padx=5)

            tk.Button(btn_frame, text="💾 Save Node", command=save_node,
                     bg=self.theme_colors['success'], fg='white', font=('Arial', 10, 'bold'),
                     relief='raised', bd=2, padx=20, pady=8, cursor='hand2').pack(side='left', padx=5)

            tk.Button(btn_frame, text="🗑️ Delete Selected", command=delete_node,
                     bg=self.theme_colors['error'], fg='white', font=('Arial', 10, 'bold'),
                     padx=15, pady=5).pack(side='left', padx=5)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to open node management: {e}")

    def add_new_node(self):
        """Add new node configuration"""
        try:
            # Create add node dialog
            node_window = tk.Toplevel(self.root)
            node_window.title("Add New Node")
            node_window.geometry("500x400")
            node_window.configure(bg=self.theme_colors['bg'])
            node_window.transient(self.root)
            node_window.grab_set()

            # Node configuration form
            form_frame = tk.Frame(node_window, bg=self.theme_colors['bg'])
            form_frame.pack(fill='both', expand=True, padx=20, pady=20)

            # Node name
            tk.Label(form_frame, text="Node Name:", font=('Arial', 11, 'bold'),
                    bg=self.theme_colors['bg'], fg=self.theme_colors['primary_text']).pack(anchor='w')
            node_name_var = tk.StringVar()
            tk.Entry(form_frame, textvariable=node_name_var, font=('Arial', 10), width=40).pack(fill='x', pady=5)

            # IP Address
            tk.Label(form_frame, text="IP Address:", font=('Arial', 11, 'bold'),
                    bg=self.theme_colors['bg'], fg=self.theme_colors['primary_text']).pack(anchor='w', pady=(10,0))
            ip_var = tk.StringVar()
            tk.Entry(form_frame, textvariable=ip_var, font=('Arial', 10), width=40).pack(fill='x', pady=5)

            # Connection type (moved up to match JSON structure)
            tk.Label(form_frame, text="Connection Type:", font=('Arial', 11, 'bold'),
                    bg=self.theme_colors['bg'], fg=self.theme_colors['primary_text']).pack(anchor='w', pady=(10,0))
            type_var = tk.StringVar(value="telnet")
            type_frame = tk.Frame(form_frame, bg=self.theme_colors['bg'])
            type_frame.pack(fill='x', pady=5)
            tk.Radiobutton(type_frame, text="Telnet", variable=type_var, value="telnet",
                          bg=self.theme_colors['bg'], fg=self.theme_colors['primary_text']).pack(side='left')
            tk.Radiobutton(type_frame, text="SSH", variable=type_var, value="ssh",
                          bg=self.theme_colors['bg'], fg=self.theme_colors['primary_text']).pack(side='left', padx=20)

            # Login (Username)
            tk.Label(form_frame, text="Login (Username):", font=('Arial', 11, 'bold'),
                    bg=self.theme_colors['bg'], fg=self.theme_colors['primary_text']).pack(anchor='w', pady=(10,0))
            login_var = tk.StringVar(value="mtcl")
            tk.Entry(form_frame, textvariable=login_var, font=('Arial', 10), width=40).pack(fill='x', pady=5)

            # Password
            tk.Label(form_frame, text="Password:", font=('Arial', 11, 'bold'),
                    bg=self.theme_colors['bg'], fg=self.theme_colors['primary_text']).pack(anchor='w', pady=(10,0))
            password_var = tk.StringVar()
            tk.Entry(form_frame, textvariable=password_var, font=('Arial', 10), width=40, show='*').pack(fill='x', pady=5)

            # SWINST Password
            tk.Label(form_frame, text="SWINST Password:", font=('Arial', 11, 'bold'),
                    bg=self.theme_colors['bg'], fg=self.theme_colors['primary_text']).pack(anchor='w', pady=(10,0))
            swinst_password_var = tk.StringVar()
            tk.Entry(form_frame, textvariable=swinst_password_var, font=('Arial', 10), width=40, show='*').pack(fill='x', pady=5)

            # Root Password
            tk.Label(form_frame, text="Root Password:", font=('Arial', 11, 'bold'),
                    bg=self.theme_colors['bg'], fg=self.theme_colors['primary_text']).pack(anchor='w', pady=(10,0))
            root_password_var = tk.StringVar()
            tk.Entry(form_frame, textvariable=root_password_var, font=('Arial', 10), width=40, show='*').pack(fill='x', pady=5)

            def save_node():
                try:
                    name = node_name_var.get().strip()
                    ip = ip_var.get().strip()
                    node_type = type_var.get().strip()
                    login = login_var.get().strip()
                    password = password_var.get().strip()
                    swinst_password = swinst_password_var.get().strip()
                    root_password = root_password_var.get().strip()

                    if not all([name, ip, login]):
                        messagebox.showwarning("Missing Fields", "Please fill in Name, IP Address, and Login")
                        return

                    # Load existing config
                    config_file = "master_config.json"
                    if os.path.exists(config_file):
                        with open(config_file, 'r') as f:
                            config = json.load(f)
                    else:
                        config = {"nodes": [], "remote_server": []}

                    # Add new node matching JSON structure
                    new_node = {
                        "name": name,
                        "type": node_type,
                        "ip": ip,
                        "login": login,
                        "password": password,
                        "swinst_password": swinst_password,
                        "root_password": root_password
                    }
                    
                    if "nodes" not in config:
                        config["nodes"] = []
                    config["nodes"].append(new_node)

                    # Save config
                    with open(config_file, 'w') as f:
                        json.dump(config, f, indent=2)

                    messagebox.showinfo("Success", f"Node '{name}' added successfully!")
                    node_window.destroy()

                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save node: {e}")

            # Buttons
            btn_frame = tk.Frame(form_frame, bg=self.theme_colors['bg'])
            btn_frame.pack(fill='x', pady=20)

            tk.Button(btn_frame, text="Save Node", command=save_node,
                     bg=self.theme_colors['success'], fg='white', font=('Arial', 10, 'bold'),
                     padx=20, pady=5).pack(side='left')

            tk.Button(btn_frame, text="Cancel", command=node_window.destroy,
                     bg=self.theme_colors['error'], fg='white', font=('Arial', 10, 'bold'),
                     padx=20, pady=5).pack(side='right')

        except Exception as e:
            messagebox.showerror("Error", f"Failed to open add node dialog: {e}")

    def manage_servers_config(self):
        """FIXED: Simplified remote server configuration matching JSON structure"""
        try:
            # Create server management window
            server_window = tk.Toplevel(self.root)
            server_window.title("Remote Server Configuration")
            server_window.geometry("750x600")
            server_window.configure(bg=self.theme_colors['bg'])
            server_window.transient(self.root)
            server_window.grab_set()

            # Enhanced Header with colored background
            header_frame = tk.Frame(server_window, bg=self.theme_colors['warning'], relief='raised', bd=2)
            header_frame.pack(fill='x', padx=0, pady=0)
            
            header_inner = tk.Frame(header_frame, bg=self.theme_colors['warning'])
            header_inner.pack(fill='x', padx=20, pady=15)

            tk.Label(header_inner, text="🌐 REMOTE SERVER CONFIGURATION",
                    font=('Arial', 16, 'bold'), bg=self.theme_colors['warning'], fg='white').pack()
            tk.Label(header_inner, text="Configure remote server connections for automation",
                    font=('Arial', 10), bg=self.theme_colors['warning'], fg='white').pack()

            # Load existing servers
            config_file = "master_config.json"
            servers = []
            if os.path.exists(config_file):
                try:
                    with open(config_file, 'r') as f:
                        config = json.load(f)
                        servers = config.get("remote_server", [])
                except:
                    servers = []

            # Server list frame with enhanced styling
            list_frame = tk.LabelFrame(server_window, text="📋 Current Remote Servers",
                                     font=('Arial', 12, 'bold'), bg=self.theme_colors['card_bg'],
                                     fg=self.theme_colors['warning'], relief='groove', bd=2)
            list_frame.pack(fill='both', expand=True, padx=20, pady=(10, 5))

            # Display current servers with listbox for selection
            listbox_frame = tk.Frame(list_frame, bg=self.theme_colors['card_bg'])
            listbox_frame.pack(fill='both', expand=True, padx=10, pady=10)
            
            scrollbar = tk.Scrollbar(listbox_frame)
            scrollbar.pack(side='right', fill='y')
            
            servers_listbox = tk.Listbox(listbox_frame, bg=self.theme_colors['display_bg'],
                                       fg=self.theme_colors['display_text'], 
                                       font=('Courier', 9),
                                       selectbackground=self.theme_colors['warning'],
                                       selectforeground='white',
                                       yscrollcommand=scrollbar.set)
            servers_listbox.pack(side='left', fill='both', expand=True)
            scrollbar.config(command=servers_listbox.yview)

            # Show existing servers with better formatting
            if servers:
                for i, server in enumerate(servers):
                    ip = server.get('ip', 'N/A').ljust(20)
                    login = server.get('own_login', 'N/A').ljust(15)
                    server_info = f"Server {i+1:2d} | {ip} | Login: {login}"
                    servers_listbox.insert(tk.END, server_info)
            else:
                servers_listbox.insert(tk.END, "No remote servers configured yet.")

            # Configuration form with enhanced styling
            config_frame = tk.LabelFrame(server_window, text="➕ Add/Edit Remote Server",
                                       font=('Arial', 12, 'bold'), bg=self.theme_colors['card_bg'],
                                       fg=self.theme_colors['success'], relief='groove', bd=2)
            config_frame.pack(fill='x', padx=20, pady=(5, 15))

            form_frame = tk.Frame(config_frame, bg=self.theme_colors['card_bg'])
            form_frame.pack(fill='x', padx=20, pady=15)

            # IP Address
            tk.Label(form_frame, text="IP Address:", font=('Arial', 11, 'bold'),
                    bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=0, column=0, sticky='w', pady=5)
            ip_var = tk.StringVar()
            tk.Entry(form_frame, textvariable=ip_var, font=('Arial', 10), width=25).grid(row=0, column=1, padx=10, pady=5)

            # Own Login
            tk.Label(form_frame, text="Own Login:", font=('Arial', 11, 'bold'),
                    bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=1, column=0, sticky='w', pady=5)
            own_login_var = tk.StringVar()
            tk.Entry(form_frame, textvariable=own_login_var, font=('Arial', 10), width=25).grid(row=1, column=1, padx=10, pady=5)

            # Own Password
            tk.Label(form_frame, text="Own Password:", font=('Arial', 11, 'bold'),
                    bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=2, column=0, sticky='w', pady=5)
            own_password_var = tk.StringVar()
            tk.Entry(form_frame, textvariable=own_password_var, font=('Arial', 10), width=25, show='*').grid(row=2, column=1, padx=10, pady=5)

            # Confirm Own Password
            tk.Label(form_frame, text="Confirm Own Password:", font=('Arial', 11, 'bold'),
                    bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=3, column=0, sticky='w', pady=5)
            own_password_confirm_var = tk.StringVar()
            tk.Entry(form_frame, textvariable=own_password_confirm_var, font=('Arial', 10), width=25, show='*').grid(row=3, column=1, padx=10, pady=5)

            # Others Remote Login
            tk.Label(form_frame, text="Others Remote Login:", font=('Arial', 11, 'bold'),
                    bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=4, column=0, sticky='w', pady=5)
            others_login_var = tk.StringVar(value="login")
            tk.Entry(form_frame, textvariable=others_login_var, font=('Arial', 10), width=25).grid(row=4, column=1, padx=10, pady=5)

            # Others Remote Password
            tk.Label(form_frame, text="Others Remote Password:", font=('Arial', 11, 'bold'),
                    bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=5, column=0, sticky='w', pady=5)
            others_password_var = tk.StringVar(value="password")
            tk.Entry(form_frame, textvariable=others_password_var, font=('Arial', 10), width=25, show='*').grid(row=5, column=1, padx=10, pady=5)

            # Confirm Others Remote Password
            tk.Label(form_frame, text="Confirm Others Password:", font=('Arial', 11, 'bold'),
                    bg=self.theme_colors['card_bg'], fg=self.theme_colors['primary_text']).grid(row=6, column=0, sticky='w', pady=5)
            others_password_confirm_var = tk.StringVar(value="password")
            tk.Entry(form_frame, textvariable=others_password_confirm_var, font=('Arial', 10), width=25, show='*').grid(row=6, column=1, padx=10, pady=5)

            # Current editing index
            current_edit_index = None

            def load_server_for_edit():
                nonlocal current_edit_index
                selection = servers_listbox.curselection()
                if selection and servers:
                    current_edit_index = selection[0]
                    server = servers[current_edit_index]
                    
                    ip_var.set(server.get('ip', ''))
                    own_login_var.set(server.get('own_login', ''))
                    own_password_var.set(server.get('own_password', ''))
                    own_password_confirm_var.set(server.get('own_password', ''))
                    others_login_var.set(server.get('others_remote_login', 'login'))
                    others_password_var.set(server.get('others_remote_password', 'password'))
                    others_password_confirm_var.set(server.get('others_remote_password', 'password'))

            def clear_form():
                nonlocal current_edit_index
                current_edit_index = None
                ip_var.set('')
                own_login_var.set('')
                own_password_var.set('')
                own_password_confirm_var.set('')
                others_login_var.set('login')
                others_password_var.set('password')
                others_password_confirm_var.set('password')

            def add_server():
                try:
                    ip = ip_var.get().strip()
                    own_login = own_login_var.get().strip()
                    own_password = own_password_var.get().strip()
                    own_password_confirm = own_password_confirm_var.get().strip()
                    others_login = others_login_var.get().strip()
                    others_password = others_password_var.get().strip()
                    others_password_confirm = others_password_confirm_var.get().strip()

                    if not all([ip, own_login, own_password]):
                        messagebox.showwarning("Missing Fields", "Please fill in IP, Own Login, and Own Password")
                        return

                    # Validate password confirmations
                    if own_password != own_password_confirm:
                        messagebox.showerror("Error", "Own Password and Confirm Own Password do not match!")
                        return
                    if others_password != others_password_confirm:
                        messagebox.showerror("Error", "Others Password and Confirm Others Password do not match!")
                        return

                    # Load config
                    if os.path.exists(config_file):
                        with open(config_file, 'r') as f:
                            config = json.load(f)
                    else:
                        config = {"nodes": [], "remote_server": []}

                    # Add new server matching JSON structure
                    new_server = {
                        "ip": ip,
                        "own_login": own_login,
                        "own_password": own_password,
                        "others_remote_login": others_login,
                        "others_remote_password": others_password
                    }

                    if "remote_server" not in config:
                        config["remote_server"] = []

                    if current_edit_index is not None:
                        # Edit existing server
                        config["remote_server"][current_edit_index] = new_server
                        action = "updated"
                    else:
                        # Add new server
                        config["remote_server"].append(new_server)
                        action = "added"

                    # Save config
                    with open(config_file, 'w') as f:
                        json.dump(config, f, indent=2)

                    messagebox.showinfo("Success", f"Remote server '{ip}' {action} successfully!")
                    server_window.destroy()

                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save server: {e}")

            def delete_server():
                selection = servers_listbox.curselection()
                if not selection or not servers:
                    messagebox.showwarning("No Selection", "Please select a server to delete")
                    return

                server_index = selection[0]
                server_ip = servers[server_index].get('ip', 'Unknown')
                
                if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete server '{server_ip}'?"):
                    try:
                        # Load config
                        with open(config_file, 'r') as f:
                            config = json.load(f)
                        
                        # Remove server
                        config["remote_server"].pop(server_index)
                        
                        # Save config
                        with open(config_file, 'w') as f:
                            json.dump(config, f, indent=2)
                        
                        messagebox.showinfo("Success", f"Server '{server_ip}' deleted successfully!")
                        server_window.destroy()
                        
                    except Exception as e:
                        messagebox.showerror("Error", f"Failed to delete server: {e}")

            # Bind double-click to load for editing
            servers_listbox.bind('<Double-Button-1>', lambda e: load_server_for_edit())

            # Buttons
            btn_frame = tk.Frame(config_frame, bg=self.theme_colors['card_bg'])
            btn_frame.pack(fill='x', padx=20, pady=10)

            tk.Button(btn_frame, text="Add New", command=clear_form,
                     bg=self.theme_colors['info'], fg='white', font=('Arial', 10, 'bold'),
                     padx=15, pady=5).pack(side='left', padx=5)

            tk.Button(btn_frame, text="Load Selected", command=load_server_for_edit,
                     bg=self.theme_colors['warning'], fg='white', font=('Arial', 10, 'bold'),
                     padx=15, pady=5).pack(side='left', padx=5)

            tk.Button(btn_frame, text="Save Server", command=add_server,
                     bg=self.theme_colors['success'], fg='white', font=('Arial', 10, 'bold'),
                     padx=15, pady=5).pack(side='left', padx=5)

            tk.Button(btn_frame, text="Delete Selected", command=delete_server,
                     bg=self.theme_colors['error'], fg='white', font=('Arial', 10, 'bold'),
                     padx=15, pady=5).pack(side='left', padx=5)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to open server manager: {e}")

    def backup_json_config(self):
        """Enhanced Backup/Restore JSON configuration files"""
        try:
            # Create backup/restore dialog
            backup_window = tk.Toplevel(self.root)
            backup_window.title("Backup & Restore Configuration")
            backup_window.geometry("600x500")
            backup_window.configure(bg=self.theme_colors['bg'])
            backup_window.transient(self.root)
            backup_window.grab_set()

            # Header
            header_frame = tk.Frame(backup_window, bg=self.theme_colors['bg'])
            header_frame.pack(fill='x', padx=20, pady=15)

            tk.Label(header_frame, text="💾 BACKUP & RESTORE CONFIGURATION",
                    font=('Arial', 14, 'bold'), bg=self.theme_colors['bg'],
                    fg=self.theme_colors['primary_text']).pack()

            # Current config info
            info_frame = tk.LabelFrame(backup_window, text="📄 Current Configuration",
                                     font=('Arial', 12, 'bold'), bg=self.theme_colors['card_bg'],
                                     fg=self.theme_colors['primary_text'])
            info_frame.pack(fill='x', padx=20, pady=10)

            info_text = tk.Text(info_frame, height=6, bg=self.theme_colors['display_bg'],
                              fg=self.theme_colors['display_text'], font=('Arial', 10))
            info_text.pack(fill='x', padx=10, pady=10)

            # Show current config info
            if os.path.exists("master_config.json"):
                try:
                    with open("master_config.json", 'r') as f:
                        config = json.load(f)
                        nodes_count = len(config.get("nodes", []))
                        servers_count = len(config.get("remote_server", []))
                        info_text.insert(tk.END, f"Current Configuration:\n")
                        info_text.insert(tk.END, f"- Nodes: {nodes_count}\n")
                        info_text.insert(tk.END, f"- Remote Servers: {servers_count}\n")
                        info_text.insert(tk.END, f"- File Size: {os.path.getsize('master_config.json')} bytes\n")
                        info_text.insert(tk.END, f"- Last Modified: {os.path.getmtime('master_config.json')}")
                except:
                    info_text.insert(tk.END, "Error reading current configuration")
            else:
                info_text.insert(tk.END, "No master_config.json file found")

            # Available backups
            backup_frame = tk.LabelFrame(backup_window, text="📋 Available Backups",
                                       font=('Arial', 12, 'bold'), bg=self.theme_colors['card_bg'],
                                       fg=self.theme_colors['primary_text'])
            backup_frame.pack(fill='both', expand=True, padx=20, pady=(10, 5))

            backup_listbox = tk.Listbox(backup_frame, bg=self.theme_colors['display_bg'],
                                      fg=self.theme_colors['display_text'], font=('Arial', 10))
            backup_listbox.pack(fill='both', expand=True, padx=10, pady=10)

            # Find backup files
            import glob
            from datetime import datetime
            backup_files = glob.glob("config_backup_*.json")
            backup_files.sort(reverse=True)  # Most recent first

            for backup_file in backup_files:
                # Extract timestamp and format it
                try:
                    # Extract timestamp from filename like "config_backup_20250929_054014.json"
                    timestamp_str = backup_file.replace("config_backup_", "").replace(".json", "")
                    if len(timestamp_str) == 15:  # YYYYMMDD_HHMMSS format
                        date_part = timestamp_str[:8]
                        time_part = timestamp_str[9:]
                        
                        # Parse the timestamp
                        dt = datetime.strptime(timestamp_str, "%Y%m%d_%H%M%S")
                        formatted_date = dt.strftime("%d/%m/%Y - %I:%M %p")
                        
                        display_text = "formatted_date ({backup_file})"
                    else:
                        display_text = backup_file
                except:
                    display_text = backup_file
                
                backup_listbox.insert(tk.END, display_text)

            def create_backup():
                try:
                    import shutil
                    from datetime import datetime
                    
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    backup_name = f"config_backup_{timestamp}.json"
                    
                    if os.path.exists("master_config.json"):
                        shutil.copy2("master_config.json", backup_name)
                        messagebox.showinfo("Backup Complete", f"Configuration backed up to:\n{backup_name}")
                        backup_window.destroy()
                    else:
                        messagebox.showwarning("No Config", "No master_config.json file found to backup")
                except Exception as e:
                    messagebox.showerror("Backup Error", f"Failed to backup configuration: {e}")

            def restore_backup():
                selection = backup_listbox.curselection()
                if not selection:
                    messagebox.showwarning("No Selection", "Please select a backup file to restore")
                    return

                backup_file = backup_files[selection[0]]
                
                if messagebox.askyesno("Confirm Restore", 
                                     f"Are you sure you want to restore from:\n{backup_file}\n\n"
                                     f"This will overwrite the current configuration!"):
                    try:
                        import shutil
                        # Create a backup of current config before restoring
                        if os.path.exists("master_config.json"):
                            from datetime import datetime
                            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                            shutil.copy2("master_config.json", f"config_backup_before_restore_{timestamp}.json")
                        
                        # Restore the selected backup
                        shutil.copy2(backup_file, "master_config.json")
                        messagebox.showinfo("Restore Complete", f"Configuration restored from:\n{backup_file}")
                        backup_window.destroy()
                    except Exception as e:
                        messagebox.showerror("Restore Error", f"Failed to restore configuration: {e}")

            # Buttons
            btn_frame = tk.Frame(backup_window, bg=self.theme_colors['bg'])
            btn_frame.pack(fill='x', padx=20, pady=(5, 15))

            tk.Button(btn_frame, text="💾 Create Backup", command=create_backup,
                     bg=self.theme_colors['success'], fg='white', font=('Arial', 10, 'bold'),
                     padx=15, pady=5).pack(side='left', padx=5)

            tk.Button(btn_frame, text="🔄 Restore Selected", command=restore_backup,
                     bg=self.theme_colors['warning'], fg='white', font=('Arial', 10, 'bold'),
                     padx=15, pady=5).pack(side='left', padx=5)

            def view_config():
                selection = backup_listbox.curselection()
                if not selection:
                    messagebox.showwarning("No Selection", "Please select a backup file to view")
                    return

                backup_file = backup_files[selection[0]]
                
                try:
                    with open(backup_file, 'r') as f:
                        config = json.load(f)
                    
                    # Create view window
                    view_window = tk.Toplevel(backup_window)
                    view_window.title(f"View Config - {backup_file}")
                    view_window.geometry("500x400")
                    view_window.configure(bg=self.theme_colors['bg'])
                    
                    # Header
                    header = tk.Label(view_window, text=f"📄 CONFIG PREVIEW: {backup_file}",
                                    font=('Arial', 12, 'bold'), bg=self.theme_colors['bg'],
                                    fg=self.theme_colors['primary_text'])
                    header.pack(pady=10)
                    
                    # Content
                    text_widget = tk.Text(view_window, bg=self.theme_colors['display_bg'],
                                        fg=self.theme_colors['display_text'], font=('Arial', 10))
                    text_widget.pack(fill='both', expand=True, padx=20, pady=10)
                    
                    # Show config summary
                    nodes = config.get("nodes", [])
                    servers = config.get("remote_server", [])
                    
                    content = f"CONFIGURATION SUMMARY:\n"
                    content += "'='*50\n\n"
                    content += f"📊 NODES ({len(nodes)} total):\n"
                    for i, node in enumerate(nodes, 1):
                        content += f"  {i}. {node.get('name', 'Unknown')} ({node.get('type', 'unknown')}) - {node.get('ip', 'No IP')}\n"
                    
                    content += f"\n🌐 REMOTE SERVERS ({len(servers)} total):\n"
                    for i, server in enumerate(servers, 1):
                        content += f"  {i}. {server.get('ip', 'Unknown')} (Login: {server.get('own_login', 'Unknown')})\n"
                    
                    content += f"\n📄 RAW JSON:\n"
                    content += "'='*50\n"
                    content += json.dumps(config, indent=2)
                    
                    text_widget.insert(tk.END, content)
                    text_widget.config(state='disabled')
                    
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to view config: {e}")

            tk.Button(btn_frame, text="👁️ View Config", command=view_config,
                     bg=self.theme_colors['info'], fg='white', font=('Arial', 10, 'bold'),
                     padx=15, pady=5).pack(side='left', padx=5)

            tk.Button(btn_frame, text="Close", command=backup_window.destroy,
                     bg=self.theme_colors['error'], fg='white', font=('Arial', 10, 'bold'),
                     padx=15, pady=5).pack(side='right', padx=5)

        except Exception as e:
            messagebox.showerror("Backup Error", f"Failed to open backup manager: {e}")

    def analyze_debug_logs(self):
        """ENHANCED: Analyze debug logs for patterns and issues"""
        try:
            # Get current debug content
            debug_content = self.debug_display.get(1.0, tk.END)
            
            # Analysis results
            analysis = []
            lines = debug_content.split('\n')
            
            # Count different log types
            error_count = len([line for line in lines if '❌' in line])
            warning_count = len([line for line in lines if '[WARNING]' in line])
            info_count = len([line for line in lines if 'ℹ️' in line])
            system_count = len([line for line in lines if '[SYSTEM]' in line])
            network_count = len([line for line in lines if '[NETWORK]' in line])
            
            analysis.append("📊 LOG ANALYSIS RESULTS:")
            analysis.append(f"[RED] Errors: {error_count}")
            analysis.append(f"⚠️ Warnings: {warning_count}")
            analysis.append(f"ℹ️ Info: {info_count}")
            analysis.append(f"🖥️ System: {system_count}")
            analysis.append(f"🌐 Network: {network_count}")
            analysis.append("")
            
            # Find recent issues
            recent_errors = [line for line in lines[-50:] if '❌' in line]
            if recent_errors:
                analysis.append("🚨 RECENT ERRORS:")
                for error in recent_errors[-3:]:  # Last 3 errors
                    analysis.append(f"- {error.strip()}")
            else:
                analysis.append("✅ No recent errors found")
            
            # Display analysis in popup window
            analysis_text = '\n'.join(analysis)
            messagebox.showinfo("📊 Log Analysis Results", analysis_text)
            
        except Exception as e:
            messagebox.showerror("Analysis Error", f"Failed to analyze logs: {e}")

    def filter_debug_logs(self):
        """ENHANCED: Filter debug logs by type"""
        try:
            # Create filter dialog
            filter_window = tk.Toplevel(self.root)
            filter_window.title("Filter Debug Logs")
            filter_window.geometry("400x300")
            filter_window.configure(bg=self.theme_colors['bg'])
            filter_window.transient(self.root)
            filter_window.grab_set()

            # Filter options
            filter_vars = {}
            filter_types = ['ERROR', 'WARNING', 'INFO', 'SYSTEM', 'NETWORK']
            
            tk.Label(filter_window, text="Select log types to show:",
                    font=('Arial', 12, 'bold'), bg=self.theme_colors['bg'],
                    fg=self.theme_colors['primary_text']).pack(pady=10)

            for log_type in filter_types:
                var = tk.BooleanVar(value=True)
                filter_vars[log_type] = var
                tk.Checkbutton(filter_window, text=f"[{log_type}]", variable=var,
                             font=('Arial', 10), bg=self.theme_colors['bg'],
                             fg=self.theme_colors['primary_text']).pack(anchor='w', padx=20)

            def apply_filter():
                try:
                    # Get selected types
                    selected_types = [t for t, v in filter_vars.items() if v.get()]
                    
                    if not selected_types:
                        messagebox.showwarning("No Selection", "Please select at least one log type")
                        return
                    
                    # Filter logs
                    all_content = self.debug_display.get(1.0, tk.END)
                    lines = all_content.split('\n')
                    
                    filtered_lines = []
                    for line in lines:
                        if any(f'[{log_type}]' in line for log_type in selected_types):
                            filtered_lines.append(line)
                    
                    # Update display
                    self.debug_display.config(state='normal')
                    self.debug_display.delete(1.0, tk.END)
                    self.insert_themed_text(self.debug_display, '\n'.join(filtered_lines), 'info')
                    self.debug_display.config(state='disabled')
                    
                    filter_window.destroy()
                    
                except Exception as e:
                    messagebox.showerror("Filter Error", f"Failed to apply filter: {e}")

            tk.Button(filter_window, text="Apply Filter", command=apply_filter,
                     bg=self.theme_colors['success'], fg='white',
                     font=('Arial', 10, 'bold'), padx=20, pady=5).pack(pady=20)

        except Exception as e:
            messagebox.showerror("Filter Error", f"Failed to open filter dialog: {e}")

    def apply_log_filter(self):
        """Apply log filter based on selected types"""
        try:
            if not hasattr(self, 'log_filter_vars'):
                return
                
            # Get selected types
            selected_types = [t for t, v in self.log_filter_vars.items() if v.get()]
            
            if not selected_types:
                # If nothing selected, show all
                selected_types = list(self.log_filter_vars.keys())
            
            # Read from log file for fresh content
            log_file = os.path.join("logs", "professional_launcher.log")
            if os.path.exists(log_file):
                with open(log_file, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
            else:
                lines = []
            
            # Filter lines based on selected types
            filtered_lines = []
            for line in lines:
                # Check if line contains any of the selected log types
                if any(f'[{log_type}]' in line for log_type in selected_types):
                    filtered_lines.append(line.strip())
                # Also include lines without any log type tag (like headers)
                elif not any(f'[{t}]' in line for t in ['ERROR', 'WARNING', 'INFO', 'SYSTEM', 'NETWORK', 'DASHBOARD', 'PROCESSES', 'SPACE', 'DEBUG']):
                    filtered_lines.append(line.strip())
            
            # Update display with color coding
            if hasattr(self, 'debug_display'):
                self.debug_display.config(state='normal')
                self.debug_display.delete(1.0, tk.END)
                
                # Add header
                header = f"🔍 Quick Filter Applied ({len(filtered_lines)} lines)\n"
                header += f"Types: {', '.join(selected_types)}\n"
                header += "="*60 + "\n"
                self.insert_themed_text(self.debug_display, header, 'highlight')
                
                # Add filtered lines with proper color coding
                for line in filtered_lines[-100:]:  # Show last 100
                    # Determine correct color tag
                    if '[ERROR]' in line or '❌' in line:
                        tag = 'error'
                    elif '[WARNING]' in line:
                        tag = 'warning'
                    elif '✅' in line or '[LAUNCH]' in line:
                        tag = 'success'
                    elif '[DASHBOARD]' in line:
                        tag = 'DASHBOARD'
                    elif '[PROCESSES]' in line:
                        tag = 'PROCESSES'
                    elif '[SPACE]' in line:
                        tag = 'SPACE'
                    elif '[DEBUG]' in line:
                        tag = 'DEBUG'
                    elif '[SYSTEM]' in line:
                        tag = 'highlight'
                    elif '[NETWORK]' in line:
                        tag = 'info'
                    elif '[INFO]' in line or 'ℹ️' in line:
                        tag = 'info'
                    else:
                        tag = 'primary'
                    self.insert_themed_text(self.debug_display, line, tag)
                
                self.debug_display.config(state='disabled')
                
                # Update statistics
                self.update_log_statistics(filtered_lines)
                
                # FIXED: Prevent auto-refresh from resetting filters
                self.filters_active = True
                
        except Exception as e:
            log_message(f"Error applying log filter: {e}", "ERROR")

    def update_log_statistics(self, lines=None):
        """Update log statistics display - REMOVED (statistics display removed)"""
        # Statistics display was removed from UI - this method is now a no-op
        pass

    def apply_advanced_filter(self):
        """Apply advanced filtering with time range and keywords"""
        try:
            time_range = self.time_filter_var.get()
            keyword = self.keyword_filter_var.get().strip()
            
            # Get selected basic filters
            selected_types = [t for t, v in self.log_filter_vars.items() if v.get()]
            
            if not selected_types:
                selected_types = list(self.log_filter_vars.keys())
            
            # Get debug content
            if hasattr(self, 'debug_display'):
                # Read from log file for fresh content
                log_file = os.path.join("logs", "professional_launcher.log")
                if os.path.exists(log_file):
                    with open(log_file, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                else:
                    lines = []
                
                # Apply time filter
                from datetime import datetime, timedelta
                now = datetime.now()
                
                if time_range == "Last Hour":
                    cutoff = now - timedelta(hours=1)
                elif time_range == "Last 4 Hours":
                    cutoff = now - timedelta(hours=4)
                elif time_range == "Today":
                    cutoff = now.replace(hour=0, minute=0, second=0, microsecond=0)
                else:  # All Time
                    cutoff = None
                
                filtered_lines = []
                for line in lines:
                    # Type filter
                    if not any(f'[{log_type}]' in line for log_type in selected_types):
                        if any(f'[{t}]' in line for t in ['ERROR', 'WARNING', 'INFO', 'SYSTEM', 'NETWORK']):
                            continue
                    
                    # Keyword filter
                    if keyword and keyword.lower() not in line.lower():
                        continue
                    
                    # Time filter (basic - just include if no timestamp parsing)
                    filtered_lines.append(line)
                
                # Update display
                self.debug_display.config(state='normal')
                self.debug_display.delete(1.0, tk.END)
                
                if filtered_lines:
                    header = f"🔍 Advanced Filter Results ({len(filtered_lines)} lines)\n"
                    header += f"Time: {time_range}, Types: {', '.join(selected_types)}"
                    if keyword:
                        header += f", Keyword: '{keyword}'"
                    header += "\n" + "="*60 + "\n"
                    
                    self.insert_themed_text(self.debug_display, header, 'highlight')
                    for line in filtered_lines[-100:]:  # Show last 100 matches
                        line = line.strip()
                        # Determine correct color tag based on content
                        if '[ERROR]' in line or '❌' in line:
                            tag = 'error'
                        elif '[WARNING]' in line:
                            tag = 'warning'
                        elif '✅' in line or '[LAUNCH]' in line:
                            tag = 'success'
                        elif '[DASHBOARD]' in line:
                            tag = 'DASHBOARD'
                        elif '[PROCESSES]' in line:
                            tag = 'PROCESSES'
                        elif '[SPACE]' in line:
                            tag = 'SPACE'
                        elif '[DEBUG]' in line:
                            tag = 'DEBUG'
                        elif '[SYSTEM]' in line:
                            tag = 'highlight'
                        elif '[NETWORK]' in line:
                            tag = 'info'
                        elif '[INFO]' in line or 'ℹ️' in line:
                            tag = 'info'
                        else:
                            tag = 'primary'
                        self.insert_themed_text(self.debug_display, line, tag)
                else:
                    self.insert_themed_text(self.debug_display, "No matches found for the specified filters.", 'warning')
                
                self.debug_display.config(state='disabled')
                
                # FIXED: Prevent auto-refresh from resetting advanced filters
                self.filters_active = True
                
        except Exception as e:
            messagebox.showerror("Filter Error", f"Failed to apply advanced filter: {e}")

    def reset_keyword_filter(self):
        """Reset keyword filter and refresh logs"""
        try:
            # Clear keyword field
            if hasattr(self, 'keyword_filter_var'):
                self.keyword_filter_var.set("")
            
            # Reset filter flags
            self.filters_active = False
            self.search_results_active = False
            
            # Refresh logs to show all content
            self.refresh_debug_logs()
            
            log_message("↺ Keyword filter reset", "INFO")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to reset keyword filter: {e}")
    
    def select_all_debug_filters(self):
        """Select all debug log filter checkboxes"""
        try:
            if hasattr(self, 'log_filter_vars'):
                for var in self.log_filter_vars.values():
                    var.set(True)
            log_message("✅ All debug filters selected", "INFO")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to select filters: {e}")
    
    def clear_all_filters(self):
        """Clear all filters - UNCHECK all checkboxes"""
        try:
            # UNCHECK all checkboxes (set to False)
            if hasattr(self, 'log_filter_vars'):
                for var in self.log_filter_vars.values():
                    var.set(False)
            
            # Clear advanced filter fields
            if hasattr(self, 'time_filter_var'):
                self.time_filter_var.set("All Time")
            if hasattr(self, 'keyword_filter_var'):
                self.keyword_filter_var.set("")
            if hasattr(self, 'log_search_var'):
                self.log_search_var.set("")
            
            # Reset filter flags
            self.filters_active = False
            self.search_results_active = False
            
            log_message("✅ All filters cleared - checkboxes unchecked", "INFO")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to clear filters: {e}")

def main():
    """Main execution function"""
    try:
        # Auto cleanup if enabled
        if app_settings.get('auto_cleanup_on_start', True):
            cleaned = cleanup_old_logs(app_settings['log_retention_days'])
        
        # Setup working directory
        setup_working_directory()
        
        # Create main window
        root = tk.Tk()
        root.title("Node Automation Launcher")
        
        # Create application
        app = NodeAutomationLauncher(root)

        # Start GUI event loop
        root.mainloop()

    except KeyboardInterrupt:
        log_message("Application interrupted by user", "SYSTEM")
    except Exception as e:
        import traceback
        traceback.print_exc()
        log_message(f"Critical error in main: {e}", "CRITICAL")
    finally:
        log_message("Node Automation Launcher shutdown", "SYSTEM")

if __name__ == "__main__":
    main()
