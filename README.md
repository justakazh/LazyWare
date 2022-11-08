## LazyWare
<img src="img.png">
A Simple Rasomware Generator build using PYTHON.

### Disclaimer !
This tool is for educational purposes only. I am not responsible for your harmful actions!

### Features 
- You can setting target disk/directory
- You can setting icon
- You can setting name of file
- You can setting message for victim
- You can setting target files to encrypt
- Automatic change extension after encrypt
- Automatic generate random key
- Automatic build exe file and source code
- Easy to use

### Installation
``` bash
python -m pip install -r requirements.txt
```
### Depedences
- https://pypi.org/project/colorama/
- https://pypi.org/project/cryptography/
- https://pypi.org/project/pyarmor/
- https://pypi.org/project/pyinstaller/

### Usage
``` bash
python generate.py 
```
#### Settings (Required)

- Insert disk or target folder
  - Target disk or folder for starting point encrypt
- File name
  - Name for file (prize, invoice, game)
- Insert extension for encrypted files.
  - change extension for encrypted files
- Insert Icon
  - Icons for file
- Insert target file extension
  - Target file extension to encrypt (.docx, .pdf, .jpg, .png)
- input readme file
  - Note for victim
