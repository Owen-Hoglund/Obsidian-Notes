Blazor apps are composed of reusable web UI components built using C#, HTML, and CSS.
With Blazor, you can:
- Generate Server-side code that handles UI interactions over a WEbSocket Connection
- Generate a client side web app that runs directly  in the browser via WebAssembly

## Blazor WebAssembly
With Blazor WebAssembly, developers can run .NET code in a browser. It's a single page app framework that uses the WebAssembly open standards without requiring plug-ins or code generation. 
.NET code exevuted via WebAssembly in a browser runs in the browsers JavaScript sandbox. The code includes all of the security and protection that the sandbox provides. THis inclusion helps prevent malicious attacks on a client machine. 
## Razor Directives
Razor directives are compenent markup used to add C# inline with HTML. With directives, developers can define single statement, methods, or larger code blocks.
### Code Directives
- You can use `@()` to add a C# statement inline with HTML.
- If you require more code, use the `@code` directive to add multiple statements, enclosed by parentheses.
- You can also add an `@functions` section to the template for methods and properties. They're added to the top of the genereated class, where the document can reference them. 
### Page Directive
The `@Page` directive is special markup that identifies a component as a page. You can use this directive to spuecifuy a route. The route maps to an attribute that the blazor engine recognizes to register and access the page. 

## Razor Data Binding
Within Razor components, you can data bind GRML elemnents to C# fields, properties, and Razor expression values. Data binding allows two-way synchronization between HTML and Microsoft .NET. 
Data is pushed from HTML to .NET when a component is rendered. Components render themselves after event-handler code executes, which is why property updates are reflected in the UI immediately after an event handler is triggered. 
You can use the `@bind` markup to bind a c# variable to an HTML object. You;ll define the C# variable by name as a string in the HTML. 