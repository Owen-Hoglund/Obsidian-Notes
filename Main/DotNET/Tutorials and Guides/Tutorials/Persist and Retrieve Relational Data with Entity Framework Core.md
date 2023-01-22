# Understanding EF Core
Entity Framework Core is an [[Object-Relational Mapper]] (ORM). ORM's provice a layer between the domain model you implement in code and the database. EF Core is a data access API that allows you to interact with the database using .NET POCO's (Plain Old CLR Objects) and strongly typed [[LINQ]]. This allows you to spend less time translating requests to and from the database and writing SQL, giving you more time to focus on other logic. 

With EF Core, you can:

-   Load data as C# objects (entities).
-   Add, modify, and delete data by calling methods on those entities.
-   Map multiple database tables to a single C# entity.
-   Handle concurrency issues that arise when multiple users simultaneously attempt to update the same record.
-   Use strongly typed Language Integrated Query ([System.Linq](https://learn.microsoft.com/en-us/dotnet/api/system.linq)) syntax to query the database.
-   Access [multiple databases](https://learn.microsoft.com/en-us/ef/core/providers/) including SQL Server, SQLite, Azure Cosmos DB, PostgreSQL, MySQL, and more.
-   Build your domain model from an existing database.
-   Manage your database schema based on your domain model.
-   Commit changes to complex, deep, and/or wide object graphs of related entities with a single method call.

## Review EF Core architecture
![[Pasted image 20230122085404.png]]
The [DbContext](https://learn.microsoft.com/en-us/ef/core/dbcontext-configuration) is a special class that represents a unit of work and provides methods to configure options, connection strings, logging, and the model used to map your domain to the database. Classes deriving from `DbContext`:

-   Represent an active session with the database.
-   Save and query instances of entities.
-   Include properties of type `DbSet<T>` representing tables in the database.

## Manage Database Schemas
EF Core provides two primary ways of keeping your EF Core model and database schema in sync. To choose between the two, decide whether your EF Core model or the database scheme is the *source of truth*. 

### Migrations (Model as the source of truth)

In real world projects, data models change as app features get implemented. As new entities are added and removed, the database schemas need to be changed accordingly. EF Core migrations provide a way to incrementally update the database schema to keep it in sync with the application's data model while preserving existing data in the database.

When a data model change is introduced, the developer uses EF Core tools to add a corresponding migration. EF Core compares the current model against a snapshot of the old model to determine the differences. C# code to implement the changes is generated. The C# files can be modified for custom behaviors or to seed data, and are tracked in your project's source control like any other source file.

Once a new migration has been generated, it can be applied to a database in various ways. EF Core records all applied migrations in a special history table. The history table keeps a record of which migrations have been applied.

### Reverse engineering (Database as the source of truth)

Reverse engineering is the process of scaffolding entity model classes and a `DbContext` class based on a database schema. This approach is often used with existing or shared databases that are managed by a DBA.

# Exercise - Migrations
in this unit, you;; create C# entity classes that will map to tables in a local SQLite database. EF migrations will produce tables from those entities. Migrations provide a way to invrementally update the database schema. 