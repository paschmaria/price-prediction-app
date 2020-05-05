# select 'development' or 'production' settings
try:
    from .local import *
except:
    from .prod import *
