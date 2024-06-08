# Firebase Storage Downloader

Firebase Storage Downloader is a Python script that easily downloads all files from a specific directory in a Firebase Storage bucket to a local folder.

## Features

+ Downloads all files from a specified directory in Firebase Storage.
+ Saves files to a designated folder on your local desktop.
+ Automatically creates the local folder if it doesn't exist.

## Requirements

+ Python 3.x
+ ```firebase-admin``` library

## Installation

+ Clone this repository:
  ```bash
  git clone https://github.com/Gabin221/FirebaseStorageDownloader.git
  cd FirebaseStorageDownloader
  ```
+ Install the required Python packages:
```bash
pip install firebase-admin
```
+ Set up your Firebase credentials:
   + Download your service account key from the Firebase console.
   + Save the key file as **cred.json** in the project directory.

## Usage

+ Update the **source_folder_name** and **bucket_name** variables in the script with your Firebase Storage directory and bucket name.
+ Run the script.
+ All files from the specified Firebase Storage directory will be downloaded to an "images" folder on your desktop.
