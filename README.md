Task: Present a Wiki written in Django
Time: ~4 hours depending on experience

At the interview the candidate should show a simple wiki system, developed in Python and preferably Django.

* ✅  The Wiki should be able to present the contents of the wiki. (hint: Django views)

* ✅ The Wiki should support links to other pages within the wiki.

* ✅ Each page should have an <edit> button. 

* ✅ A page in edit-mode should have a <save> button.

* ✅ A link to a wiki page should be indicated by [ ], as in [somepage] the name of the page should in this case be somepage

* ✅ A link to a non-existing page should create a new empty page in edit-mode.

Optional bonus points for:

* ✅ Adding a headline to each page.

* Setting a different link color (red) on links which will create a new page.

* ✅ Adding a view counter on pages. 

* Make and use Pytest unitests

* Adding permissions to pages, so only users who are logged in can edit. (But all can view) (hint: Django permissions)

* Adding a search function (hint: __icontains is useful)

* Using Docker

* ✅ Pushing to github

* Deploy in cloud


## Run Project

0. Create and activate virtual environment (https://virtualenv.pypa.io/en/latest/)
1. Install packages
```
pip install requirements.txt
```
2. Run migrations (SQLite will be used for this task purposes)
```
python3 manage.py migrate
```
3. Start locals server
```
python3 manage.py runserver
```