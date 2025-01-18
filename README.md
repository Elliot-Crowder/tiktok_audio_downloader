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

---

## Setup Instructions

---

### 1. Install Dependencies

- Install Dependencies and add your **user_data_tiktok.json** to the same directory as the python script.

  - **Install the required dependencies** by running the following command in your terminal or command prompt:

  ```bash
      pip install -r requirements.txt
  ```

### 2. Run the script

- In your console/ command prompt, use the following command:

```python
    python tiktok_audio_downloader.py
```

- inside the console you should be prompted to type in your desired output directory (ie where the mp3 files will be downloaded.) Simply Paste in the path to your directory and the script will download all of your files.

---

## Note

- please ignore console output regarding timeouts. It was included for logging purposes and I am to lazy to remove it.

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

## Contributions

Contributions are welcome! If you'd like to contribute, please feel free to:

- **Submit pull requests** to improve the code or add new features.
- **Submit issues** if you encounter bugs or have suggestions for improvements.
- **Provide recommendations** to enhance the functionality or usability of the project.

### How to Contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes, and write tests if applicable.
4. Commit your changes with clear messages.
5. Push to your forked repository.
6. Open a pull request with a description of your changes.

### Questions?

If you have any questions or need assistance, don't hesitate to ask! You can open an issue, and we will respond as soon as possible.

## Acknowledgements

Thank you to everyone who has contributed to this project! (me)
