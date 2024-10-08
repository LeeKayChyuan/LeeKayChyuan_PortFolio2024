package game.weapon;

import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.Exit;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.positions.Location;
import edu.monash.fit2099.engine.weapons.WeaponItem;
import game.Status;
import game.action.AttackAction;
import game.action.SellAction;
import game.item.Sellable;

/**
 * A class representing a metal pipe as a weapon in the game world.
 * Metal pipes are used as weapons that can be picked up, dropped off, and used by actors to attack.
 * Extends the {@link WeaponItem} class.
 * Implements functionality for attacking hostile actors.
 *
 * @author Chen Ching Tung
 * @version 1.0.0
 * @since 2024-04-19
 */
public class MetalPipe extends WeaponItem implements Sellable {
    Location currentLocation;

    int salePrice = 35;

    /**
     * Constructor for MetalPipe class.
     * Creates a metal pipe with a name, display character, damage, verb, and hit rate.
     */
    public MetalPipe() {
        super("Metal Pipe", '!', 1, "hits", 20);
    }

    /**
     * Updates the current location of the owner.
     *
     * @param currentLocation The current location of the metal pipe.
     * @param actor The actor carrying the metal pipe.
     */
    @Override
    public void tick(Location currentLocation, Actor actor) {
        super.tick(currentLocation, actor);
        this.currentLocation = currentLocation;
    }

    @Override
    public String sell(Actor actor, GameMap map){
        actor.removeItemFromInventory(this);
        actor.addBalance(this.getSalePrice());
        return actor + " sold the " + this + " for " + this.getSalePrice() + " credits";
    }
    @Override
    public int getSalePrice(){
        return salePrice;
    }

    /**
     * Generates a list of allowable actions for the metal pipe based on its current location.
     * If the other actor is hostile to the player, adds an attack action for the hostile actor.
     *
     * @param otherActor The other actor targeted for attack.
     * @param location The location where the metal pipe is currently placed.
     * @return An action list containing attack actions for hostile actors.
     */
    @Override
    public ActionList allowableActions(Actor otherActor, Location location) {
        ActionList actions = new ActionList();
        if (otherActor.hasCapability(Status.BUYER)){
            actions.add(new SellAction(this));
        }
        if (otherActor.hasCapability(Status.HOSTILE_TO_PLAYER)) {
            for (Exit exit : this.currentLocation.getExits()) {
                Location destination = exit.getDestination();
                Actor actor = destination.getActor();
                if (actor == otherActor)
                    actions.add(new AttackAction(actor, exit.getName(), this));
            }
        }
        return actions;
    }
}
