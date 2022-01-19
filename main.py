from Usuario import Usuario

guido = Usuario("Guido", "guido@gmai.com")
nibles = Usuario("Nibles", "nibles@gmai.com")
benny = Usuario("Benny","benny@gmail.com")

guido.hacer_depósito(100).hacer_depósito(100).hacer_depósito(100).mostrar_balance_usuario()

guido.hacer_retiro(100).mostrar_balance_usuario()

nibles.hacer_depósito(100).hacer_depósito(50).mostrar_balance_usuario()

nibles.hacer_retiro(50).hacer_retiro(50).mostrar_balance_usuario()

benny.hacer_depósito(1000).mostrar_balance_usuario()

benny.hacer_retiro(30).hacer_retiro(200).hacer_retiro(40).mostrar_balance_usuario()

benny.transferir_dinero(nibles,500).mostrar_balance_usuario()

nibles.mostrar_balance_usuario()

