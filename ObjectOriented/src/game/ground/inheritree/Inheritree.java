package game.ground.inheritree;

import edu.monash.fit2099.engine.positions.Ground;

/**
 * A class representing an "Inheritree" ground in the game world.
 * The Inheritree is a special type of ground that evolves from a small tree to a big tree over time.
 * It contains a tree instance that can change from a small tree to a big tree during the game.
 * Extends the {@link Ground} class.
 *
 * @author Chen Ching Tung
 * @version 1.0.0
 * @since 2024-04-19
 */
public class Inheritree extends Tree {
    /**
     * Tree_Phase representing the phase of the tree
     */
    private Tree_Phase tree;  // The tree instance contained in the Inheritree

    /**
     * Constructor for creating an Inheritree.
     * Initializes the Inheritree with a small tree by default.
     */
    public Inheritree() {
        super(',');
        this.tree = new Sprout();  // Initialize with a small tree by default
    }
}
