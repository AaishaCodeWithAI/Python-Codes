def get_valid_age():
    """Get and validate age input from user"""
    while True:
        try:
            age = int(input("Enter age (0-120): "))
            if 0 <= age <= 120:
                return age
            else:
                print("Please enter a valid age between 0 and 120.")
        except ValueError:
            print("Invalid input. Please enter a whole number for age.")

def get_valid_yes_no(prompt):
    """Get and validate yes/no input from user"""
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes', 'y', 'no', 'n']:
            return response in ['yes', 'y']
        else:
            print("Please enter 'yes' or 'no'.")

def get_residency_status():
    """Get and validate residency status"""
    while True:
        response = input("How long have you been a resident? (in years): ").strip()
        try:
            years = float(response)
            if years >= 0:
                return years
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_age_category(age):
    """Determine age category"""
    if age < 13:
        return "child"
    elif age < 18:
        return "teenager"
    elif age < 65:
        return "adult"
    else:
        return "senior"

def check_voting_eligibility(age, is_citizen, is_suspended, residency_years):
    """
    Check if a person is eligible to vote based on multiple criteria
    
    Args:
        age (int): Person's age
        is_citizen (bool): Whether person is a citizen
        is_suspended (bool): Whether person's voting rights are suspended
        residency_years (float): Years of residency
    
    Returns:
        tuple: (eligible (bool), reason (str))
    """
    if age < 18:
        return False, f"Must be at least 18 years old (currently {age})"
    
    if not is_citizen:
        return False, "Must be a citizen to vote"
    
    if is_suspended:
        return False, "Voting rights are currently suspended"
    
    if residency_years < 1:
        return False, f"Must be a resident for at least 1 year (currently {residency_years:.1f} years)"
    
    return True, "Eligible to vote"

def display_person_summary(person_data):
    """Display a formatted summary for a person"""
    print("\n" + "="*50)
    print("VOTING ELIGIBILITY SUMMARY")
    print("="*50)
    
    # Personal information
    print(f"\nPersonal Information:")
    print(f"  Age: {person_data['age']} years ({person_data['age_category']})")
    print(f"  Citizen: {'Yes' if person_data['is_citizen'] else 'No'}")
    print(f"  Residency: {person_data['residency_years']:.1f} years")
    print(f"  Voting Rights Suspended: {'Yes' if person_data['is_suspended'] else 'No'}")
    
    # Eligibility result
    print(f"\nEligibility Check:")
    print(f"  Status: {'ELIGIBLE' if person_data['eligible'] else 'NOT ELIGIBLE'}")
    print(f"  Reason: {person_data['reason']}")
    print("="*50)

def process_one_person():
    """Process one person's voting eligibility check"""
    print("\n" + "-"*30)
    print("NEW VOTER REGISTRATION")
    print("-"*30)
    
    # Get all required information with validation
    age = get_valid_age()
    is_citizen = get_valid_yes_no("Are you a citizen? (yes/no): ")
    residency_years = get_residency_status()
    is_suspended = get_valid_yes_no("Are your voting rights suspended? (yes/no): ")
    
    # Determine age category
    age_category = get_age_category(age)
    
    # Check eligibility
    eligible, reason = check_voting_eligibility(age, is_citizen, is_suspended, residency_years)
    
    # Prepare data for display
    person_data = {
        'age': age,
        'age_category': age_category,
        'is_citizen': is_citizen,
        'residency_years': residency_years,
        'is_suspended': is_suspended,
        'eligible': eligible,
        'reason': reason
    }
    
    # Display summary
    display_person_summary(person_data)
    
    return person_data

def main():
    """Main program function"""
    print("="*60)
    print("VOTING ELIGIBILITY CHECKER")
    print("="*60)
    print("This program checks voting eligibility based on:")
    print("- Age (must be 18+)")
    print("- Citizenship status")
    print("- Residency (must be resident for 1+ years)")
    print("- Voting rights suspension status")
    print("="*60)
    
    all_records = []
    
    while True:
        # Process one person
        person_data = process_one_person()
        all_records.append(person_data)
        
        # Ask if user wants to check another person
        print("\n" + "-"*30)
        check_another = input("Check another person? (yes/no): ").strip().lower()
        
        if check_another not in ['yes', 'y']:
            break
    
    # Display summary if multiple people were checked
    if len(all_records) > 1:
        display_final_summary(all_records)

def display_final_summary(records):
    """Display a final summary for multiple records"""
    print("\n" + "="*60)
    print("FINAL SUMMARY")
    print("="*60)
    
    total_processed = len(records)
    eligible_count = sum(1 for record in records if record['eligible'])
    
    print(f"Total people processed: {total_processed}")
    print(f"Total eligible to vote: {eligible_count}")
    print(f"Total not eligible: {total_processed - eligible_count}")
    
    if eligible_count > 0:
        print("\nEligible voters:")
        for i, record in enumerate([r for r in records if r['eligible']], 1):
            print(f"  {i}. {record['age']} year old {record['age_category']}")
    
    if total_processed - eligible_count > 0:
        print("\nNot eligible (reasons):")
        for i, record in enumerate([r for r in records if not r['eligible']], 1):
            print(f"  {i}. {record['reason']}")
    
    print("="*60)
    print("Thank you for using the Voting Eligibility Checker!")
    print("="*60)

# Run the program
if __name__ == "__main__":
    main()
