# https://manpages.ubuntu.com/manpages/disco/man1/nfdump.1.html

# Исходное задание:
# Протарифицировать абонента с IP-адресом 192.168.250.62 с коэффициентом k: 0,5руб/Мб первые 100Мб, далее 1руб/Мб


# Согласно Примечанию2, так как кол-во трафика абонента слишком мало, уменьшим единицу учета до байт (вместо мегабайт),
# следовательно исходное задание будет звучать, как:
# Протарифицировать абонента с IP-адресом 192.168.250.62 с коэффициентом k: 0,5руб/байт первые 100байт, далее 1руб/байт


import matplotlib.pyplot as plt
import os


def lineplot(x_data, y_data, x_label="", y_label="", title=""):
    # Создаю холст
    fig, ax = plt.subplots()

    
    ax.plot(x_data, y_data, lw = 1, color = '#5A009D', alpha = 1)

    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    fig.savefig('diagram.png')


def main_2():

    ip_addr = "192.168.250.62"
    pivot = {}
    first_b = 100
    first_b_cost = 0.5
    later_b_cost = 1
    input_file = open("traf.csv","r")
    cost = 0
    total_bytes = 0
    for line in input_file:
        line = line.replace("\n","").split(",")
        if ip_addr in line[1] or ip_addr in line[2]:
            if "M" in line[3]:
                mb = int(float(line[3][:-1])*1024*1024)
                total_bytes += mb
                if int(float(line[0])) in pivot:
                    pivot[int(float(line[0]))] = pivot[int(float(line[0]))] + mb
                else:
                    pivot[int(float(line[0]))] = mb
            else:
                total_bytes += int(line[3])
                if int(float(line[0])) in pivot:
                    pivot[int(float(line[0]))] = pivot[int(float(line[0]))] + int(line[3])
                else:
                    pivot[int(float(line[0]))] = int(line[3])

    # Проверяем распространяется ли Примечание 2 на наши исходные данные.
    if total_bytes/1024 > first_b:
        if total_bytes/(1024*1024) > first_b:
            cost = first_b*first_b_cost + (int(total_bytes/(1024*1024))-first_b)*later_b_cost
            # считаем в мб
        else:
            cost = first_b*first_b_cost + (int(total_bytes/1024-first_b))*later_b_cost
            # считаем в кб
    elif total_bytes > first_b:
        cost = first_b*first_b_cost + (total_bytes-first_b)*later_b_cost
        # считаем в байтах
    else:
        cost = 0
        print("Невозможно рассчитать абонента в связи с малым кол-вом потраченного трафика")
        exit(99)

    # print(f"Итоговая сумма: {cost} рублей")

    x_line = []
    y_line = []
    sorted_income = {k: pivot[k] for k in sorted(pivot)}
    for key,value in sorted_income.items():
        x_line.append(key)
        y_line.append(value)


    lineplot(x_line,y_line,"Timestamp (sec)","Trafic (bytes)","Diagram of trafic in time")

    return cost


if __name__ == '__main__':
    os.chdir('/home/Mobile/Lab_2')
    cost = main_2()
    print(f"Итоговая стоимость: {cost} рублей")
    print("Диаграмма сформированна, она находится в директории Lab_2 под именем diagram.png")
    