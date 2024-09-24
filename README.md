# PDFTOCSV
## Download Tesseract locally

windows - https://github.com/UB-Mannheim/tesseract/releases/download/v5.4.0.20240606/tesseract-ocr-w64-setup-5.4.0.20240606.exe

mac - 
```sudo port install tesseract```

## Setup Environment path variables

Add the location of dowanlaoded file into the system environment varaibles as path. Restart your system to fix this.

## Make an empty directory and open it in your code editor

Open in VS code and run the following to pull all the files from this repo

`git init`

`git remote add origin https://github.com/Darshanshetty0/pdftocsv.git`

`git pull origin main`

`git status`

If everything was successfull, you should see the following output in your terminal:

`On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean
`

## Setup the files to run loaclly

Run these following to setup your django app

`cd myimgtocsv`

`pip install django pytesseract`

`python manage.py runserver`

open the localhost server in any browser, you should get the following:
![image](https://github.com/user-attachments/assets/ef47bf39-4df4-46d9-81f6-33001a87d992)

