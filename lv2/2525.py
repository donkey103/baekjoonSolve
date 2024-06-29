hour, min = map(int, input().split())
time = int(input())

add_hour = (time + min) // 60
mod_min = (time + min) % 60

mod_hour = (hour + add_hour) % 24

print(f'{mod_hour} {mod_min}')