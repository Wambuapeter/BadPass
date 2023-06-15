# BadPass

BadPass is a Django-based web application that helps users securely store and manage their passwords.

## Features

- User Registration and Authentication: Users can create an account and securely log in to the password manager using an OTP sent to your email.
- Password Storage: Users can store their passwords securely, ensuring they are encrypted and protected.
- Password Generation: Generate strong and secure passwords automatically, following specific requirements.
- Password Strength Analysis: Evaluate the strength of user passwords and provide feedback on their complexity.
- Two-Factor Authentication (2FA): Enhance security by integrating an additional layer of authentication.
- Password Expiration and Reminders: Set password expiration dates and receive reminders to update passwords regularly.
- Password History and Versioning: Maintain a history of previously used passwords to prevent reuse.
- Secure Password Recovery: Allow users to recover their passwords securely if they forget them.

## Installation

1. Clone the repository:

git clone https://github.com/Wambuapeter/BadPass.git

2. Create a virtual environment and activate it:

Refer to AutoDjango/README.md

3. Install the dependencies:

pip3 install -r requirements.txt

4. Run the server

python3 manage.py runserver

5. Open your web browser and navigate to `http://localhost:8000` to access BadPass password manager.

## Configuration

- Configure the SMTP EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD settings in the Django `settings.py` file for sending account verification emails.
- Update the `KEY` in `settings.py` with a unique and secure secret key for your application.

## Contributing

Contributions to the Password Manager project are welcome! If you find any issues or have suggestions for new features, please submit them through GitHub issues. You can also contribute by creating pull requests with bug fixes or enhancements.

## Support

If you have any questions or need assistance with the Password Manager project, feel free to reach out to me at peterwambua025@gmail.com.

Enjoy using the Password Manager to secure and manage your passwords effectively!
