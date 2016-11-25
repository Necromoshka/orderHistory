from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import ProcessFormView
from django.core.urlresolvers import reverse
from .models import userMainTeble


class userMainView(ProcessFormView):
    def post(self, request, *args, **kwargs):
        try:
            pn = request.GET["page"]
        except KeyError:
            pn = "1"
        self.success_url = self.success_url + "?page=" + pn
        return super(userMainView, self).post(request, *args, **kwargs)

class userMainCreate(CreateView):
    model = userMainTeble
    template_name = "usermaincreate.html"
