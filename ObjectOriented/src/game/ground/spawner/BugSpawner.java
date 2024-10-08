package game.ground.spawner;

import edu.monash.fit2099.engine.actors.Actor;
import game.actor.AlienBug;

import java.util.Random;

/**
 * Class bug spawner implements from the spawner class, and is used to spawn
 * alien bugs into the game world
 * @Author Andrew Chong Han Wen
 */
public class BugSpawner implements Spawner{

    /**
     * Target for alien bug to follow
     */
    Actor target;

    /**
     * Constructor method
     * @param target
     */
    public BugSpawner(Actor target){
        this.target = target;
    }

    /**
     * Spawning method, spawns a new alien bug into the game world
     * @return new alien bug object
     */
    @Override
    public Actor spawn() {
        Random random = new Random();
        return new AlienBug(random.nextInt(1000), this.target);
    }

    /**
     * Returns the spawn rate
     * @return spawn rate integer
     */
    @Override
    public Integer getChance() {
        return 10;
    }
}