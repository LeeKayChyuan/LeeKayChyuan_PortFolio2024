package game.item;

import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.items.Item;
import edu.monash.fit2099.engine.positions.Exit;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.positions.Location;
import game.Ability;
import game.Status;
import game.action.SellAction;

/**
 * An abstract class that creates a new Sellable Item which will
 * easily allow items to be sold in the game
 * Extends the {@link Item} class.
 *
 * @author Toby Marsden
 * @version 1.0.0
 * @since 2024-05-18
 */

public abstract class SellableItem extends Item implements Sellable {
    int salePrice;
    /***
     * Constructor.
     *  @param name the name of this Item
     * @param displayChar the character to use to represent this item if it is on the ground
     * @param portable true if and only if the Item can be picked up
     */
    public SellableItem(String name, char displayChar, boolean portable, int price) {
        super(name, displayChar, portable);
        this.salePrice = price;
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
    public abstract String sell(Actor actor, GameMap map);

    /**
     *
     * This method will implement the fetching of the sale price of the item
     *
     * @return the sale price of the item
     */
    @Override
    public int getSalePrice(){
        return this.salePrice;
    }


    /**
     *
     * This method implements the sale of the item including any necessary special features
     *
     * @param otherActor the actor selling the item
     * @param location the location on the map which the player is standing on
     * @return action list with sell action
     */
    @Override
    public ActionList allowableActions(Actor otherActor, Location location) {
        ActionList actions = super.allowableActions(otherActor);
        if(otherActor.hasCapability(Status.BUYER))
            actions.add(new ActionList(new SellAction(this)));
        return actions;
    }
}
