import inspect

def getargspec_compat(func):
    if not inspect.isfunction(func) and not inspect.ismethod(func):
        raise TypeError(f"{func} is not a Python function or method")
    
    spec = inspect.getfullargspec(func)
    
    args = spec.args
    varargs = f"'{spec.varargs}'" if spec.varargs else None
    keywords = f"'{spec.varkw}'" if spec.varkw else None
    defaults = spec.defaults

    args_repr = f"args={args}"
    varargs_repr = f"varargs={varargs}" if varargs is not None else "varargs=None"
    keywords_repr = f"keywords={keywords}" if keywords is not None else "keywords=None"
    defaults_repr = f"defaults={defaults}" if defaults is not None else "defaults=None"

    print(f"ArgSpec({args_repr}, {varargs_repr}, {keywords_repr}, {defaults_repr})")

# Example function and classes
def my_function(a, b=1, *args, **kwargs):
    pass

class MyClass:
    def __init__(self, x, y=0):
        self.x = x
        self.y = y

    def method1(self):
        pass

    def method2(self, z):
        pass

class MyOtherClass:
    def __init__(self, a, b=0):
        self.a = a
        self.b = b

    def method1(self):
        pass

    def method2(self, c, d=0):
        pass

function_name = input("Enter the name of the function: ")
obj0 = globals().get(function_name)

if obj0 is None or not (inspect.isfunction(obj0) or inspect.ismethod(obj0)):
    print(False)
else:
    print(True)
    getargspec_compat(obj0)

# --- Class and method input ---
class_name = input("Enter the name of the class: ")
clsn = globals().get(class_name)

if clsn is None or not inspect.isclass(clsn):
    print(False)
else:
    print(True)
    method_name = input("Enter the name of the method: ")
    if hasattr(clsn, method_name):
        method = getattr(clsn, method_name)
        if inspect.isfunction(method) or inspect.ismethod(method):
            print(True)
            getargspec_compat(method)
        else:
            print(False)
    else:
        print(False)