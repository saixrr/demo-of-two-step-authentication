# demo-of-two-step-authentication
The code is a Python script using Tkinter for student registration. It validates user inputs for username, password, email, and mobile number. Successful registration allows login via QR code or email-based OTP. User details are displayed in a new window upon successful authentication.
It is just a simple code.you can run it on idle.
The QR code functionality is implemented using the pyqrcode and OpenCV libraries. If the user chooses the QR code option, a QR code is generated containing the password and sent to the user's email address using the smtplib library.
For the OTP option, the script generates a random 4-digit OTP and sends it to the user's email. The user is prompted to enter the received OTP in a new window. If the entered OTP matches the generated one, another window is displayed with the user's details, including their username, password, email, and mobile number.
