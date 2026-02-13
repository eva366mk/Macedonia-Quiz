#!/usr/bin/env python3
"""
Macedonia Quiz Master - Launcher
Simple Python script to start the app and open browser
"""

import subprocess
import webbrowser
import time
import sys
import os

def print_header():
    print("\n" + "="*50)
    print("  Macedonia Quiz Master")
    print("="*50 + "\n")

def main():
    print_header()
    
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Check if venv exists
    venv_path = os.path.join(script_dir, '.venv')
    if not os.path.exists(venv_path):
        print("❌ Virtual environment not found!")
        print("\n📋 Please run SETUP.bat first:")
        print(f"   {os.path.join(script_dir, 'SETUP.bat')}\n")
        input("Press Enter to exit...")
        sys.exit(1)
    
    print("✓ Starting the app...")
    print("  (This may take 10-15 seconds)\n")
    
    # Determine Python executable
    if sys.platform == 'win32':
        python_exe = os.path.join(venv_path, 'Scripts', 'python.exe')
    else:
        python_exe = os.path.join(venv_path, 'bin', 'python')
    
    # Start Streamlit
    try:
        process = subprocess.Popen(
            [python_exe, '-m', 'streamlit', 'run', 'Home.py', '--logger.level=error'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    except FileNotFoundError:
        print("❌ Error: Could not find Python executable")
        input("Press Enter to exit...")
        sys.exit(1)
    
    # Wait for server to start
    print("⏳ Waiting for server to start...")
    time.sleep(8)
    
    # Open browser
    print("🌐 Opening browser...\n")
    webbrowser.open('http://localhost:8501')
    
    print("="*50)
    print("  App is running!")
    print("="*50)
    print("\n✓ Browser should open in a moment")
    print("✓ If not, visit: http://localhost:8501")
    print("\nPress Ctrl+C to stop the app\n")
    
    try:
        process.wait()
    except KeyboardInterrupt:
        print("\n\nShutting down...")
        process.terminate()
        process.wait()

if __name__ == '__main__':
    main()
