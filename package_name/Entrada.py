def main():
    # Entrada de dados do usuário
    has_permission = input().lower() == "true"
    age = int(input())

    # TODO: Verifique condições de acesso
    if has_permission == True and age >= 18:

        print("Acesso permitido")

    elif has_permission == True and age <= 18:

        print("Idade insuficiente")

    else:

        print("Acesso negado")


if __name__ == "__main__":
    main()
