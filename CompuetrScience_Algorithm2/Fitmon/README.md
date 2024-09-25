Question 1
You are an adventurer in FITWORLD– a magical world where humans and FITMONs live in
 harmony. FITMONs are insanely cute creatures 1 which make everyone around them happy.
 Each FITMON has a cuteness_score where a higher score means a cuter FITMON.
 Recently, it was discovered that it is possible to fuse FITMONs together. The fusing process
 could increase or decrease the cuteness_score of the resulting FITMON. Thus, you set out to
 fuse FITMONs together, to create the very cutest FITMON possible, that no FITMON ever
 was. In order to do so, you head over to a FITMON Center

 Question 2
 You are a bear stuck in the forest and would like to escape the forest. Unfortunately, the
 forest itself is known as the Delulu Forest where it is easy to get lost. Your ancestors have left
 markings on various large trees in the forest to help you escape the forest, where each of the
 large tree will provide a road to one or more other large tree. This is drawn onto a treemap
 that is given to you:
 • There are a total of |T| trees in the forest, from t0 all the way to t|T|−1.
 • One of the trees would be start which is where you begin from.
 • One or more trees would be exits which is where you can exit from. These trees would
 be marked in the treemap given to you.
 • There are |R| roads in total connecting the trees, from r0 all the way to r|R|−1.
 • You can go from tree-u to tree-v if a road r = (u,v) exist. However, you can’t go from
 tree-v to tree-u unless the opposite road r′ = (v,u) also exist in the treemap.
 • It takes w-minutes to travel along the road r = (u,v,w). The travel time could differ
 between, and all of the time to travel along the road is stated in the treemap itself.
 You then find out the reason why it is called the Delulu Forest– the exit is nothing but a
 delusion and even after reaching the exit tree, you are still stuck in the forest due to the seal
 of the forest. However, your ancestor left a hint– certain trees are Solulu trees. You can claw
 at the tree to destroy that Solulu tree. Doing so will undo the seal of the forest, and then you
 will be able to exit the forest at an exit tree.
 • There are |S| Solulu trees in the forest, from s0 all the way to s|S|−1.
 • You would require y-minutes to claw at a Solulu tree-s in order to destroy it.
 • Some Solulu trees will teleport you to another tree-t upon destruction. This teleportation
 might bring you closer to, or further from your exit.
 You can’t bear to be in the forest anymore and would want to escape as soon as possible. Thus,
 you use your pawsome computer science knowledge of Graphs to find figure out the quickest
 way to exit the Delulu forest. 