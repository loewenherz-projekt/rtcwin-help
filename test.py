import socket
import json

HOST = '127.0.0.1'
PORT = 2500
REQUEST = '{"cmd":"get_data"}'

def main():
    print(f"[1] Starte Verbindung zu {HOST}:{PORT} ...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            print("[2] Verbindung hergestellt.")
        except Exception as e:
            print(f"[Fehler] Verbindung fehlgeschlagen: {e}")
            return

        print(f"[3] Sende Anfrage: {REQUEST}")
        s.sendall(REQUEST.encode('utf-8'))

        print("[4] Warte auf Antwort vom Server ...")
        response = s.recv(4096)
        response_str = response.decode('utf-8')
        print(f"[5] Antwort erhalten: {response_str}")

        print("[6] Versuche, Antwort als JSON zu lesen und zu formatieren ...")
        try:
            data = json.loads(response_str)
            print("[7] Formatiertes JSON:")
            print(json.dumps(data, indent=4, ensure_ascii=False))
        except Exception as e:
            print(f"[Fehler] Antwort ist kein gültiges JSON: {e}")
            print("[Rohdaten]:", response_str)

if __name__ == "__main__":
    main()
