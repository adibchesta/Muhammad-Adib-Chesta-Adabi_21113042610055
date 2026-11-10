from pathlib import Path
import json

path = Path("username.json")


def get_new_username():
    username = input("Masukkan username baru: ")
    path.write_text(json.dumps(username))
    return username


def greet_user():
    if path.exists():
        username = json.loads(path.read_text())

        print(f"Apakah username kamu {username}?")
        answer = input("Ketik yes atau no: ")

        if answer.lower() == "yes":
            print(f"Selamat datang kembali, {username}!")

        else:
            username = get_new_username()
            print(f"Selamat datang, {username}!")

    else:
        username = get_new_username()
        print(f"Kami akan mengingat kamu saat kembali, {username}!")


greet_user()