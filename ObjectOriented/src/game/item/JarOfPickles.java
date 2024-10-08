package game.item;

import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.items.Item;
import edu.monash.fit2099.engine.positions.GameMap;
import game.action.ConsumeAction;

import java.util.Random;

/**
 * A class that represents a Jar Of Pickles as an Item in the game world.
 * Jar of Pickles can be picked up and eaten by the actor
 * Extends the {@link Item} class.
 * Implements the {@link Consumable} class.
 *
 * @author Chen Ching Tung
 * @version 1.0.0
 * @since 2024-05-05
 */
public class JarOfPickles extends SellableItem implements Consumable, Sellable {

    private final int heal = 1;

    /***
     * Constructor of JarOfPickles class.
     * Create JarOfPickles with name, display character and portability status.
     */
    public JarOfPickles() {
        super("Jar of Pickles", 'n', true, 25);
    }

    /**
     * Generates a list of allowable actions of the Jar of Pickles.
     * Adds a consume action to the list of actions for the other actor.
     * @param otherActor The actor interacting with the Jar of Pickles.
     * @return An action list containing the action that can be performed by other actor.
     */
    public ActionList allowableActions(Actor otherActor) {
        ActionList actions = super.allowableActions(otherActor);
        actions.add(new ActionList(new ConsumeAction(this)));
        return actions;
    }

    /**
     * Execute the eat a jar of pickle by the actor interacting with it.
     * Remove this item from the actor's inventory.
     * 50% chance to get heal or hurt.
     * @param actor the actor that are interacting with this jar of pickles.
     * @return A string that shows whether the interacting actor is hurt or heal.
     */
    @Override
    public String consume(Actor actor) {
        actor.removeItemFromInventory(this);
        Random random = new Random();
        if(random.nextInt(2) > 0) {
            actor.heal(this.heal);
            return String.format("The %s heals the %s by %d hit points", this, actor, this.heal);
        }
        else{
            actor.hurt(this.heal);
            return String.format("The %s hurt the %s by %d hit points", this, actor, this.heal);
        }

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
        Random random = new Random();

        if (random.nextInt(100) > 50) {
            actor.removeItemFromInventory(this);
            actor.addBalance(this.getSalePrice());
            return actor + " sold the Jars of pickles for " + this.getSalePrice() + " credits";
        }
        else {
            int discountPrice = 50;
            actor.removeItemFromInventory(this);
            actor.addBalance(discountPrice);
            System.out.println("The factory asked for a discount and offered 10 credits for the Jars of pickles .");
            System.out.println(actor + " accepted the offer");
            return actor + " sold the Jars of pickles for " + discountPrice + " credits";
        }
    }


    /**
     * Provides a description of the eat a jar of pickles for display in the menu.
     *
     * @param actor The actor interacting with this jar of pickles.
     * @return A description of the eat a jar of pickles.
     */
    @Override
    public String menuDescription(Actor actor) {
        return  " heal " + this.heal + " hit points";
    }
}
