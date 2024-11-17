# GPS Location Tracking and Sharing Automation
This project consists of two Python scripts, GPSTracking.py and OpenMaps.py, which are designed to work together to automate the process of extracting, displaying, and sharing GPS coordinates obtained from an Android device. By leveraging the Android Debug Bridge (ADB) and automation libraries, the project simplifies tasks such as location extraction, map navigation, and message sharing via WhatsApp.

## Scripts Overview
### 1. GPSTracking.py: GPS Extraction Tool
This script is a utility for extracting and displaying the GPS coordinates of a connected Android device using the ADB command: adb shell dumpsys location. It parses the output for the most recent location update and logs key details, including the location provider, latitude, and longitude.
#### Key Features:
- Extracts GPS coordinates from the Android device in real-time.
- Uses a regex pattern to identify and parse the location data.
- Outputs the GPS provider, latitude, and longitude to the console.
- Runs continuously with periodic updates (default interval: 1 second).
### 2. OpenMaps.py: GPS Mapping and Sharing Automation
This script extends the functionality of GPSTracking.py by incorporating additional steps to integrate the extracted GPS data into Google Maps and share the location via WhatsApp. It automates the process using tools like PyAutoGUI, PyWhatKit, and Pyperclip.
#### Key Features:
- Extracts GPS coordinates using ADB.
- Opens Google Maps in a web browser and pastes the GPS coordinates into the search bar.
- Shares the Google Maps link for the location via WhatsApp to a specified phone number.
Uses automation to interact with the browser and clipboard for seamless operation.
Runs periodically (default interval: 1 minute) to retrieve and share updated location data.

## Core Dependencies
- Android Debug Bridge (ADB): Used to extract the GPS location from the Android device.
- PyAutoGUI: Automates GUI interactions, such as clicking and typing.
- PyWhatKit: Sends messages via WhatsApp.
- Pyperclip: Manages clipboard operations for copying and pasting text.
- Regular Expressions (re): Parses the ADB output to extract relevant GPS information.
- Webbrowser: Opens Google Maps in the default browser.
- Time and Sleep: Manages periodic execution.

## Use Case
This project is ideal for scenarios where automated location tracking and sharing are required, such as:
- Real-Time Location Monitoring: Continuously fetches and logs GPS data from a device.
- Emergency Sharing: Quickly shares location links via WhatsApp in emergencies.
- Remote Assistance: Sends precise GPS coordinates for navigation assistance.

## How It Works
1. Location Extraction:
- ADB retrieves the device's last known location via the dumpsys location command.
- The script parses the output to extract latitude and longitude.
2. Map Navigation:
- The GPS coordinates are entered into Google Maps through a browser automation process.
- The script retrieves the shareable link for the location.
3. Message Sending:
- The location link is shared via WhatsApp to a predefined phone number using automation tools.

## Limitations and Considerations
Device Connectivity: Requires an Android device connected and ADB enabled.
Screen Resolution: PyAutoGUI coordinates may need adjustment for different screen setups.
Permission Constraints: Ensure necessary permissions are granted on the Android device for GPS access.
WhatsApp Web Login: Requires WhatsApp Web to be pre-configured and logged in on the system.
This project demonstrates the integration of Python scripting, system utilities, and automation libraries to create a robust tool for GPS tracking and sharing.
