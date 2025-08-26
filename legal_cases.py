class CivilCase:
    def __init__(self, case_number, client_name, damages):
        self.case_number = case_number
        self.client_name = client_name
        self.damages = damages
        self.status = "Open"

    def get_summary(self):
        return f"Civil Case {self.case_number} - {self.client_name} - Damages: {self.damages} - Status: {self.status}"

    def close_case(self):
        self.status = "Closed"


class CriminalCase:
    def __init__(self, case_number, client_name, charges):
        self.case_number = case_number
        self.client_name = client_name
        self.charges = charges
        self.status = "Open"

    def get_summary(self):
        return f"Criminal Case {self.case_number} - {self.client_name} - Charges: {', '.join(self.charges)} - Status: {self.status}"

    def close_case(self):
        self.status = "Closed"


class FamilyLawCase:
    def __init__(self, case_number, client_name, case_type):
        self.case_number = case_number
        self.client_name = client_name
        self.case_type = case_type
        self.status = "Open"

    def get_summary(self):
        return f"Family Law Case {self.case_number} - {self.client_name} - Type: {self.case_type} - Status: {self.status}"

    def close_case(self):
        self.status = "Closed"


def main():
    cases = []

    while True:
        print("1.Add Civil 2.Add Criminal 3.Add Family 4.List Cases 5.Close Case 6.Exit")
        choice = input("Choose: ")

        if choice == '1':
            cn = input("Case #: ")
            cl = input("Client: ")
            dmg = input("Damages: ")
            cases.append(CivilCase(cn, cl, dmg))
            print("Civil case added.")

        elif choice == '2':
            cn = input("Case #: ")
            cl = input("Client: ")
            ch = [c.strip() for c in input("Charges (comma sep): ").split(",") if c.strip()]
            cases.append(CriminalCase(cn, cl, ch))
            print("Criminal case added.")

        elif choice == '3':
            cn = input("Case #: ")
            cl = input("Client: ")
            ct = input("Family case type: ")
            cases.append(FamilyLawCase(cn, cl, ct))
            print("Family law case added.")

        elif choice == '4':
            if not cases:
                print("No cases.")
            else:
                for i, c in enumerate(cases, 1):
                    print(f"{i}. {c.get_summary()}")

        elif choice == '5':
            if not cases:
                print("No cases to close.")
            else:
                for i, c in enumerate(cases, 1):
                    print(f"{i}. {c.case_number} ({c.status}) - {c.client_name}")
                try:
                    idx = int(input("Close case #: "))
                    if 1 <= idx <= len(cases):
                        cases[idx - 1].close_case()
                        print("Case closed.")
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
