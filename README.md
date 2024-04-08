# Team 13's project for COMP 3220: Object Oriented Analysis Software and Design

**Project Backend (Flask/Python Scripts):** Jovic Panahon, Jacob Bondy, Lena Al-Shehmany, Henok Gebremichael, and Michael Sun.

**Project Frontend (HTML/CSS/JavaScript):** Lena Al-Shehmany, Henok Gebremichael, Michael Sun, and Mishal Siddiqui.

**Project Diagrams (UML):** Yasmin Ismail and Jacob Bondy.

# Instructions on how to install and run.

```bash
git clone https://github.com/jpanahon/comp-3220-project.git
cd comp-3220-project
flask run
```

`app.py` - Main entry point of the website

`tools/parser.py` - Downloads data and passes it off to the data handler class

`tools/data_handler.py` - Sorts the data and put it into the database

`tools/init_db.py` - Initializes the database

`tools/schema.sql` - Initializes the tables of the database

`templates` - Folder that consists of the HTML files for the front end

`static` - Folder that consists of the CSS and image files for the front end

`data` - Folder that consists of subfolders that hold the data used for the database
