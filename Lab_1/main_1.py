# Протарифицировать абонента с номером 911926375 с коэффициентом k: 4руб/минута исходящие звонки, 
# 0руб/минута входящие первые 5 минут, далее 1руб/минута, 
# смс - первые 5шт бесплатно, далее 1руб/шт
# https://docs.google.com/document/d/1eKgto1g8Lu0dLhxssqUSP4WpMlWk98otQqONZ0Ghf2M/edit
import os
def main_1():
    client_number = "911926375"
    to_fare_free = 5
    to_fare = 1
    from_fare = 4
    free_sms = 5
    sms_cost = 1
    total_calls = 0
    total_sms = 0
    cdr = open("data.csv","r")
    for line in cdr:
        line = line.replace("\n","").split(",")
        
        if line[1] == client_number:
            total_calls += from_fare*float(line[3])
            current_sms = int(line[4])
            while current_sms != 0:
                if free_sms != 0:
                    current_sms -= 1
                    free_sms -= 1
                else:
                    total_sms += sms_cost
                    current_sms -= 1
        elif line[2] == client_number:
            current_call = float(line[3])
            if current_call > to_fare_free:
                total_calls += (current_call - to_fare_free)*to_fare    

    return total_calls,total_sms
    
if __name__ == '__main__':
    os.chdir('/home/Mobile/Lab_1')
    total_calls,total_sms = main_1()
    print(f"Звонков на сумму: {total_calls}")
    print(f"Cмс на сумму: {total_sms}")
    print(f"Общий счет: {total_calls + total_sms}")