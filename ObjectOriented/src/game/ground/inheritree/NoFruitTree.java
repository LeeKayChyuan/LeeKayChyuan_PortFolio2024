package game.ground.inheritree;

import edu.monash.fit2099.engine.positions.Location;

/**
 * NoFruitTree abstract class extends from the Tree_Phase class
 * To be extended by trees that do not need to produce fruits
 *
 * @author Andrew Chong Han Wen
 */
public abstract class NoFruitTree extends Tree_Phase {
    /**
     * Age threshold for the tree to grow
     */
    protected int age_threshold;
    /**
     * Next tree phase to be set
     */
    protected Tree_Phase setTree;
    /**
     * Current age of the tree
     */
    private int age;

    /**
     * Constructor for the NoFruitTree
     * @param displayChar
     */
    public NoFruitTree(char displayChar) {
        super(displayChar);
    }

    /**
     * Tick method which increases the current age, and sets the next phase of the tree
     * @param location    the location of the tree
     * @param tree the game world containing the tree
     */
    @Override
    public void tick(Location location, Tree tree) {
        // Increment the age of the small tree
        this.age++;

        // If the age exceeds a certain threshold, replace the small tree with a big tree
        if (age > age_threshold) {
            tree.setTree(setTree);
        }
    }
}
