package game.action;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.positions.Location;


/**
 * A class representing an action that allows an actor to move to a specified location on the map.
 * This action implements the movement functionality within the game environment.
 * @author Abrar Ahmed Syed Ali
 * @version 1.0.0
 * @since 31/05/2024
 */
 public class MoveToAction extends Action {
    private Location moveToLocation;
    /**
     * One of the 8-d navigation
     */

    private String direction;

    /**
     * Constructor to create an Action that will move the Actor to a Location in a given Direction.  A currently-unused
     * menu hotkey will be assigned.
     *
     * Note that this constructor does not check whether the supplied Location is actually in the given direction
     * from the Actor's current location.  This allows for (e.g.) teleporters, etc.
     *
     * @param moveToLocation Location to move to
     * @param direction String describing the direction to move in, e.g. "north"
     */

    public MoveToAction(Location moveToLocation, String direction) {
        this.moveToLocation = moveToLocation;
        this.direction = direction;
    }
    public GameMap map(){
        return this.moveToLocation.map();
    }
    /**
     * Allow the Actor to be moved.
     *
     * Overrides Action.execute()
     *
     * @see Action#execute(Actor, GameMap)
     * @param actor The actor performing the action.
     * @param map The map the actor is on.
     * @return a description of the Action suitable for the menu
     */

    @Override
    public String execute(Actor actor, GameMap map) {
        map.moveActor(actor, moveToLocation);
        return actor + " arrived at " + moveToLocation + " in " + direction;
    }
    /**
     * Returns a description of this movement suitable to display in the menu.
     *
     * @param actor The actor performing the action.
     * @return a String, e.g. "Player moves east"
     */

    @Override
    public String menuDescription(Actor actor) {
        return actor + " travels to " + direction;
    }
}