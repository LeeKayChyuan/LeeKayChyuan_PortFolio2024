package game;

import edu.monash.fit2099.engine.displays.Display;
import edu.monash.fit2099.engine.positions.FancyGroundFactory;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.positions.World;
import game.action.MoveToAction;
import game.actor.*;
import game.ground.*;
import game.ground.inheritree.Inheritree;
import game.ground.spawner.BugSpawner;
import game.ground.spawner.Spiderspawner;
import game.ground.spawner.SuspiciousAstronautSpawner;
import game.item.JarOfPickles;
import game.item.LargeBolts;
import game.item.MetalSheets;
import game.item.PotOfGold;
import game.weapon.MetalPipe;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;


/**
 * The main class to start the game.
 * Created by: Adrian Kristanto
 * @author Adrian Kristanto
 * Modified by: Chen Ching Tung
 *
 */
public class Application {

    public static void main(String[] args) {

        World world = new World(new Display());
        FancyGroundFactory groundFactory = new FancyGroundFactory(new Dirt(),
                new Wall(), new Floor(), new Puddle(), new Inheritree());

        List<String> map = Arrays.asList(
                "...~~~~.........~~~...........",
                "...~~~~.......................",
                "...~~~........................",
                "..............................",
                ".............#####............",
                ".............#___#...........~",
                ".............#___#..........~~",
                "........#....##_##.........~~~",
                "............,....~~........~~~",
                "................~~~~.......~~~",
                ".............~~~~~~~........~~",
                "......~.....~~~~~~~~.........~",
                ".....~~~...~~~~~~~~~..........",
                ".....~~~~~~~~~~~~~~~~........~",
                ".....~~~~~~~~~~~~~~~~~~~....~~");
        GameMap gameMap = new GameMap(groundFactory, map);
        world.addGameMap(gameMap);

        List<String> parkingMap = Arrays.asList(
                ".......",
                ".#####.",
                ".#___#.",
                ".#___#.",
                ".##_##.",
                ".......",
                ".......",
                ".......",
                ".......",
                ".......");
        GameMap parking  = new GameMap(groundFactory, parkingMap);
        world.addGameMap(parking);

        List<String> moonMap = Arrays.asList(
                "..........................~~~~",
                "..........................~~~~",
                "..........,...............~~~~",
                "~..........................~..",
                "~~...........#####............",
                "~~~..........#___#............",
                "~~~..........#___#............",
                "~~~..........##_##............",
                "~~~..................~~.......",
                "~~~~................~~~~......",
                "~~~~...............~~~~~......",
                "..~................~~~~.......",
                "....................~~........",
                ".............~~...............",
                "............~~~~..............");
        GameMap moon  = new GameMap(groundFactory, moonMap);
        world.addGameMap(moon);

        for (String line : FancyMessage.TITLE.split("\n")) {
            new Display().println(line);
            try {
                Thread.sleep(200);
            } catch (Exception exception) {
                exception.printStackTrace();
            }
        }
        ArrayList<MoveToAction> moveActions = new ArrayList<>();
        moveActions.add(new MoveToAction(gameMap.at(15, 6), "to Polymorphia!"));
        moveActions.add(new MoveToAction(parking.at(3,3), "to Factory!"));
        moveActions.add(new MoveToAction(moon.at(15,6), "to Moon!"));
        ComputerTerminal computerTerminal = new ComputerTerminal(moveActions);
        gameMap.at(15, 5).setGround(computerTerminal);
        parking.at(3,2).setGround(computerTerminal);
        parking.at(3,8).addActor(new HumanoidFigure());
        moon.at(15,5).setGround(computerTerminal);
        gameMap.at(4, 5).setGround(new Craters(new Spiderspawner()));
        gameMap.at(14, 12).setGround(new Craters(new SuspiciousAstronautSpawner()));

        gameMap.at(15, 9).addItem(new LargeBolts());
        gameMap.at(15, 8).addItem(new MetalSheets());
        gameMap.at(22,10).addItem(new MetalPipe());
        gameMap.at(7, 8).addItem(new JarOfPickles());
        gameMap.at(8, 8).addItem(new PotOfGold());
        gameMap.at(10, 8).addItem(new JarOfPickles());

        Player player = new Player("Intern", '@', 4);
        player.addBalance(100);
        world.addPlayer(player, gameMap.at(15, 6));
        gameMap.at(20, 5).setGround(new Craters(new BugSpawner(player)));
        Random random = new Random();
        gameMap.at(7, 9).addActor(new AlienBug(random.nextInt(1000),player));
        gameMap.at(1, 3).addActor(new SuspiciousAstronaut());
        gameMap.at(5, 9).addActor(new HuntsmanSpider());

        world.run();
        for (String line : FancyMessage.YOU_ARE_FIRED.split("\n")) {
            new Display().println(line);
            try {
                Thread.sleep(200);
            } catch (Exception exception) {
                exception.printStackTrace();
            }
        }
    }
}