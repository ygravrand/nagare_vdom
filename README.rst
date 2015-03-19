=======
Context
=======
Using ``Nagare`` (www.nagare.org), you can write components in Python to code your web applications.
Components actions are executed server side and views are rendered to the client.
Thanks to Stackless Python continuation, there is no need to manually handle sessions, write controllers and the such.
Actions are written as regular callables and attached to elements of the view (e.g. a link, a submit button...)

=======
Problem
=======
``Nagare`` renders a whole page but is also capable of rendering some components asynchronously.
In other words, some parts of the rendered page can change without the page being reloaded.
In simple scenarios, it works painlessly, you just switch to an asynchronous renderer for the desired components.
There are times though when we would want other components, for example the ones being affected by a callable, to be refreshed, without knowing the list.
I find existing solutions to this problem clumsy and inelegant.

========
Approach
========
``react.js`` shares many similarities with Nagare, starting with the component approach.
Its "virtual DOM" implementation allows it to use a straightforward updating scheme: well, update everything, and let the virtual dom compute the actual changes.
@Matt-Esch also wrote a ``virtual-dom`` implementation.
The goal of the ``nagare_vdom`` experiment is to try and use ``virtual-dom`` to solve our asynchronous rendering problems.

=======
Roadmap
=======
For now, there is only a quickly written demo app with only one component.
I'd like to follow the following steps:

1. Add other examples
2. Add an online working example
3. Provide installation instructions and binaries
4. Extract a library to use on top of nagare with any nagare app.

 