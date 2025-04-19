from pet import Pet

def main():
    # Create a pet with custom type
    my_pet = Pet("Rex", "Golden Retriever")
    
    print("\n🌟 Welcome to the Digital Pet Simulator! 🌟")
    print(f"Meet your new {my_pet.pet_type}, {my_pet.name}!\n")
    
    # Initial status
    my_pet.get_status()
    
    # Test basic methods
    my_pet.eat("kibble")
    my_pet.play("fetch")
    my_pet.sleep()
    
    # Check status after actions
    my_pet.get_status()
    
    # Test training
    my_pet.train("roll over")
    my_pet.train("play dead")
    my_pet.train("shake hands")
    
    # Show tricks
    my_pet.show_tricks()
    
    # Test extra methods
    my_pet.bathe()
    my_pet.exercise()
    my_pet.celebrate_birthday()
    
    # Final status
    my_pet.get_status()

if __name__ == "__main__":
    main()