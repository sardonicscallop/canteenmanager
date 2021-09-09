# canteenmanager

Little project I'm doing for fun in my spare time, with plans to implement in real life. Goal of this project is to automate management over school canteen. It stores basic data about pupils, takes care of their subscriptions, and generates cards with barcodes for each student. Built on flask & postgresql.

Idea of writing this piece of software had grown on mine middle school frustration. I had to attend canteen's accountant each month, to get new ticket. Using this software, this would be completely unnecessary – each pupil would get ticket with barcode representing their identification number only once. Cook, when giving their meal, would just scan it. On computer screen it would be shown if there's active and paid subscription or not, and it'd be noted into database that this particular pupil had taken their meal on this day. I estimate, that it could reduce needed time to service pupils by around ⅓, since there wouldn't be need to mark by pen that pupil had already eaten their meal.

## Functionality overview

At current stage it's still work in progress. Soon it'll have all basic features, like:

* accessing & storing basic personal data of clients
* managing pupils' subscriptions
* 'barcode scanner mode' – automated interface:
  * showing basic personal data (name, surname)
  * showing if there's an active subscription, and if it's paid,
  * annotating in database that meal for today has been taken
* user credentials handling
* basic user management

## Plans for the future

Although the app is usable, it still needs improvement to meet my quality standards. I would like to:

* polish UI
* implement users' roles
* implement classes with possibility of making simple reports for each class
* implement data security measures, like manual and automatic database backup
* implement app update api
* make config accessible for users
* implement first run
* get rid of some junk code, e.g. implementing toolbars api
* get use of JavaScript to make pages more dynamic. For example, implement 'clients' module as a single page.
* remove dependency on wide network connection

## Third party software

This software uses these third-party libraries:

* Bootstrap
* Flask and its dependencies
* KDE Breeze icon set
* psycopg2 database driver
* sqlalchemy and flask-sqlalchemy

For additional legal information, see LICENSE.md.