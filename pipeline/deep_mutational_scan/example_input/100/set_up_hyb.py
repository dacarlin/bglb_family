import os 
from glob import glob 
import jinja2 

def render(template, context):
    path, filename = os.path.split(template)
    ld = jinja2.FileSystemLoader(path or './')
    return jinja2.Environment(loader=ld).get_template(filename).render(context)

def get_threaded_templates():
    for g in glob('*thread.pdb'):
        yield {'path': g, 'weight': 1.0}

templates = get_threaded_templates()
context = {'templates': templates} 

with open('hyb_protocol.xml', 'w') as fn:
    fn.write(render('hyb.xml', context)) 
