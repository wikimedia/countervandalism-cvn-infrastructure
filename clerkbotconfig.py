# Configuration for clerkbot

# IRC server
HOST = "irc.libera.chat"
PORT = 6667

# IRC user (used to identify with NickServ)
nickname = "cvn-clerkbot"
password = "cvn-clerkbot:***"

# IRC initial channels to join onconnect
channels = ["#countervandalism", "#cvn-staff", "#cvn-bots"]

# MySQL config
useMySQL = True
sqlhost = "localhost"
sqlport = 3306
sqluser = "root"
sqlpw = "root"
sqldbname = "cvnclerkbot"
