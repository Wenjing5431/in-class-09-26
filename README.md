# in-class-09-26

starting point: <https://github.com/umn-5117-f18/in-class-09-19>

docs:

* <http://flask.pocoo.org/docs/1.0/api/>
* <https://medium.com/@thegavrikstory/manage-raw-database-connection-pool-in-flask-b11e50cbad3>


heroku setup:

```
heroku create
heroku addons:create heroku-postgresql:hobby-dev
# use `heroku pg:psql` and run `schema.sql`
git push heroku master
heroku open
```

local setup:

```
# setup
pipenv install
# add
# create .env with datastore connection params (see .env.example)

# run
pipenv shell
heroku local dev
```

heroku commands:

```
heroku logs --tail
heroku pg
heroku pg:psql
```
