package game.ground.spawner;

import edu.monash.fit2099.engine.actors.Actor;
import game.actor.SuspiciousAstronaut;

/**
 * Class SuspiciousAstronautSpawner implements the Spawner interface, and is used to spawn
 * suspicious astronaut monsters into the game world
 * @Author Abrar Ahmed Syed Ali
 * @Modified Abrar Ahmed Syed Ali and Andrew Chong Han Wen
 */
public class SuspiciousAstronautSpawner implements Spawner{

    /**
     * Spawns a new SuspiciousAstronaut object into the game world
     * @return new SuspiciousAstronaut object
     */
    @Override
    public Actor spawn() {
        return new SuspiciousAstronaut();
    }

    /**
     * Returns the spawn rate of the monster
     * @return spawn rate
     */
    @Override
    public Integer getChance() {
        return 5;
    }
}
