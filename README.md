# PyRecorder
Screen Recorder using Python `3.10.X`. (uses numpy, cv2 and pyautogui)

## How to use
- Download the `.zip` then extract it to anywhere
- Execute the `recorder.py` file
- Open a localhost (local server) on index.html (using **VSCode LiveServer** or **XAMPP** or opening in your browser)
- Once you have did it, just open the website and there you go!

## How it works
- Take an screenshot of the screen.
- Optimizes it (compress the image and convert to jpg +) resizes to 800x480.
- Saves the screenshot to a folder.
- Removes the last screenshot. (so the folder doesn't get big)
- Updates the website image source every 900ms so it synchronizes perfectly with the screenshots and with the system/local time.
(as the recorder are based on your time)

The screenshots are being taken within a 500ms delay or so, and the final processing time is something around 700ms, 9+7 = 16 so the final FPS is 1.6 (i think)
