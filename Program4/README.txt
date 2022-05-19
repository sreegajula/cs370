Sree Gajula
12/03/2021

python3 gajula-MP4.py --generate-qr
python3 gajula-MP4.py --get-otp

May need to install libraries:
pip3 install --user pillow
pip3 install --user qrcode

I was unable to test this program with the Android GA application. 
While working on this assignment, I first found the qr code library and implemented that to generate a random QR code, and continued to work on getting the right data.
I used a static key for the assignment as that still worked with GA. My OTP function runs in sync with GA to generate the correct code every 30 seconds using the truncate function.
