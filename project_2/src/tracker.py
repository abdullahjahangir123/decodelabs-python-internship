def start_expense_tracker():
    # PHASE 1: INITIALIZATION (MEMORY STAGE)
    # total variable ko loop ke bahar rakhna zaroori hai taake data amnesia na ho
    total_spent = 0 
    
    print("=" * 50)
    print("      DECODELABS - EXPENSE TRACKER BACKEND ENGINE      ")
    print("=" * 50)
    print("Instructions:")
    print("- Enter expense amounts as numbers (e.g., 100, 50, 22.5)")
    print("- Type 'exit' or 'quit' to stop the program and get the total bill.")
    print("-" * 50)

    # PHASE 2: CONTINUOUS DATA STREAM (THE ENGINE LOOP)
    while True:
        # User se raw input receiving
        user_input = input("Enter expense amount: ").strip().lower()

        # PHASE 3: THE SENTINEL / KILL SWITCH (EXIT MECHANISM)
        if user_input in ['exit', 'quit']:
            print("\n" + "=" * 50)
            print("Shutting down the Engine... Core Logic Terminated.")
            break

        # PHASE 4: THE DIGITAL POKA-YOKE (ERROR-HANDLING BARRIER)
        try:
            # String input ko float (decimal number) mein transform karne ki koshish
            current_expense = float(user_input)

            # Defensive Check: Expense kabhi negative nahi ho sakti
            if current_expense < 0:
                print("[VALIDATION ERROR]: Expense cannot be negative! Try again.")
                continue

            # PHASE 5: DATA ACCUMULATION (STATE UPDATE)
            # total = total + new_expense (Financial Truth Logic)
            total_spent += current_expense
            print(f"[SUCCESS]: Added ${current_expense:.2f} | Current Total: ${total_spent:.2f}")
            print("-" * 30)

        except ValueError:
            # Agar user ne "ten" ya koi invalid character enter kiya toh yeh block crash hone se bachayega
            print("[DISASTER AVERTED]: Invalid Input! Please enter a valid number or 'exit'.")
            print("-" * 30)

    # PHASE 6: FINAL OUTPUT STREAM (PRESENTATION)
    print(f"FINAL AUDIT RESULT -> Total Amount Spent: ${total_spent:.2f}")
    print("=" * 50)

# Program ko run karne ke liye function ko call karein
if __name__ == "__main__":
    start_expense_tracker()
