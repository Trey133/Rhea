#!/usr/bin/env python
import os
os.system('rm config.py')
os.system("(echo '#!/usr/bin/python\nusername = \"13\" > config.py)'")
os.system("(echo -n 'password = '; openssl rand -base64 13 ; > config.py)")
