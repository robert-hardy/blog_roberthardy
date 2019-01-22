roberthardy.io
====
This repository contains all the content for the site and all blog articles.

It was built following instructions on [Martin Brochhaus's guide](http://martinbrochhaus.com/pelican2.html). You can see Martin's source code in [his GitHub repo](https://github.com/mbrochh/mbrochh-blog).

If you wish to make corrections or amendments or suggestions, please do so via
a pull request.


Installs
----

    brew install python3
    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt

Note: without the `Markdown` install Pelican will seem to work but will not
process markdown files.

Quick start
----

- `make devserver`,
- visit [localhost:8000](http://localhost:8000/),
- force a rebuild with `pelican content`,
- `make github`,
- visit [robert-hardy.github.io/site/](https://robert-hardy.github.io/site/).
