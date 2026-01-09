#funktion som visar layouten med gissningar och markeringar
def display_layout(guesses, marks_list):
    print("\n" + "="*60)
    print("Drag #           Drag            Feedback")
    print("-"*60 + "\n")
    
    for round_num in range(12,0,-1):
        guess_index = round_num - 1
        
        if guess_index < len(guesses):
            guess_str = " ".join(map(str, guesses[guess_index]))
            marks_str = " ".join(marks_list[guess_index])
            print(f"{round_num:2d}               {guess_str}         {marks_str}")
        else:
            print(f"{round_num:2d}")
        
print("="*60 + "\n")