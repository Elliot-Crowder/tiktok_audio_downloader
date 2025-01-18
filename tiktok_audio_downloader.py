import ijson
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# need to make it so that if a url is invalid then it just goes on to the next one
import re

basePath = "https://www.tiktok.com/music/song-"
#https://www.tiktok.com/music/song-6976649967591802882
def grabUrlId(url:str):
    match = re.search(r'/(\d+)\.html$',url)
    return match.group(1) if match else "";


def buildSongUrl(Badurl:str):
    return basePath+str(grabUrlId(Badurl))

# Function to download TikTok audio
def download_tiktok_audio(tiktok_url,driver): 
    try:

        # type in url
        urlInput = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'link_url')))
        #sendUrl to input field
        urlInput.send_keys(tiktok_url)


        #define xpath expression for locating download button
        download_redirect_expression = "//button[contains(@class, btn) and contains(@class, orange) and text()='Download']"
        #identify the download redirect button
        downloadRedirectButton = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,download_redirect_expression)))
        
        #click the button
        downloadRedirectButton.click()


        blockPopup()
        #download the mp3
        download_button_expression = "//a[contains(@class, btn) and contains(@class, orange) and contains(@class,download) and text()='Download MP3' and @data-event='mp3_download_click']"
        downloadButton = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,download_button_expression)))
        downloadButton.click()
        blockPopup()

        #navigate back to the start menu
        download_anothermp3_button_expression = ""
        download_anothermp3_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,download_anothermp3_button_expression)))
        download_anothermp3_button.click()
        time.sleep(5)
    except Exception as e:
        print(e)
    finally:
        driver.quit



def blockPopup(driver, timeout=10):
    try:
        modal = WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.CLASS_NAME, "modal")))

        if modal:

            close_button_expression = "//a[contains(@class, btn) and contains(@class, orange) and contains(@class,modal-close) and text()='Close']"
            close_button = WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,close_button_expression)))
            close_button.click()
            print("Modal closed successfully")
    except:
        print("no modal found or timed out")


def main(download_folder):
    options = Options()
    options.add_experimental_option("prefs", {
  "download.default_directory": download_folder,
  "download.prompt_for_download":False,
  "safebrowsing.enabled":True,
  "excludeSwitches": ["disable-popup-blocking"]
  })
    
    options.add_extension('cjpalhdlnbpafiamejdnhcphjbkeiagm.crx')

    #initialize web driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    try:
        #load page
        driver.get("https://musicaldown.com/")


        with open('./user_data_tiktok.json', 'r', encoding='utf-8') as data:
            favorites = ijson.items(data, 'Activity.Favorite Sounds.FavoriteSoundList.item')
            for sound in favorites:
                songUrl = buildSongUrl(sound["Link"])
                print(songUrl)

    except FileNotFoundError as e:
        print(e)
        print('File not found in working directory')
    except Exception as e:
        print('bad stuff happened')
        print(e)



    


# Example usage:
if __name__ == "__main__":
    download_folder = input("Enter the path to the directory you would like your files to be downloaded to: ")
    # download_folder = r"D:\My Desktop\music\tiktok audios"  # Set your download folder path here
    main(download_folder)
    # tiktok_url = "https://www.tiktok.com/t/ZT2eAVa2G/"  # Replace with your TikTok audio URL
   
    # download_tiktok_audio(tiktok_url, download_folder)