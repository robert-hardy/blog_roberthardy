Title: Erlang for Python users
Date: 2019-01-22 11:00
Category: Programming
Summary: Erlang described so a Python user can grok

## Summary

In order to make the basic concepts of Erlang accessible to a Python user, I
split Erlang into four pieces:

1. **The 'data manipulation' stuff**

    Erlang is very similar to Python here.

    You can do list comprehensions, ranges, dicts. Practically everything you
do in Python is available in Erlang.

    On top of this, Erlang gives you _pattern matching_ and atoms. I really
like these bits.

    Oh and Erlang has no mutable state.

2. **The OTP stuff**

    Fred Hebert's brilliant book dedicates a number of chapters to OTP. But
what on earth is it?

    OTP is a massive topic but most texts introduce `gen_server` early on. As
an approximation, we will show how the `gen_server` can be seen as a clever
kind of `import`. Erlang's OTP is much bigger than this, but this should give
you a sense of where OTP sits in the stack.

3. **The process stuff**

    OTP is possible because of the central role that processes have been given
in Erlang. Processes and OTP are at the core of Erlang's strategy for building
fault-tolerant code.

    But _processes are just processes_. There is nothing else going on that you
need to know about, at least for this level of understanding.

4. **Fault-tolerant systems**

    This is where Erlang stands out: you can build systems which are protected
from those very-rare-but-hard-to-find bugs.

    Of course, in a system that handles a lot of load, the term 'very rare' is
relative. I quote from [Fred's Zen of
Erlang](https://ferd.ca/the-zen-of-erlang.html):

    > ... a once in a billion bug will show up every 3 hours in a system doing 100,000
    > requests a second ...

    > ... a once in a million bug could similarly show up once every 10 seconds on
    > such a system ...


## Erlang 'data manipulation' stuff: lists, functions, etc.

Here is the factorial function in Erlang:
```
factorial(1) -> 1;
factorial(N) -> N * factorial(N-1).
```
You can see for yourself how pattern matching is used.

Here is a list comprehension which produces a list of tuples:

```
# In Python:
[ (x, y, x*y) for x in range(1, 10) for y in range(1, 10) ]

% In Erlang:
[ {X, Y, X*Y} || X<-lists:seq(1, 10), Y<-lists:seq(1, 10) ]
```

Note that all variables in Erlang must start with a capital letter, otherwise
they get interpreted as an atom.


To run Erlang code you can use [the escript
command](http://erlang.org/doc/man/escript.html). On that page there is an
example for the factorial function.
```erlang
#!/usr/bin/env escript
% vim: ft=erlang

main([String]) ->
    try
        N = list_to_integer(String),
        F = fac(N),
        io:format("factorial ~w = ~w\n", [N,F])
    catch
        _:_ ->
            usage()
    end;
main(_) ->
    usage().

usage() ->
    io:format("usage: factorial integer\n"),
    halt(1).

fac(0) -> 1;
fac(N) -> N * fac(N-1).
```


## OTP
### The gen_server 'behaviour'
Suppose I wanted to make it possible to 'hot swap' code in Python. Here is one
simple way to do that.

I create two files, one of functions:

```
# my_functions.py
def func_a(x):
    return 2 * x

def func_b(x):
    return x + 100
```

and one which acts as a layer of indirection:

```
# my_module.py
from my_functions import func_a

func = func_a
```

At the command line I can call the function in `my_module`:

```
> import my_module
> my_module.func(10)
20
```

I can hot-swap too:

```
> from my_functions import func_b
> my_module.func = func_b
> my_module.func(10)
120
```

The important point is that this has been done by creating a layer of
indirection. I do not call the functions directly, I call something which goes
on to call the functions. No magic here.

This is somewhat analogous to how `gen_server` works: you register your
functions with a `gen_server` and call your functions via the `gen_server`.

Registering is done with the `handle_call/3` and `handle_cast/2` functions in
the `gen_server`. Hot swapping is done with the `code_change/3` function.

### What does this mean?
OTP is a lot of things and contains a lot of goodies, but the idea I want to
emphasize is that `gen_server` and some of the other OTP 'behaviours' (that is
the name they get given) are playing with the way the code itself is managed.
You do not have to use these OTP structures, but if you do then you can benefit
from a lot of code-management that people have perfected over the years.

## Processes
The short piece above on OTP should give you a sense of how Erlang brings
something quite different to the table: you are able to have a much finer
control on how your code is loaded/run/stopped/started/etc.

The building block for this is the _process_. In Erlang it is trivially easy to
create a new process and run a function within that process. Here we run a
simple multiply-and-print function from within a newly-spawned process:

```
% this_module.erl
my_multiplication_function(Arg1, Arg2) ->
   io:format("~p times ~p is ~p", [Arg1, Arg2, Arg1 * Arg2]).
start() ->
   spawn(this_module, my_multiplication_function, [2, 10]),
```

### But why?

One of the main reasons for wrapping functions inside processes is that it
allows us to build fault-tolerant systems.

If we run a function inside a process and a one-in-a-million bug happens that
kills the function then our process will exit and we can react to that --
probably by restarting the process and re-running the function (perhaps with a
modified set of parameters that are less likely to break).

## Fault-tolerant systems
When Erlangers talk about 'let it crash', they do not mean that they write
shoddy code which does not handle edge cases and therefore breaks.

They mean that if a function breaks for some unexpected (and probably hard to
debug) reason, then:

- let the process die,
- let the process tell a supervising process that it is dead and give it a
stack trace,
- so that the supervisor process (or its supervisor, or its supervisor's
supervisor, ...) can potentially restart that process and
function in a safer state.

These random 'breaks for unexpected reasons' will happen very often in a system
which handles many many requests. I quote from [Fred's Zen of
Erlang](https://ferd.ca/the-zen-of-erlang.html):

> ... a once in a billion bug will show up every 3 hours in a system doing 100,000
> requests a second ...

> ... a once in a million bug could similarly show up once every 10 seconds on
> such a system ...


## Answering my own StackOverflow question
Go have a look at [my Erlang noobie question on
StackOverflow](https://stackoverflow.com/q/54290276/1243435), and my answer.

At that point in time I had grokked that Erlang's data-manipulation language
was sufficiently similar to Python and had gotten some familiarity with the
process-spawning parts, but I had not yet grokked how OTP fitted into the
language.
