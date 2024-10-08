package game.actor;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.actors.attributes.BaseActorAttributes;
import edu.monash.fit2099.engine.displays.Display;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.displays.Menu;

import edu.monash.fit2099.engine.positions.Location;
import game.Ability;
import game.Status;

/**
 * Class representing the Player.
 * The Player class extends the Actor class and represents the player-controlled character in the game.
 * It allows the player to interact with the game world through actions.
 *
 * Extends the {@link Actor} class.
 *
 * @author Chen Ching Tung
 * @version 1.0.0
 * @since 2024-04-19
 */
public class Player extends Actor {

    /**
     * Constructor for creating a Player.
     *
     * @param name        Name to call the player in the UI
     * @param displayChar Character to represent the player in the UI
     * @param hitPoints   Player's starting number of hit points
     */
    public Player(String name, char displayChar, int hitPoints) {
        super(name, displayChar, hitPoints);
        this.addCapability(Status.HOSTILE_TO_ENEMY);  // The player is initially hostile to enemy actors
        this.updateDamageMultiplier(0.2f);
    }

    /**
     * Defines the player's behavior during their turn.
     * Displays the player's health and shows a menu of available actions for the player to choose from.
     *
     * @param actions    List of available actions for the player
     * @param lastAction The action performed by the player on the previous turn
     * @param map        The current game map
     * @param display    The display object to print messages or menus
     * @return The action selected by the player for the current turn
     */
    @Override
    public Action playTurn(ActionList actions, Action lastAction, GameMap map, Display display) {

        // Display the player's health and balance
        display.println("Player's health: " + this.getAttribute(BaseActorAttributes.HEALTH));
        display.println("Player's balance: " + this.getBalance());


        // Handle multi-turn Actions
        if (lastAction.getNextAction() != null)
            return lastAction.getNextAction();
        // Show the menu of available actions for the player to choose from
        Menu menu = new Menu(actions);
        return menu.showMenu(this, display);


    }
}
