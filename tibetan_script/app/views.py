from django.shortcuts import render

from app.forms import OriginInputForm
from app.models import TibetToPinyin

def index(request):
    c = {}
    form = OriginInputForm(request.POST or None)
    if form.is_valid():
        orgin_text = form.cleaned_data['orgin_text']
        lines = orgin_text.splitlines()
        output_lines = []
        for line in lines:
            output_line = []
            words = line.replace('།།', '་').replace('།', '་').replace('\t', '་').replace(' ', '་').split('་')
            for word in words:
                if word:
                    obj, created = TibetToPinyin.objects.get_or_create(tibet=word)
                    if obj.pinyin:
                        output_line.append(obj.pinyin)
                    else:
                        output_line.append('X')
                    output_str = ''.join(output_line)
            output_lines.append(line)
            output_lines.append(output_str)
        print(output_lines)
    c['form'] = form
    c['output'] = output_lines
    return render(request, 'app/index.html', c)
