import pyautogui
import webbrowser
from time import sleep
import pywhatkit as kit
import subprocess
import pyperclip
import re

phone_number = "+11111111111"
location = ()  # location tuple
def open_google_maps():
    # Open the default web browser and navigate to Google Maps
    webbrowser.open("https://www.google.com/maps")

    # Wait for the browser to open and load the page
    sleep(5)

    # Maximize the browser window (optional, depending on your screen and browser)
    # pyautogui.hotkey('ctrl', 'command', 'f')  # On Mac
    # pyautogui.hotkey('winleft', 'up')  # On Windows


def paste_coordinates(lat, lon):
    # Copy the coordinates to clipboard
    coordinates = f"{lat}, {lon}"
    pyautogui.write(coordinates)
    pyautogui.hotkey('ctrl', 'a')  # Select all
    pyautogui.hotkey('ctrl', 'c')  # Copy to clipboard

    # Click on the Google Maps search box and paste the coordinates
    sleep(5)  # Wait to make sure the page is fully loaded
    pyautogui.click(1623, 160)  # Adjust x, y to where the search box is located
    #pyautogui.hotkey('ctrl', 'v')  # Paste the coordinates
    pyautogui.press('enter')  # Press Enter to search
    sleep(2)
    pyautogui.click(x=1499, y=476)  # click on the share button
    sleep(3)
    pyautogui.click(x=766, y=610)  # copy link
    pyautogui.doubleClick()
    sleep(3)
    try:
        kit.sendwhatmsg_instantly(phone_number, pyperclip.paste())
    finally:
        pass

def get_gps_location():
    global location
    try:
        # using Android Debug Bridge (ADB)
        # adb shell dumpsys location  findstr gps Lo"
        result = subprocess.run(["adb", "shell", "dumpsys", "location"], capture_output=True, text=True)
        output = result.stdout

        # Regex to match lines with last location
        location_pattern = re.compile(r"last location=Location\[(\w+) (\d+\.\d+),(\d+\.\d+)")
        matches = location_pattern.findall(output)

        if matches:
            for match in matches:
                provider, latitude, longitude = match
                print(f"Provider: {provider}, Latitude: {latitude}, Longitude: {longitude}")
                location = (latitude, longitude)
        else:
            print("No location found")

    except subprocess.CalledProcessError as e:
        print(f"Error executing adb command: {e}")

if __name__ == "__main__":
        while True:
        get_gps_location()
        open_google_maps()
        paste_coordinates(float(location[0]), float(location[1]))
        sleep(60) #get the location every Minute
