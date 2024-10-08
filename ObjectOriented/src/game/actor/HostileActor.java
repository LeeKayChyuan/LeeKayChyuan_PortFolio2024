package game.actor;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actions.DoNothingAction;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.actors.Behaviour;
import edu.monash.fit2099.engine.displays.Display;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.weapons.IntrinsicWeapon;
import game.Ability;
import game.Status;
import game.action.AttackAction;
import game.behavior.AttackBehavior;

import java.util.TreeMap;

/**
 * Represents a hostile actor in the game world that can engage in combat with other actors.
 * Hostile actors inherit attributes and behaviors from the {@link Actor} class and can detect nearby enemies to attack.
 *
 * @author Chen Ching Tung
 * @version 1.0.0
 * @since 2024-04-19
 */
public abstract class HostileActor extends Actor {

    boolean canKill = false;
    IntrinsicWeapon weapon;
    TreeMap<Integer, Behaviour> behaviours = new TreeMap<>();

    /**
     * Constructor for creating a new HostileActor.
     *
     * @param name        the name of the Actor
     * @param displayChar the character that will represent the Actor in the display
     * @param hitPoints   the Actor's starting hit points
     */
    public HostileActor(String name, char displayChar, int hitPoints) {
        super(name, displayChar, hitPoints);
        this.addCapability(Status.HOSTILE_TO_PLAYER);
        this.addCapability(Ability.CANT_OVER_FLOOR);
    }

    /**
     * Overrides the {@code playTurn()} method of the {@link Actor} class.
     * Hostile actors implement their logic for the actor's turn.
     *
     * @param actions    collection of possible Actions for this Actor
     * @param lastAction The Action this Actor took last turn
     * @param map        the map containing the Actor
     * @param display    the display object for rendering
     * @return the Action to be performed
     */
    @Override
    public Action playTurn(ActionList actions, Action lastAction, GameMap map, Display display) {
        for (Behaviour behaviour : behaviours.values()) {  // Iterate through the behaviors
            Action action = behaviour.getAction(this, map);  // Get the action from the behavior
            if (action != null) {
                return action;
            }
        }
        return new DoNothingAction();  // If no action is found, do nothing
    }


    public void setInstantKill(){
        this.weapon = new IntrinsicWeapon(Integer.MAX_VALUE, "smite", 100);
        this.behaviours.put(1, new AttackBehavior(weapon));
    }

    /**
     * Returns a collection of Actions that the otherActor can perform to attack the current Actor.
     * It adds an {@link AttackAction} to the action list if the other actor has the {@code HOSTILE_TO_ENEMY} capability.
     *
     * @param otherActor the Actor that might be performing attack
     * @param direction  string representing the direction of the other Actor
     * @param map        current GameMap
     * @return a collection of Actions
     */
    @Override
    public ActionList allowableActions(Actor otherActor, String direction, GameMap map) {
        ActionList actions = new ActionList();
        if(otherActor.hasCapability(Status.HOSTILE_TO_ENEMY)){
            actions.add(new AttackAction(this, direction));
        }
        return actions;
    }
}
