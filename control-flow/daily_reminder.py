task= input("Enter your task:").strip()
priority= input("Priority (high/medium/low):").strip().lower()
time_bound=("Is it time-bound? (yes/no):").strip().lower()

match priority:
    case 'high':
        if time_bound=='yes':
            print(f"Reminder: {'task'} is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {'task'} is a high priority task that requires immediate attention!")
    case 'medium':
        if time_bound=='yes':
            print(f"Reminder: {'task'} is a medium priority task that should be completed soon!")
        else:
            print(f"Reminder: {'task'} is a medium priority task that should be completed!")    
    case 'low':
        if time_bound=='yes':
            print(f"Reminder: {'task'} is a low priority task that can be done later!") 
        else:
            print(f"Reminder: {'task'}  is a low priority task. Consider completing it when you have free time!")