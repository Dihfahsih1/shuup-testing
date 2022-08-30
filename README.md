# Software-Testing-of-Shuup

### Migrate database.
python -m shuup_workbench migrate

### Import some basic data.
python -m shuup_workbench shuup_init

### Create superuser so you can login admin panel
python -m shuup_workbench createsuperuser

### Run the Django development server (on port 8000 by default).
python -m shuup_workbench runserver
