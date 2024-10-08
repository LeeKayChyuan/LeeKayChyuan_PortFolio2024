package game.ground.inheritree;

import edu.monash.fit2099.engine.positions.Exit;
import edu.monash.fit2099.engine.positions.Ground;
import edu.monash.fit2099.engine.positions.Location;

import java.util.List;

/**
 * An abstract class representing tree phases in the game world.
 * Extends the {@link Ground} class.
 *
 * @author Chen Ching Tung
 * @version 1.0.0
 * @since 2024-04-19
 */
public abstract class Tree_Phase extends Ground {

    /**
     * Constructor.
     *
     * @param displayChar character to display for this type of terrain
     */
    public Tree_Phase(char displayChar) {
        super(displayChar);
    }

    /**
     * Performs a game tick for the tree.
     * This method is called once per turn to perform any updates or actions related to the tree.
     *
     * @param location    the location of the tree
     * @param tree the game world containing the tree
     */
    public void tick(Location location, Tree tree) {
        super.tick(location);
    }

    /**
     * Finds neighboring locations where items can be dropped.
     *
     * @param location      the location of the tree
     * @param dropLocations a list to store neighboring locations where items can be dropped
     */
    public void findLocation(Location location, List<Location> dropLocations) {

        // Iterate over the exits of the current location
        for (Exit exit : location.getExits()) {
            Location neighbor = exit.getDestination();

            // Check if actors can enter the neighboring location
            if (neighbor.canActorEnter(null)) {
                dropLocations.add(neighbor);
            }
        }
    }
}

