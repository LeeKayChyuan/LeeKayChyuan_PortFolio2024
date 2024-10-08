package game.item;

import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.items.Item;
import edu.monash.fit2099.engine.positions.GameMap;


/**
 * An interface class that creates a new Sellable Item which will
 * easily allow items to be sold in the game
 *
 * @author Toby Marsden
 * @version 1.0.0
 * @since 2024-05-18
 */
public interface Sellable {


    /**
     *
     * This method will implement the sale of the item including any necessary special features
     *
     * @param actor the actor selling the item
     * @param map the map which the player is standing on
     * @return string confirming the sale of the item
     */
    String sell(Actor actor, GameMap map);


    /**
     *
     * This method will implement the fetching of the sale price of the item
     *
     * @return the sale price of the item
     */
    int getSalePrice();

}
