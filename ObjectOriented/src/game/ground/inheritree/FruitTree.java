package game.ground.inheritree;

import edu.monash.fit2099.engine.items.Item;
import edu.monash.fit2099.engine.positions.Location;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

/**
 * FruitTree serves as the base for trees that produce fruits
 *
 * @author Andrew Chong Han Wen
 */
public abstract class FruitTree extends Tree_Phase {
    /**
     * Fruit type to be spawned by the tree
     */
    protected Item fruit;

    /**
     * Constructor for FruitTree
     * @param displayChar
     */
    public FruitTree(char displayChar){
        super(displayChar);
    }

    /**
     * Tick method which spawns fruits around the surrounding of the tree
     * @param location    the location of the tree
     * @param tree the game world containing the tree
     */
    @Override
    public void tick(Location location, Tree tree){
        // List to store neighboring locations where items can be dropped
        List<Location> dropLocations = new ArrayList<>();
        // Find neighboring locations where items can be dropped
        findLocation(location, dropLocations);

        // Randomly determine if the big tree produces big fruits
        Random random = new Random();
        int chance = random.nextInt(100);
        if (dropLocations.size() != 0 && chance < 20) {
            // Add a big fruit to a random neighboring location if conditions are met
            dropLocations.get(random.nextInt(dropLocations.size())).addItem(fruit);
        }
    }
}
