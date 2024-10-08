package game.ground.inheritree;

import edu.monash.fit2099.engine.positions.Location;
import game.item.SmallFruit;

/**
 * A class representing a small tree in the game world.
 * Small trees are a type of tree that can produce small fruits.
 * Extends the {@link Tree_Phase} class.
 *
 * @author Andrew Chong Han Wen
 * @version 1.0.0
 * @since 2024-04-19
 */
public class Sapling extends FruitTree {
    private int age;
    /**
     * Constructor for creating a small tree.
     * Initializes the age of the tree.
     */
    public Sapling() {
        super('t');
        super.fruit = new SmallFruit();
        age = 0;
    }

    /**
     * Tick method of Sapling spawns the fruits from its parent tick method, and then ages the tree based on the age threshold.
     * @param location    the location of the tree
     * @param tree the game world containing the tree
     */
    @Override
    public void tick(Location location, Tree tree) {
        super.tick(location, tree);

        // Increment the age of the small tree
        this.age++;

        // If the age exceeds a certain threshold, replace the small tree with a big tree
        if (age > 6) {
            tree.setTree(new YoungTree());
        }
    }
}
