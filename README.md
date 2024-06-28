# My Awesome Project

Behold My Awesome Project!

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands
### Running the Vite Dev Server

This app integrates with a Vue frontend located in `vue_frontend`.
##### With PyCharm
The Vite dev server may be runfrom PyCharm using the pre-built run configurations.  First, ensure that 
PyCharm project's Node interpreter is properly set (Languages & Frameworks -> Node.js), then run the run 
configuration named ```npm install```.  After that, run the configuration named `vite dev` to launch Vite dev server.


##### From the console
Alternatively you, may run the Vite dev server directly from the project directory:
```sh
cd vue_frontend
npm install
npm run dev
````

For more information, refer to the [Vue3 Vite Django Cookiecutter project](https://github.com/ilikerobots/cookiecutter-vue-django).



### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy my_awesome_project

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.

### Vue

For production deployment, the Vue frontend must be built into static resources, which will be served
using the same Django staticfiles strategy as the rest of your site.  

If you are using the production Docker configuration, this will be performed automatically when the images are built.  

Otherwise, you must build the static assets yourself as part of your build and deploy process, sometime before the 
`collectstatic` management command is run. The static assets may be built by running `npm run build` from within the 
`vue_frontend` directory. The resulting files will be placed into the `my_awesome_project/static/vue` directory 
and are handled subsequently as standard static assets. 

Note the setting `VUE_FRONTEND_USE_DEV_SERVER` dictates whether your Django app will be expecting to serve Vue assets 
from the Vite Dev Server or from a static build.  This setting defaults to the same as `DEBUG`, but can be modified as 
needed.

For more information, refer to the [Vue3 Vite Django Cookiecutter project](https://github.com/ilikerobots/cookiecutter-vue-django).
