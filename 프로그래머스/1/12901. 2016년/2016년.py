def solution(a, b):
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    
    total_days = sum(month_days[:a - 1]) + b 
    day_index = (total_days + 4) % 7 
    
    return days[day_index]
