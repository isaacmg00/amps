
/*  NQueens.java by Isaac Garcia
    COMP 333
    12/9/2022 
*/
import java.lang.Math.*;
import java.util.*;

public class NQueens {
    // class variables
    int n;
    int curcol;
    int[] queenPos;
    int[] nextAvail;

    // check the nextAvail row to get the next available row to place a queen on the
    // board
    // verifies that there are no conflicts with any existing queen positions
    public int getNextAvail(int c) {
        int pos = nextAvail[c];

        while (true) {
            // the special noposavailable code so that our main loop knows that there are no
            // suitable positions available
            if (pos == n) {
                return 1000;
            }
            // check for conflicts with rows, columns, diagonals
            else if (nc(c, pos)) {
                nextAvail[c]++;
                return pos;
            } else {
                nextAvail[c]++;
                pos = nextAvail[c];
            }
        }
    }

    // return true if no conflicts and false if conflicts are present
    public boolean nc(int c, int pos) {
        // check for row/diagonal conflicts
        for (int prev = c - 1; prev >= 0; prev--) {
            int prevpos = queenPos[prev];
            if (pos == prevpos)
                return false;

            int colDiff = c - prev;
            int rowDiff = pos - prevpos;
            if (Math.abs(colDiff) == Math.abs(rowDiff))
                return false;
        }
        return true;
    }

    // main solve method, takes parameter <size> that simulates a chess board of
    // size <size x size>
    public void solve(int size) {
        // initialize variables
        n = size;
        curcol = 0;
        queenPos = new int[size];
        nextAvail = new int[size];
        int solutions = 0;

        // -1 denotes an Unassigned position in the array of queens
        for (int i = 0; i < queenPos.length; i++) {
            queenPos[i] = -1;
        }

        while (true) {
            // one solution found, and we have advanced off the right end of the board
            if (curcol == n) {
                // neatly print out the single solution and continue
                System.out.println(Arrays.toString(queenPos));

                curcol = curcol - 1;
                queenPos[curcol] = -1;
                solutions++;
                continue;
            }

            // no more solutions (all solutions found)
            if (curcol == -1) {
                System.out.println("Solutions found for puzzle size " + size + "x" + size + ": " + solutions);
                break;
            }

            // find suitable position for queen in curcol
            else {
                int pos = getNextAvail(curcol);
                if (pos == 1000) {
                    // backtrack
                    nextAvail[curcol] = 0;
                    queenPos[curcol] = -1;
                    curcol -= 1;
                    continue;
                } else {
                    // move on forward
                    queenPos[curcol] = pos;
                    curcol++;
                    continue;
                }
            }
        }
    }

    /*
     * tester class
     * NOTE: Change the parameter in test.solve() to change the size of the chess
     * board
     * Default = 8
     */
    public static void main(String[] args) {
        NQueens test = new NQueens();
        test.solve(8);
    }
}