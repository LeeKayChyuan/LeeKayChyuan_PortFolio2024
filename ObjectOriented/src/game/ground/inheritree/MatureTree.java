package game.ground.inheritree;

import game.item.BigFruit;

/**
 * A class representing a big tree in the game world.
 * Big trees are a type of tree that can produce big fruits.
 * Extends the {@link Tree_Phase} class.
 *
 *
 * @author Andrew Chong Han Wen
 * @version 1.0.0
 * @since 2024-04-19
 */
public class MatureTree extends FruitTree {

    /**
     * Constructor for creating a big tree.
     */
    public MatureTree() {
        super('T');
        super.fruit = new BigFruit();
    }
}
