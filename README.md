# PlayerData Interview Exercise

##### Language: Python

### Description

A small application to track runs based on distance and time.
The program also calculates approximate number of calories burned using Léger's formula.

### Environment Variables

|Variable Name | description | default value |
|---|---|---|
|APP_HOST| The host server IP for the application | `localhost` |
|APP_PORT| The port on which the server listens |`8080`|
|LOG_LEVEL| The level of logging to use when running the program | `DEBUG` |
|ENVIRONMENT| The environment in which the application is being run (usually production or development) | `development` |
|DATABASE_URL| The URL for the database, including usename and password | `sqlite:///app.db` |
|DATABASE_LOGGING| Whether or not to enable echo of database calls through SQLAlchemy | `False` |
