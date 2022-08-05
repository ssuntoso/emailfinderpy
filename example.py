import emailfinderpy as em

print(em.verify_email('ssuntoso@gmail.com'))
# True

print(em.verify_multiple_email(['s.suntoso@gmail.com', 'ssuntoso@gmail.com'], 'Sean'))
#   Name                Email   Status
#0  Sean  s.suntoso@gmail.com  Veified
#1  Sean   ssuntoso@gmail.com  Veified

print(em.email_finder('Sean', '', 'Suntoso', 'gmail.com'))
#            Name                Email   Status
#0  sean  suntoso   ssuntoso@gmail.com  Veified
#1  sean  suntoso  s.suntoso@gmail.com  Veified