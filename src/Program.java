package src;
import src.Controller.PetController;
import src.Model.Pet;
import src.Services.IRepository;
import src.Services.PetRepository;
import src.Userinterface.ConsoleMenu;

public class Program {
    public static void main(String[] args) throws Exception {

        IRepository<Pet> myFarm = new PetRepository();
        PetController controller = new PetController(myFarm);
        new ConsoleMenu(controller).start();
    }
}    
