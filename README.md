#########################################################
# 1. Configure default python interpreter in vscode
#########################################################

# Install "pylance" from vscode extention

# select default python interpreter
Ctrl + Shift + P
...

#########################################################
# 2. Coding & Run
#########################################################

.env
cofig.py
main.py

uvicorn main:app --reload

#########################################################
# 3. Test
#########################################################

# Install package
pip install httpie

# Test with http
http http://localhost:8000


#########################################################
# 4. Init alembic and setup to create db/table
#########################################################

env.py
alembic revision --autogenerate -m "create table"
alembic upgrade head

---
alembic history
alembic downgrade -1


#########################################################
# 5. Add codes
#########################################################

schemas.py
database.py
models.py
crud.py
routers/events.py

#########################################################
# 6. Test with http
#########################################################

# add event
http POST http://localhost:8000/events name="write event" completed=false

# get events
http http://localhost:8000/events

# get event with id
http http://localhost:8000/events/1

# delete event with id
http DELETE http://localhost:8000/events/1

# update event with id and new values set
http PUT http://localhost:8000/events/2 name="Update event" completed=true