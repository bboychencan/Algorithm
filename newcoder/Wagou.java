import java.util.Scanner;
import java.util.Arrays;

public class Wagou{
    public static int[] parent;
    public static int[] rank;
    
    public static int find(int x){
        if(parent[x] == -1){
            return x;
        }
        parent[x] = find(parent[x]);
        return parent[x];
    }
    
    public static boolean union(int a, int b){
        int x = find(a);
        int y = find(b);
        if(x == y){
            return false;
        }
        if(rank[x] < rank[y]){
            parent[x] = y;
        }else if(rank[x] > rank[y]){
            parent[y] = x;
        }else{
            parent[x] = y;
            rank[y] += 1;
        }
        return true;
    }
    
    public static void main(String[] args){
        int n, m;
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        parent = new int[n + 1];
        rank = new int[n + 1];
        Arrays.fill(parent, -1);
        Arrays.fill(rank, 1);
        int[][] edges = new int[m][3];
        for(int i=0; i<m; i++){
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
        }
        Arrays.sort(edges, (a, b) -> (Integer.compare(a[2], b[2])));
        int edgecount = 0;
        int res = 0;
        for(int i=0; i<m; i++){
            int x = find(edges[i][0]);
            int y = find(edges[i][1]);
            if(x == y){
                continue;
            }
            union(x, y);
            edgecount += 1;
            res += edges[i][2];
            if(edgecount == n-1){
                break;
            }
        }
        System.out.println(res);
    }
}