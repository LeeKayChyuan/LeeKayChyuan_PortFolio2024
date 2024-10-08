package game.ground.inheritree;

import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.Ground;
import edu.monash.fit2099.engine.positions.Location;

/**
 * Tree abstract class to serve as a base for all tree types
 *
 * @author Andrew Chong Han Wen
 */
public abstract class Tree extends Ground {
    private Tree_Phase tree;

    /**
     * Constructor for creating a Tree.
     * Initializes the Inheritree with a small tree by default.
     */
    public Tree(char display) {
        super(display);
        this.tree = new Sprout();
    }

    /**
     * Sets the tree instance contained in the Inheritree.
     *
     * @param tree the tree instance to set
     */
    public void setTree(Tree_Phase tree) {
        this.tree = tree;
        setDisplayChar(tree.getDisplayChar());  // Update the display character based on the new tree type
    }

    /**
     * Checks if an actor can enter the Inheritree.
     * Actors cannot enter an Inheritree.
     *
     * @param actor the actor attempting to enter
     * @return always returns false since actors cannot enter
     */
    @Override
    public boolean canActorEnter(Actor actor) {
        return false;
    }

    /**
     * Performs a game tick for the Inheritree.
     * This method is called once per turn to perform any updates or actions related to the Inheritree.
     * It delegates the tick operation to the contained tree instance.
     *
     * @param location the location of the Inheritree
     */
    @Override
    public void tick(Location location) {
        super.tick(location);  // Call the superclass tick method
        tree.tick(location, this);  // Delegate the tick operation to the contained tree instance
    }
}
