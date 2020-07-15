def setexpiry(request,seconds):
    request.session.set_expiry(seconds)