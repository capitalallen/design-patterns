from rx import Observable, Observer

# get and return the quotes
def get_quotes():
    import contextlib, io
    zen = io.StringIO()
    with contextlib.redirect_stdout(zen):
        import this

    quotes = zen.getvalue().split('\n')[1:]
    return quotes

"""
takes an Observer object obs as input, and, 
using the sequence of quotes, sends each quote using the on_next() 
and signals the end (after the last quote has been sent) using on_completed(). 
"""
def push_quotes(obs):

    quotes = get_quotes()
    for q in quotes:
        if q:  # skip empty
            obs.on_next(q)
    obs.on_completed()

# implement the Observer to be used, using a subclass of the Observer base class,
class ZenQuotesObserver(Observer):

    def on_next(self, value):
        print(f"Received: {value}")

    def on_completed(self):
        print("Done!")

    def on_error(self, error):
        print(f"Error Occurred: {error}")
# define the source to be observed,
source = Observable.create(push_quotes)
# subscription to the Observable,
source.subscribe(ZenQuotesObserver())