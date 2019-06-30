import datetime
now = datetime.datetime.now()

from gmail import GMail, Message
gmail = GMail('nguyenmson98@gmail.com','kazarushinnisuto')

html_content = '''
<p style="text-align: center;">Cong hoa xa hoi chu nghia Viet Nam</p>
<p style="text-align: center;">Doc lap tu do hanh phuc</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><strong>DON XIN NGHI HOC</strong></p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: left;">Em chao thay, em ten la Nguyen Minh Son</p>
<p style="text-align: left;">Hom nay, em xin thay cho phep em nghi hoc vi {{sickness}} </p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: right;">Em xin cam on!</p>
<p style="text-align: right;">Nguyen Minh Son</p>
'''
from random import choice
reason = ['om','di du lich','ve que']
sickness = choice(reason)
html_new = html_content.replace("{{sickness}}", sickness)

msg = Message(
    'Test Message',
    to='nguyenmson98@gmail.com',
    html=html_new)

if now.hour > 7 or (now.hour == 7 and now.minute > 0 or now.second > 0):
    gmail.send(msg)