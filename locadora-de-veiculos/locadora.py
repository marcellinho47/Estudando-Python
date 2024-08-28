import os

cars = [
    ('Fusca', 50),
    ('Gol', 100),
    ('Celta', 150),
    ('Corolla', 200),
    ('Civic', 250),
    ('Fusion', 300),
    ('Cruze', 350),
    ('Hilux', 400),
    ('Ranger', 450),
    ('S10', 500)
]

rented_cars = []


def show_cars():
    os.system("cls")
    print('Carros disponíveis para locação:\n')
    for i, car in enumerate(cars):
        print(f'[{i}] - {car[0]} - R$ {car[1]}')


def rent_car():
    while True:
        show_cars()
        car_index = int(input('\nDigite o número do carro que deseja alugar: '))

        if 0 <= car_index < len(cars):
            print(f'Você escolheu o carro {cars[car_index][0]}')
            break

    while True:
        days = int(input('\nInforme a quantidade de dias que deseja alugar o carro: '))

        if days <= 0:
            print('\nVocê precisa alugar o carro por pelo menos 1 dia')
            continue
        else:
            print('\nVocê escolheu alugar o carro por', days, 'dias')

        car = cars[car_index]
        while True:
            print(f'\nO aluguel do carro {car[0]} por {days} dias custará R$ {car[1] * days}')
            print('\nDeseja confirmar a locação?')
            print('[1] - Sim')
            print('[2] - Não')
            confirm = int(input('\nDigite o número da opção desejada: '))
            if confirm == 1:
                car = cars.pop(car_index)
                rented_cars.append(car)
                print(f'\nVocê alugou o carro {car[0]} por R$ {car[1] * days} durante {days} dias')
                input('\n\nPressione ENTER para voltar ao menu principal')
                return
            elif confirm == 2:
                print('\nLocação cancelada')
                return


def list_rented_cars():
    os.system("cls")

    if len(rented_cars) == 0:
        print('Nenhum carro alugado')
        input('\n\nPressione ENTER para voltar ao menu principal')
        return

    print('Carros alugados:\n\n')
    for i, car in enumerate(rented_cars):
        print(f'[{i}] - {car[0]} - R$ {car[1]}')


def return_car():
    if len(rented_cars) == 0:
        print('Nenhum carro alugado')
        input('\n\nPressione ENTER para voltar ao menu principal')
        return

    while True:
        list_rented_cars()
        car_index = int(input('\nDigite o número do carro que deseja devolver: '))

        if 0 <= car_index < len(rented_cars):
            print(f'Você escolheu devolver o carro {rented_cars[car_index][0]}')
            break

    while True:
        print('\nDeseja confirmar a devolução?')
        print('[1] - Sim')
        print('[2] - Não')
        confirm = int(input('\nDigite o número da opção desejada: '))
        if confirm == 1:
            car = rented_cars.pop(car_index)
            cars.append(car)
            print(f'\nVocê devolveu o carro {car[0]}')
            input('\n\nPressione ENTER para voltar ao menu principal')
            return
        elif confirm == 2:
            print('\nDevolução cancelada')
            input('\n\nPressione ENTER para voltar ao menu principal')
            return


def main():
    while True:
        os.system("cls")
        print('Bem-vindo à locadora de veículos\n')
        print('[1] - Alugar carro')
        print('[2] - Devolver carro')
        print('[3] - Listar carros alugados')
        print('[4] - Sair')
        option = int(input('\nDigite o número da opção desejada: '))

        if option == 1:
            rent_car()
        elif option == 2:
            return_car()
        elif option == 3:
            list_rented_cars()
            input('\n\nPressione ENTER para voltar ao menu principal')
        elif option == 4:
            break


if __name__ == '__main__':
    main()
