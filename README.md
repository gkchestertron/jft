#JFT
JFT is a simple clone of the popular template helper JST from the backbone-on-rails gem for Ruby on Rails. It simply wraps your js templates up in a dictionary and injects them as a global object (named JFT) into your javascript.

##Usage
1. Put your javascript templates in assets/js/templates/
    - if you want them somewhere else, add JFT\_TEMPLATE\_PATH to your app's config before calling jft.init, and set it to wherever you keep your templates.
2. Add jft.py to your project. 
3. Import it in your main application file. 
4. Call jft.init(app) (or whatever you named your application instance)
5. Then in your layout (or any template where you want your js templates injected into you javascript), add {{ JFT }} to the head  tag of your html. Then in your javascript, you can access any template with JFT['path relative to /assets/js/templates/']. It is probably best to put it at the top of your head tag.
