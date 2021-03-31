# Travis CI Demo

### Fork this repository

If you are currentlly signed in to your github account and are viewing this from github you can simply click on the fork button in the top left of the page.

### Create a Travis account

Go to [travis-ci.com](https://travis-ci.com/) (not travis-ci.org as this is depriciated and will be shut down at some point) and click sign up and then sign up with your github account.

After signing up you will be redirected to github and propted to allow access from travis-ci. Accept this and return to [travis-ci.com](https://travis-ci.com/). 

In the top right coner there should be a profile icon. Click this to reveal a drop down menu and then click on Settings.

If not already there navigate to the github repositories tab and click the button "Manage repositories on GitHub". This will navigate you back to github and allow you to manage travis-ci's access to your repositories.

Under repository access click on "Only select repositories", select "travis-ci-demo", and then click the green "Aprove and install" button.

This should vnavigate you back to [travis-ci.com](https://travis-ci.com/) where you can verify that the repository is being tracked.

### Create `.travis.yml` file

Now our repository is hooked in to travis-ci but is not running anything yet because we haven't told it what to do. To do this create a file named `.travis.yml` in the base directory (`/path/to/travis-ci-demo/`) of the repository.

This is essentially the instructions for what travis-ci should do and what enviroment(s) to run the tests in.

1. First, tell it you want to use ubuntu 18.04 by adding the line `dist: bionic`.

2. Next, tell it you want to test using the python language by adding the line `language: python`

3. Then, to specify which versions of python we want to run we add a new section labeled `python:` follows by new lines containing the version numbers we want to run written like `  - "<major>.<minor>"`. For this demo we will use versions 3.7 and 3.8 so it should look like the following:

```
python:
  - "3.7"
  - "3.8"
```

4. Now, we have some requirements we need to install. We can do this by adding a new section titled `install:` followed by a new line with the pip install instruction written like `  - pip install -r requirements.txt`. Since the build always starts in the base directory of the repository it will see the requirements.txt file in the current working directory when this is run.

5. Lastly, we need to run out test suite using pytest. we can do this by adding a section `script:` followed by the the pytests comand. Recall that we are in the base directory of the repository and our tests are in the /tests repository so we either need to write the command like `  - pytest -v ./tests/` or we can first cd into the directory and then run pytest like so:
```
script:
  - cd tests
  - pytest -v
```

Now our `.travis.yml` file should look something like the following:

```
dist: bionic
language: python
python:
  - "3.7"
  - "3.8"
install:
  - pip install -r requirements.txt
script:
  - pytest -v ./tests/
```

After pushing these changes travis should start running two builds. (one for 3.7 and one for 3.8) We can navigate to [travis-ci.com](https://travis-ci.com/) to check on the status of those builds. They will first construct the enviroment, install the dependencies, and then run the test suite. THis should be all successful until the test suite is run and then it should pass all but the `test_env_var_txt` test.

### Adding encrypted enviroment variables to travis-ci

If your repository build requires a password or something you don't want included for the world to see you can create an encrypted enviroment variable to your travis build with will not be visable unless you do something like print it out inside your build process/ test suite. 

Navigate to [travis-ci.com](https://travis-ci.com/) click on your profile picture in the upper right of the page, click settings, and then on the repositories tab click on the travis-ci-demo repository.

This should take you to a repository page with build history, etc. on the middle right of the page there should be a "more options" button. Click that to reveal a drop down menu and select "Settings". This should bring you to the repository settings page. 

About midway down the page there should be an enviroment variables section. We are going to add a new enviroment variable named `TRAVIS_ENV_VAR_TEST` with the value `asdf`. Click the add button to create the variable.

Now back at our repository we can edit the `.travis.yml` file and use this enviroment variable to pass our last test.

Right above the `install:` section we can add a `before_install:` section followed by a new line and the command `  - echo ${TRAVIS_ENV_VAR_TEST} > env_var.txt`

Now our `.travis.yml` file should look like the following:

```
dist: bionic
language: python
python:
  - "3.7"
  - "3.8"
before_install:
  - echo ${TRAVIS_ENV_VAR_TEST} > env_var.txt
install:
  - pip install -r requirements.txt
script:
  - pytest -v ./tests/
```

After pushing this our next builds should both pass.
