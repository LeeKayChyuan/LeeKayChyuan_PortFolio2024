package game.ground;

import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.actors.attributes.ActorAttributeOperations;
import edu.monash.fit2099.engine.actors.attributes.BaseActorAttributes;
import edu.monash.fit2099.engine.positions.Ground;

import edu.monash.fit2099.engine.positions.Location;
import game.action.ConsumeAction;
import game.item.Consumable;


/**
 * A class that represents puddle.
 * Created by: Chen Ching Tung
 * @author Riordan D. Alfredo
 * Modified by: Chen Ching Tung & Lee Kay Chyuan
 */
public class Puddle extends Ground implements Consumable {

    /***
     * Constructor of Puddle class.
     * Create Puddle with display character.
     */
    public Puddle() {
        super('~');
    }

    /**
     * Generates a list of allowable actions of the Puddle.
     * Adds a consume action to the list of actions for the other actor if the actor is on the Puddle.
     * @param otherActor The actor interacting with the Jar of Pickles.
     * @param location The location of this Puddle.
     * @param direction The direction of this Puddle from the actor interacting to it.
     * @return An action list containing the action that can be performed by other actor.
     */
    @Override
    public ActionList allowableActions(Actor otherActor, Location location, String direction){
        ActionList actions = super.allowableActions(otherActor, location, direction);
        if (location.getActor() == otherActor) {
            actions.add(new ActionList(new ConsumeAction(this)));
        }
        return actions;
    }

    /**
     * Execute the drink the water in the Puddle by the actor interacting with it.
     * Modify the Maximum Base Actor Health Attribute by increasing 1.
     * @param actor the actor that are interacting with this puddle.
     * @return A string that shows the water was drink and increase the Max Health point .
     */
    @Override
    public String consume(Actor actor) {
        actor.modifyAttributeMaximum(BaseActorAttributes.HEALTH, ActorAttributeOperations.INCREASE, 1);
        return String.format("The water increase the %s maximum health point by 1", this, actor);
    }

    /**
     * Provides a description of the drink the water in the Puddle for display in the menu.
     * @param actor The actor interacting with this jar of pickles.
     * @return A description of the drink the water in the Puddle.
     */
    @Override
    public String menuDescription(Actor actor) {
        return " Drink the water in the puddle";
    }

    /**
     * Provides a name Puddle
     * @return a string of the name of Puddle
     */
    public String toString() {
        return "puddle";
    }
}
