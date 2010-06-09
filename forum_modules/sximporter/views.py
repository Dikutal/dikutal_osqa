from django.shortcuts import render_to_response
from django.template import RequestContext
from forum.views.admin import super_user_required
import importer
from zipfile import ZipFile
import os

@super_user_required
def sximporter(request):
    list = []
    if request.method == "POST" and "dump" in request.FILES:
        dump = ZipFile(request.FILES['dump'])
        members = [f for f in dump.namelist() if f.endswith('.xml')]
        extract_to = os.path.join(os.path.dirname(__file__), 'tmp')
        dump.extractall(extract_to, members)
        importer.sximport(extract_to, request.POST)
        dump.close()

    return render_to_response('modules/sximporter/page.html', {
    'names': list
    }, context_instance=RequestContext(request))