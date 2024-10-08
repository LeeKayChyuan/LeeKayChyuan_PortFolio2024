package game.ground.spawner;

import edu.monash.fit2099.engine.actors.Actor;

/**
 * The Spawner interface represents an object that spawns actors in the game world.
 * Implementing classes are responsible for defining how actors are spawned and determining the chance of spawning.
 *
 * @author Chen Ching Tung
 * @version 1.0.0
 * @since 2024-04-19
 */
public interface Spawner {

    /**
     * Spawns an monster in the game world.
     *
     * @return The actor that is spawned.
     */
    public Actor spawn();

    /**
     * The chance of spawning a monster.
     *
     * @return The chance of spawning, represented as an integer.
     */
    public Integer getChance();
}
