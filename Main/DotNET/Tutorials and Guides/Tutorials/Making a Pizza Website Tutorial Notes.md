After having made a new project and added a page 'Pizza', we are now ready to make a data model to perform operations on. 
A *model* class is needed to represent a pizza in inventory. The model contains properties that represent the characteristics of a pizza. The model is used to pass data in the web app and to persist pizza options in the data store. In this unit, that data store will be a local in-memory caching service. In a real world application, you would consider using a database, such as [[SQL Server]], with [[Entity Framework Core]]. 

## Create a Pizza Model
Run `mkdir Models` and `mkdir Services`.