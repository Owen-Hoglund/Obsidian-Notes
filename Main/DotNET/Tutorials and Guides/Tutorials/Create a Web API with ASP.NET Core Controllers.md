To begin, we create the scaffolding for our C# based web API project by creating a new directory and opening it in VSCode, then running the command `dotnet new webapi -f net6.0` [[DotNET CLI Commands#new webapi|(more detail here)]] in the terminal. This will create some files and directories for us. 
Of note:
`Controllers/` - Contains classes with public methods exposed as HTTP endpoints
`Program.cs` - Configures services and the app's HTTP request pipeline, and contains the app;s managed entry point. 
`ContosoPizza.csproj` - Contains configuration metadata for the project

## Build and Test the Web API
run `dotnet run` in the terminal. This could give you some trouble, but look at what the terminal tells you, for example, mine is below
```
info: Microsoft.Hosting.Lifetime[14]
      Now listening on: http://localhost:5105
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Development
```
## The base class: `ControllerBase`
A [[Controller]] is a public class with one or more public methods known as *[[actions]]*. By convention, a controller is placed in the project roots *Controllers* directory. The actions are exposed as HTTP endpoints via routing.  So an HTTP `GET` request to `https://localhost:{PORT}/weatherforecast` causes the `Get()` method of the `WeatherForecastController` class to be executed.

This class inherits from the `ControllerBase` base class. This base class provides a lot of standard functionality for handling HTTP requests. 

## API controller class attributes
```C#
[ApiController]
[Route("[controller]")]
public class WeatherForecastController : ControllerBase
```
`[ApiController]` - enables opinionated behaviors that make it easier to build web APIs. 
`[Route]` - defines the routing pattern `[controller]`. The controller token is replaced by the controllers name (case-insensitive, without the *Controller* suffix)


# Add a data store
Before we implement a web API, we need a data store on which we can perform operations. We need a `model` Class to represent things, in this tutorial we use it to represent a pizza in inventory. In this unit, our data store is going to be a simple local in-memory caching service. In a real world application, we would consider using a database, such as SQL Server, with Entity Framework Core. 

## Create a pizza model
We now make a new directory called Models in our root folder using `mkdir Models`. 
paste in the following code 
```cs
namespace ContosoPizza.Models;

public class Pizza
{
    public int Id { get; set; }
    public string? Name { get; set; }
    public bool IsGlutenFree { get; set; }
}
```
Now we need a data service. We create a directory called Services in the same way as above. Add a file called PizzaService and insert the following code 
```cs
using ContosoPizza.Models;

namespace ContosoPizza.Services;

public static class PizzaService
{
    static List<Pizza> Pizzas { get; }
    static int nextId = 3;
    static PizzaService()
    {
        Pizzas = new List<Pizza>
        {
            new Pizza { Id = 1, Name = "Classic Italian", IsGlutenFree = false },
            new Pizza { Id = 2, Name = "Veggie", IsGlutenFree = true }
        };
    }

    public static List<Pizza> GetAll() => Pizzas;

    public static Pizza? Get(int id) => Pizzas.FirstOrDefault(p => p.Id == id);

    public static void Add(Pizza pizza)
    {
        pizza.Id = nextId++;
        Pizzas.Add(pizza);
    }

    public static void Delete(int id)
    {
        var pizza = Get(id);
        if(pizza is null)
            return;

        Pizzas.Remove(pizza);
    }

    public static void Update(Pizza pizza)
    {
        var index = Pizzas.FindIndex(p => p.Id == pizza.Id);
        if(index == -1)
            return;

        Pizzas[index] = pizza;
    }
}
```

## Add A Controller
A controller is a public class with one or more public methods known as actions. 
1. Select the Controllers folder in vscode and add a new controller PizzaController.cs
2. add the following code, as we learned, this class derives from ControllerBase, the base class for working with HTTP requests in ASP.NET Core. It also includes `[ApiController]` and `[Route]` as attributes. As before, the `[Route]` attribute defines a mapping to the `[Controller]` token. Because this controller class is named `PizzaController`, this controller handles requests to  `https://localhost:{PORT}/pizza`.
```cs
using ContosoPizza.Models;
using ContosoPizza.Services;
using Microsoft.AspNetCore.Mvc;

namespace ContosoPizza.Controllers;

[ApiController]
[Route("[controller]")]
public class PizzaController : ControllerBase
{
    public PizzaController()
    {
    }
}
```

## Get all pizzas
The first REST verb that we need to implement is GET, where a client can get all pizzas from the API. You can use the built-in `[HttpGet]` attribute to define a method that will return the pizzas from the service. Replace the comment GET in our PizzaController Code with 
```cs
[HttpGet]
public ActionResult<List<Pizza>> GetAll() =>
    PizzaService.GetAll();
```

This code responds only to the HTTP verb GET, as denoted by the `[HttpGet]` attribute. 
It returns an [[ActionResult]] instance of type List\<Pizza>. 
It queries the service for all pizza and automatically returns data with a `Content-Type` value of `application/json`

## Retrieve a single pizza
The client might also want to request information about a specific pizza instead of the entire list. You can implement another GET action that requires an `id` parameter. you can use the built in [[HTTP GET ID|`HttpGet("{id}")`]] attribute tp define a method that will return the pizzas from our service.  The routing logic registers `[HttpGet]` (without `id`) and `[HttpGet("{id}")]` (with `id`) as two different routes. You can then write a separate action to retrieve a single item.
Replace the `// GET by Id action` comment in _Controllers/PizzaController.cs_ with the following code:
```cs 
[HttpGet("{id}")]
public ActionResult<Pizza> Get(int id)
{
    var pizza = PizzaService.Get(id);

    if(pizza == null)
        return NotFound();

    return pizza;
}
```

The preceding action:

-   Responds only to the HTTP `GET` verb, as denoted by the `[HttpGet]` attribute.
-   Requires that the `id` parameter's value is included in the URL segment after `pizza/`. Remember, the controller-level `[Route]` attribute defined the `/pizza` pattern.
-   Queries the database for a pizza that matches the provided `id` parameter.


Each `ActionResult` instance used in the preceding action is mapped to the corresponding HTTP status code in the following table:
![[Pasted image 20230121151839.png]]

# Enabling POST
`[[HttpPost|[HttpPost]]]`We want users to be able to add new items. If we want users to be able to add a new item to the endpoint, we must implement the POST action by using the [[HttpPost|[HttpPost]]] attribute.  
The `[HttpPost]` attribute will map HTTP `POST` requests sent to `http://localhost:5000/pizza` by using the `Create()` method. Instead of returning a list of pizzas, as we saw with the `Get()` method, this method returns an `IActionResult` response.

`IActionResult` lets the client know if the request succeeded and provides the ID of the newly created pizza. `IActionResult` does this by using standard HTTP status codes, so it can easily integrate with clients regardless of the language or platform they're running on.
![[Pasted image 20230121153230.png]]

## PUT
Modifying or updating a pizza in inventory is done similarly to POST but it uses the [[HttpPut]] attribute and takes in the id parameter in addition to the `Pizza` object that needs to be updated. 
![[Pasted image 20230121153658.png]]
## DELETE

One of the easier actions to implement is the `DELETE` action, which takes in just the `id` parameter of the pizza to remove from the in-memory cache:
![[Pasted image 20230121153748.png]]

