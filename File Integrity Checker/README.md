 README for File Integrity Checker

---

 File Integrity Checker

This is a simple Python-based application with a GUI that allows users to monitor and verify the integrity of files. By calculating and storing the hash values of files, the application can determine whether a file has been modified, tampered with, or corrupted.

---

 Features
1. Add Files  
   - Add a file to the system, calculate its hash, and store it in a local database (`file_hashes.json`).
2. Verify Integrity  
   - Check if a file is unchanged by comparing its current hash with the stored hash.
3. GUI-Based Interface  
   - User-friendly Tkinter interface with buttons for easy navigation.
4. SHA-256 Hashing  
   - Uses the SHA-256 algorithm for a secure and accurate integrity check.

---

 Technologies Used
- Python 3.x
- Tkinter (for GUI)
- Hashlib (for hash calculations)
- JSON (for database storage)

