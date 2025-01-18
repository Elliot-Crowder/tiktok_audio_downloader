# TikTok Saved Audios Downloader

This project is an **automation script** designed to help TikTok users download all their saved audios. The script utilizes the user's **user_data_tiktok.json** file to identify and retrieve the audios by interfacing with an existing web service.

---

## Features

- Uses the **user_data_tiktok.json** file (not the text export of user data) to identify saved audios.
- Automates interactions with an existing web service to handle the downloading process.
- Saves the downloaded audios to a user-defined output directory.

---

## Prerequisites

### 1. TikTok Data Export

- Obtain your **user_data_tiktok.json** file from TikTok:
  - Go to TikTok settings and request your data export.
  - Once you receive the data, locate the file named `user_data_tiktok.json`.
- This file contains essential metadata about your saved audios.
- Ensure that the file is placed in the **working directory** of the script for it to be accessible.

### 2. Python Version

- This script requires **Python 3.11.5**.
- Verify your Python version by running:
  ```bash
  python --version
  ```

### 3. Setup Instructions

- Install Dependencies and add your **user_data_tiktok.json** to the same directory as the python script.

  - **Install the required dependencies** by running the following command in your terminal or command prompt:

  ```bash
      pip install -r requirements.txt
  ```
