package game.ground.inheritree;

/**
 * YoungTree class is a phase of a tree in the game world that does not produce any fruits
 *
 * @author Andrew Chong Han Wen
 */
public class YoungTree extends NoFruitTree{

    /**
     * Constructor method for YoungTree, sets the age threshold and the next tree phase
     */
    public YoungTree() {
        super('y');
        super.age_threshold = 5;
        super.setTree = new MatureTree();
    }
}
