helpinghand
===========

Run test server:

```cd server ; make test```

Launches a test server at ```127.0.0.1:8000```

To edit point browser to ```127.0.0.1:8000/admin``` to test the menus and pages ```127.0.0.1:8000/menu/menuname``` and ```127.0.0.1:8000/page/pagename```.

Launch either the iOS or android, at this point they should be able to load the main menu. iOS succeeds at the moment, can't figure out how to get the debugging info from the android emulator, but it is failing for some reason.

If it says ```Hey there mister. You're looking mighty fine.``` it is trying to butter you up. It has failed and does not know how to tell you. Ignore its false praise and kill it.

Work todo
==============
* Need to implement handlebars templates to put the data into before loading
* Stack of places visited and back buton to pop
* Cache
* Styling for native feel
* Page transition (I Hear this is hard)
* Streamline server with api to get data without all the extra stuff we don't need (just the content div sans styling)
