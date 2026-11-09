from user_912 import User

class Admin(User):
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = [
            "dapat menambahkan postingan",
            "dapat menghapus postingan",
            "dapat melarang pengguna"
        ]

    def show_privileges(self):
        print("Hak akses admin:")
        for privilege in self.privileges:
            print(f"- {privilege}")
        