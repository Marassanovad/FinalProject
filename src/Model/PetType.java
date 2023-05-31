package src.Model;

public enum PetType {
    Cat,
    Dog,
    Hamster,
    Horse,
    Camel,
    Donkey;

    public static PetType getType (int typeId){
        switch (typeId){
            case 1:
                return PetType.Cat;
            case 2:
                return PetType.Dog;
            case 3:
                return PetType.Hamster;
            case 4:
                return PetType.Horse;
            case 5:
                return PetType.Donkey;
            case 6:
                return PetType.Camel;
            default:
                return null;
        }
    }
}