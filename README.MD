# ![Instagram Logo](static/images/logo.png)
### By Victor K. Maina
## [See it on Heroku](https://instagram-clone-ip.herokuapp.com/)
---

This project is an Instagram clone built with Django. The application has a UI similar to Instagram's web version.

A running version of this app already deployed on Heroku. [Click here](https://instagram-clone-ip.herokuapp.com/) to use it.

## Installation

The following installations instruction are for Ubuntu.

### Setup

To run this application, you will need Python, Git and Postgresql on your system.

```sh
sudo apt install python3 git postgresql
```

Once that is done, clone this repository onto you computer and enter the new directory.

```sh
git clone https://github.com/VictorKMaina/instagram
cd instagram/
```

### Dependencies

The app requires some dependencies to run. To install them, first create a  virtual environment and activate it.

```sh
python3 -m venv env
source env/bin/activate
```

Then install the dependencies using pip.

```sh
pip install -r requirements.txt
```

### Database

Since the app also needs a database to run, we need to set up Postgres.Postgres will need you to create a username and password to access databases. You can follow the steps [here](https://www.postgresql.org/docs/8.0/sql-createuser.html) to get started.

Once you have a Postgres username, enter Postgres using `psql` on your terminal and create a new database.

```sh
psql
```
```postgres
CREATE DATABASE instagram;
```

### Environment Variables

Now that you have a database create, you need to create some environment variables so that Django can use. In the project's root directory, create a `.env` file. Add the following to it, updating it with your own information.

```
SECRET_KEY='<Your Secret Key>'
DEBUG=True
DB_NAME='instagram'
DB_USER='<Your Postgres Username>'
DB_PASSWORD='<Your Postgres Password>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS=['*']
DISABLE_COLLECTSTATIC=1
``` 

### Sendgrid

During the login process, the app sends a confirmation email to a new user. For this to work, it needs to be intergrated with Sendgrid. Here are the steps to generating an API key from Sendgrid's documentation.

>1. Sign up for a [SendGrid account](https://signup.sendgrid.com/)
>
>2. Create and store a SendGrid [API key](https://app.sendgrid.com/settings/api_keys) with full access "Mail Send" permissions.
>
>3. Verify your [Sender Identity](https://sendgrid.com/docs/for-developers/sending-email/sender-identity/)

On step 3, use the quick verification method to verify one email address. Remember this address.

Once you have generated your API key, add it to the environment variables.

```
SENDGRID_API_KEY='<Your Sendgrid API Key>'
```

In the project directory, navigate to `/app/email.py`. Edit the from email property and insert your verified email address.

```python
def send_activation_email(request, user, email_address):
    message = Mail(
        from_email="<Verified Email Address>",
        ...
```

### Migrations

Now that the `.env` file is ready to use, we need to upgrade our database to correspond with the app's models.

```sh
python manage.py migrate
```

## Usage

The app is now ready to run. 

```sh
python managy.py runserver
```

## External Links

1. [User Flow Diagram | Google Drive](https://drive.google.com/file/d/1S_cTUnkkmoTWZXHHpe-mEcUMS8084xsY/view?usp=sharing)
2. [Wireframe | Figma.com](https://www.figma.com/file/Vyoaw3cvw24Je2YWYRNRLV/Instagram-Clone?node-id=0%3A1)
2. [ER Diagram | Google Drive](https://drive.google.com/file/d/1wVSowmUe-68efjLQDlviJM2vPng4KTCo/view?usp=sharing)

## [LICENSE](LICENSE/)