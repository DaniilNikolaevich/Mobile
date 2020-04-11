import os
from jinja2 import Template
import pdfkit
import sys
sys.path.extend(['/home/Mobile','/home/Mobile/Lab_1','/home/Mobile/Lab_2'])
from Lab_1 import main_1
from Lab_2 import main_2

os.chdir('/home/Mobile/Lab_1')
total_calls,total_sms = main_1.main_1()
phone_sum = total_calls + total_sms
os.chdir('/home/Mobile/Lab_2')
inet_sum = main_2.main_2()
os.chdir('/home/Mobile/Lab_3')
def generate():


    context = {}
    context['inet_sum'] = f'{inet_sum} рублей'
    context['phone_sum'] = f'{phone_sum} рублей'
    context['nds'] = "{0:.2f} рублей".format(0.2*(inet_sum+phone_sum))
    context['total_sum'] = f'{inet_sum + phone_sum} рублей'
    

    html_file = open('Template.html', 'r', encoding='utf-8')
    html = html_file.read()

    template = Template(html)
    output = template.render(context=context)
    with open('certificate.html', 'wb') as f:
        f.write(output.encode('utf-8'))
    options = {
        'page-size': 'A4',
        'margin-top': '2cm',
        'margin-left': '3cm',
        'margin-right': '2cm'
    }
    pdfkit.from_file('certificate.html', 'certificate.pdf', options=options)
    os.remove('certificate.html')

if __name__ == '__main__':
    generate()
    print("PDF Файл успешно создан. Он находится в директории Lab_3")
    
