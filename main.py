import json

def load_credentials(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def simulate_auth(service):
    print(f"\n[+] Testando serviço: {service['name']}")

    username = service.get("username")
    password = service.get("password")
    token = service.get("auth_token")

    if username == "admin" and password == "admin":
        print("[!] Credencial fraca encontrada (admin/admin)")
    elif "test" in username or "test" in password:
        print("[!] Credencial de teste encontrada")
    elif len(password) < 8:
        print("[!] Senha fraca detectada")
    else:
        print("[OK] Credenciais parecem mais seguras")

    if token:
        print(f"[INFO] Token detectado: {token[:10]}...")

def main():
    data = load_credentials("credentials.json")

    for service in data["services"]:
        simulate_auth(service)

if __name__ == "__main__":
    main()