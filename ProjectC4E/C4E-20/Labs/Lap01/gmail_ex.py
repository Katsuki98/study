from gmail import GMail, Message
gmail = GMail('nguyenmson98@gmail.com','...')

html_content = '''
<p style="text-align: center;">Cong hoa xa hoi chu nghia Viet Nam</p>
<p style="text-align: center;">Doc lap tu do hanh phuc</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><strong>DON XIN NGHI HOC</strong></p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: left;">Em chao thay, em ten la.....</p>
<p style="text-align: left;">Hom nay {{sickness}} </p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: right;">Em xin cam on</p>
<p style="text-align: right;">cjsakhcjsik&nbsp;</p>
'''
from random import choice
reason = ['a','ab','acd']
sickness = choice(reason)
html_new = html_content.replace("{{sickness}}", sickness)

msg = Message(
    'Test Message',
    to='20130075@student.hust.edu.vn',
    html=html_new)
gmail.send(msg)