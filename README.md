# Find a Coach

Focus on coaching and Find a Coach will manage your coaching sessions.

## Roadmap

### Next steps

- Nasadenie na prod
- Kúpa domény a presmerovanie domény
- Sprovoznenie admina
- Vytvorenie datového modelu - návrh a realizácia
- Switch na sqlite

#### Datový model

Mentor

- meno a priezvisko
- odmentorovaných hodín

Klient:

- odkaz na mentora
- objednané, dodané hodiny
- datumy a časy lekcií
- ďalšia lekcia, zadanie vš. lekcií
- celkové ciele
- posledná prebraná téma
- domáca úloha
- plán na ďalšiu tému

Lekcia:

- odkaz na klienta
- odkaz na mentora
- dátum a čas
- poznámky
- plán na ďalšiu lekciu
- domáca úloha

#### Future

- lokalizácia rozhrania

## Tips and Tricks

Open local terminal:

- Using the command palette (default ctrl+shift+p/cmd+shift+p), there is an option
- Terminal: Create New Integrated Terminal (local)

## How to run Django management commands

Execution in the docker image
'./manage.py showmigrations'

Or from integrated terminal
'docker compose -f docker-compose.local.yml run --rm django python manage.py showmigrations'

## Technical notes

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

### Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

### Basic Commands

#### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      '$ python manage.py createsuperuser'

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

#### Type checks

Running type checks with mypy:

    '$ mypy findacoach'

#### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    '$ coverage run -m pytest'
    '$ coverage html'
    '$ open htmlcov/index.html'

##### Running tests with pytest

    '$ pytest'

#### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

#### Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at <https://sentry.io/signup/?code=cookiecutter> or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

### Deployment

The following details how to deploy this application.

#### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
