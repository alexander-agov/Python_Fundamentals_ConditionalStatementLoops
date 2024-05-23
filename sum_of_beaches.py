s = input()
s_lower = s.lower()
sand_count = s_lower.count("sand")
water_count = s_lower.count("water")
fish_count = s_lower.count("fish")
sun_count = s_lower.count("sun")
total_count = sand_count + water_count + fish_count + sun_count
print(total_count)