1) Install Google USB Driver (usb_driver) folder
2) Using powershell or cmd type : abd
3) Make Sure that your android device is connected and USB Debugging is on
4) Verify by typing : abd devices (in the cmd or powershell)
5) adb shell dumpsys -----> to get all info about the device
6) adb shell dumpsys location -----> only to get the final location details
7) adb shell dumpsys location  findstr gps Lo" -----> filtering the important info such as the longitude & latitude


-----------------------------------------------
Powershell Script to get the location every 1 sec
-----------------------------------------------

while ($true) {
    $location = adb shell dumpsys location | Select-String "last location="
    if ($location) {
        foreach ($loc in $location) {
            $fields = $loc -split "[=\[\],]+"
            if ($fields.Length -gt 2) {
                $latitude = $fields[3]
                $longitude = $fields[4]
                Write-Output "Latitude: $latitude, Longitude: $longitude"
            }
        }
    }
    Start-Sleep -Seconds 1
}

================================================

GPSTracking.py

Is a python script that accomplishes the same task of extracting and displaying GPS coordinates from the output of the adb shell dumpsys location command.


================================================

OpenMaps.py

Full script that gets the location via ADB , Apply it to GoogleMaps and then sends it to a certain phone number on whatsapp.
