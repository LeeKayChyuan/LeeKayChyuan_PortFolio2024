package game.item;

import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.items.Item;
import edu.monash.fit2099.engine.positions.GameMap;


import java.util.Random;

/**
 * A class representing metal sheets as an item in the game world.
 * Metal sheets are used as an item that can be picked up, dropped off, and potentially used by actors.
 * Extends the {@link Item} class.
 *
 * @author Chen Ching Tung
 * @version 1.0.0
 * @since 2024-04-19
 */
public class MetalSheets extends SellableItem implements Sellable {

    /**
     * Constructor for MetalSheets class.
     * Creates metal sheets with a name, display character, and portability status.
     */
    public MetalSheets() {
        super("Metal Sheets", '%', true, 20);
    }


    /**
     *
     * This method implements the sale of the item including any necessary special features
     *
     * @param actor the actor selling the item
     * @param map the map which the player is standing on
     * @return string confirming the sale of the item
     */
    public String sell(Actor actor, GameMap map){
        Random random = new Random();

        if (random.nextInt(100) > 60) {
            actor.removeItemFromInventory(this);
            actor.addBalance(this.getSalePrice());
            return actor + " sold the " + this + " for " + this.getSalePrice() + " credits";
        }
        else {
            int discountPrice = 10;
            actor.removeItemFromInventory(this);
            actor.addBalance(discountPrice);
            System.out.println("The factory asked for a discount and offered 10 credits for the large bolts.");
            System.out.println(actor + " accepted the offer");
            return actor + " sold the " + this + " for " + discountPrice + " credits";
        }
    }

}
