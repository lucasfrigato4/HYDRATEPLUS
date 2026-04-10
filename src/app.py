from src.storage import load_data, save_data

def add_water(amount):
    if amount <= 0:
        raise ValueError("Quantidade inválida")

    data = load_data()
    data["consumed"] += amount
    save_data(data)
    return data

def set_goal(goal):
    if goal <= 0:
        raise ValueError("Meta inválida")

    data = load_data()
    data["goal"] = goal
    save_data(data)

def show_status():
    data = load_data()
    consumed = data["consumed"]
    goal = data["goal"]

    percentage = (consumed / goal) * 100

    print(f"\n💧 Consumo: {consumed}ml / {goal}ml ({percentage:.2f}%)")

    if consumed < goal:
        print("⚠️ Você ainda não atingiu sua meta!")
    else:
        print("✅ Meta atingida! Parabéns!")

def menu():
    while True:
        print("\n=== Hydrate+ ===")
        print("1 - Adicionar água")
        print("2 - Definir meta")
        print("3 - Ver status")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            amt = int(input("Quantidade (ml): "))
            add_water(amt)

        elif op == "2":
            goal = int(input("Nova meta (ml): "))
            set_goal(goal)

        elif op == "3":
            show_status()

        elif op == "0":
            break

        else:
            print("Opção inválida")

if __name__ == "__main__":
    menu()