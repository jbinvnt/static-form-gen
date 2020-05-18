# Static Form Generator

## Background

Frameworks such as Django can provide functions that automatically generate HTML form input elements to match the columns in a database table. To render a form, the developer sends a class containing the fields to the template. This [feature](https://docs.djangoproject.com/en/stable/topics/forms/modelforms/) avoids a source of repetition in the front end and back end. Otherwise model attributes would need to be enumerated twice: once when defining the database, and again when building the forms.

## The Problem

Unfortunately, automatic form rendering in any web framework relies on the ability to dynamically generate HTML. Projects that serve static pages and interact with the framework through AJAX don't have this option. This can require the developer to make every change twice, once in both parts of the app. One solution might be to create an API endpoint that serializes a description of the form, but this would diminish the efficiency advantage that AJAX provides.

## The Solution

This project allows efficiency without the need to Write Everything Twice by providing a management command that can directly render forms inside static files. It does this by searching for tags indicating the type and start/end of the form, and then calling the render method on the appropriate form class.

## Instructions

### Common

In your files, mark the location where the form output should be placed by using `<SForm class="yourClass">` and then on the next line a closing `</SForm>` tag. For HTML, comment out these tags so they are not rendered by the browser. Depending on the output of the render method, you may need to add enclosing form tags and a submit button.

### Django

To add this command to your project, move the [genforms.py](genforms.py) script into the appropriate directory according to [this guide](https://docs.djangoproject.com/en/stable/howto/custom-management-commands/). You can then run it with `python manage.py genforms <args>`. This command should be run **before** copying static files to where they will ultimately be served from (in Django, this is done by `collectstatic`). Django does not render form tags or a submit button.

## The Example Projects

### Django

The Django example is a minimal app that can be run using Docker Compose. It provides the ability to generate a form that creates `Car` objects. Here's how to run the example:

1. Follow the instructions above for copying [genforms.py](genforms.py) to the correct directory.
2. To generate the form, run the command `docker-compose run web python django/manage.py genforms example.forms example/static`.
3. [Migrate the database](https://docs.djangoproject.com/en/stable/topics/migrations/) and run the server using `docker-compose up`.
4. Visit the form page in a browser at [static/index.html]()
5. You can verify that the form works properly by [creating a superuser](https://docs.djangoproject.com/en/stable/intro/tutorial02/#creating-an-admin-user) and then viewing the `Car` section of the admin page.

## Limitations

While this project can save a lot of time for developers, there are some limitations. You will need AJAX if you want dynamically calculated default values or dynamic pre-filled input. Also, this solution doesn't fully conform to the principle of loose coupling because a change in the model still requires a separate change in the form. However, at least this script allows the changes to be made quickly and easily.

## Extensions

The management command to run this script can be included as part of build automation workflows. Future plans for improving this project include adding support for other frameworks such as Ruby on Rails or ASP.NET Core.
