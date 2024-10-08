package game.ground.spawner;

import edu.monash.fit2099.engine.actors.Actor;
import game.actor.HuntsmanSpider;

/**
 * A class representing a spider spawner in the game world.
 * Spiderspawner is responsible for spawning huntsman spiders.
 * Implements the {@link Spawner} interface.
 *
 * The chance of spawning a spider is set to 5 by default.
 *
 * @author Chen Ching Tung
 * @version 1.0.0
 * @since 2024-04-19
 */
public class Spiderspawner implements Spawner {
    private int chance = 5;

    /**
     * Spawns a huntsman spider in the game world.
     *
     * @return The huntsman spider that is spawned.
     */
    @Override
    public Actor spawn() {
        return new HuntsmanSpider();
    }

    /**
     * The chance of spawning a huntsman spider.
     *
     * @return The chance of spawning, represented as an integer.
     */
    @Override
    public Integer getChance() {
        return this.chance;
    }
}
