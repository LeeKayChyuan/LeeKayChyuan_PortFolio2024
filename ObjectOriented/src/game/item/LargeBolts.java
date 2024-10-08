package game.item;

import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.items.Item;
import edu.monash.fit2099.engine.positions.GameMap;


/**
 * A class representing large bolts as an item in the game world.
 * Large bolts are used as an item that can be picked up, dropped of and potentially used by actors.
 * Extends the {@link Item} class.
 *
 * @author Chen Ching Tung
 * @version 1.0.0
 * @since 2024-04-19
 */
public class LargeBolts extends SellableItem implements Sellable {

    /**
     * Constructor for LargeBolts class.
     * Creates large bolts with a name, display character, and portability status.
     */
    public LargeBolts() {
        super("Large Bolts", '+', true, 25);
    }


    /**
     *
     * This method implements the sale of the item including any necessary special features
     *
     * @param actor the actor selling the item
     * @param map the map which the player is standing on
     * @return string confirming the sale of the item
     */

    @Override
    public String sell(Actor actor,  GameMap map){
        actor.removeItemFromInventory(this);
        actor.addBalance(this.getSalePrice());
        return actor + " sold the " + this + " for " + this.getSalePrice() + " credits";
    }


    /**
     * Retrieves the sale price of the large bolts.
     *
     * @return the sale price of the large bolts
     */
    public int getSalePrice() {
        return salePrice;
    }

}
