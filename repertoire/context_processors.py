from datetime import datetime

def data(request):
    date = datetime.today()
    return locals()