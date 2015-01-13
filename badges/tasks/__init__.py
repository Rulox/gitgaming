import pkgutil
"""
    We load dynamically every python file in /tasks.

    So we can do from badges.tasks import *, and everything will be loaded.
"""
modules = pkgutil.iter_modules(path=["."])
a = []
for loader, mod_name, ispkg in modules:
    a.append(str(mod_name))

__all__ = a