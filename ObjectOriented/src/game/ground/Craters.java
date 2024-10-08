package game.ground;

import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.Exit;
import edu.monash.fit2099.engine.positions.Ground;
import edu.monash.fit2099.engine.positions.Location;
import game.ground.spawner.Spawner;

import java.util.ArrayList;
import java.util.Random;

/**
 * A class representing craters as a type of ground in the game world.
 * Craters are impassable by actors and can potentially spawn monsters.
 * Extends the {@link Ground} class.
 * Implements functionality for ticking and spawning monsters in the craters.
 *
 * @author Chen Ching Tung
 * @version 1.0.0
 * @since 2024-04-19
 */
public class Craters extends Ground {
    private Spawner monster;

    /**
     * Constructor for Craters class.
     * Creates craters with a display character and a monster spawner.
     *
     * @param monster The spawner used to generate monsters in the craters.
     */
    public Craters(Spawner monster) {
        super('u');
        this.monster = monster;
    }

    /**
     * Performs actions that occur every turn for the craters.
     * Determines whether a monster should be spawned based on the spawner's chance.
     *
     * @param location The location of the craters on the map.
     */
    @Override
    public void tick(Location location) {
        super.tick(location);
        Random random = new Random();
        int chance = random.nextInt(100);
        if (chance < this.monster.getChance())
            dropMonster(location);
    }

    /**
     * Determines whether an actor can enter the craters.
     * Craters are impassable by actors, so this method always returns false.
     *
     * @param actor The actor attempting to enter the craters.
     * @return False, indicating that actors cannot enter the craters.
     */
    @Override
    public boolean canActorEnter(Actor actor) {
        return false;
    }

    /**
     * Drops a spider at a random location adjacent to the craters.
     * The spider is spawned using the monster spawner associated with the craters.
     *
     * @param location The location of the craters on the map.
     */
    public void dropMonster(Location location) {
        Random random = new Random();
        ArrayList<Location> dropLocations = new ArrayList<>();
        for (Exit exit : location.getExits()) {
            Location neighbor = exit.getDestination();
            if (neighbor.canActorEnter(null))
                dropLocations.add(neighbor);
        }
        if (dropLocations.size() > 0)
            dropLocations.get(random.nextInt(dropLocations.size())).addActor(monster.spawn());
    }
}
