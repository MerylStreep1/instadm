import instadm

# Imposta le tue credenziali di Instagram
username = "your_username"
password = "your_password"

# Crea un'istanza di InstaDM
client = instadm.Client(username, password)

# Imposta il destinatario del messaggio
recipient = "recipient_username"

# Imposta il messaggio
message = "This is a message sent directly."

# Invia il messaggio
client.send_direct_message(recipient, message)
