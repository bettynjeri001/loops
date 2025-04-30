#  break and continue 

# break
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in days_of_week:
    if day == "Friday":
        print("It's Friday! Stopping the loop.")
        break  # Stop the loop when we reach Friday
    print(f"Today is {day}.")


    # continue

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in days_of_week:
    if day == "Saturday" or day == "Sunday":
        continue  # Skip the weekends (Saturday and Sunday)
    print(f"Today is {day}.")
